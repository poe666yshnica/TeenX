def add(x, y):

   return x + y

def subtract(x, y):

   return x - y

def multiply(x, y):

   return x * y

def divide(x, y):

   if y == 0:

       return "Ошибка: на ноль делить нельзя"

   return x / y

num1 = float(input("Введите первое число: "))

num2 = float(input("Введите второе число: "))

print("Выберите операцию:")

print("1. Сложение")

print("2. Вычитание")

print("3. Умножение")

print("4. Деление")

choice = input("Введите номер операции (1/2/3/4): ")

if choice == '1':

   result = add(num1, num2)

   operation = "+"

elif choice == '2':

   result = subtract(num1, num2)

   operation = "-"

elif choice == '3':

   result = multiply(num1, num2)

   operation = "*"

elif choice == '4':

   result = divide(num1, num2)

   operation = "/"

print(f"Результат: {num1} {operation} {num2} = {result}")