task='''
Вводятся (конкретные цифры - для примера)
1) объем рюкзака 60
2) число возможных предметов 4
3) сам набор предметов
    100 50
    120 30
    100 50
    100 50

Необходимо собрать наиболее дорогой вариант рюкзака для этого объема
Предметы можно резать на кусочки (т.е. алгоритм будет жадным)

'''


class Item:
    def __init__(self, cost, weight):
        self.cost = cost
        self.weight = weight

    def __repr__(self):
        return repr((self.cost, self.weight))


def calcMaxCost(items, W):
    res = 0
    items.sort(key=lambda item: -item.cost / item.weight)
    for item in items:
        if item.weight < W:
            res += item.cost
            W = W - item.weight
        else:
            res += (item.cost * W) / item.weight
            break
    return res

def main():
    items = []
    count, W = map(int, input("\nВведите число предметов и размер рюкзака через пробел ").split(" "))
    for i in range(1, count + 1):
        inp = tuple(map(float, input(
            "Введите предмет в формате вес,цена ".format(i)).split(","))
                    )
        items.append(Item(inp[0], inp[1]))
    print("\nВведены предметы: " + str(items))
    print("Заполнить \"непрерывный\" рюкзак можно на сумму {}"
          .format(calcMaxCost(items, W))
          )


if __name__ == "__main__":
    main()
