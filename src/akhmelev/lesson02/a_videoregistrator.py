task='''
Даны события events и интервал работы регистратора.

Реализуйте методы naive_calc и fast_calc, так, 
чтобы общее число включений регистратора на
заданный период времени (1) было минимальным, 
а все события events были зарегистрированы.
Одно и то же событие не может быть зарегистрировано 
в двух разных включениях регистратора

Методы вовращают list включений регистратора

Алгоритм жадный. Для реализации обдумайте надежный шаг.
'''


def naive_calc(events, interval):
    # напишите "наивный" O(n^2) алгоритм вычисления времени запуска регистратора
    local_events=list(events)
    res=[]
    while len(local_events)>0:
        start=min(local_events)
        res.append(start)
        stop=start+interval

        i=len(local_events)
        while i>0:
            i=i-1
            if local_events[i]<=stop:
                local_events.pop(i)
    return res


def fast_calc(events, interval):
    # напишите O(n log n) алгоритм вычисления времени запуска регистратора
    local_events=sorted(events)
    print("==========",local_events)
    res=[]
    stop=local_events[0]-interval
    for event in local_events:
        if event > stop:
            res.append(event)
            stop=event+interval
    return res


def main():
    print("Пример ввода:1,1.1,1.6,2.2,2.4,2.7,3.9,8.1,9.1,5.5,3.7")
    events = list(map(float, input("Введите события через запятую: ").split(",")))
    interval = float(input("\nВведите время работы регистратора (например 1.0): "))
    print("\nВведены события: " + str(events))
    print("Интервал:{}".format(interval))
    print("Наивный O(n^2) алгоритм: {}".format(naive_calc(events, interval)))
    print("\tO(n log n) алгоритм: {}".format(fast_calc(events, interval)))


if __name__ == "__main__":
    main()