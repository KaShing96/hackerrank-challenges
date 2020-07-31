# === Imports ===
import pytest

import functions as fnc

from func_timeout import func_timeout as fo 
from func_timeout.exceptions import FunctionTimedOut

from datetime import datetime 

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
        with open(f, 'r') as fr: 
            contents = fr.read() 

        # Contents is a single string
        # Split it by \n
        contents = contents.split('\n')

        # Loop through contents
        # Split by '-arg' and '-ans'
        for s in contents:
            if s == '-arg':
                # Set mode
                mode = s

            elif s == '-ans':
                # Set mode
                mode = s

            else:
                # Build case
                try: 
                    cases[len(cases) - 1][mode].append(s)

                except IndexError:
                    cases.append({
                        mode: [s]
                    })

                except KeyError:
                    cases[len(cases) - 1][mode] = [s]

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
                    10,
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

        print("\ntest case " + str(cx) + ": " + str(c['time_taken']))

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


# def run_test():




# # === Imports ===
# import pytest
# import json
# import os

# import functions as fnc

# from func_timeout import func_timeout as to
# from func_timeout.exceptions import FunctionTimedOut

# from datetime import datetime

# from colorama import Fore
# from colorama import Style

# # === Constants ===
# TIMEOUT = 10
# TERMINAL_COL = os.get_terminal_size().columns

# # === Test function ===
# __time = None 


# def clock(reset=False): 
#     """ Clock function."""
#     global __time 

#     if not reset: 
#         if __time is None: 
#             __time = datetime.now()

#             result = __time - __time 

#         else: 
#             result = datetime.now() - __time

#             __time = datetime.now()

#         return result
#     else: 
#         __time = None

#         return datetime.now() - datetime.now()


# def sclock(reset=False):
#     """Clock function with return as string."""
#     return str(clock(reset))


# def DEBUG(*args, **kwargs):
#     """Debug print function."""
#     print(*args, **kwargs)


# def CLOCKBUG(*args, **kwargs):
#     """Debug with clock function."""
#     args = list(args) 
#     args.append(sclock())
#     args = tuple(args)

#     print(*args, **kwargs)


# # === Test ===
# def run_test(f):
#     """Basic function to handle tests."""
#     # Filename
#     DEBUG()
#     for _ in range(TERMINAL_COL):
#         DEBUG("-", end='')
#     DEBUG("FILENAME:", f)

#     # Reset clock
#     sclock(True) 

#     # Open file
#     with open(f, "r") as fr:
#         # tests = json.load(fr)
#         tests = fr.read()

#         DEBUG(tests)

#     CLOCKBUG("File loading:")

#     # List of all exceptions
#     all_exceptions = []

#     # Running tests
#     for tx, t in enumerate(tests): 
#         exceptions = []

#         tx 

#         # Extracting argument and answers
#         json_args = t['arg'].split(' ')
#         json_ans = t['ans']

#         DEBUG("Arguments:", str(json_args)[:TERMINAL_COL//2])

#         args = json_args
#         ans = json_ans

#         try: 
#             result = to(
#                 TIMEOUT, 
#                 fnc.commonChild,
#                 (
#                     args[0],
#                     args[1]
#                 )
#             )
#         except FunctionTimedOut as e:
#             exceptions.append(e)

#         CLOCKBUG("Runtime:")

#         # Check answer
#         try:
#             assert result == ans, args 
#         except Exception as e:
#             exceptions.append(e)

#         if len(exceptions) > 0: 
#             all_exceptions.append(exceptions)

#         DEBUG()

#     for ex in all_exceptions:
#         for e in ex:
#             assert False, e
            

# # === Tests ===
# def test_test_values(): 
#     """Tests more basic tests."""
#     run_test("tests.txt")


# # def test_verification_values():
# #     run_test("verifications.json")


# # TODO Unit tests for functions in functions.py