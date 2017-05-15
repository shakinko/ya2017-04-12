task = '''
Разработайте алгоритм поиска в глубину для заданного графа.
Граф ненаправленный и невзвешенный. В примере задан граф вида.

A - B - C
  \ |   |
D   E - F
| \     |
G - H   I

Перебор вершин выполняйте в алфавитном порядке.
Выведите каждое ребро в порядке обхода как древестное или как обратное в формате:
A->B  - древестное
A<-E - обратное.
Дважды одно ребро не выводите (даже если оно повторно определено). 

Выведите также список вершин с их pre и post - значениями.
A(1,14) - pre=1 post=14
E(3,4)  - pre=3 post=4

Для заданного на рисунке графа (задан в dataA.txt) ожидается такой вывод:
A->B
B->C
C->F
F->E
A<-E
B<-E
F->I
D->G
G->H
D<-H
A(0,11)
B(1,10)
C(2,9)
D(12,17)
E(4,5)
F(3,8)
G(13,16)
H(14,15)
I(6,7)

'''


def printGraphA(fin):
    def explore(vertex):
        if not vertex in visited:
            visited.add(vertex)
            for to in graph.get(vertex):
                ename=sorted([to,vertex])
                ename=str(ename[0])+str(ename[1])
                if not ename in edges:
                    edges.append(ename)
                    if not to in visited:
                        lines.append(vertex+"->"+to)
                        explore(to)
                    else:
                        lines.append(to+"<-"+vertex)

    def dfs(graph):
        for vertex in sorted(graph.keys()):
            if not vertex in visited:
                explore(vertex)

    lines = []
    visited = set()
    edges = []
    graph = dict()
    for line in fin.readlines():
        key, value = line.replace("\n", "").split(":")
        value = sorted(value.split(","))
        graph.update({key: value})
    dfs(graph)
    # for v in graph: print(v + ":" + str(graph.get(v)))
    return lines


def main():
    f = open("dataA.txt")
    lines = printGraphA(f)
    for line in lines:
        print(line)


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
