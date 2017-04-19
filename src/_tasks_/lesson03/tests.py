import os
from unittest import TestCase
from .a_huffman import encode
from .b_huffman import decode
from .c_heapmax import MaxHeap

#############################################################################################
#   Для тестов нажмите Ctrl+Shift+F10 установив курсор на  Run (или создайте конфигурацию)  #
#############################################################################################
class Run(TestCase):
    # Уровень A
    def test_A(self):
        fn=os.path.dirname(os.path.abspath(__file__))+"/dataHuffman.txt"
        res = encode(fn)
        self.assertEqual(res, "01001100100111")

    # Уровень B
    def test_B(self):
        fn=os.path.dirname(os.path.abspath(__file__))+"/encodeHuffman.txt"
        res = decode(fn)
        self.assertEqual(res, "abacabad")

    # Уровень C
    def test_C(self):
        h = MaxHeap()
        m = [-1, 2, 3, 6, 7, 8, -5, 4, 2, 5, 34, 234, -4, 45, 6, 6, 23, 423, 56, 423, -23, 789, -4, 234, 123, 123, -234,
             23423234, 23, 4, 234, 234, -23, 42, 342]
        for v in m:
            h.insert(v)
        for v in reversed(sorted(m)):
            self.assertEqual(v, h.extractMax())
