for x in range(0,10):
    print("***")

for x in range(0, 10):
    print(x)

print("==========")
#шаг цикла (прибавлять определенное число за раз, например только четные)
for x in range(0, 10, 2):
    print(x)
print("=========")
#Прервать цикл если
for x in range(0, 10, 2):
    print(x)
    if x == 4:
        break