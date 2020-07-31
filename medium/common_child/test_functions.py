# === Imports ===
import pytest
import json
import os

import functions as fnc

from func_timeout import func_timeout as to
from func_timeout.exceptions import FunctionTimedOut

from datetime import datetime

from colorama import Fore
from colorama import Style

# === Constants ===
TIMEOUT = 10
TERMINAL_COL = os.get_terminal_size().columns

# === Test function ===
__time = None 


def clock(reset=False): 
    """ Clock function."""
    global __time 

    if not reset: 
        if __time is None: 
            __time = datetime.now()

            result = __time - __time 

        else: 
            result = datetime.now() - __time

            __time = datetime.now()

        return result
    else: 
        __time = None

        return datetime.now() - datetime.now()


def sclock(reset=False):
    """Clock function with return as string."""
    return str(clock(reset))


def DEBUG(*args, **kwargs):
    """Debug print function."""
    print(*args, **kwargs)


def CLOCKBUG(*args, **kwargs):
    """Debug with clock function."""
    args = list(args) 
    args.append(sclock())
    args = tuple(args)

    print(*args, **kwargs)


def run_test(f):
    """Basic function to handle tests."""
    # Filename
    DEBUG()
    for _ in range(TERMINAL_COL):
        DEBUG("-", end='')
    DEBUG("FILENAME:", f)

    # Reset clock
    sclock(True) 

    # Open file
    with open(f, "r") as fr:
        tests = json.load(fr)
    CLOCKBUG("File loading:")

    # List of all exceptions
    all_exceptions = []

    # Running tests
    for tx, t in enumerate(tests): 
        exceptions = []

        tx 

        # Extracting argument and answers
        json_args = t['arg'].split(' ')
        json_ans = t['ans']

        DEBUG("Arguments:", str(json_args)[:TERMINAL_COL//2])

        args = json_args
        ans = json_ans

        try: 
            result = to(
                TIMEOUT, 
                fnc.commonChild,
                (
                    args[0],
                    args[1]
                )
            )
        except FunctionTimedOut as e:
            exceptions.append(e)

        CLOCKBUG("Runtime:")

        # Check answer
        try:
            assert result == ans, args 
        except Exception as e:
            exceptions.append(e)

        if len(exceptions) > 0: 
            all_exceptions.append(exceptions)

        DEBUG()

    for ex in all_exceptions:
        for e in ex:
            assert False, e

    # if len(all_exceptions) > 0:


    #     assert False, all_exceptions

    # errors = []

    # for tx, t in enumerate(tests):
    #     tx
        
    #     args = t["arg"].split(' ')
    #     ans = t["ans"]

    #     __start = datetime.now()

    #     try: 
    #         result = to(
    #             TIMEOUT, 
    #             fnc.commonChild,
    #             (
    #                 args[0],
    #                 args[1]
    #             )
    #         )
    #     except FunctionTimedOut as e:
    #         errors.append(e, TIMEOUT) 
    #         continue

    #     print(datetime.now() - __start)
        
    #     try: 
    #         assert result == ans, args
    #     except Exception as e: 
    #         errors.append(e, datetime.now() - __start)

    # for e in errors: 
    #     assert False, e
            

# === Tests ===
def test_test_values(): 
    """Tests more basic tests."""
    run_test("tests.json")


def test_verification_values():
    run_test("verifications.json")


# TODO Unit tests for functions in functions.py