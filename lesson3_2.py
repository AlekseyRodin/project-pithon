action = input('выберете операцию (+, -, *, /) ')
num_a = int(input("Введите число А "))
num_b = int(input("Введите число В "))

if action == "+":
	print(num_a, "+", num_b, "=", num_a + num_b)
elif action == "-":
	print(num_a, "-", num_b, "=", num_a - num_b)
elif action == "*":
	print(num_a, "*", num_b, "=", num_a * num_b)
elif action == "/":
	print(num_a, "/", num_b, "=", num_a / num_b)
else:
	print("Ошибка: такой операции не существует. Попробуйте ещё раз.")