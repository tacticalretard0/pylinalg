# 2d vector and 2x2 matrix

from math import sqrt, radians, sin, cos

class Vec2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    ####
    # RETURNS

    def length(self):
        return sqrt(self.x*self.x + self.y*self.y)

    def get_normalized(self):
        le = self.length()

        if le != 0:
            return Vec2(self.x / le, self.y / le)
        
        return Vec2()

    def dot(self, other):
        return self.x*other.x + self.y*other.y

    def get_rounded(self, places=0):
        return Vec2(round(self.x, places), round(self.y, places))

    def get_truncated(self):
        return Vec2(int(self.x), int(self.y))

    def get_rotated(self, deg):
        theta = radians(deg)

        st = sin(theta)
        ct = cos(theta)

        newx = self.y * st + self.x * ct
        newy = self.y * ct - self.x * st

        return Vec2(newx, newy)

    def get_rotatedc(self, deg):
        theta = radians(deg)

        st = sin(theta)
        ct = cos(theta)

        newx = self.x * ct - self.y * st
        newy = self.x * st + self.y * ct

        return Vec2(newx, newy)

    def copy(self):
        return Vec2(self.x+0, self.y+0)

    ####
    # MODIFIES SELF
        # none yet

    ####
    # OPERATOR OVERLOADING

    def __repr__(self):
        return f"Vec2({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)

        if isinstance(other, (int, float)):
            return Vec2(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)

        if isinstance(other, (int, float)):
            return Vec2(self.x - other, self.y - other)

