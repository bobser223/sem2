import turtle
from vecSum import vecSum

class Zero:
    def __init__(self):
        self._position = (0, 0)
        self.__v1 = (-5, 0)
        self.__v2 = (0, 20)
        self.__v3 = (10, 0)
        self.__v4 = (0, -40)
        self.__v5 = (-10, 0)
        self.__v6 = (0, 20)

    def set_position(self, x, y):
        self._position = (x, y)

    def __calculate_abs_position(self):
        absV1 = vecSum(self.__v1, self._position)
        absV2 = vecSum(self.__v2, absV1)
        absV3 = vecSum(self.__v3, absV2)
        absV4 = vecSum(self.__v4, absV3)
        absV5 = vecSum(self.__v5, absV4)
        absV6 = vecSum(self.__v6, absV5)
        return absV1, absV2, absV3, absV4, absV5, absV6

    def draw(self):
        abs_vectors = self.__calculate_abs_position()
        turtle.penup()
        turtle.goto(abs_vectors[0])
        turtle.pendown()
        turtle.goto(abs_vectors[1])
        turtle.goto(abs_vectors[2])
        turtle.goto(abs_vectors[3])
        turtle.goto(abs_vectors[4])
        turtle.goto(abs_vectors[5])
        turtle.penup()

if __name__ == '__main__':
    two = Zero()
    two.set_position(204, -67)
    two.draw()
    turtle.mainloop()