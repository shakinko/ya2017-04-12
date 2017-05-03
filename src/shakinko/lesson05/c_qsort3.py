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
    def partition(a, l, r):
        # случайная опорная точка
        x = random.randint(l, r - 1)

        j = l + 1
        a[l], a[x] = a[x], a[l]

        for i in range(l + 1, r):
            if a[i] < a[l]:
                a[i], a[j] = a[j], a[i]
                j += 1

        a[l], a[j - 1] = a[j - 1], a[l]
        return j

    def quick_sort(a, l=0, r=len(a)):
        while l < r:
            m = partition(a, l, r)
            # m-l сравним с r-m
            if (m-l)<(r-m):
                quick_sort(a, l, m-1)
                l = m + 1
            else:
                quick_sort(a, m, r)
                r = m - 1

    return quick_sort(a)


def fill_events_from_cams_quick3(cams, events):
    # events - нужно обновить (т.е. функция ничего не возвращает по return)
    Point = collections.namedtuple("Point", {"time": 0, "type": 0})
    points = list()
    for cam in cams:
        points.append(Point(time=cam.start, type=-1))
        points.append(Point(time=cam.stop, type=1))
    for event in events:
        points.append(Point(time=event.time, type=0))

    tst = [1, 10, 2, 11, 0, 77, 5]
    my_qsort3(tst)
    print (tst)

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
