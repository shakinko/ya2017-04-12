import collections
import random

task = '''
Видеорегистраторы и площадь (нужно реализовать qsort3).
Условие то же что и в задаче А.

    По сравнению с задачей A доработайте алгоритм сортировки так, чтобы
    он оптимально использовал время и память (нужно реализовать qsort3):
        - за оптимизацию стека отвечает элиминация хвостовой рекурсии
        - при элиминации в рекурсию отправляйте меньшую часть массива
        - сортировка выполняется на месте
        - рекурсионные вызовы должны проводится на основе 3-разбиения
        - опорный элемент должен выбираться случайно


    Sample Input:
    3 11
    0 5
    2 3
    7 10
    10 9 8 7 6 5 4 3 2 1 0
    Sample Output:
    1 1 1 1 0 1 1 2 2 1 1

'''

Cam = collections.namedtuple("Cam", {"start": 0, "stop": 0})
Event = collections.namedtuple("Event", {"time": 0, "cams": 0}, rename=True)


def my_qsort3(a):
    def partition3(a, l, r):
        x, j, t = a[l], l, r
        i = j

        while i <= t:
            if a[i] < x:
                a[j], a[i] = a[i], a[j]  # элемент пошел в левую часть
                j += 1  # пр. граница левой части сдвинулась вперед

            elif a[i] > x:
                a[t], a[i] = a[i], a[t]  # элемент пошел в правую часть
                i -= 1  # корректируем i, чтобы не перепрыгивать через обновленный на предыдущ. шаге a[i]
                t -= 1  # лев. граница правой части сдвинулась назад
            i += 1
        return j, t

    def q_sort3(a, l, r):
        while l < r:  # цикл вместо if для элиминации хвостовой рекурсии
            k = random.randint(l, r)  # случайный опорный элемент
            a[l], a[k] = a[k], a[l]  # этот элемент становится слева, от его значения зависит работа partition3
            m1, m2 = partition3(a, l, r)  # делим массив на 3 части

            if m1 - l < r - m2:
                q_sort3(a, l, m1 - 1)  # в рекурсию идет меньшая часть массива (левая)
                l = m1 + 1  # ОК, отсортировали часть массива. Двигаем границу в начало неотсортированной части

            else:
                q_sort3(a, m2 + 1, r)  # или в рекурсию идет опять же меньшая часть массива (правая)
                r = m2 - 1  # ОК, отсортировали часть массива. Двигаем границу в конец неотсортированной части

    return q_sort3(a, 0, len(a) - 1)


def fill_events_from_cams_quick3(cams, events):
    # events - нужно обновить (т.е. функция ничего не возвращает по return)
    Point = collections.namedtuple("Point", {"time": 0, "type": 0})
    points = list()
    for cam in cams:
        points.append(Point(time=cam.start, type=-1))
        points.append(Point(time=cam.stop, type=1))
    for event in events:
        points.append(Point(time=event.time, type=0))

    my_qsort3(points)
    onCam = 0
    d = dict()
    for p in points:
        if p.type == 0:
            d.update({p.time: onCam})
        else:
            onCam -= p.type
    for i in range(0, len(events)):
        t = events[i].time
        onCam = d.get(events[i].time)
        events[i] = Event(t, onCam)
    pass
    # !!!!!!!!!!!!!!!!!!!!!!!!!     КОНЕЦ ЗАДАЧИ     !!!!!!!!!!!!!!!!!!!!!!!!!


def main():
    # чтение одной строки чисел из файла
    def arr(filename):
        str = filename.readline().replace("\n", "").split(" ")
        return list(map(int, str))

    f = open("dataC.txt")
    cam_count, event_count = arr(f)
    cams = list()
    events = list()
    for i in range(0, cam_count):
        cam_data = arr(f)
        assert len(cam_data) == 2
        cams.append(Cam(cam_data[0], cam_data[1]))
    events_data = arr(f)
    assert len(events_data) == event_count
    for t in events_data:
        events.append(Event(t, -999))
    f.close()
    fill_events_from_cams_quick3(cams, events)
    for e in events:
        print(e.cams, end=" ")


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()

"""
    def q_sort3(a, l, r):
        if l >= r:
            return
        k = random.randint(l, r)
        a[l], a[k] = a[k], a[l]
        m1, m2 = partition3(a, l, r)
        # какая часть массива меньше: (m1-l-1) или (r-m2-1)?

        q_sort3(a, l, m1 - 1)
        q_sort3(a, m2 + 1, r)

"""