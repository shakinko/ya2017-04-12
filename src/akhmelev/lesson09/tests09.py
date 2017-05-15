import os
from unittest import TestCase
from .a_knapsack import getMaxWeightA
from .b_knapsack import getMaxWeightB
from .c_calculator import calcC

#############################################################################################
#   Для тестов нажмите Ctrl+Shift+F10 установив курсор на  Run (или создайте конфигурацию)  #
#############################################################################################

class Run(TestCase):
    def fn(self, filename):
        return os.path.dirname(os.path.abspath(__file__)) + "/" + filename

    # Уровень A
    def test_A(self):
        fn = self.fn("dataA.txt")
        res=getMaxWeightA(fn)
        self.assertEqual(14, res)

    # Уровень B
    def test_B(self):
        fn = self.fn("dataB.txt")
        res=getMaxWeightB(fn)
        self.assertEqual(9, res)

    # Уровень C
    def test_C(self):
        fn = self.fn("dataC.txt")
        res=calcC(fn)
        self.assertEqual(14, len(res)-1)
