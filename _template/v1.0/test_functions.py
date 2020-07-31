# === Imports ===
import pytest

import functions as fnc

from func_timeout import func_timeout as fo 
from func_timeout.exceptions import FunctionTimedOut

from datetime import datetime 

# === Variables ===
TIME_LIMIT = 10

# === Debug functions ===
def DEBUG(*args, **kwargs):
    """
    Debug function.
    """
    print(*args, **kwargs)


# === Test functions ===
def get_test_vals(f):
    """
    Extract arguments and answers from test file. 

    Params
    ======
    f: str
        The file to extract the parameters from
    """
    cases = []

    try: 
        # Load cases into string
        with open(f, "r") as fr:
            contents = fr.read() 

        # Contents is a single string
        # Split it by "\n"
        contents = contents.split("\n")

        # Loop through the contents
        # Split by "-arg" and "-ans"
        for s in contents: 

            # Whenever you get "-arg", you append a new case to cases, instantiated with "-arg" and "-ans" as keys, with lists as values
            if s == "-arg":
                # Set mode as arg
                mode = s

                # Append a new case
                cases.append({
                    "-arg": [],
                    "-ans": []
                })

            elif s == "-ans":
                # Set mode as arg
                mode = s 

            else: 
                # Build the case
                try: 
                    cases[-1][mode].append(s) 

                except Exception as e:
                    raise e

        return cases

    except Exception as e:
        raise e
    

def run_test(f, ignores=[], raise_errors=True): 
    """
    Runs the test required for the test file.
     
    Params
    ======
    f: str
        The name of the test file.
    ignores: list of int
        The index of the case to ignore
    """
    # Ensure that #ignores# is a list
    if type(ignores) == type(1):
        ignores = [ignores]

    #  Extract arguments
    cases = get_test_vals(f)

    # Loop through args and ans
    for cx, c in enumerate(cases): 
        # If cx is in #ignores#, we ingore it
        if cx in ignores: 
            continue
    
        # Unpack arguments and answers
        args = c['-arg']
        ans = c['-ans']

        # Repackage into string
        args = '\n'.join(args)
        ans = '\n'.join(ans)

        # Instantiate fnc arguments
        fnc.set_inputs(args)

        # Get start time
        start_time = datetime.now()

        # Run function
        try:

            try: 
                fo(
                    TIME_LIMIT,
                    fnc.main,
                    (args,)
                )

                # fnc.main(args)

            except FunctionTimedOut as e:
                raise e

            except Exception as e:
                raise e

            # Check answers
            assert "\n".join(fnc.fptr.get_answers()) == ans 
        
        except Exception as e:
            c['error'] = e

        except FunctionTimedOut as e:
            c['error'] = e

        # Get time taken
        c['time_taken'] = datetime.now() - start_time

    # Give conclusions about each test case
    # Loop through cases to check for errors
    for cx, c in enumerate(cases):
        # Check for ignores
        if cx in ignores: 
            continue

        print(f"\ntest case {str(cx)}: {str(c['time_taken'])}")

    for c in cases:
        # Only print errors if requested
        if raise_errors: 

            try: 
                raise c['error']

            except KeyError as e:
                # Suggests there are no errors
                continue 


# === Run test ===
def test_test_values():
    """
    Runs test on the test values.
    """
    run_test("tests.txt")


def test_verification_values():
    """
    Runs test on the verification values.
    """
    run_test("verifications.txt")