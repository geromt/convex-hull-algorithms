#!/usr/bin/python3

import random
import sys
from collections import deque
from typing import List

from utils.math_utils import slope, cross_product
from utils.point import Point, gen_random_points
from utils.graph import graph_convex_hull


class GrahamConvexHull:
    """Calculate the Convex Hull of a set of points with Graham Algorithm

    Attributes
    ----------
    min_y : Point
        Point with the least y coordinate
    points : List[Point]
        List of points ordered by its slopes with respect min_y. min_y is not
        included in this list

    Methods
    -------

    """

    def __init__(self, points: List[Point]):
        """Initializer of the class.

        :param points: List of points from which we will calculate the convex
            hull
        """
        self.points = points

        self.min_y = min(self.points, key=lambda x: x.y)
        self.points.remove(self.min_y)
        self.points.sort(key=self._key_slope)

    def _key_slope(self, p: Point):
        """
        Auxiliary function. Returns the number to order the points
        :param p: Point
        :return: Number to order p
        """
        s = slope(self.min_y, p)
        if s < 0:
            s = 180 + s

        return s

    def graham_convex_hull(self) -> List[Point]:
        """
        Calculate the convex hull of the points in the points attribute and
        min_y point

        :return: List of vertices of the convex hull in inverse clockwise order
        """

        # We use deque to achieve O(1) complexity to do push and pop from the
        # stack
        stack = deque([self.min_y])

        # Copy the points so as to not to destroy the points in the attribute
        points = self.points.copy()

        # Graham Algorithm
        p = points.pop(0)
        while len(points) > 0:
            if len(stack) == 1:
                stack.append(p)
                p = points.pop(0)
                continue

            # We use cross the cross product to know if p is on the left or
            # right of the line that pass through the last two points
            if cross_product(stack[-2], stack[-1], p) > 0:
                stack.append(p)
                p = points.pop(0)
            else:
                stack.pop()

        # Check if the last point is in the convex hull
        while True:
            if cross_product(stack[-2], stack[-1], p) > 0:
                stack.append(p)
                break
            else:
                stack.pop()

        return list(stack)


def main():
    points = gen_random_points(int(sys.argv[1]), 0, 0, 100, 100)
    graham = GrahamConvexHull(points)

    print(f"The point with less y coordinate: {graham.min_y}")
    print("Ordered points:")
    for i in graham.points:
        print(i)

    print("\nPoints in the convex hull in inverse clockwise order:")
    for i in graham.graham_convex_hull():
        print(i)

    graph_convex_hull(graham.points + [graham.min_y],
                      graham.graham_convex_hull())


if __name__ == "__main__":
    main()
