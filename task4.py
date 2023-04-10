# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10
#     7 -> "Нельзя определить"

numberProducts = int(input("Введите количество изделий: "))
MIN_BATCH = 6
STAFF = 3
EDGE_COEFFICIENT = 2
MIDLE_COEFFICIENT = 4
if numberProducts % MIN_BATCH == 0:
    edgeNumber = int((numberProducts / STAFF) / EDGE_COEFFICIENT)
    midleNumber = int(edgeNumber * MIDLE_COEFFICIENT)
    print(f"{numberProducts} -> {edgeNumber} {midleNumber} {edgeNumber}")
else:
    print("Нельзя определить")
