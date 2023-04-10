# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input("Введите трёхзначное число: "))
result = 0
while (number > 0):
    ost = number % 10
    number = number//10
    result += ost
print(f"result: {result}")
