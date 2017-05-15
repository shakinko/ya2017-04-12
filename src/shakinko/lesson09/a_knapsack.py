task = '''
Задача на программирование: рюкзак с повторами

Первая строка входа содержит целые числа
    1<=W<=100000     вместимость рюкзака
    1<=n<=300        сколько есть вариантов золотых слитков
                     (каждый можно использовать множество раз).
Следующая строка содержит n целых чисел, задающих веса слитков:
  0<=w[1]<=100000 ,..., 0<=w[n]<=100000

Найдите методами динамического программирования
максимальный вес золота, который можно унести в рюкзаке.


Sample Input:
10 3
1 4 8
Sample Output:
10

Sample Input 2:
15 3
2 8 16
Sample Output 2:
14
'''


def getMaxWeightA(filename):
    f = open(filename)
    W, n = map(int, f.readline().replace("\n", "").split(" "))
    item = list(map(int, f.readline().replace("\n", "").split(" ")))
    d = [0] * (W + 1)
    assert len(item) == n
    for w in range(1, W + 1):
        # цикл по кускам.  Входит ли кусок в этот объем wi
        # с учетом того, что мы уже положили
        for i in range(0, n):
            wi = item[i]
            ci = item[i]
            prev = w-wi
            if prev >= 0:
                d[w] = max(d[w], d[prev]+ci)

    return d[W]

def main():
    res = getMaxWeightA("dataA.txt")
    print(res)


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
