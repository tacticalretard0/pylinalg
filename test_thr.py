
import sys

from math import pi, e

import pylinalg.thr as pyla3

correct = {
    "length": 10,
    "get_normalized": pyla3.Vec3(1, 0, 0),
    "dot": 0,
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

testvec = pyla3.Vec3(10, 0, 0)

check(testvec.length(), "length")

check(testvec.get_normalized(), "get_normalized")

check(testvec.get_normalized().dot(pyla3.Vec3(0, -10, 0).get_normalized()), "dot")

