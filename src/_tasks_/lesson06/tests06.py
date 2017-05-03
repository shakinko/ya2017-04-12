import random
import math
from unittest import TestCase
from .a_simlpe_avl import AvlA
from .b_lazy_deletion_avl import AvlB
from .c_full_deletion_avl import AvlC

#############################################################################################
#   Для тестов нажмите Ctrl+Shift+F10 установив курсор на  Run (или создайте конфигурацию)  #
#############################################################################################

class Run(TestCase):
    def generate_arr(self):
        array = []
        for i in range(0, 100):
            array.append(random.randint(-9, 99))
        return array

    # Уровень A
    def test_A(self):
        array = self.generate_arr()
        avlA = AvlA()
        for item in array:
            avlA.add(item, -1 * item)
        for i in range(0, len(array)):
            key = array[i]
            value = avlA.lookup(key).value
            self.assertEqual(key, -1 * value)
        balance_ok = avlA.root.height < 1.4405 * math.log(len(array) + 2, 2) - 1.3277
        self.assertTrue(balance_ok, "Ошибка балансировки A")
        print(avlA)

    # Уровень B
    def test_B(self):
        array = self.generate_arr()
        avlB = AvlB()
        print("Добавление узлов")
        for item in array:
            avlB.add(item, -1 * item)
        for i in range(0, len(array)):
            key = array[i]
            value = avlB.lookup(key).value
            self.assertEqual(key, -1 * value)
        balance_ok = avlB.root.height <= 1.4405 * math.log(len(array) + 2, 2) - 1.3277
        self.assertTrue(balance_ok, "Ошибка балансировки после добавления B")
        print(avlB)
        print("Удаление половины узлов")
        for i in range(len(array)//2-1, len(array)):
            avlB.delete(array[i])
        balance_ok = avlB.root.height <= 1.4405 * math.log(len(array)//2 + 2, 2) - 1.3277
        self.assertTrue(balance_ok, "Ошибка балансировки после удаления B")
        print(avlB)

    # Уровень C
    def test_C(self):
        array = self.generate_arr()
        avlC = AvlC()
        print("Добавление узлов")
        for item in array:
            avlC.add(item, -1 * item)
        for i in range(0, len(array)):
            key = array[i]
            value = avlC.lookup(key).value
            self.assertEqual(key, -1 * value)
        balance_ok = avlC.root.height <= 1.4405 * math.log(len(array) + 2, 2) - 1.3277
        self.assertTrue(balance_ok, "Ошибка балансировки после добавления B")
        print(avlC)
        print("Удаление половины узлов")
        for i in range(len(array)//2-1, len(array)):
            avlC.delete(array[i])
        balance_ok = avlC.root.height <= 1.4405 * math.log(len(array)//2 + 2, 2) - 1.3277
        self.assertTrue(balance_ok, "Ошибка балансировки после удаления B")
        print(avlC)
