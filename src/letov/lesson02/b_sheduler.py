task='''
Даны (введены) интервальные события events
реализуйте метод calcStartTimes, так, чтобы число принятых к выполнению
непересекающихся событий было максимально.
Алгоритм жадный. Для реализации обдумайте надежный шаг.

Решение приведите в calcStartTimes(events, begin, end):
    events - события которые нужно распределить в аудитории
    в период [begin, end] (включительно).
Оптимизация проводится по наибольшему числу непересекающихся событий.
начало и конец событий могут совпадать.

Порядок событий хронологический, а оставшееся в графике свободное время 
для новых неизвестных событий должно быть максимальным.
'''

class Event:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __repr__(self):
        return repr((self.start, self.stop))


def calcStartTimes(events, begin, end):
    local_events = sorted(events, key = lambda event:event.stop)
    res = []
    t = begin
    for event in local_events:
        if event.start >= t and event.stop <= end:
            res.append(event)
            t = event.stop
    return res


def calcMaxCostMinBlank(items, W):
    # Повышенная сложность (необязательно, и не проверяется):
    # Добавьте новый алгоритм на максимум событий при минимуме свободного времени,
    # но учтите, что на нём тесты не пройдут, а сам алгоритм заметно усложнится)

    # Ключевое требование:
    # асимптотика аглоритма по сравнению с предыдущим не должна ухудшиться

    return


def main():
    count = int(input("\nВведите общее число событий: "))
    events = []
    begin = None
    end = None
    for i in range(1, count + 1):
        inp = tuple(map(float, input(
            "Введите событие №{} в формате начало,конец ".format(i)).split(","))
                    )
        event = Event(inp[0], inp[1])
        if not begin or begin > event.start: begin = event.start
        if not end or end < event.stop: end = event.stop
        events.append(event)
    print("\nВведены события:" + str(events))
    print("O(n log n) алгоритм запланировал события:\n {}" \
          .format(calcStartTimes(events, begin, end))
          )


if __name__ == "__main__":
    main()

