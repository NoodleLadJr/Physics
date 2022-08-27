import math


class Vector2:
    """A 2 Component Vector That Stores an Angle in Degrees by Default"""
    X: float = 0.0
    Y: float = 0.0

    def __init__(self, x: int = 0, y: int = 0):
        self.X = x
        self.Y = y

    @classmethod
    def from_components(cls, x: float, y: float):
        return Vector2(x,y)

    @classmethod
    def from_length(cls, length: float, angle: float, precision: int = 3):
        X = round(length * math.cos(math.radians(angle)), precision)
        Y = round(length * math.sin(math.radians(angle)), precision)
        return Vector2(X,Y)

    @classmethod
    def unit_vector(cls, angle: float):
        return Vector2.from_length(1.0, angle)

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2.from_components((self.X + other.X), (self.Y + other.Y))
        else:
            return Vector2.from_components((self.X + other), (self.Y + other))

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2.from_components((self.X - other.X), (self.Y - other.Y))
        else:
            return Vector2.from_components((self.X - other), (self.Y - other))

    def __abs__(self):
        return self.length()

    def __int__(self):
        return int(self.length())

    def __mul__(self, other):
        return Vector2.from_components((self.X * other), (self.Y * other))

    def __truediv__(self, other):
        try:
            return Vector2.from_components((self.X / other), (self.Y / other))
        except ZeroDivisionError:
            return self

    def __str__(self):
        return "X: " + str(self.X) + " Y: " + str(self.Y)

    def __round__(self, n=None):
        return Vector2.from_components(round(self.X, n), round(self.Y, n))

    def length(self):
        return math.sqrt(math.pow(self.X, 2) + math.pow(self.Y, 2))

    def length_squared(self):
        return math.pow(self.X, 2) + math.pow(self.Y, 2)

    def distance(self, other: "Vector2") -> float:
        return (other-self).length()

    def angle(self):
        return math.degrees(math.atan2(self.Y, self.X))

    def normalize(self):
        return self / self.length()
