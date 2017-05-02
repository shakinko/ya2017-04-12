import collections

task = '''
Видеорегистраторы и площадь (большая задача на сортировку).

На площади установлена одна или несколько камер.
Известны данные о том, когда каждая из них включалась и выключалась (отрезки работы)
Известен список событий на площади (время начала каждого события).
Вам необходимо определить для каждого события сколько камер его записали.

Данные читаются из текстового файла.
В первой строке задано два целых числа:
    число включений камер (отрезки) 1<=n<=50000
    число событий (точки) 1<=m<=50000.

Следующие n строк содержат по два целых числа ai и bi (ai<=bi) -
координаты концов отрезков (время работы одной какой-то камеры).

Последняя строка содержит m целых чисел - координаты точек.
Все координаты не превышают 1E8 по модулю (!).

Для оптимального решения задачи потребуется сортировка qsort. Она должна повторить
функциональность стандартного метода sorted (вход - массив, выход - отсортированный массив).

Точка считается принадлежащей отрезку, если она находится внутри него или на границе.
Для каждой точки в порядке их появления во вводе (!) выведите,
скольким отрезкам она принадлежит.

    Sample Input:
    2 3
    0 5
    7 10
    1 6 11
    Sample Output:
    1 0 0

'''

Cam = collections.namedtuple("Cam", {"start": 0, "stop": 0})
Event = collections.namedtuple("Event", {"time": 0, "cams": 0}, rename=True)

def my_qsort(a):
    def partition(a, l, r):
        x = a[l]
        j = l

        for i in range(l + 1, r):
            if a[i] <= x:
                j += 1
                a[j], a[i] = a[i], a[j]

        a[l], a[j] = a[j], a[l]
        return j

    def quick_sort(a, l=0, r=len(a)):
        if l >= r:
            return
        m = partition(a, l, r)
        # quick_sort(a, l, m - 1) # такой оптимизированный способ, когда m-й элемент считаем уже отсортированным
        quick_sort(a, l, m)  # так работает
        quick_sort(a, m + 1, r)
    return quick_sort(a)


def fill_events_from_cams(cams, events):
    # events - нужно обновить (т.е. функция ничего не возвращает по return)
    Point = collections.namedtuple("Point", {"time": 0, "type": 0})
    points = list()
    for cam in cams:
        points.append(Point(time=cam.start, type=-1))
        points.append(Point(time=cam.stop, type=1))
    for event in events:
        points.append(Point(time=event.time, type=0))

    my_qsort(points)
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
    fill_events_from_cams(cams, events)
    for e in events:
        print(e.cams, end=" ")


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
