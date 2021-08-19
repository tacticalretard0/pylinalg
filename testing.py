# test file to make sure changes are working

import pylinalg.two as pyla2
import pylinalg.thr as pyla3

chungus = pyla3.Vec3(1, 1, 1)

matungus = pyla3.Mat4(
    2, 0, 0, 0,
    0, 1, 0, 0,
    0, 0, 3, 0,
    0, 0, 0, 10
)

print(chungus * matungus)

