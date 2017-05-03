task = '''
 Lesson 3. C_Heap.
 Задача: построить max-кучу = пирамиду = бинарное сбалансированное дерево на массиве.
 ВАЖНО! НЕЛЬЗЯ ИСПОЛЬЗОВАТЬ НИКАКИЕ КОЛЛЕКЦИИ, КРОМЕ ARRAYLIST (его можно, но только для массива)

      Проверка проводится по данным файла
      Первая строка входа содержит число операций 1 ≤ n ≤ 100000.
      Каждая из последующих nn строк задают операцию одного из следующих двух типов:

      Insert x, где 0 ≤ x ≤ 1000000000 — целое число;
      ExtractMax.

      Первая операция добавляет число x в очередь с приоритетами,
      вторая — извлекает максимальное число и выводит его.

      Sample Input:
      6
      Insert 200
      Insert 10
      ExtractMax
      Insert 5
      Insert 500
      ExtractMax

      Sample Output:
      200
      500

     РЕМАРКА. Это задание исключительно учебное.
     Свои собственные кучи нужны довольно редко.
     "В реальном бою" все существенно иначе. 
     Изучите и используйте коллекции языка
     
}

'''


class MaxHeap():
    def __init__(self) -> None:
        super().__init__()
        self._heap = []

    def __repr__(self) -> str:
        return repr(self._heap)

    def siftDown(self, i):
        return

    def siftUp(self,i):
        return


    def extractMax(self):
        return

    def insert(self, param):
        return


def findMaxValue(filename):
    # эта процедура читает данные из файла, ее можно не менять.
    f = open(filename)
    heap = MaxHeap()
    maxValue = 0
    # прочитаем строку для кодирования из тестового файла
    count = int(f.readline().replace("\n", ""))
    for i in range(0, count):
        s = str(f.readline().replace("\n", ""))
        print("s=" + s)
        if s.find("ExtractMax") == 0:
            res = heap.extractMax()
            if (res > maxValue):
                maxValue = res
            print(maxValue)
        if s.find(" ") > 0:
            cmd, strValue = s.split(" ")
            if cmd == "Insert":
                heap.insert(int(strValue))
    return maxValue


def main():
    res = findMaxValue("heapData.txt")
    print(res)


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
