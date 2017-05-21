task='''
 Lesson 3. B_Huffman.
 Восстановите строку по её коду и беспрефиксному коду символов.

 В первой строке входного файла заданы два целых числа
 kk и ll через пробел — количество различных букв, встречающихся в строке,
 и размер получившейся закодированной строки, соответственно.

 В следующих kk строках записаны коды букв в формате "letter: code".
 Ни один код не является префиксом другого.
 Буквы могут быть перечислены в любом порядке.
 В качестве букв могут встречаться лишь строчные буквы латинского алфавита;
 каждая из этих букв встречается в строке хотя бы один раз.
 Наконец, в последней строке записана закодированная строка.
 Исходная строка и коды всех букв непусты.
 Заданный код таков, что закодированная строка имеет минимальный возможный размер.

        Sample Input 1:
        1 1
        a: 0
        0

        Sample Output 1:
        a


        Sample Input 2:
        4 14
        a: 0
        b: 10
        c: 110
        d: 111
        01001100100111

        Sample Output 2:
        abacabad
'''

def decode(filename):
    f = open(filename)
    count, lenght = map(int, f.readline().replace("\n", "").split(" "))
    d = dict()
    for i in range(0, count):
        ch, code = f.readline().replace("\n", "").split(": ")
        d.update({code: ch})
    s = f.readline().replace("\n", "")
    buff = ""
    res = ""
    for symbol in s:
        buff = buff + symbol
        ch = d.get(buff)
        if ch:
            res = res + ch
            buff = ""
    f.close()
    return res

def main():
    res = decode("encodeHuffman.txt")
    print(res)


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
