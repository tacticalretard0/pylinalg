# 3d vector (also has w) and 4x4 matrix

from math import sqrt, radians, sin, cos

class Vec3:
    def __init__(self, x=0, y=0, z=0, w=1):
        self.x = x
        self.y = y
        self.z = z

        self.w = w

        # aliases
        self.get_normalised = self.get_normalized

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

    def get_stepped(self, amount):
        add = self.get_normalized()

        add *= amount

        return self + add

    ####
    # MODIFIES SELF
        # none yet

    ####
    # OPERATOR OVERLOADING

    def __repr__(self):
        return f"Vec3({self.x}, {self.y}, {self.z}, w={self.w})"

    def __eq__(self, other):
        return (
            self.x == other.x and
            self.y == other.y and
            self.z == other.z
        )

    def __add__(self, other):
        if isinstance(other, Vec3):
            return Vec3(
                self.x + other.x,
                self.y + other.y,
                self.z + other.z
            )

        if isinstance(other, (int, float)):
            return Vec3(
                self.x + other,
                self.y + other,
                self.z + other
            )

    def __sub__(self, other):
        if isinstance(other, Vec3):
            return Vec3(
                self.x - other.x,
                self.y - other.y,
                self.z - other.z
            )

        if isinstance(other, (int, float)):
            return Vec3(
                self.x - other,
                self.y - other,
                self.z - other    
            )

    def __mul__(self, other):
        if isinstance(other, Vec3):
            return Vec3(
                self.x * other.x,
                self.y * other.y,
                self.z * other.z
            )

        if isinstance(other, (int, float)):
            return Vec3(
                self.x * other,
                self.y * other,
                self.z * other
            )

        if isinstance(other, Mat4):
            new = Vec3()
            
            m = other

            new.x = self.x * m.m[0][0] + self.y * m.m[1][0] + self.z * m.m[2][0] + self.w * m.m[3][0]
            new.y = self.x * m.m[0][1] + self.y * m.m[1][1] + self.z * m.m[2][1] + self.w * m.m[3][1]
            new.z = self.x * m.m[0][2] + self.y * m.m[1][2] + self.z * m.m[2][2] + self.w * m.m[3][2]

            new.w = self.x * m.m[0][3] + self.y * m.m[1][3] + self.z * m.m[2][3] + self.w * m.m[3][3]

            return new

    def __truediv__(self, other):
        if isinstance(other, Vec3):
            new = self.copy()

            if other.x != 0:
                new.x /= other.x
            if other.y != 0:
                new.y /= other.y
            if other.z != 0:
                new.z /= other.z

            return new

        if isinstance(other, (int, float)):
            if other != 0:
                return Vec2(
                    self.x / other,
                    self.y / other,
                    self.z / other    
                )

            return Vec2()

class Mat4:
    def __init__(self, *init):
        self.m = [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
        ]
        
        row = 0
        col = 0
        le = 0
        for item in init:
            try:
                self.m[row][col] = item
            except IndexError:
                raise Exception("Mat4: too many items in initializer")

            col += 1
            if col > 3:
                row += 1
                col = 0
            
            le += 1

        if le != 4*4:
            raise Exception("Mat4: not enough items in initializer")

    ####
    # OPERATOR OVERLOADING

    def __repr__(self):
        res = ""

        for row in self.m:
            for col in row:
                res += f"{col} "
            res += '\n'

        return res.strip()

