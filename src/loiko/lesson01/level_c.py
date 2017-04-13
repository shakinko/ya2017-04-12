# coding=utf-8
from unittest import TestCase

'''
Level C. Вам Необходимо реализовать 2 задачи 
по ускоренным алгоритмам расчетов с числами Фибоначчи fib(a)

1) c_01_last_digit_fibo(a) (время O(a))
вычислить последнюю цифру числа Фибоначчи
Известны пределы: 0<=a<=1e8

2) c_02_mod_big_fibo(a,b) (время O(b)) )
итерационный вариант, в котором вычисляется остаток от деления fib(a)%b
Известны пределы: 0<=a<=1e20 0<=b<=1e8 b<fib(a)

Проверьте работоспособность через ввод и тесты
'''


def c_01_last_digit_fibo(n):
    #ваше решение
    return None


def c_02_mod_big_fibo(n, m):
    #ваше решение
    return None


def main():
    a, b = map(int, input().split(" "))
    tmpl = "c_01_mod_fibo result={}\n" \
           + "c_02_mod_big_fibo result={}\n"
    s = tmpl.format(str(c_01_last_digit_fibo(a)),
                    str(c_02_mod_big_fibo(a,b))
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
class Test_FibMod(TestCase):

    def test_c_01_mod_fibo(self):
        inp = [1234567, 10]
        out = [3,5]
        for one in map(lambda x, y: [x, y], inp, out):
            self.assertEqual(
                one[1],
                c_01_last_digit_fibo(one[0]),
                msg="incorrect calc with n={}. Expected z={}". \
                    format(one[0], one[1])
            )

    def test_c_02_mod_big_fibo(self):
        inp = [[12345678, 1234567],[1234567, 123456],[10,2]]
        out = [419800,30541,1]
        for one in map(lambda x, y: [x, y], inp, out):
            self.assertEqual(
                one[1],
                c_02_mod_big_fibo(one[0][0], one[0][1]),
                msg="incorrect calc with x,y={},{}. Expected z={}". \
                    format(one[0][0], one[0][1], one[1])
            )

#############################################################################################
#  Конец  тестов                                                             А.Хмелев 2017  #
#############################################################################################
