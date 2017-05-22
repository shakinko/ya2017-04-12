import os

from unittest import TestCase

#############################################################################################
#   Для тестов нажмите Ctrl+Shift+F10 установив курсор на  Run (или создайте конфигурацию)  #
#############################################################################################
from .a_bfs import print_bfs_a
from .b_dijkstra import print_b_dijkstra


class Run(TestCase):
    def fn(self, filename):
        return os.path.dirname(os.path.abspath(__file__)) + "/" + filename

    # Уровень A
    def test_A(self):
        fn = self.fn("dataA.txt")
        f = open(fn)
        res = print_bfs_a(f)
        lines = [
            "A=0",
            "B=1",
            "C=2",
            "D=5",
            "E=1",
            "F=2",
            "G=5",
            "H=4",
            "I=3"
        ]
        for i in range(0, len(lines)):
            self.assertEqual(lines[i], res[i])

    # Уровень B
    def test_B(self):
        fn = self.fn("dataB.txt")
        f = open(fn)
        res = print_b_dijkstra(f)
        print(res)
        lines = [
            "A=0",
            "B=1",
            "C=3",
            "D=4",
            "E=4",
            "F=6",
            "G=5",
            "H=6"
        ]
        for i in range(0, len(lines)):
            self.assertEqual(lines[i], res[i])

            # Уровень C
            # Не тестируется
            # Тестовое покрытие для этой задачи реализовать сложно.
            # Тут будет проверка вручную. Когда решите замените 1 на 2.

    def test_C(self):
        self.assertEqual(1, 2)
