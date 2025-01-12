from time import sleep

cars = ['lada', 'bmw', 'fiat', 'gazele', 'uaz', 'kia']
# вывести только содержимое
for x in cars:
    print(x)
print('==========')

#создать массив чисел
numerlist = list(range(0, 10))
print(numerlist)
print('==========')

#умножить каждый элемент на 2
for x in numerlist:
    x = x * 2
    print(x)

print('==========')

#найти самый маленький элемент
numerlist.sort()
print(numerlist)
print('Самый маленький элемент:' + str(numerlist[0]))
print('==========')

#найти самый большой элемент
numerlist.sort(reverse=True)
print(numerlist)
print(numerlist[0])
print('Самый большой элемент:' + str(numerlist[0]))
print('==========')

print('Другой способ')
print('Самый маленький элемент:' + str(min(numerlist)))
print('Самый большой элемент:' + str(max(numerlist)))
print('==========')

#Сумма массива
print('Сумма всех элементов в массиве:' + str(sum(numerlist)))
print('==========')

#передать часть элементов в другой массив
mycars = cars[1:3]
print(mycars)
print('==========')
#Передать все
mycars = cars[:]
print(mycars)
print('==========')

#Передать от 3 и до конца
mycars = cars[3:]
print(mycars)
print('==========')

#Передать 1, 3, 5
cars = ['lada', 'bmw', 'fiat', 'gazele', 'uaz', 'kia']
indexes = [1,3,5]
mycars = [cars[i] for i in indexes]
print(mycars)