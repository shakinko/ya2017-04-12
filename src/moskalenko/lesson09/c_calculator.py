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
    return [1]


def main():
    res = calcC("dataC.txt")
    count=len(res)-1
    print(count)
    print(res)


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
