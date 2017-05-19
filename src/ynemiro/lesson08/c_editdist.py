task = '''
Задача на программирование: расстояние Левенштейна
    https://ru.wikipedia.org/wiki/Расстояние_Левенштейна
    http://planetcalc.ru/1721/
Дано:
    Две данных непустые строки длины не более 100, содержащие строчные буквы латинского алфавита.
Необходимо:
    Решить задачу МЕТОДАМИ ДИНАМИЧЕСКОГО ПРОГРАММИРОВАНИЯ
    Итерационно вычислить алгоритм преобразования двух данных непустых строк
    Вывести через запятую редакционное предписание в формате:
     операция("+" вставка, "-" удаление, "~" замена, "#" копирование)
     символ замены или вставки
    Sample Input 1:
    ab
    ab
    Sample Output 1:
    #,#,
    Sample Input 2:
    short
    ports
    Sample Output 2:
    -s,~p,#,#,#,+s,
    Sample Input 3:
    distance
    editing
    Sample Output 2:
    +e,#,#,-s,#,~i,#,-c,~g,
    P.S. В литературе обычно действия редакционных предписаний обозначаются так:
    - D (англ. delete) — удалить,
    + I (англ. insert) — вставить,
    ~ R (replace) — заменить,
    # M (match) — совпадение.
'''


def getDistanceEdintingC(inpstr, outstr):
    a, h = inpstr, len(inpstr)
    b, w = outstr, len(outstr)
    d = [[-1] * (w + 1) for i in range(h + 1)]
    for i in range(0, h + 1):
        for j in range(0, w + 1):
            if d[i][j] == -1:
                if i == 0:
                    d[i][j] = j
                elif j == 0:
                    d[i][j] = i
                else:
                    insdist = d[i][j - 1] + 1
                    deldist = d[i - 1][j] + 1
                    char_a = a[i - 1]
                    char_b = b[j - 1]
                    cost = 0 if char_a == char_b else 1
                    subdist = d[i - 1][j - 1] + cost
                    d[i][j] = min(insdist, deldist, subdist)
    res = ""
    i, j = h, w

    while i > 0 or j > 0:
        if d[i][j - 1] == d[i][j] - 1:
            op = "+"
            sym = b[j - 1]
            res = op + sym + "," + res
            j = j - 1
        elif d[i - 1][j] == d[i][j] - 1:
            op = "-"
            sym = a[i - 1]
            res = op + sym + "," + res
            i = i - 1
        elif d[i - 1][j - 1] == d[i][j] - 1:
            op = "~"
            sym = b[j - 1]
            res = op + sym + "," + res
            i, j = i - 1, j - 1
        else:
            op = "#"
            res = op + "," + res
            i, j = i - 1, j - 1
    return res


def main():
    f = open("dataABC.txt")

    def solve(f):
        a = f.readline().replace("\n", "")
        b = f.readline().replace("\n", "")
        c = getDistanceEdintingC(a, b)
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
