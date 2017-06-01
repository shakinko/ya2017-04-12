import math

task = '''

Финансовые балансы. 

Даны счета, между ними проводятся расчеты заданного объема, 
Задача представлена в виде графа платежей, где вершины - счета, ребра - расчеты.

Нужно определить кратчайшие расстояния графа из заданной вершины.
Разработайте решение на основе алгоритма Беллмана-Форда. 
Граф направленный и взвешенный. В примере задан граф карты вида:

См. image_С.jpg

Тестовое покрытие для этой задачи не реализовано. 
Тут будет проверка вручную.
'''

def print_c_bellman_ford(fin):
    W, F = {}, {}
    start = fin.readline().replace("\n", "")

    for line in fin.readlines():
        key, value = line.split(":")
        for i in [s.split("=") for s in value.split(",")]:
            W.update({(key, i[0]): int(i[1])})
            F[key], F[i[0]] = [math.inf if i[0] != start else 0] * 2  # все уникальные вершины, где бы они ни нашлись

    for k in range(1, len(F)):
        for j, i in W.keys():
            if F[j] + W[j, i] < F[i]:
                F[i] = F[j] + W[j, i]

    return [d + "=" + str(F[d]) for d in sorted(F.keys())]   # метод должен вернуть массив строк (для вывода в консоль)

def main():
    f = open("dataC.txt")
    lines = print_c_bellman_ford(f)
    for line in lines:
        print(line)


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
