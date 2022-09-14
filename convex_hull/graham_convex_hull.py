#!/usr/bin/python3

import random
from collections import deque
import matplotlib.pyplot as plt

# Constantes
LENGTH = 100  # Coordenada x máxima donde pueden aparecer los puntos
WIDTH = 100   # Coordenada y máxima donde pueden aparecer los puntos
N_POINTS = 20 # Número de puntos si los puntos se generan al azar


class Point:
    """
    Clase que representa un punto en el plano

    Atributos
    ---------
    x : float
        Coordenada x
    y : float
        Coordenada y
    """

    def __init__(self, x, y):
        """Inicializador de la clase"""
        self.x = x
        self.y = y

    def __str__(self):
        """Regresa una cadena que representa la clase"""
        return f"Point({self.x}, {self.y})"


def slope(p1, p2):
    """Calcula la pendiente de la línea que pasa por los puntos p1 y p2"""
    return (p2.y - p1.y)/(p2.x - p1.x)


def cross_product(p1, p2, p3):
    """Calcula el producto cruz de las líneas que pasan por los puntos p1-p2 y p1-p3"""
    return (p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x)


class GrahamConvexHull:
    """Clase para calcular el cierre convexo de un lista de puntos

    Atributos
    ---------
    min_y : Point
        Punto con la menor coordenada y
    points : List
        Lista de puntos ordenados con respecto al ángulo que forman con
        el punto min_y
    """

    def __init__(self, n, points=None):
        """Inicializador de la clase

        Parámetros
        ----------
        n : int
            Número de puntos que serán generados
        points : List, optional
            Si no se provee esta lista se generarán una lista de puntos random
        """
        if points is None:
            self.points = []
            self._gen_random_points(n)
        else:
            self.points = points

        self.min_y = min(self.points, key=lambda x: x.y)
        self.points.remove(self.min_y)
        self.points.sort(key=self._key_slope)

    def _gen_random_points(self, n):
        """Genera una lista de n puntos en posición random"""
        for i in range(n):
            x = random.uniform(0, WIDTH)
            y = random.uniform(0, LENGTH)
            self.points.append(Point(x, y))

    def _key_slope(self, p):
        """Función auxiliar que devuelve el número con respecto al cual se
        ordenorán los puntos"""
        s = slope(self.min_y, p)
        if s < 0:
            s = 180 + s

        return s

    def graham_convex_hull(self):
        """Calcula el cierre convexo de los puntos en points. Regresamos
        una lista con los puntos en el contorno del cierre convexo en
        dirección opuesta a las manecillas del reloj."""

        # Se utiliza un deque como stack para lograr complejidad O(1)
        # al hacer push y pop
        stack = deque([self.min_y])
        points = self.points.copy()
        p = points.pop(0)
        while len(points) > 0:
            if len(stack) == 1:
                stack.append(p)
                p = points.pop(0)
                continue

            if cross_product(stack[-2], stack[-1], p) > 0:
                stack.append(p)
                p = points.pop(0)
            else:
                stack.pop()

        # Revisamos si el último punto está en el contorno del cierre
        while True:
            if cross_product(stack[-2], stack[-1], p) > 0:
                stack.append(p)
                break
            else:
                stack.pop()

        return list(stack)


def draw(points, min_y, convex_hull):
    """Dibuja la lista de puntos y el cierre convexo"""
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.title("Cierre convexo de un conjunto de puntos")

    x_points = [p.x for p in points]
    x_points.append(min_y.x)
    y_points = [p.y for p in points]
    y_points.append(min_y.y)
    plt.scatter(x_points, y_points, marker="o")

    x_points = [p.x for p in convex_hull]
    x_points.append(min_y.x)
    y_points = [p.y for p in convex_hull]
    y_points.append(min_y.y)
    plt.plot(x_points, y_points)
    plt.show()


def main():
    graham = GrahamConvexHull(N_POINTS)

    print(f"PUNTO CON COORDENADA Y MENOR\n{graham.min_y}\n")
    print("PUNTOS ORDENADOS")
    for i in graham.points:
        print(i)
    print("\nPUNTOS EN EL CONTORNO DEL CIERRE CONVEXO")
    for i in graham.graham_convex_hull():
        print(i)

    draw(graham.points, graham.min_y, graham.graham_convex_hull())


if __name__ == "__main__":
    main()
