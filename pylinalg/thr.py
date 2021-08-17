# 3d vector (also has w) and 4x4 matrix

from math import sqrt, radians, sin, cos

class Vec3:
    def __init__(self, x=0, y=0, z=0, w=1):
        self.x = x
        self.y = y
        self.z = z

        self.w = w

    ####
    # RETURNS

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

    def dot(self, other):
        return (
            self.x*other.x +
            self.y*other.y +
            self.z*other.z
        )

    ####
    # MODIFIES SELF
        # none yet

    ####
    # OPERATOR OVERLOADING

    def __repr__(self):
        return f"Vec3({self.x}, {self.y}, {self.z})"

    def __eq__(self, other):
        return (
            self.x == other.x and
            self.y == other.y and
            self.z == other.z
        )

