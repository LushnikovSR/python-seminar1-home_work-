# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no
#     001001 -> yes

ticket = input("Введите номер билета: ")
HALF_TICKET = int(len(ticket)/2)
ticketNumberParts = (int(ticket[:HALF_TICKET]), int(ticket[HALF_TICKET:]))
results = []
for number in ticketNumberParts:
    sumDigits = 0
    while (number > 0):
        ost = int(number % 10)
        number = number//10
        sumDigits += ost
    results.append(sumDigits)
if (results[0] == results[1]):
    print(f"{ticket} -> yes")
else: 
    print(f"{ticket} -> no")
    
