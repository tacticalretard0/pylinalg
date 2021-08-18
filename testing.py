# test file to make sure changes are working

import pylinalg.two as pyla2
import pylinalg.thr as pyla3

lol = pyla2.Vec2(10, 10)

mat = pyla2.Mat3(
    0, 1, 0,
    0, 1, 0,
    0, 1, 0
)

print(lol.get_normalised())

