# 2d vector (also has w) and 3x3 matrix

from math import sqrt, radians, sin, cos

class Vec2:
    def __init__(self, x=0, y=0, w=1):
        self.x = x
        self.y = y
        
        self.w = w

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

    def get_stepped(self, amount):
        add = self.get_normalized()

        add *= amount

        return self + add

    def get_rotated(self, deg):
        theta = radians(deg)

        st = sin(theta)
        ct = cos(theta)

        newx = self.y * st + self.x * ct
        newy = self.y * ct - self.x * st

        return Vec2(newx, newy)

    def get_rounded(self, places=0):
        return Vec2(round(self.x, places), round(self.y, places))

    def get_truncated(self):
        return Vec2(int(self.x), int(self.y))


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

    def __mul__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x * other.x, self.y * other.y)

        if isinstance(other, (int, float)):
            return Vec2(self.x * other, self.y * other)

        if isinstance(other, Mat3):
            new = Vec2()
            
            m = other

            new.x = self.x * m.m[0][0] + self.y * m.m[1][0] + self.w * m.m[2][0]
            new.y = self.x * m.m[0][1] + self.y * m.m[1][1] + self.w * m.m[2][1]

            new.w = self.x * m.m[0][2] + self.y * m.m[1][2] + self.w * m.m[2][2]

            return new

    def __truediv__(self, other):
        if isinstance(other, Vec2):
            new = self.copy()

            if other.x != 0:
                new.x /= other.x
            if other.y != 0:
                new.y /= other.y

            return new

        if isinstance(other, (int, float)):
            if other != 0:
                return Vec2(self.x / other, self.y / other)

            return Vec2()

class Mat3:
    def __init__(self, lis):
        self.m = lis

