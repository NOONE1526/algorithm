from time import sleep
N = int(input("Enter the number of tasks: "))
time = []
penalty = []
time_res = []
order, new_order, new_penalty= [], [], []

def check(init):
    sum_el = []
    suma = {}
    for i in time:
        sum_el = []      
        for b in enumerate(penalty):
            if time.index(i) != b[0]:
                sum_el.append(i*b[1])
                # print(sum_el)
                # sleep(1)
            # else:
            #     print(penalty)
            #     print(time)
            #     print(b[0], time.index(i))
        suma.update({i:sum(sum_el)})
    list(suma.values())
    new_penalty.append(min(list(suma.values())))

    if init != "first":
        order.append(min(suma, key=suma.get))
        kill(time.index(min(suma, key=suma.get)))

    else:
        order.append(min(suma, key=suma.get))
        # print(f"time is {time}")
        new_penalty.append(min(suma))
        print("new penalty " ,new_penalty)
        return suma

def kill(ind):
    if len(time) == 1:
        return
    del penalty[ind]
    del time[ind]
    check('')

for i in range(N):
    time.append(int(input("Enter the time needed for task " + str(i+1) + ": ")))
time_res = list(time)

for i in range(N):
    penalty.append(int(input("Enter the daily penalty for task " + str(i+1) + ": ")))

check('')                                       #запускаем функцию определения правильной очереди без параметра
for i in order:                                 #формируем очередь из индексов элементов
    new_order.append(time_res.index(i)+1)       #очерь формируется основываясь на неприкосаемом списке time_res

print("The minimum penalty is:", sum(new_penalty))
print("The order of tasks to be executed is:", new_order)