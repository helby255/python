#Простейший
cities = ['Chelyabinsk', 'Yekaterinburg', 'Moscow', 'd.Paris', 'kirat']
print(cities)
#Число элементов в массиве
print(len(cities))
#Отдельный элемент
print(cities[0])
#c большой буквы
print(cities[4].title())

#Поменять город
print("До:")
print(cities)
print("После:")
cities[3] = 'Ufa'
print(cities)
print('==========')

#Добавить элемент
print("До:")
print(cities)
cities.append('Komarovo')
print("После:")
print(cities)
print('==========')

#Добавить элемент в определенное место
print("До:")
print(cities)
cities.insert(1, 'Fedorovka')
print("После:")
print(cities)
print('==========')

#Убрать элемент
print("До:")
print(cities)
del cities[3]
print("После:")
print(cities)
print('==========')

#Убрать по названию
print("До:")
print(cities)
print("После:")
cities.remove('Ufa')
print(cities)
print('==========')

#указать удаленный элемент
print("До:")
print(cities)
deleted_city = cities.pop(1)
print ("Удален:" + deleted_city)
print("После:")
print(cities)
print('==========')

#сортировать
print("До:")
print(cities)
cities.sort()
print("После:")
print(cities)
print('==========')

#сортировать в обратном порядке
print("До:")
print(cities)
cities.sort(reverse=True)
#второй вариант
#cities.reverse()
print("После:")
print(cities)
print('==========')
