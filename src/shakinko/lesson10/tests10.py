import os
from unittest import TestCase
from a_dfs import printGraphA
from b_topological_sort import printGraphB


#############################################################################################
#   Для тестов нажмите Ctrl+Shift+F10 установив курсор на  Run (или создайте конфигурацию)  #
#############################################################################################

class Run(TestCase):
    def fn(self, filename):
        return os.path.dirname(os.path.abspath(__file__)) + "/" + filename

    # Уровень A
    def test_A(self):
        fn = self.fn("dataA.txt")
        f = open(fn)
        res = printGraphA(f)
        lines = [
            "A->B",
            "B->C",
            "C->F",
            "F->E",
            "A<-E",
            "B<-E",
            "F->I",
            "D->G",
            "G->H",
            "D<-H",
            "A(0,11)",
            "B(1,10)",
            "C(2,9)",
            "D(12,17)",
            "E(4,5)",
            "F(3,8)",
            "G(13,16)",
            "H(14,15)",
            "I(6,7)"]
        for i in range(0, len(lines)):
            self.assertEqual(lines[i], res[i])

    # Уровень B
    def test_B(self):
        fn = self.fn("dataB.txt")
        f = open(fn)
        res = printGraphB(f)
        lines = [
            "G(4,5)",
            "H(6,7)",
            "F(3,8)",
            "D(2,9)",
            "E(10,11)",
            "C(1,12)",
            "A(0,13)",
            "B(14,15)"
        ]
        for i in range(0, len(lines)):
            self.assertEqual(lines[i], res[i])

    # Уровень C
    # Не тестируется
        # Тестовое покрытие для этой задачи реализовать сложно.
        # Тут будет проверка вручную. Когда решите замените 1 на 2.
    def test_C(self):
        self.assertEqual(1, 2)


