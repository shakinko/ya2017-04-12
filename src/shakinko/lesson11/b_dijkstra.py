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

INF = 1e10

class Dist:
    vertex = "X"
    distance = 0

    def __init__(self, vertex, distance) -> None:
        super().__init__()
        self.vertex = vertex
        self.distance = int(distance)

    def __lt__(self, other):  # x < y вызывает x.__lt__(y)
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
# Элемент heap[0] всегда содержит наименьший элемент

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
    def bfs_dijkstra(fin, start):
        dist = []
        for vertex in graph:
            dist.append(Dist(vertex, INF if not vertex == start else 0))  # наш результат поначалу = 0, INF, ...

        q = Heap()
        q.push(Dist(start, 0))             # start поначалу это просто строка, а нам нужен Dist

        while q.size() > 0:
            u = q.pop()                    # u это откуда, она уже обновлена, v неизвестная = inf
            for v in graph.get(u.vertex):  # v это теперь Dist число там l(u, v) . В задаче А это были просто вершины
                if getDist(dist, u.vertex) + v.distance < getDist(dist, v.vertex):
                    setDist(dist, v.vertex, getDist(dist, u.vertex) + v.distance)  # dist[v] <-- dist[u] + l(u, v)  # обновлённое значение
                    q.push(v)
        return dist

    start = fin.readline().replace("\n", "")
    graph = {}

    for line in fin.readlines():
        key, value = line.replace("\n", "").split(":")  # хороший пример использования split

        # где value пустое, там у нас просто пустой список
        d = [Dist(*s.split("=")) for s in value.split(",")] if value else []  # * распаковывает коллекцию и передает ее элементы в функцию.
        graph.update({key: d})


    for v in graph:
        print(v + ":" + ",".join(map(str, graph.get(v))) if graph.get(v) else "")

    dist = bfs_dijkstra(graph, start)
    lines = []
    # метод должен вернуть массив строк (для вывода в консоль)
    for d in dist: lines.append(str(d))

    return lines

def main():
    f = open("dataB.txt")
    lines = print_b_dijkstra(f)
    for line in lines: print(line)


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
