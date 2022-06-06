total = 0
total_2 = 1
action = input('выберете операцию (+, -, *, /) ')
operands = int(input("Введите колличество операндов"))

if action == "+":
  for line in range(operands):
    num = int(input("Введите число: "))
    total += num
  print("сумма: ", total)
elif action == "-":
  for line in range(operands):
    num = int(input("Введите число: "))
    total -= num 
  print("разность: ", total)
elif action == "*":
  for line in range(operands):
    num = int(input("Введите число: "))
    total_2 = num * total_2
  print("произведение: ", total_2)
elif action == "/":
  for line in range(operands):
    num = int(input("Введите число: "))
    total_2 = num / total_2
  print("ltktybt: ", total_2)
else:
  print('wrong enter')