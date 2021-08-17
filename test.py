# test file because why not

import sys

from math import pi, e

import pylinalg.two as pyla2

correct = {
    "length": 10,
    "get_normalized": pyla2.Vec2(1, 0),
    "get_rounded": pyla2.Vec2(3, 3),
    "get_truncated": pyla2.Vec2(3, 2),
    "get_rotated": pyla2.Vec2(0, -10),
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

testvec = pyla2.Vec2(10, 0)

check(testvec.length(), "length")

check(testvec.get_normalized(), "get_normalized")

get_rounded_test = pyla2.Vec2(pi, e)
check(get_rounded_test.get_rounded(), "get_rounded")
del get_rounded_test

get_truncated_test = pyla2.Vec2(pi, e)
check(get_truncated_test.get_truncated(), "get_truncated")
del get_truncated_test

get_rotated_test = testvec.get_rotated(90).get_rounded()
check(get_rotated_test, "get_rotated")
del get_rotated_test

