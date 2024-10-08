from math import pi


class Ball:
    def __init__(self, r):
        assert r > 0
        self.r = r
        self.roundedPi = round(pi, 5)
    def area(self):
        result = 4 * pi * self.r ** 2
        return result

    def perimeterOrVolume(self):
        result = (4/3) * pi * self.r ** 3
        return result
    def __str__(self) -> str:
        return f"Ball: r={self.r}"