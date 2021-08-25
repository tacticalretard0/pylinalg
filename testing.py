# test file to make sure changes are working

import pylinalg.two as pyla2
import pylinalg.thr as pyla3

chungus = pyla3.Vec3(1, 0, 0)

matungus = pyla3.Mat4.make_rotateZ(90)

print(chungus * matungus)

