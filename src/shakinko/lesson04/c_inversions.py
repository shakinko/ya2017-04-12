import os

task = '''
Рассчитать число инверсий одномерного массива.
Сложность алгоритма должна быть не хуже, чем O(n log n)

Первая строка содержит число 1<=n<=10000,
вторая - массив A[1…n], содержащий натуральные числа, не превосходящие 10E9.
Необходимо посчитать число пар индексов 1<=i<j<n, для которых A[i]>A[j]A[i]>A[j].

    (Такая пара элементов называется инверсией массива.
    Количество инверсий в массиве является в некотором смысле
    его мерой неупорядоченности: например, в упорядоченном по неубыванию
    массиве инверсий нет вообще, а в массиве, упорядоченном по убыванию,
    инверсию образуют каждые (т.е. любые) два элемента.
    )

Sample Input:
5
2 3 9 2 9
Sample Output:
2
'''


class inv_counter():

    #измените конструктор так, чтобы в inv было число инверсий массива
    def __init__(self, m) -> None:
        self.inv=None

def main():
    fn = os.path.dirname(os.path.abspath(__file__)) + "/dataC.txt"
    f = open(fn)
    size = int(f.readline().replace("\n", ""))
    strings = f.readline().replace("\n", "").split(" ")
    array = list(map(int, strings))
    assert size==len(array)
    print(" array=", array)
    inv=inv_counter(array).inv
    print(" inv=", inv)


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
