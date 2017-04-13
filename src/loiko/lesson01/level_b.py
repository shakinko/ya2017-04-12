# coding=utf-8
from unittest import TestCase

'''
Level B. Вам Необходимо реализовать 2 способа для вычисления 
наибольшего общего делителя (вход - любые целые числа)

1) b_01_naive_gsd(a,b) (время O(n))
итерационный вариант, в котором наивно ищется наибольшее число от 1 до min(a,b)
2) b_02_fast_gsd(a,b)
рекурсивный вариант за время O(log(n)) 

Проверьте работоспособность через ввод и тесты
'''


# def b_01_naive_gsd(a, b):
#     if (a+b) == 0:
#         return 0
#     a = abs(a)
#     b = abs(b)
#     res = 1
#     for i in range(1, min(a,b)+1):
#         if a%i == 0 and b%i == 0:
#             res = i
#     return res

def b_02_fast_gsd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a>b:
        return a%b
    else:
        return b%a



def main():
    a, b = map(int, input().split(" "))
    tmpl = "b_01_naive_gsd result={}\n" \
           + "b_02_fast_gsd result={}\n"
    s = tmpl.format(str(0),
                    str(b_02_fast_gsd(a, b))
                    )
    print(s)


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()


#############################################################################################
#   Для тестов нажмите Ctrl+Shift+F10 установив курсор class Test (или через конфигурацию)  #
#############################################################################################
class Test_gsd(TestCase):
    inp = [12, 15], [1, 1], [-1, -1], [1, 10], [5, 10], [24, 24], [0, 0], [5, 10], [290345, 9275101]
    out = [3, 1, 1, 1, 5, 24, 0, 5, 11]

    def one(self, fun, inp, out):
        for one in map(lambda x, y: [x, y], inp, out):
            self.assertEqual(
                one[1],
                fun(one[0][0], one[0][1]),
                msg="incorrect calc with x,y={},{}. Expected z={}". \
                    format(one[0][0], one[0][1], one[1])
            )

    # def test_b_01_naive_gsd(self):
    #     self.one(b_01_naive_gsd, self.inp, self.out)

    def test_b_02_fast_gsd(self):
        self.one(b_02_fast_gsd, self.inp, self.out)

#############################################################################################
#  Конец  тестов                                                             А.Хмелев 2017  #
#############################################################################################
