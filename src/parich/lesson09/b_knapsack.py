task = '''
Задача на программирование: рюкзак без повторов

Первая строка входа содержит целые числа
    1<=W<=100000     вместимость рюкзака
    1<=n<=300        число золотых слитков
                    (каждый можно использовать только один раз).
Следующая строка содержит n целых чисел, задающих веса каждого из слитков:
  0<=w[1]<=100000 ,..., 0<=w[n]<=100000

Найдите методами динамического программирования
максимальный вес золота, который можно унести в рюкзаке.

Sample Input:
10 3
1 4 8
Sample Output:
9
'''


def getMaxWeightB(filename):
    f = open(filename)
    W, n = map(int, f.readline().replace("\n", "").split(" "))
    item = list(map(int, f.readline().replace("\n", "").split(" ")))
    assert len(item) == n
    d = [[0] * (W + 1) for i in range(n + 1)]
    # for s in d:
    #     print(s)
    for i in range(1, n + 1):
        wi = item[i - 1]
        ci = item[i - 1]
        for w in range(1, W + 1):
            if w - wi >= 0:
                d[i][w] = max(d[i - 1][w], d[i - 1][w - wi] + ci)
            else:
                d[i][w] = d[i - 1][w]

    return d[n][W]


def main():
    res=getMaxWeightB("dataB.txt")
    print(res)


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()

