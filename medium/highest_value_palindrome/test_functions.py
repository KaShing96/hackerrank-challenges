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
        args = t["arg"].split(' ')
        ans = str(t["ans"])

        length = int(args[0])
        moves = int(args[1])
        string = args[2]

        __start = datetime.now()

        result = to(
            10, 
            fnc.highestValuePalindrome,
            (
                string, 
                length, 
                moves
            )
        )

        print(datetime.now() - __start)

        assert result == ans, [tx if t[0] != t[1] else None for tx, t in enumerate(zip(result, ans))]


# === Tests ===
def test_test_values(): 
    """Tests more basic tests."""
    run_test("tests.json")


def test_highest_value_palindrome():
    run_test("verifications.json")


# TODO Unit tests for functions in functions.py