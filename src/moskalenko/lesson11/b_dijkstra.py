import heapq
import math

task = '''
Оптимальное прохождение карты. 

Даны города, между ними есть дороги с односторонним движением заданной длины, 
нужно определить кратчайшие расстояния из заданного города во все остальные.

Задача представлена в виде графа карты, где вершины - города, ребра - дороги.
Разработайте решение на основе алгоритма Дейкстры. 
Граф направленный и взвешенный. В примере задан граф карты вида:

См. image_B.jpg

В первой строке файла - стартовая вершина, в остальных - структура графа карты
Перебор вершин выполняйте в алфавитном порядке.
Для заданного графа карты (задан в dataB.txt) ожидается такой вывод:

A=0
B=1
C=3
D=4
E=4
F=6
G=5
H=6

'''


class Dist:
    vertex = "X"
    distance = 0

    def __init__(self, vertex, distance) -> None:
        super().__init__()
        self.vertex = vertex
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __str__(self) -> str:
        return str(self.vertex) + "=" + str(self.distance)


def getDist(arr, vertex):
    for d in arr:
        if vertex == d.vertex:
            return d.distance

def setDist(arr, vertex, value):
    for d in arr:
        if vertex == d.vertex:
            d.distance=value

# очередь, выделена в отдельный
# класс для удобного использования

class Heap():
    def __init__(self) -> None:
        self._heap = []
        heapq.heapify(self._heap)

    def size(self):
        return len(self._heap)

    def push(self, node):
        heapq.heappush(self._heap, node)

    def pop(self):
        n = heapq.heappop(self._heap)
        return n

    def update(self):
        heapq.heapify(self._heap)



def print_b_dijkstra(fin):
    lines = []
    # метод должен вернуть массив строк (для вывода в консоль)
    return lines

def main():
    f = open("dataB.txt")
    lines = print_b_dijkstra(f)
    for line in lines:
        print(line)


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
