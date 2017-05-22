from bisect import bisect, bisect_left
from random import randint

task = '''
Дано:
    целое число 1<=n<=1E5 ( ОБРАТИТЕ ВНИМАНИЕ НА РАЗМЕРНОСТЬ! )
    массив A[1…n] натуральных чисел, не превосходящих 2E9.

Необходимо:
    Выведите максимальное 1<=k<=n, для которого гарантированно найдётся
    подпоследовательность индексов i[1]<i[2]<…<i[k] <= длины k,
    для которой каждый элемент A[i[k]] не больше любого предыдущего
    т.е. для всех 1<=j<k, A[i[j]]>=A[i[j+1]].

    В первой строке выведите её длину k,
    во второй - её индексы i[1]<i[2]<…<i[k]
    соблюдая A[i[1]]>=A[i[2]]>= ... >=A[i[n]].

    (индекс начинается с 1)

Решить задачу МЕТОДАМИ ДИНАМИЧЕСКОГО ПРОГРАММИРОВАНИЯ
Время n*log(n)

    Sample Input:
    5
    5 3 4 4 2

    Sample Output:
    4
    1 3 4 5
'''


def getNotUpSeqIndexses(filename):
    # тут реализуйте логику задачи методами динамического программирования (!!!)
    # подумайте как стоит организовать динамику, чтобы получить решение за n log n
    # тесты не проверят скорость, а я проверю, и скорость и идею ;)
    # для корректной проверки рекомендуется сгенерировать тестовый файл размера 1E5
    # !!!!!!!!!!!!!!!!!!!!!!!!!     НАЧАЛО ЗАДАЧИ     !!!!!!!!!!!!!!!!!!!!!!!!!

    INF = int(2e10)  # будем считать это бесконечностью, т.к. на входе у нас числа < 2E9

    # считываем исходный массив
    f = open(filename)
    n = int(f.readline().replace("\n", ""))
    array = list(map(int, f.readline().replace("\n", "").split(" ")))
    array.append(0)
    array = list(reversed(array))
    len_a = len(array)

    d = [INF] * len_a
    d[0] = -INF

    pos = [0] * len_a
    pre = [0] * len_a

    for i in range(len_a):
        j = bisect(d, array[i])
        if d[j - 1] <= array[i] < d[j]:
            d[j] = array[i]
            pos[j] = i
            pre[i] = pos[j - 1]

    res = []
    i = pos[bisect_left(d, INF)-1]
    while i:
        res.append(len_a - i)
        # res.append(array[i])
        i = pre[i]

    print(len(res))
    return res
    # !!!!!!!!!!!!!!!!!!!!!!!!!     КОНЕЦ ЗАДАЧИ     !!!!!!!!!!!!!!!!!!!!!!!!!


def main():
    print ("Входные данные: dataC.txt из гита")
    filename = "dataC.txt"
    answer = getNotUpSeqIndexses(filename)
    for i in answer: print(i, end=" ")

    print("\n\nВходные данные: сгенерированный массив из 100000 случайных элементов")
    f = open('big_data.txt', 'w')
    f.write('11' + '\n')

    for i in range(0, 99999):
        f.write(str(randint(1, 2E9)) + " ")
    f.write(str(randint(1, 2E9)) + "\n")
    f.close()
    filename = "big_data.txt"
    answer = getNotUpSeqIndexses(filename)
    for i in answer: print(i, end=" ")


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
