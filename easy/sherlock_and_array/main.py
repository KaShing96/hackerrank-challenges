# === Imports ===
import json

from pathlib import Path

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from selenium.webdriver.remote.remote_connection import LOGGER

from bs4 import BeautifulSoup

import re

import os

import string 

# === Console class and functions ===
class Status():
    """
    A class to handle console messages.
    """
    def __init__(self, s):
        """
        s is the status
        """
        self.s = s

        print(f"[RUNNING] {s}", end="\r")

    
    def success(self):
        """
        Prints the success status
        """
        print(f"[SUCCESS] {self.s}")


    def failure(self, e=None):
        """
        Prints the failure status
        """
        print(f"[FAILED] {self.s}")

        if e is not None:
            raise e


# === WebDriver Waits ===
def wait_for_element(driver, method, s, wait_time=10):
    """
    Waits for s to be loaded via method.
    E.g. By.ID, "myDynamicElement"
    """
    return WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((method, s))
    )


# === String functions ===
def replace_printable(s, printables, wild=" "):
    """
    If the character in s is not in printables, replaces by wild.
    """
    new_s = ""

    for i in s: 
        new_s += i if i in printables else wild
        
    return new_s


# === Script ===
if __name__ == "__main__":
    # === Check if it is the base copy from _template ===
    # Ensure this is not in the '_template' folder, so the base copy is not overwritten
    s = Status("Verifying script integrity")

    template_check = Path.cwd()

    try: 
        assert "_template" not in str(template_check.absolute()), "This is located in /_template and may overwrite the base copy."
    except Exception as e: 
        s.failure(e)
        
    s.success()

    # === Load settings ===
    s = Status("Loading script settings")

    settings = None 

    with open("settings.json", "r") as fr:
        settings = json.load(fr)

    try: 
        assert settings is not None, "Settings could not be loaded."
    except Exception as e:
        s.failure(e)

    s.success()
    
    # === Load user configurations ===
    s = Status("Loading user settings")

    configs = None

    with open("config.json", "r") as fr:
        configs = json.load(fr) 

    try: 
        assert configs is not None, "User configurations could not be obtained."
    except Exception as e:
        s.failure(e)

    link = configs["link"]

    try:
        assert link is not None, "Link could not be obtained."
    except Exception as e:
        s.failure(e)

    s.success()

    # === Obtain geckodriver ===
    s = Status("Obtaining driver")

    driver_name = settings["driver_name"]
    driver_link = None

    current_dir = Path().cwd()

    while True:
        contents = [str(x.name) for x in current_dir.iterdir()]

        if driver_name not in contents:
            current_dir = current_dir.parent

        else: 
            for i in current_dir.iterdir():
                if driver_name == i.name:
                    driver_link = i

            break

    try: 
        assert driver_link is not None, "Driver not found."
    except Exception as e:
        s.failure(e)

    s.success()

    # === Launch driver ===
    # Set up options to disable logging and run headless
    options = Options()
    options.add_argument("--headless")
    
    LOGGER.setLevel(logging.WARNING)

    # Connect to HackerRank
    s = Status("Connecting to HackerRank")

    driver = webdriver.Firefox(executable_path=driver_link, options=options)
    driver.get(link)

    # === Skip login prompt ===
    # The page will redirect to a 'request login'  page, which we will ignore
    x_button_class_name = "close-icon"

    try: 
        x_button_elem = wait_for_element(driver, By.CLASS_NAME, x_button_class_name)

        x_button_elem.click()

    except Exception as e:

        s.failure(e)

    s.success()

    # === Verify language ===
    s = Status("Verifying programming language")

    bs = BeautifulSoup(driver.page_source, "lxml")

    # Assert that the correct language is selected
    language_box_class_name = "css-1hwfws3"

    if bs.find("div", {"class": language_box_class_name}) != configs["language"]:

        # Identify the correct language
        driver.find_element_by_class_name(language_box_class_name).click() 

        bs = BeautifulSoup(driver.page_source, "lxml")

        languages_class_name = "css-m62ux7"

        languages = bs.find("div", {"class": languages_class_name}).findChildren()

        correct_language_id = None 

        for l in languages: 
            if l.getText() == configs["language"]:
                correct_language_id = l.attrs["id"]

        assert correct_language_id is not None, "The programming language could not be found." 

        driver.find_element_by_id(correct_language_id).click()

    s.success()

    # === Copy online editor code ===
    s = Status("Copying code")

    # Read online editor contents
    bs = BeautifulSoup(driver.page_source, "lxml")

    editor_class = "view-lines"
    line_class = "view-line"
    editor_contents = bs.find("div", {"class": editor_class})
    editor_contents = bs.findAll("div", {"class": line_class})
    editor_contents = [t.getText() for t in editor_contents]

    # Read original function.py
    # with open(settings["functions"], "r") as fr:
    with open(settings["reference_functions"], "r") as fr:
        original_function_contents = fr.read()

    # Replace function.py
    block_under_man = None 

    # Filter non-printables and non-tokens
    printables = set(string.printable + "\n\r\t")

    # Obtain function name
    function_name = None

    # Headers
    import_header = False

    with open(settings["functions"], "w") as fw:
        # We write everything from the editor until the 'if name == ...' section
        for tx, t in enumerate(editor_contents): 
            if re.match(r"if", t):
                # To be custom-replaced
                block_under_main = "\n".join(editor_contents[tx:])

                break 

            # Do not print out interpreter
            elif re.match(r"#", t):
                continue

            # Isolate function name
            elif re.match(r"def", t):
                function_name = t[4:-1]

                function_args = len(list(filter(lambda x: x == ",", function_name)))

                fw.write(f"\n# === Function === \ndef {function_name}:\n    \"\"\"\n    Your code goes here.\n    \"\"\"\n    pass\n\n")

            # Allow imports
            elif re.match(r"import", t):
                if not import_header:
                    fw.write("# === Imports ===\n")

                    import_header = True

                fw.write(replace_printable(t, printables))
                fw.write("\n")

        for tx, t in enumerate(original_function_contents.split("\n")):
            # We only continue from line 6 onwards for # === Main ===
            if tx >= 6 and tx <= 18:
                fw.write(t)
                fw.write("\n")

            # Then, we add the manual section
            if tx == 19:
                # Version check
                # 3.0 has the following as line number 2
                # fptr = open(os.environ['OUTPUT_PATH'], 'w')
                assert replace_printable(block_under_main.split("\n")[1], printables).strip() == "fptr = open(os.environ['OUTPUT_PATH'], 'w')", replace_printable(block_under_main.split("\n")[1], printables)
                
                for i in block_under_main.split("\n")[3:]:
                    fw.write(replace_printable(i, printables))
                    fw.write("\n")

                break
                
        # Then we add the remainder
        fw.write("\n".join(original_function_contents.split("\n")[20:]))

    s.success()

    # === Replace README ===
    s = Status("Setting up README.md")

    title_class = "text-headline"

    with open("README.md", "w") as fw:
        title = bs.find("div", {"class": title_class})

        fw.write(f"# {title.getText()}\n\nThis problem can be found at [here]({link}).")

    s.success()

    # === Obtain sample inputs and outputs ===
    s = Status("Obtaining sample tests")

    # Obtain possible 'Sample Inputs' from the problem statement
    bs = BeautifulSoup(driver.page_source, "lxml")

    sample_input_body_class = "challenge_sample_input_body"
    sample_output_body_class = "challenge_sample_output_body"

    sample_inputs = bs.findAll("div", {"class": sample_input_body_class})

    sample_outputs = bs.findAll("div", {"class": sample_output_body_class})

    try:
        assert len(sample_inputs) == len(sample_outputs)
    except Exception as e:
        s.failure(e)

    # Generate test case files
    # test_folder_name = "/test_cases"
    test_folder = Path().cwd().iterdir()

    for t in test_folder:
        if settings["test_folder"] == t.name:
            # Switch directory
            os.chdir(t) 
            
            # Write arguments
            for ix, (i, j) in enumerate(zip(sample_inputs, sample_outputs)):
                with open(f"{ix}.txt", "w") as fw:
                    fw.write(f"{i.getText().strip()}\n---\n{j.getText().strip()}")
                     
            break

    s.success()

    # === Close driver ===
    s = Status("Closing driver")    

    driver.close()

    s.success()