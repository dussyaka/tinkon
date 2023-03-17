n = int(input())                        # ввод количества чисел
page = list(map(int, input().split()))  # ввод чилел

otrezki = []                            # список разумных отрезков
counter = 0                             # cчётчик нормальных отрезков

for i in range(n - 1):                  # цикл поиска разумных отрезков
    for j in range(i + 1, n):
        if sum(page[i:j + 1]) == 0:
            otrezki.append([i, j])      # добавляем отрезок в список

for i in range(n - 1):                  # цикл подсчёта нормальных отрезков
    for j in range(i + 1, n):
        flag = False
        for k in range(len(otrezki)):
            if i <= otrezki[k][0] and j >= otrezki[k][1]:
                flag = True             
        if flag == True:                # если хоть раз встречается разумный подотрезок то
            counter += 1                # +1 нормальный отрезок

print(counter)                          # вывод счётчика нормальных отрезков
