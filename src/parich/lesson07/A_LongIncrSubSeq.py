task='''
Задача на дин. программирование: наибольшая возростающая подпоследовательность
см.     https://ru.wikipedia.org/wiki/Задача_поиска_наибольшей_увеличивающейся_подпоследовательности
        https://en.wikipedia.org/wiki/Longest_increasing_subsequence

Дано:
    целое число 1≤n≤1000
    массив A[1…n] натуральных чисел, не превосходящих 2E9.

Необходимо:
    Выведите максимальное 1<=k<=n, для которого гарантированно найдётся
    подпоследовательность индексов i[1]<i[2]<…<i[k] <= длины k,
    для которой каждый элемент A[i[k]]больше любого предыдущего
    т.е. для всех 1<=j<k, A[i[j]]<A[i[j+1]].

Решить задачу МЕТОДАМИ ДИНАМИЧЕСКОГО ПРОГРАММИРОВАНИЯ

    Sample Input:
    5
    1 3 3 2 6

    Sample Output:
    3
'''
def getSeqSize(filename):
    f = open(filename)
    n = int(f.readline().replace("\n", ''))
    array = list(map(int, f.readline().replace("\n", '').split(" ")))
    assert(n==len(array))
    d = [1] * len(array)
    ans = 0
    for i in range(0, n):
        for j in range(0, i):
            if array[i] > array[j] and d[j] + 1 > d[i] :
                d[i] = d[j] + 1
                if ans < d[i]:
                    ans = d[i]
    return ans

def main():
    filename = "dataA.txt"
    answer = getSeqSize(filename)
    print(answer)

# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
