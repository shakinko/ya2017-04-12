from unittest import TestCase
from .a_videoregistrator import naive_calc, fast_calc
from .b_sheduler import Event, calcStartTimes
from .c_knapsack import Item, calcMaxCost


#############################################################################################
#   Для тестов нажмите Ctrl+Shift+F10 установив курсор на  Run (или создайте конфигурацию)  #
#############################################################################################
class Run(TestCase):
    events = [
        Event(0, 3), Event(0, 1), Event(1, 2), Event(3, 5),
        Event(1, 3), Event(1, 3), Event(1, 3), Event(3, 6),
        Event(2, 7), Event(2, 3), Event(2, 7), Event(7, 9),
        Event(3, 5), Event(2, 4), Event(2, 3), Event(3, 7),
        Event(4, 5), Event(6, 7), Event(6, 9), Event(7, 9),
        Event(8, 9), Event(4, 6), Event(8, 10), Event(7, 10)
    ]

    # Уровень A
    def test_A_naive_calc(self):
        events = [1, 1.1, 1.6, 2.2, 2.4, 2.7, 3.9, 8.1, 9.1, 5.5, 3.7]
        interval = 1
        self.assertEqual(20.5, sum(naive_calc(events, interval)))

    def test_A_fast_calc(self):
        events = [1, 1.1, 1.6, 2.2, 2.4, 2.7, 3.9, 8.1, 9.1, 5.5, 3.7]
        interval = 1
        self.assertEqual(20.5, sum(fast_calc(events, interval)))

    # Уровень B
    def test_B_0_10(self):
        self.assertEqual(str(calcStartTimes(self.events, 0, 10)), "[(0, 1), (1, 2), (2, 3), (3, 5), (6, 7), (7, 9)]")

    def test_B_1_7(self):
        self.assertEqual(str(calcStartTimes(self.events, 1, 7)), "[(1, 2), (2, 3), (3, 5), (6, 7)]")

    def test_B_2_8(self):
        self.assertEqual(str(calcStartTimes(self.events, 2, 8)), "[(2, 3), (3, 5), (6, 7)]")

    def test_B_5_10(self):
        self.assertEqual(str(calcStartTimes(self.events, 5, 10)), "[(6, 7), (7, 9)]")

    def test_B_2_6(self):
        self.assertEqual(str(calcStartTimes(self.events, 2, 6)), "[(2, 3), (3, 5)]")

    # Уровень C
    def test_C_calcMaxCost(self):
        items = [
            Item(60, 20),
            Item(100, 50),
            Item(120, 30),
            Item(100, 50)
        ]

        data = [
            (0, 0.0),
            (10, 40.0),
            (20, 80.0),
            (30, 120.0),
            (40, 150.0),
            (50, 180.0),
            (60, 200.0),
            (70, 220.0),
            (80, 240.0),
            (90, 260.0)
        ]
        for inp in data:
            fullCost = calcMaxCost(items, inp[0])
            self.assertEqual(fullCost, inp[1])
