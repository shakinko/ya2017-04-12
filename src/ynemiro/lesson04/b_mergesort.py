import os

task = '''
Реализуйте сортировку слиянием для одномерного массива.
Сложность алгоритма должна быть не хуже, чем O(n log n)

Первая строка содержит число 1<=n<=10000,
вторая - массив A[1…n], содержащий натуральные числа, не превосходящие 10E9.
Необходимо отсортировать полученный массив.

Sample Input:
5
2 3 9 2 9
Sample Output:
2 2 3 9 9
'''


def merge(lm, lr):
    l = 0
    r = 0
    res = []
    while (l + r) < (len(lm) + len(lr)):
        if r >= len(lr) or (l < len(lm) and lm[l] <= lr[r]):
            res.append(lm[l])
            l += 1
        else:
            res.append(lr[r])
            r += 1
    return res


def mergeSort(m):
    # ваше решение
    lm = []
    lr = []
    if len(m) > 1:
        c = len(m) // 2
        lm = m[:c]
        lr = m[c:]
        mergeSort(lm)
        mergeSort(lr)
    return merge(lm, lr)


def main():
    fn = os.path.dirname(os.path.abspath(__file__)) + "/dataB.txt"
    f = open(fn)
    size = int(f.readline().replace("\n", ""))
    strings = f.readline().replace("\n", "").split(" ")
    array = list(map(int, strings))
    assert size == len(array)

    print(" array=", array)
    sort = mergeSort(array)
    print(" sort=", sort)


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
