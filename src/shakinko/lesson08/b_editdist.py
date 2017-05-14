task = '''
Задача на программирование: расстояние Левенштейна
    https://ru.wikipedia.org/wiki/Расстояние_Левенштейна
    http://planetcalc.ru/1721/

Дано:
    Две данных непустые строки длины не более 100, содержащие строчные буквы латинского алфавита.

Необходимо:
    Решить задачу МЕТОДАМИ ДИНАМИЧЕСКОГО ПРОГРАММИРОВАНИЯ
    Итерационно вычислить расстояние редактирования двух данных непустых строк

    Sample Input 1:
    ab
    ab
    Sample Output 1:
    0

    Sample Input 2:
    short
    ports
    Sample Output 2:
    3

    Sample Input 3:
    distance
    editing
    Sample Output 3:
    5
'''


def getDistanceEdintingB(inpstr, outstr):
    a, h = inpstr, len(inpstr)
    b, w = outstr, len(outstr)
    d = [[-1] * (w + 1) for i in range(h + 1)]

    # чтобы избавиться от рекурсии нужен цикл
    for i in range(0, h + 1):
        for j in range(0, w + 1):
            if d[i][j] == -1:
                # тогда надо считать
                # i=0 это самая верхняя строчка
                if i == 0:
                    d[i][j] = j
                elif j == 0:
                    d[i][j] = i
                else:
                    # вставка, значит мы пришли слева
                    insdist = d[i][j - 1] + 1
                    deldist = d[i - 1][j] + 1
                    char_a = a[i - 1]
                    char_b = b[j - 1]
                    cost = 0 if char_a == char_b else 1
                    subdist = d[i - 1][j - 1] + cost
                    d[i][j] = min(insdist, deldist, subdist)

                    # for s in d:
                    #    print(s)
                    # print("-----------------------")
    return d[i][j]

def main():
    f = open("dataABC.txt")

    def solve(f):
        a = f.readline().replace("\n", "")
        b = f.readline().replace("\n", "")
        c = getDistanceEdintingB(a, b)
        print(a, b, c)

    # String 1 & 2
    solve(f)
    # String 3 & 4
    solve(f)
    # String 5 & 6
    solve(f)
    f.close()


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
