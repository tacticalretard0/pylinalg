# test file because why not

import sys

from math import pi, e

import pylinalg.two as pyla2

correct = {
    "length": 10,
    "get_normalized": pyla2.Vec2(1, 0),
    "dot": 0,
    "get_rotated": pyla2.Vec2(0, -10),
    "get_rotatedc": pyla2.Vec2(0, 10),
    "get_rounded": pyla2.Vec2(3, 3),
    "get_truncated": pyla2.Vec2(3, 2),
    "get_stepped": pyla2.Vec2(15, 0),
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

check(testvec.get_normalized().dot(pyla2.Vec2(0, -10).get_normalized()), "dot")

check(testvec.get_stepped(5), "get_stepped")

rotation_test = testvec.get_rotated(90).get_rounded()
check(rotation_test, "get_rotated")

rotation_test = testvec.get_rotatedc(90).get_rounded()
check(rotation_test, "get_rotatedc")
del rotation_test

rounding_truncation_test = pyla2.Vec2(pi, e)
check(rounding_truncation_test.get_rounded(), "get_rounded")

check(rounding_truncation_test.get_truncated(), "get_truncated")
del rounding_truncation_test


