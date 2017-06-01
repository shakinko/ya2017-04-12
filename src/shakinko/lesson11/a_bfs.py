import math
import queue

task = '''
Оптимальное прохождение лабиринта. 

Даны комнаты, между комнатами есть двери, нужно определить
кратчайший путь из заданной комнаты во все остальные.

Задача представлена в виде графа, где вершины - комнаты, ребра - двери.
Разработайте алгоритм определения словаря кратчайших путей графа с обходом в ширину. 
Граф ненаправленный и невзвешенный. В примере задан лабиринт вида:

A - B - C
  \ |   |
D   E - F
| \     |
G - H - I

В первой строке файла - стартовая вершина, в остальных - структура лабиринта
Перебор вершин выполняйте в алфавитном порядке.
Для заданного лабиринта (задан в dataA.txt) ожидается такой вывод:

A=0
B=1
C=2
D=5
E=1
F=2
G=5
H=4
I=3
'''

def print_bfs_a(fin):
    def bfs(fin, start):
        dist = dict()

        for vertex in graph:
            dist.update({vertex: math.inf if not vertex == start else 0})

        q=queue.Queue()
        q.put(start)
        while not q.empty():
            # u это откуда. u это обновлённая, v неизвестная = inf
            u = q.get()
            for v in graph.get(u):
                if dist.get(v) == math.inf:
                    dist.update({v:dist.get(u)+1})
                    q.put(v)


        print(dist)
        return dist

    start = fin.readline().replace("\n", "")
    graph = dict()

    for line in fin.readlines():
        key, value = line.replace("\n", "").split(":")
        value = list(value.split(","))
        graph.update({key:value})

    # print (graph)
    for v in graph: print(v + ":" + str(graph.get(v)))
    dist = bfs(graph, start)
    lines = []
    for vertex in dist.keys():
        lines.append(vertex + "=" + str(dist.get(vertex)))


    # метод должен вернуть массив строк (для вывода в консоль)
    return lines

def main():
    f = open("dataA.txt")
    lines = print_bfs_a(f)
    for line in lines:
        print(line)

# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
