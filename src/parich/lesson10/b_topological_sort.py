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
     def explore(vertex):
         nonlocal clo
         if vertex not in visited:
             pre.update({vertex: clo})
             clo += 1
             visited.add(vertex)
             for to in graph.get(vertex):
                 if to == "": break
                 if to not in visited:
                     explore(to)
         post.update({vertex: clo})
         sort_lines.append(vertex + "(" + str(pre.get(vertex)) + "," + str(clo) + ")")
         clo += 1
     def dfs(graph):
         for vertex in sorted(graph.keys()):  # yfgh
             if vertex not in visited:
                 explore(vertex)
     clo = 0
     sort_lines = []
     visited = set()
     pre, post, graph = {}, {}, {}
     for line in fin.readlines():
         key, value = line.replace("\n", "").split(":")
         value = sorted(value.split(","))
         graph.update({key: value})
     dfs(graph)
     return sort_lines


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