import os
from unittest import TestCase
from A_LongIncrSubSeq import getSeqSize
from B_LongDivComSubSeq import getSeqIndexses
from C_LongNotUpSubSeq import getNotUpSeqIndexses


#############################################################################################
#   Для тестов нажмите Ctrl+Shift+F10 установив курсор на  Run (или создайте конфигурацию)  #
#############################################################################################

class Run(TestCase):
    def fn(self, filename):
        return os.path.dirname(os.path.abspath(__file__)) + "/" + filename

    # Уровень A
    def test_A(self):
        self.assertEqual(3, getSeqSize(self.fn("dataA.txt")))

    # Уровень B
    def test_B(self):
        self.assertEqual([1, 2, 4], getSeqIndexses(self.fn("dataB.txt")))

    # Уровень C
    def test_C(self):
        self.assertEqual([1, 3, 4, 5], getNotUpSeqIndexses(self.fn("dataC.txt")))

