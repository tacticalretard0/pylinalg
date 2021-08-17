# 3d vector and 4x4 matrix

from math import sqrt, radians, sin, cos

class Vec3:
    def __init__(x=0, y=0, z=0, w=1):
        self.x = x
        self.y = y
        self.z = z

        self.w = w

    def length(self):
        return sqrt(
            self.x*self.x +
            self.y*self.y +
            self.z*self.z
        )

    def get_normalized(self):
        le = self.length()

        if le != 0:
            return Vec3(
                self.x / le,
                self.y / le,
                self.z / le
        )

        return Vec3()

