# === Imports ===
import pytest
import json

import functions as fnc

from func_timeout import func_timeout as to

from datetime import datetime

# === Test function ===
def run_test(f):
    """Basic function to handle tests."""
    with open(f, "r") as fr:
        tests = json.load(fr)

    for tx, t in enumerate(tests):
        tx
        
        args = t["arg"].split(' ')
        ans = t["ans"]

        args = args[1:]
        result = [None] * len(args)

        __start = datetime.now()

        for ax, a in enumerate(args):
            result[ax] = to(
                10, 
                fnc.sherlockAndAnagrams,
                (
                    a,
                )
            )

        print(datetime.now() - __start)

        for r, a in zip(result, ans): 
            assert r == a


# === Tests ===
def test_test_values(): 
    """Tests more basic tests."""
    run_test("tests.json")


def test_highest_value_palindrome():
    run_test("verifications.json")


# TODO Unit tests for functions in functions.py