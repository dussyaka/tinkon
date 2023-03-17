n, s = map(int, input().split())                                    # ввод количества студентов и максимальной суммы их баллов
score = []
for _ in range(n):
    score.append(list(map(int, input().split())))                   # ввод диапазона возможных баллов для i ученика

summ = 0
result = []
for i in range(n):
    result.append([i, score[i][1]])                                 # сделал список в котором хранится исходный i ученика и максимально возможный его балл 

while summ != s:                                                    # пока промежуточная сумма баллов не станет нужной
    summ = 0
    for i in range(n):
        summ += result[i][1]                                        # считаем промежуточную сумму баллов учеников
    result.sort(key=lambda x: x[1])                                 # сортируем список по количеству баллов
    for i in range(n):                                              # отбираем у учеников по баллу в пределах возможного, не трогая медиану
        if result[i][1] - score[result[i][0]][0] != 0 and i != n // 2:
            result[i][1] = result[i][1] - 1
            break
print(result[n // 2][1])                                            # вывод итоговой медианы