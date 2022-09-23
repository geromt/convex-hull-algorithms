from typing import List

import matplotlib.pyplot as plt

from utils.point import Point


def graph_convex_hull(points: List[Point], convex_hull: List[Point]):
    """
    Draw the list of points and its convex hull

    :param points: List of points
    :param convex_hull: List of vertices of the convex hull of the points in
        clockwise or inverse clockwise order
    """
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Convex Hull of a set of points")

    x_points = [p.x for p in points]
    y_points = [p.y for p in points]

    plt.scatter(x_points, y_points, marker="o")

    x_points = [p.x for p in convex_hull]
    x_points.append(x_points[0])
    y_points = [p.y for p in convex_hull]
    y_points.append(y_points[0])

    plt.plot(x_points, y_points)
    plt.show()
