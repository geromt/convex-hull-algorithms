import random
from typing import List


class Point:
    """
    Class to represent a point in the plane

    Attributes
    ----------
    x: int
        Coordinate x
    y: int
        Coordinate y
    """

    def __init__(self, x: float, y: float):
        """
        Initializer of the class

        :param x: Coordinate x
        :param y: Coordinate y
        """
        self._x = x
        self._y = y

    def get_x(self) -> float:
        """
        Getter of x

        :return: The x coordinate
        """
        return self._x

    def get_y(self) -> float:
        """
        Getter of y

        :return: The y coordinate
        """
        return self._y

    # Properties
    x = property(get_x)
    y = property(get_y)

    def __str__(self) -> str:
        """
        Returns a string representation of the class

        :return: String that represent the class
        """
        return f"Point({self.x}, {self.y})"


def gen_random_points(n: int, x1: float, y1: float, x2: float,
                      y2: float) -> List[Point]:
    """Generate a list of random generated points contented by the rectangle
    with coordinate (x1, y1) in the bottom left corner and coordinate (x2, y2)
    in the top right corner

    :param n: Number of points to generate
    :param x1: x coordinate of the bottom left corner
    :param y1: y coordinate of the bottom left corner
    :param x2: x coordinate of the top right corner
    :param y2: y coordinate of the top right corner
    :return: List of n randomly generated points
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if x1 >= x2:
        raise ValueError("x1 must be less than x2")
    if y1 >= y2:
        raise ValueError("y1 must be less than x2")

    points = []
    for i in range(n):
        x = random.uniform(x1, x2)
        y = random.uniform(y1, y2)
        points.append(Point(x, y))

    return points
