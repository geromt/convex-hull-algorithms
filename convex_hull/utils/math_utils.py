from utils.point import Point


def slope(p1: Point, p2: Point) -> float:
    """Calculate the slope between two points

    :param p1: First point
    :param p2: Second point
    :return: Slope between p1 and p2
    """
    return (p2.y - p1.y)/(p2.x - p1.x)


def cross_product(p1: Point, p2: Point, p3: Point) -> float:
    """
    Calculate the cross product of the points (p2 - p1) and (p3 - p1)

    :param p1: First point
    :param p2: Second point
    :param p3: Third point
    :return: The cross product of (p2 - p1) and (p3 - p1)
    """
    return (p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x)
