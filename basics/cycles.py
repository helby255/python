from time import sleep

for x in range(0,10):
    print("***")

for x in range(0, 10):
    print(x)

print("==========")
#шаг цикла (прибавлять определенное число за раз, например только четные)
for x in range(0, 10, 2):
    print(x)
print("=========")
#Прервать цикл если дошел до числа 4
for x in range(0, 10, 2):
    print(x)
    if x == 4:
        break
print("=========")
#бесконечный цикл
#a = 0
#while True:
#    print(a)
#    a+=1

#Дойти до 60 с интервалом в 1 секунду
b = 0
while True:
    print(b)
    sleep(1)
    b+=1
    if b == 60:
        break