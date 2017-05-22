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
        nonlocal clo
        if not vertex in visited:

            # previsit
            pre.update({vertex: clo})
            clo += 1

            visited.add(vertex)
            for to in graph.get(vertex):
                ename = ord(to) * ord(vertex)  # наши вершины обозначены A..Z и даже при простом перемножении не дадут коллизий
                                               # для более сложных графов генерировать ключ надо будет по более сложной формуле

                if ename not in edges:
                    edges.append(ename)

                    if to not in visited:
                        lines.append(vertex+"->"+to)
                        explore(to)
                    else:
                        lines.append(to+"<-"+vertex)
        # postvisit
        post.update({vertex: clo})
        clo += 1

    def dfs(graph):
        for vertex in sorted(graph.keys()):
            if vertex not in visited:
                explore(vertex)

    lines = []
    clo = 0
    visited = set()
    edges = []
    pre = {}
    post = {}
    graph = {}


    for line in fin.readlines():
        key, value = line.replace("\n", "").split(":")
        value = sorted(value.split(","))
        graph.update({key: value})


    dfs(graph)
    # for v in graph: print(v + ":" + str(graph.get(v)))

    for vertex in sorted(graph.keys()):     # работает и без sorted
        lines.append(vertex + "(" + str(pre.get(vertex)) + "," + str(post.get(vertex)) + ")")


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
