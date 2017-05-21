task = '''
Первая строка содержит число 1<=n<=10000, вторая - n натуральных чисел, не превышающих 10.
Выведите упорядоченную по неубыванию последовательность этих чисел.

При сортировке реализуйте метод со сложностью O(n)

Пример: https://karussell.wordpress.com/2010/03/01/fast-integer-sorting-algorithm-on/
Вольный перевод: http://programador.ru/sorting-positive-int-linear-time/
'''


def countSort(inarray):
    min_item = max_item = 0
    for i in range(0, len(inarray)):
        if inarray[i] < min_item: min_item = inarray[i]
        if inarray[i] > max_item: max_item = inarray[i]

    if min_item < 0:
        shift = - min_item
    else:
        shift = 0

    M = max_item + shift + 1
    B = [0] * M
    for j in inarray:
        B[j + shift] += 1

    j = 0
    for item in range(M):
        for i in range(B[item]):
            inarray[j] = item - shift
            j += 1
    return inarray
    # !!!!!!!!!!!!!!!!!!!!!!!!!     КОНЕЦ ЗАДАЧИ     !!!!!!!!!!!!!!!!!!!!!!!!!


def main():
    # подготовка к чтению данных
    f = open("dataB.txt")

    def arr(filename):
        str = filename.readline().replace("\n", "").split(" ")
        return list(map(int, str))

    count = arr(f)[0]
    array = arr(f)
    f.close()
    assert count == len(array)
    print(countSort(array))
    print(sorted(array))


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
