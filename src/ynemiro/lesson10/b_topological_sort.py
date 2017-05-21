task = '''
Разработайте алгоритм топологической сортировки для заданного графа.
Граф направленный и невзвешенный. В примере задан граф вида.

A   D   G
 \ / \ /
  C   F
 / \ / \
B   E   H

Все связи направлены слева-направо.
Перебор вершин выполняйте в алфавитном порядке.
Выведите топологически отсортированный граф в виде списока вершин с их pre и post - значениями.
A(0,13)   - pre=0  post=13
E(10,11)  - pre=10 post=11

Для заданного на рисунке графа (задан в dataBdemo.txt) ожидается такой вывод:
G(4,5)
H(6,7)
F(3,8)
D(2,9)
E(10,11)
C(1,12)
A(0,13)
B(14,15)

'''


def printGraphB(fin):
    lines = []
    graph = dict()
    visited = set()
    dist = dict()
    count = [0]
    st = []

    def explorer(vertex, count):
        if not vertex in visited:
            c = list()
            c.append(count[0])
            dist.update({vertex: c})
            visited.add(vertex)
            count[0] += 1
            if graph.get(vertex)[0] != '':
                for to in graph.get(vertex):
                    explorer(to, count)
                t = dist.get(vertex)
                t.append(count[0])
                dist.update({vertex: t})
                count[0] += 1
                st.append(vertex)
            else:
                t = dist.get(vertex)
                t.append(count[0])
                dist.update({vertex: t})
                count[0] += 1
                st.append(vertex)

    for line in fin.readlines():
        key, value = line.replace("\n", "").split(":")
        value = sorted(value.split(","))
        graph.update({key: value})

    for vertex in sorted(graph.keys()):
        if not vertex in visited:
            explorer(vertex, count)

    for l in st:
        lines.append(l + "(" + str(dist.get(l)).replace("[", "") .replace("]", "").replace(" ", "") + ")")

    return lines



def main():
    f = open("dataB.txt")
    lines = printGraphB(f)
    for line in lines:
        print(line)


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
