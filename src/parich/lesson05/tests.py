import os
import random
from unittest import TestCase

from .a_qsort import Cam, Event, fill_events_from_cams, my_qsort
from .b_countsort import countSort
from .c_qsort3 import fill_events_from_cams_quick3, my_qsort3


#############################################################################################
#   Для тестов нажмите Ctrl+Shift+F10 установив курсор на  Run (или создайте конфигурацию)  #
#############################################################################################
class Run(TestCase):
    def generate_arr(self):
        array = []
        for i in range(0, 100):
            array.append(random.randint(-100, 200))
        return array

    # Уровень A
    def test_A(self):
        def one(fntxt):
            def ints(filename):
                str = filename.readline().replace("\n", "").split(" ")
                return list(map(int, str))

            fn = os.path.dirname(os.path.abspath(__file__)) + "/" + fntxt
            f = open(fn)
            cam_count, event_count = ints(f)
            cams = list()
            events = list()
            for i in range(0, cam_count):
                cam_data = ints(f)
                assert len(cam_data) == 2
                cams.append(Cam(cam_data[0], cam_data[1]))
            events_data = ints(f)
            assert len(events_data) == event_count
            for t in events_data:
                events.append(Event(t, -999))
            f.close()
            fill_events_from_cams(cams, events)
            s = ""
            for e in events:
                s = s + str(e.cams) + " "
            print(s)
            return s

        self.assertEqual(one("dataA.txt"), "1 0 0 ")
        self.assertEqual(one("dataC.txt"), "1 1 1 1 0 1 1 2 2 1 1 ")

        # проверка сортировки
        array = self.generate_arr()
        myarr = list(array)
        my_qsort(myarr)
        array.sort()
        for i in range(0, len(array)):
            self.assertEqual(array[i], myarr[i])

    # Уровень B
    def test_B(self):
        # проверка сортировки
        array = self.generate_arr()
        myarr = countSort(list(array))
        array.sort()
        for i in range(0, len(array)):
            self.assertEqual(array[i], myarr[i])

    # Уровень C
    def test_C(self):
        def one(fntxt):
            def ints(filename):
                str = filename.readline().replace("\n", "").split(" ")
                return list(map(int, str))

            fn = os.path.dirname(os.path.abspath(__file__)) + "/" + fntxt
            f = open(fn)
            cam_count, event_count = ints(f)
            cams = list()
            events = list()
            for i in range(0, cam_count):
                cam_data = ints(f)
                assert len(cam_data) == 2
                cams.append(Cam(cam_data[0], cam_data[1]))
            events_data = ints(f)
            assert len(events_data) == event_count
            for t in events_data:
                events.append(Event(t, -999))
            f.close()
            fill_events_from_cams_quick3(cams, events)
            s = ""
            for e in events:
                s = s + str(e.cams) + " "
            print(s)
            return s

        self.assertEqual(one("dataA.txt"), "1 0 0 ")
        self.assertEqual(one("dataC.txt"), "1 1 1 1 0 1 1 2 2 1 1 ")

        # проверка сортировки
        array = self.generate_arr()
        myarr = list(array)
        my_qsort3(myarr)
        array.sort()
        for i in range(0, len(array)):
            self.assertEqual(array[i], myarr[i])
