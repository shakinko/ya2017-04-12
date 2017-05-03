task = '''
Решите задачу A повторно, добавляя метод удаления узлов.
Метод del(key) должен реализовать "ленивое" удаление с коэффициентом обновления 0.5,
т.е. полное перестроение дерева производится когда количество удаленных узлов
становится равным или большим количества оставшихся в дереве.
'''


# ----------------------------------- ДЕРЕВО ------------------------------------
class AvlB():
    # ------------------------------- ОТДЕЛЬНЫЙ УЗЕЛ ------------------------------------
    class Node():
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.height = 0

        def balance(self):
            return (self.left.height if self.left else -1) - (
                self.right.height if self.right else -1)

        def __str__(self):
            # return str(self.key)+"/"+str(self.balance())+"/"+str(self.height)
            # return str(self.key)+"/"+str(self.height)
            return str(self.key)


    def __init__(self, root=None):
        self.root = root  # корень
        self._outlist = list()  # вспомогательный лист в котором строится дерево для вывода его на экран
        # for lazy deletion
        self.nodecount = 0
        self.delcount = 0

    def free(self):
        if not self.root:
            return
        self._free(self.root)

    def add(self, key, value):
        pass

    def delete(self,key):
        pass

    def copy(self, node):
        pass

    def lookup(self, key):
        o = self._lookup(self.root, key)
        if o:
            return o

    def _free(self, tree):
        pass

    def _lookup(self, tree, key):
        pass

    def _create(self, key, value):
        pass

    def _height(self, tree):
        pass

    def _add(self, tree, key, value):
        pass

    def _right_rotate(self, tree):
        pass

    def _left_rotate(self, tree):
        pass

    def _leftright_rotate(self, tree):
        pass

    def _rightleft_rotate(self, tree):
        pass

    # обновление массива для строкового представления дерева
    def _dfs_print(self, tree, level):
        if level == 0:
            self._outlist = list()
        if len(self._outlist) < level + 1:
            self._outlist.append(" ")
        self._outlist[level] += (str(tree) if tree else ".") + " "
        if tree:
            self._dfs_print(tree.left, level + 1)
            self._dfs_print(tree.right, level + 1)

    # строковое представление дерева
    def __str__(self) -> str:
        self._dfs_print(self.root, 0)
        out = ""
        max = 0
        for s_Level in self._outlist:
            if len(s_Level) > max:
                max = len(s_Level)
        for s_Level in self._outlist:
            spaces = ""
            line = s_Level
            while (len(line) <= max):
                line = s_Level
                spaces += " "
                line = line.replace(" ", spaces)
            subspaces = " " * (len(spaces) - 1)
            while (len(line) > max):
                line = line.replace(spaces, subspaces, 1)
            if len(line.replace(".","").replace(" ",""))>0:
                out += line + "\n"
        out += "-"*max
        return out


# ----------------------------------ПРОВЕРКА РАБОТОСПОСОБНОСТИ #########################
def main():
    # чтение одной строки из файла
    def arr(filename):
        return filename.readline().replace("\n", "").split(" ")
    f = open("dataB.txt")
    count = int(arr(f)[0])
    avl = AvlB()
    keys=list()
    for i in range(0, count):
        data = arr(f)
        assert len(data) == 2
        avl.add(data[0], int(data[1]))
        keys.append(data[0])
    print(avl)
    print("Удаление половины узлов")
    for i in range(count//2, count):
        avl.delete(keys[i])
    print(avl)


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
