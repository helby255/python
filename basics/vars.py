#Простой вывод переменных
a = "hello"
b = 123

print(a)
print (b)

# Можно соеденить две переменные:
firstname = "Fedor"
lastname = "Rudin"
age = 23
# " " - пробел для того чтобы разделить при выводе
fullname = firstname + " " + lastname

print (fullname)

# Для вывода числа необходимо преобразовать переменную в строку:
print (fullname + " " + str(age) + " годика")

#Регистр играет роль:

lowregistry = "testlow"
UPREGISTRY = "TESTUP"

print(lowregistry + " "+ UPREGISTRY)

#Числа
#Базовая математика работает из коробки:
num1 = 111111
num2 = 222222
numsum = (num1 + num2)

# оба print выведут одинаковое:
print(numsum)
print(num1 + num2)