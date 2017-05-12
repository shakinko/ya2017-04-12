import os
from unittest import TestCase
from a_editdist import getDistanceEdintingA
from b_editdist import getDistanceEdintingB
from c_editdist import getDistanceEdintingC


#############################################################################################
#   Для тестов нажмите Ctrl+Shift+F10 установив курсор на  Run (или создайте конфигурацию)  #
#############################################################################################

class Run(TestCase):
    def fn(self, filename):
        return os.path.dirname(os.path.abspath(__file__)) + "/" + filename

    # Уровень A
    def test_A(self):
        f = open(self.fn("dataABC.txt"))

        def solve(f):
            a = f.readline().replace("\n", "")
            b = f.readline().replace("\n", "")
            c = getDistanceEdintingA(a, b)
            print(a,b,c)
            return c

        # String 1 & 2
        self.assertEqual(0, solve(f))
        # String 3 & 4
        self.assertEqual(3, solve(f))
        # String 5 & 6
        self.assertEqual(5, solve(f))
        # String 7 & 8
        self.assertEqual(15, solve(f))
        f.close()

    # Уровень B
    def test_B(self):
        f = open(self.fn("dataABC.txt"))

        def solve(f):
            a = f.readline().replace("\n", "")
            b = f.readline().replace("\n", "")
            c = getDistanceEdintingB(a, b)
            print(a,b,c)
            return c

        # String 1 & 2
        self.assertEqual(0, solve(f))
        # String 3 & 4
        self.assertEqual(3, solve(f))
        # String 5 & 6
        self.assertEqual(5, solve(f))
        # String 7 & 8
        self.assertEqual(15, solve(f))
        f.close()

    # Уровень C
    def test_C(self):
        f = open(self.fn("dataABC.txt"))

        def testSolve(f):
            a = f.readline().replace("\n", "")
            b = f.readline().replace("\n", "")
            operations = getDistanceEdintingC(a, b)
            c = operations.replace(",,", "╣,")
            i, j = 0, 0
            out = ""
            while j < len(c):
                ch = ',' if c[j + 1] == '╣' else c[j + 1]
                if c[j] == "#":
                    out = out + a[i]
                    i, j = i + 1, j + 2
                elif c[j] == "~":
                    out = out + ch
                    i, j = i + 1, j + 3
                elif c[j] == "+":
                    out = out + ch
                    j = j + 3
                else:
                    i, j = i + 1, j + 3
            print("a=" + a, "b=" + b, "operations=" + operations, "out=" + out, "", sep="\n")
            self.assertEqual(out, b, "Incorrect transform from A to B")

        # String 1 & 2
        testSolve(f)
        # String 3 & 4
        testSolve(f)
        # String 5 & 6
        testSolve(f)
        # String 7 & 8
        testSolve(f)
        f.close()

