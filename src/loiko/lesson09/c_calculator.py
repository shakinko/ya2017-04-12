import math

task = '''

У вас есть примитивный калькулятор, который умеет выполнять всего 
три операции с текущим числом x: 
    заменить x на 2x, 
    заменить x на 3x
    заменить x на x+1
По данному целому числу 1≤n≤1E5 определите минимальное число операций k, 
необходимое, чтобы получить n из 1. 
Выведите число k и последовательность промежуточных чисел.

Sample Input 1:
1
Sample Output 1:
0
1
 
Sample Input 2:
5
Sample Output 2:
3
1 2 4 5
 
Sample Input 3:
96234
Sample Output 3:
14
1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234 
'''


def calcC(filename):
    f = open(filename)
    N = int(f.readline().replace("\n", ""))
    #N=5
    d_array = [math.inf]*(N+1)
    num_array = [-1]*(N+1)

    d_array[N]=0
    for i in range (N, 0, -1):
        temp_d = d_array[i]+1
        if i%3==0 and (d_array[i//3]>temp_d):
            d_array[i // 3] = temp_d
            num_array[i//3] = i
        if i%2==0 and (d_array[i//2]>temp_d):
            d_array[i // 2] = temp_d
            num_array[i // 2] = i
        if d_array[i-1]>temp_d:
            d_array[i - 1] = temp_d
            num_array[i - 1] = i
    while i != 1:
        for i in range (1, N):
            print (i)
            i = num_array[i]

    res = []
    while i!=-1:
        i==1
        res.append(i)
        i = num_array[i]
    return res
    print (len(res)-1)

def main():
    res = calcC("dataC.txt")
    count=len(res)-1
    print(count)
    print(' '.join(str(e) for e in res))



# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
