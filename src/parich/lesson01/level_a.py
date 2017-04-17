# coding=utf-8
from unittest import TestCase

'''
Level A. Вам Необходимо реализовать 3 способа для вычисления чисел Фибоначчи

1) a_01_naive_fibonachi_recursive (время O(2^n))
рекурсивный вариант, в котором код совпадает с мат.определением чисел Фибоначчи
2) a_02_cashed_fibonachi(n) (время O(n))
рекурсивный вариант с кешированием уже рассчитанных значений
3) a_03_iteration_fibonachi(n) (время O(n)):
итерационный вариант с кешированием двух последних значений

Проверьте работоспособность через ввод и тесты
'''


def f_o1(n):
    assert n >= 0
    f = 1 / 5 ** (1 / 2) * (((1 + 5 ** (1 / 2)) / 2) ** n - ((1 - 5 ** (1 / 2)) / 2) ** n)
    return f


def a_01_naive_fibonachi_recursive(n):
    fun = a_01_naive_fibonachi_recursive
    assert n >= 0
    if n < 2:
        return n
    else:
        return fun(n - 2) + fun(n - 1)

cashe = {}

def a_02_cashed_fibonachi(n):
    fun = a_02_cashed_fibonachi
    assert n >= 0
    if cashe.get(n):
        return cashe.get(n)
    if n < 2:
        res = n
    else:
        res = fun(n - 2) + fun(n - 1)
    cashe.setdefault(n, res)
    return res


def a_03_iteration_fibonachi(n):
    assert n >= 0
    a, b = 0, 1
    if n < 2:
        return n
    else:
        for i in range(0, n):
            a, b = b + a, a
        return a


def main():
    n = int(input("Input n:"))
    tmpl = "a_01_naive_fibonachi_recursive result={}\n" \
           + "a_02_cashed_fibonachi result={}\n" \
           + "a_03_iteration_fibonachi result={}\n"
    s = tmpl.format(str(a_01_naive_fibonachi_recursive(n)),
                    str(a_02_cashed_fibonachi(n)),
                    str(a_03_iteration_fibonachi(n))
                    )
    print(s)


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()


#############################################################################################
#   Для тестов нажмите Ctrl+Shift+F10 установив курсор на  тест (или создайте конфигурацию) #
#############################################################################################
class Test_Fib(TestCase):
    fib1000 = 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875

    def one(self, fun, inp, out):
        for one in map(lambda x, y: [x, y], inp, out):
            self.assertAlmostEqual(
                one[1],
                fun(one[0]),
                delta=0.1,
                msg="incorrect calc with n=" + str(one[0])
            )
        with self.assertRaises(AssertionError):
            fun(-1)

    def test_a_00_calc_o1_fibonachi(self):
        inp = [0, 1, 5, 10]
        out = [0, 1, 5, 55]
        self.one(f_o1, inp, out)

    def test_a_01_naive_fibonachi(self):
        inp = [0, 1, 5, 10]
        out = [0, 1, 5, 55]
        self.one(a_01_naive_fibonachi_recursive, inp, out)

    def test_a_02_cashed_fibonachi(self):
        inp = [0, 1, 5, 10, 1000]
        out = [0, 1, 5, 55, self.fib1000]
        self.one(a_02_cashed_fibonachi, inp, out)

    def test_a_03_iteration_fibonachi(self):
        inp = [0, 1, 5, 10, 1000]
        out = [0, 1, 5, 55, self.fib1000]
        self.one(a_03_iteration_fibonachi, inp, out)

#############################################################################################
#  Конец  тестов                                                             А.Хмелев 2017  #
#############################################################################################
