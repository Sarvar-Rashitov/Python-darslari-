import math
# Shart operatorlari 

# Boshlang'ich  daraja 
# 1 -misol
x = int(input("Enter the number:>>> "))
y = int(input("Enter the number:>>> "))
if(x ** 2 + y ** 2) > ((x + y) ** 2):
  print("")
else:
  print("")

# 2 - masala
salary = int(input("Enter the salary:>>> "))
work_experience = int(input("Enter the work experience:>>> "))
if 2 <= work_experience < 5:
  bonus = salary * 0.02
elif 5 <= work_experience < 10:
  bonus = salary * 0.05
else:
  print("No bonus is set for the work experience entered.")
print(f"Bonus = {bonus}")
print(f"General salary = {salary + bonus}")

# 3 - misol
x_0 = int(input("Enter the coordinate A(x_0 , y_0) -> x_0 = "))
y_0 = int(input("Enter the coordinate A(x_0 , y_0) -> y_0 = "))
x_1 = int(input("Enter the coordinate B(x_1 , y_1) -> x_1 = "))
y_1 = int(input("Enter the coordinate B(x_1 , y_1) -> y_1 = "))
d_A = math.sqrt(x_0 ** 2 + y_0 ** 2)
d_B = math.sqrt(x_1 ** 2 + y_1 ** 2)
if d_A > d_B:
  print("The distance of the vector A(x_0, y_0) is loger")
elif d_A == d_B:
  print("The distance of the vectors are equal")
else:
  print("The distance of the vector B(x_1, y_1) is loger")

# 4 - misol
a = int(input("Enter the value of triangle side a = "))
b = int(input("Enter the value of triangle side b = "))
c = int(input("Enter the value of triangle side c = "))
if c ** 2 == a ** 2 + b ** 2:
  print("right triangle")
elif c ** 2 > a ** 2 + b ** 2:
  print("Obtuse triangle")
elif c ** 2 < a ** 2 + b ** 2:
  print("Acute triangle")
else:
  print("Triangle inequality does not hold")

# 5 - misol
a = int(input("Enter the number:>>> "))
b = int(input("Enter the number:>>> "))
c = int(input("Enter the number:>>> "))
if a > 0:
  d = a ** 2
  print(f"a^2 = {d}")
if b > 0:
  d = b ** 2
  print(f"b^2 = {d}")
if c > 0:
  d = c ** 2
  print(f"c^2 = {d}")
if a < 0:
  print(f"a = {a}")
if b < 0:
  print(f"b = {b}")
if c < 0:
  print(f"c = {c}")

# 6 - misol
x = int(input("Enter the coordinate x = "))
y = int(input("Enter the coordinate y = "))
if x > 0 and y > 0:
  print("First quarter")
elif x < 0 and y > 0:
  print("Second quarter")
elif x < 0 and y < 0:
  print("Third quarter")
else:
  print("Fourth quarter")

# 7 - misol
a_1 = int(input("Enter the value of triangle side a_1 = "))
b_1 = int(input("Enter the value of triangle side b_1 = "))
c_1 = int(input("Enter the value of triangle side c_1 = "))
a_2 = int(input("Enter the value of triangle side a_2 = "))
b_2 = int(input("Enter the value of triangle side b_2 = "))
c_2 = int(input("Enter the value of triangle side c_2 = "))
p_1 = (a_1 + b_1 + c_1) / 2
p_2 = (a_2 + b_2 + c_2) / 2
S_1 = math.sqrt(p_1 * (p_1 - a_1) * (p_1 - b_1) * (p_1 - c_1))
S_2 = math.sqrt(p_2 * (p_2 - a_2) * (p_2 - b_2) * (p_2 - c_2))
if S_1 > S_2:
  print("The first triangle has a larger area")
elif S_1 == S_2:
  print("The areas of the triangles are equal")
else:
  print("The second triangle has a larger area")

# 8 -misol
a = int(input("Enter the number:>>> "))
b = int(input("Enter the number:>>> "))
c = int(input("Enter the number:>>> "))
if a > 0:
  d = a ** 3
  print(f"{a}^3 = {d}")
if b > 0:
  d = b ** 3
  print(f"{b}^3 = {d}")
if c > 0:
  d = c ** 3
  print(f"{c}^3 = {d}")
if a < 0:
  print(f"{a} = {0}")
if b < 0:
  print(f"{b} = {0}")
if c < 0:
  print(f"{c} = {0}")

# 9 - misol
n = int(input("Enter the natural number:>>> "))
if n % 2 == 0 and n % 5 == 0:
  print(f"The number {n} is even and divisible by 5")
elif n % 3 == 0:
  print(f"The number {n} is even and not divisible by 5")
else:
  print(f"The number {n} is not even and divisible by 5")


# 10 -misol
x = int(input("Enter the coordinate x = "))
y = int(input("Enter the coordinate y = "))
if x > 0 and y > 0:
  print("The point is in the first quarter")
else:
  print("The point is not in the first quarter")

# 11 - misol
deposit_amount = int(input("Enter the deposit amount:>>> "))
deposit_period = int(input("Enter the deposit period:>>> "))
if deposit_period <= 6:
  monthly_payment = deposit_amount * (0.06 / 12)
elif 6 < deposit_period <= 12:
  monthly_payment = deposit_amount * (0.08 / 12)
else:
  print("Invalid deposit period entered.")
print(f"\nmonthly payment = {monthly_payment}")

# 12 - misol
x = int(input("Enter the number:>>> "))
y = int(input("Enter the number:>>> "))
if abs(x - y) ** 2 > abs(x ** 2 - y ** 2):
  print("The square of the difference is large")
else:
  print("The difference of the square is large")

# 13 - misol
x_0 = int(input("Enter the coordinate A(x_0 , y_0) -> x_0 = "))
y_0 = int(input("Enter the coordinate A(x_0 , y_0) -> y_0 = "))
x_1 = int(input("Enter the coordinate B(x_1 , y_1) -> x_1 = "))
y_1 = int(input("Enter the coordinate B(x_1 , y_1) -> y_1 = "))
d_A = math.sqrt(x_0 ** 2 + y_0 ** 2)
d_B = math.sqrt(x_1 ** 2 + y_1 ** 2)
if d_A > d_B:
  print("The distance of the vector B is near")
elif d_A == d_B:
  print("The distance of the vectors are equal")
else:
  print("The distance of the vector A is near")

# 14 - misol
a = int(input("Enter the value of triangle side a = "))
b = int(input("Enter the value of triangle side b = "))
c = int(input("Enter the value of triangle side c = "))
if a == b == c:
  print("The triangle is equilateral")
elif a == b or b == c or c == a:
  print("The triangle is isosceles")
else:
  print("The triangle is scalene")

# 15 - misol
a = int(input("Enter the number:>>> "))
b = int(input("Enter the number:>>> "))
c = int(input("Enter the number:>>> "))
if c ** 2 == a ** 2 + b ** 2:
  print("Pythagorean triple completed")
elif b ** 2 == a ** 2 + c ** 2:
  print("Pythagorean triple completed")
elif a ** 2 == b ** 2 + c ** 2:
  print("Pythagorean triple completed")
else:
  print("Pythagorean triple not completed")

# 16 - misol 
s_circle = int(input("Enter the area of the circle:>>> "))
s_square = int(input("Enter the area of the square:>>> "))
r = math.sqrt(s_circle /math.pi)
a = math.sqrt(s_square)
if 2 * r <= a:
  print("The circle is inside the square")
elif math.sqrt(2) * r >= a:
  print("The square is inside the circle")
else:
  print("The circle and the square do intersect")

# 17 - misol
current_time = input("Enter the current time:>>> ")
current_time = current_time.strip() 
time_oclock = int(current_time[0:2])
time_minut = int(current_time[3:5])
if 0 < time_oclock <= 12 and 60 > time_minut >= 0:
  print("pm")
if time_oclock == 0:
  time_oclock = 24 
if 12 < time_oclock <= 24 and 60 > time_minut >= 0:
  if time_minut > 0 and time_oclock == 24:
    print("pm")
  else:
    print("am")
elif time_oclock > 24 or time_minut > 60 :
  print("You entered incorrectly time.")

# 18 - misol 
n = int(input("Enter the natural number:>>> "))
last_number = str(n).strip()
last_number = int(last_number[-1])
if n % 2 == 0:
    print("The number you entered is couple")
elif last_number + 3 == 10:
    print("The number you entered is ending with 7")
else:
    print("Error")