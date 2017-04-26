import random
from unittest import TestCase

from .a_binary_find import binaryFind
from .b_mergesort import mergeSort
from .c_inversions import inv_counter


#############################################################################################
#   Для тестов нажмите Ctrl+Shift+F10 установив курсор на  Run (или создайте конфигурацию)  #
#############################################################################################
class Run(TestCase):
    def arr(self):
        array = []
        for i in range(0, 100):
            array.append(random.randint(-100, 200))
        return array
    # Уровень A
    def test_A(self):
        array = self.arr()
        array.sort()
        for i in range(0, len(array)):
            value = array[i]
            indexFrom1 = binaryFind(array, value)
            findvalue = array[indexFrom1 - 1]
            self.assertEqual(value, findvalue)

    # Уровень B
    def test_B(self):
        array = self.arr()
        test = mergeSort(array)
        array.sort()
        print(test)
        print(array)
        for i in range(0, len(array)):
            self.assertEqual(test[i], array[i])
        self.assertEqual(mergeSort([]), [])
        self.assertEqual(mergeSort([1]), [1])

    # Уровень C
    def test_C(self):
        m = [2, 3, 9, 2, 9]
        inv = inv_counter(m).inv
        self.assertEqual(inv, 2)
        m = [-1, 2, 3, 6, 7, 8, -5, 4, 2, 5, 34, 234, -4, 45, 6,
             6, 23, 423, 56, 423, -23, 789, -4, 234, 123, 123,
             -234, 23423234, 23, 4, 234, 234, -23, 42, 342]
        inv = inv_counter(m).inv
        self.assertEqual(inv, 206)
