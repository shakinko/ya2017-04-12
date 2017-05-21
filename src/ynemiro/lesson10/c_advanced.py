task = '''
Определите компоненты сильной связности для заданного графа
Выведите топологически отсортированные компоненты сильной связности
для этого графа.

Тестовое покрытие для этой задачи реализовать сложно. 
Тут будет проверка вручную.
'''


def printGraphC(fin):
    lines = []
    graph = dict()
    trans_graph = dict()  # транспонированный граф
    visited = set()
    dist = dict()  # словарь с pre и post значениями
    count = [0]  # счетчик для подсчета pre/post
    st = []  # массив с vertex после топологической сортировки

    def explorer(vertex, count, graph):
        if not vertex in visited:
            c = list()
            c.append(count[0])
            dist.update({vertex: c})
            visited.add(vertex)
            count[0] += 1
            if graph.get(vertex)[0] != '':
                for to in graph.get(vertex):
                    explorer(to, count, graph)

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
        trans_graph.update({key: ['']})  # заодно делаем заготовку для транспонированного графа

    # транспонируем граф

    for v in sorted(graph.keys()):
        for child in graph.get(v):
            t = trans_graph.get(child)
            if t[0] == '':
                t[0] = v
            else:
                t.append(v)
                trans_graph.update({child: sorted(t)})

            #  Делаем топологическую сортировку

    for vertex in sorted(graph.keys()):
        if not vertex in visited:
            explorer(vertex, count, graph)

        # Очищаем посещенные графы, счетчик pre/post, сохраняем порядок vertex после топологической сортировки

    visited.clear()
    count = [0]
    st_temp = st
    st = []

    # Делаем обход траспонированного графа в порядке уменьшения окончания обхода vertex

    for v in reversed(st_temp):
        if not v in visited:
            explorer(v, count, trans_graph)

        # Выводим компонентами сильной связанности, учитывая что есть ребро между компонентами, при котором время выхода из одной компоненты
        # сильной связанности всегда меньше чем время входа в vertex другой.
    m = ''
    for l in st:
        if m == '':
            m = l
            lines.append(l + "(" + str(dist.get(l)).replace("[", "").replace("]", "").replace(" ", "") + ")")
        elif dist.get(l)[0] > dist.get(m)[1]:
            lines.append("Новая компонента сильной связанности")
            lines.append(l + "(" + str(dist.get(l)).replace("[", "").replace("]", "").replace(" ", "") + ")")
            m = l
        else:
            m = l
            lines.append(l + "(" + str(dist.get(l)).replace("[", "").replace("]", "").replace(" ", "") + ")")

    return lines


def main():
    f = open("dataC.txt")
    lines = printGraphC(f)
    for line in lines:
        print(line)


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
