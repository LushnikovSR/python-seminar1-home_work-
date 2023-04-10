# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

length = int(input("Введите длину шоколадки: "))
wide = int(input("Введите ширину шоколадки: "))
numberPieces = int(input("Введите желаемое количество кусочков: "))
sumPieces = length * wide
if ((numberPieces % length == 0 or numberPieces % wide == 0) and sumPieces > numberPieces):
    print(f"{length} {wide} {numberPieces} -> yes")
else: 
    print(f"{length} {wide} {numberPieces} -> no")
