task = '''
Первая строка содержит число 1<=n<=10000, вторая - n натуральных чисел, не превышающих 10.
Выведите упорядоченную по неубыванию последовательность этих чисел.

При сортировке реализуйте метод со сложностью O(n)

Пример: https://karussell.wordpress.com/2010/03/01/fast-integer-sorting-algorithm-on/
Вольный перевод: http://programador.ru/sorting-positive-int-linear-time/
'''


def countSort(inarray):
    # тут реализуйте логику задачи с применением сортировки подсчетом
    n = 10
    count_array = [i * 0 for i in range(0, n)]
    out_array = []
    for num in inarray:
        count_array[num] += 1
    for i in range(1, len(count_array)):
        while count_array[i] > 0:
            out_array.append(i)
            count_array[i] -= 1
    return out_array
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
