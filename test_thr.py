
import sys

from math import pi, e

import pylinalg.thr as pyla3

correct = {
}

def info(passed, res, action):
    print("="*5)
    print(action, end=", ")
    print("test passed" if passed else "!! test failed !!")
    print()
    print(f"result: {res}")
    print()
    print(f"expected: {correct[action]}")
    print("-"*5)
    print()

def check(res, action):
    if res != correct[action]:
        info(False, res, action)
        sys.exit()

    info(True, res, action)



