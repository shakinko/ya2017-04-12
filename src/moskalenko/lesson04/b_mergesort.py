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


def merge(left, right):
    i = j = 0
    res = list()

    for k in range(0, len(left) + len(right)):
        if (left[i] >= right[j]):
            res.append(right[j])
            if j < len(right) - 1:
                j += 1
            else:

                while i < len(left):
                    res.append(left[i])  # добавляем остаток из left
                    i += 1
                break

        elif (left[i] < right[j]):
            res.append(left[i])
            if i < len(left) - 1:
                i += 1
            else:

                while j < len(right):
                    res.append(right[j])  # добавляем остаток из right
                    j += 1
                break
    return res


def mergeSort(m):
    if len(m) < 2:
        return m

    c = len(m) // 2
    # разделим по возможности поровну (+/- 1)
    left = mergeSort(m[:c])
    right = mergeSort(m[c:])
    return merge(left, right)


def main():
    fn = os.path.dirname(os.path.abspath(__file__)) + "/dataB.txt"
    f = open(fn)
    size = int(f.readline().replace("\n", ""))
    strings = f.readline().replace("\n", "").split(" ")
    array = list(map(int, strings))
    assert size == len(array)

    print(" array=", array)
    sort = mergeSort(array)
    print(" sort =", sort)


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
