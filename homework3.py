# Mantiqiy amallar

# boshlang'ich bosqich 

# 1 - misol 
A = True
B = False
C = False

# a
a = (A or not A and B) or C 
print(a)  #  true

# b
b = not A or A and (B or C)
print(b)  # false

# c
c = (A or B and not C) and C 
print(c)  # false

# 2 - misol 
X = False
Y = True
Z = False

# a
a = X and not(Z or Y) or not Z
print(a) # true

# b
b = not X or X and (Y or Z)
print(b) # true

# c
c = (X or Y and not Z) and Z
print(c) # false

# 3 - misol 
# a
x = 2
y = 1
a = (not(x * y < 0)) and (y > x)
print(a)  # false

# b
x = 2
y = -2
b = (x >= 2) or (y * y != 5)
print(b) # true

# 5 -misol 
a = int(input("Son kiriting:>>> "))
b = int(input("Son kiriting:>>> "))
c = a % 2 == 0 and b % 2 == 0
print(c) 

# 6 - misol 
X = False
Y = True
Z = False

# a
a = X or Y and not Z
print(a)    # true

# b
b = not X and not Y
print(b)    # false

# c
c = not(X and Y) or Z 
print(c)     # true

# 7 - misol 
# a 
x = 1
y = 2
a = (x >= 0) and (y * y != x)
print(a)      #true

# b 
x = 2
y = 4 
b = (x * y != 0) or (y > x)
print(b)      #true

# 8 - misol 
# a
x = 1
y = 2
a = (not(x * y < 0 )) or (y > x)
print(a)   # true

# b
x = 2
y = 1
b = (x * y != 0) and (y < x)
print(b)  # true

# 9 - misol 
a = int(input("Son kiriting:>>> "))
b = (100 <=a) and (a <= 999)
print(b) 

# 10 - misol 
a = int(input("Son kiriting:>>> "))
b = int(input("Son kiriting:>>> "))
c = int(input("Son kiriting:>>> "))
d = (a < 45) or (b < 45) or (c < 45 )
print(d)

# 11 - misol 
a = int(input("Son kiriting:>>> "))
b = a % 3 == 0 and a % 10 == 0
print(b)

# 12 - misol 
a = int(input("Son kiriting:>>> "))
b = (-137 < a < -51) or (55 < a < 123)
print(b)

# 13 - misol 
x = int(input("Son kiriting:>>> "))
y = int(input("Son kiriting:>>> "))
z = int(input("Son kiriting:>>> "))
a = (x % 5 == 0) or (y % 5 == 0) or (z % 5 == 0)
print(a) 

# 14 - misol 
x = int(input("Son kiriting:>>> "))
y = int(input("Son kiriting:>>> "))
z = int(input("Son kiriting:>>> "))
a = (x > 80) or (y > 80) or (z > 80)
print(a)

# 15 - misol 
a = int(input("Son kiriting:>>> "))
b = not(-10 < a < -2) and not (2 < a <15)
print(b)

# 16 - misol 
a = int(input("Son kiriting:>>> "))
b = (a % 1000 == 0) and (a != 4999)
print(b)

# 17 - misol 
a = int(input("Son kiriting:>>> "))
b = (a % 3 == 0) and (a % 2 == 0)
print(b)

# 18 - misol 
a = int(input("Son kiriting:>>> "))
b = int(input("Son kiriting:>>> "))
c = (a % 2 == 0) and (b % 2 == 0)
print(c)

# 19 - misol 
a = int(input("Son kiriting:>>> "))
b = int(input("Son kiriting:>>> "))
c = int(input("Son kiriting:>>> "))
d = (a % 2 == 0) or (b % 2 == 0) or (c % 2 == 0)
print(d)

# 20 - misol 
a = int(input("Son kiriting:>>> "))
b = not(a % 3 == 0) and not(a % 4 == 0)
print(b) 


# O'rta bosqich 
# Shart operatorlari (if) (elif) (else)
# 1 - misol 
# a
a = int(input("Son kiriting:>>> "))
b = int(input("Son kiriting:>>> "))
if a % 2 == 0:
    print(f"{a} soni juft")
elif b % 2 == 0:
    print(f"{b} son juft son")
else:
    print("Kiritilgan sonlar juft emas")
 
# b
a = int(input("Son kiriting:>>> "))
b = int(input("Son kiriting:>>> "))
c = int(input("Son kiriting:>>> "))
if (a % 3 == 0) and (b % 3 == 0) and (c % 3 == 0):
    print(input(f"Kiritilgan sonlar har biri 3 karrali"))
else:
    print("Kiritilgan sonlar 3 karrali emas")

# 2 - misol
# a
n = int(input("Son kiriting:>>> "))
if n % 4 == 0:
  print(f"{n} soni to`rtga bo'linadi")
elif n % 7 == 0:
  print(f"{n} soni yettiga bo'linadi")
else:
  print(f"{n} soni to`rtga ham yetttiga ham bo'linmaydi")

# b
n = int(input("Son kiriting:>>> "))
if n % 5 == 0 and n % 10 != 0:
  print(f"{n} soni beshga bo'linadi")
elif n % 10 == 0:
  print(f"{n} soni nol bilan tugiydi")
else:
  print(f"{n} soni 5 ga bo'linmaydi")

#  3 -misol
n = int(input("Son kiriting:>>> "))
m = int(input("Son kiriting:>>> "))
k = int(input("Son kiriting:>>> "))
l = int(input("Son kiriting:>>> "))
if n > k and m < l:
  if n + m > k:
    print(f"{n} + {m} > {k}")
  else:
    print(f"{n} + {m} <= {k}")
else:
  print(f"{n} > {k} va {m} < {l} shartlar bir vaqtning o'zida bajarilmadi")

# 4 - misol
n = int(input("Son kiriting:>>> "))
if (n % 3 == 0) and (n % 9 != 0):
  print(f"{n} soni 3 ga bo'linadi 9 ga bolinmaydi")
elif (n % 4 == 0) and (n % 5 == 0) and (n % 24 == 0):
  print(f"{n} soni 4 ga bo'linadi 5 ga va 24 ga bo'linadi")
else:
  print(f"{n} soni shartlarni qanoatlantirmadi")

# 5 - misol
k = int(input("Son kiriting:>>> "))
l = int(input("Son kiriting:>>> "))
n = int(input("Son kiriting:>>> "))
m = int(input("Son kiriting:>>> "))
if (m ** 2 )> (l ** 2):
  if n > 2:
    if(n > 1) and (m <= l + k):
      print(f"{n} > 1 va {m} <= {l} + {k}")
    else:
      print(f"{n} > 1 va {m} <= {l} + {k} shartlar bajarilmadi")
  else:
    print(f"{n} > 2 shart bajarilmadi")
else:
  print(f"{m} ** 2 > {l} ** 2 shart bajarilmadi")

# 6 - misol
depozit_summasi = int(input("Depozit summasini kiriting:>>> "))
if 0 < depozit_summasi < 5000:
  print(f"Yillik to`lov: {depozit_summasi * 0.2}")
elif 5000 < depozit_summasi < 10000:
  print(f"Yillik to`lov: {depozit_summasi * 0.22}")
else:
  print(f"{depozit_summasi} bu summaga yillik to'lov belgilanmagan")

# 7 - misol
n = int(input("Sonkiriting:>>> "))
if (n % 2 == 0) and (n % 7 == 0) and (n % 11 != 0) and (n % 13 != 0):
  print(f"{n} soni haqiqiy")
else:
  print(f"{n} soni haqiqiy emas")

# 8 - misol
n = int(input("Son kiriting:>>> "))
if (n % 3 != 0) and (n % 7 == 0) and (n % 10 == 0):
  print(f"{n} soni haqiqiy")
else:
  print(f"{n} soni haqiqiy emas")

# 9 - misol
k = int(input("Son kiriting:>>> "))
l = int(input("Son kiriting:>>> "))
n = int(input("Son kiriting:>>> "))
m = int(input("Son kiriting:>>> "))
if k == 0:
  if l>m:
    print("Sonlar to'g'ri")
  else:
    print("Sonlar noto'g'ri")
elif k < 0:
  if (2 *l - 3 * n) < m:
    print("Sonlar to'g'ri")
  else:
    print("Sonlar noto'g'ri")
else:
  print("Sonlar noto'g'ri")

# 10 - misol
n = int(input("Son kiriting:>>> "))
if (n % 3 != 0) or (n % 7 == 0):
  print("Haqiqiy")
if (n % 5 != 0) and (n % 4 != 0):
  print("Haqiqiy")
if (n % 8 == 0) and (n % 11 == 0):
  print("Haqiqiy")
else:
  print("Mavhum")

# 11 - misol
xarid_qiymati = int(input("Sotib olingan xarid qiymati:>>> "))
if 400 <xarid_qiymati< 600:
  chegirma = xarid_qiymati * 0.05
elif 600 <xarid_qiymati< 1000:
  chegirma = xarid_qiymati * 0.1
else:
  print(f"{xarid_qiymati} bu qiymatga chegirma belgilanmagan")
  print(f"Umumiy xarid qiymati = {xarid_qiymati}")
print(f"Chegirma = {chegirma}")
print(f"Umimiy xarid qiymati = {xarid_qiymati - chegirma}")

#  12-misol
k = int(input("Son kiriting:>>> "))
l = int(input("Son kiriting:>>> "))
n = int(input("Son kiriting:>>> "))
m = int(input("Son kiriting:>>> "))
if k + l + n + m > 0:
  if (k > 0) and (2 * m > 1):
    print(f"{2 * m} > {1}")
  elif (k < 0) and (n > 31):
    print(f"{n} > {31}")
  else:
    print("Shartlarni qanoatlantirmadi")
else:
  print(f"{k} + {l} + {n} + {m} <= {0}")

# 13 -misol
t = int(input("Enter the time(from 0 to 24) of the conversation.:>>> "))
dt = int(input("Enter the duration(in minuts) of conversation:>>> "))
cost_minut = int(input("Enter the price per minute of the call:>>> "))
day = int(input("Enter the day of the week(from 1 to 7):>>> "))
if (day == 1) or (day == 2) or (day == 3) or (day == 4) or (day == 5):
  if (0 <= t <= 8) or (22 <= t <= 24):
    discount = cost_minut * dt * 0.2
    print(f"\nCost = {cost_minut * dt} sent")
    print(f"Discount = {discount} sent")
    print(f"General cost = {cost_minut * dt - discount} sent")
  else:
      print(f"\nIn {t} time on  {day} is not discount")
elif (day == 6) or (day == 7):
  if 8 < t < 22:
    discount = cost_minut * dt * 0.1
    print(f"\nCost = {cost_minut * dt} sent")
    print(f"Discount = {discount} sent")
    print(f"General cost = {cost_minut * dt - discount} sent")
  elif (0 <= t <= 8) or (22 <= t <= 24):
    discount = cost_minut * dt * 0.3
    print(f"\nCost = {cost_minut * dt} sent")
    print(f"Discount = {discount} sent")
    print(f"General cost = {cost_minut * dt - discount} sent")

# 14 - misol 
# 1
X = True
Y = True
Z = True
a = not(not X and Y) or (X and not Z)
print(a)  # true

# 2 
X = False
Y = False
Z = False
a = not(not X and Y) or (X and not Z)
print(a)  # true

# 3
X = True
Y = True
Z = False
a = not(not X and Y) or (X and not Z)
print(a)  # true

# 4
X = True
Y = False
Z = True
a = not(not X and Y) or (X and not Z)
print(a)  # true

# 5
X = True
Y = False
Z = False
a = not(not X and Y) or (X and not Z)
print(a)  #true 

# 6
X = False
Y = True
Z = False
a = not(not X and Y) or (X and not Z)
print(a)  # false

# 7
X = False
Y = True
Z = True
a = not(not X and Y) or (X and not Z)
print(a) # false

# 8
X = False
Y = False
Z = True
a = not(not X and Y) or (X and not Z)
print(a)  # true

# 15 - misol
math = int(input("Math grade:>>> "))
physics = int(input("Physics grade:>>> "))
Computer_science = int(input("Computer  science grade:>>> "))
if (math == 4) or (math == 5):
  if (physics == 4) or (physics == 5):
    if (Computer_science == 4) or (Computer_science == 5):
      print("True")
    else:
      print("False")
  else:
    print("False")
else:
  print("False")

#  16 -misol
a = int(input("Son kiriting:>>> "))
b = int(input("Son kiriting:>>> "))
c = int(input("Son kiriting:>>> "))
d = int(input("Son kiriting:>>> "))
if (a % 2 == 0) and (b % 2 == 0):
  print("True")
elif (c % 2 == 0) and (d % 2 == 0):
  print("True")
else:
  print("False")
# if (a % 2 == 0 and b % 2 == 0) or (c % 2 == 0 and d % 2 == 0):
#   print("True")
# else:
#   print("False")

# 17 - misol
a = int(input("Son kiriting:>>> "))
b = int(input("Son kiriting:>>> "))
c = int(input("Son kiriting:>>> "))
d = int(input("Son kiriting:>>> "))
if (a % 3 == 0) and ((b % 5 == 0) or (c % 5 == 0) or (d % 5 == 0)):
  print("True")
elif (b % 3 == 0) and ((a % 5 == 0) or (c % 5 == 0) or (d % 5 == 0)):
  print("True")
elif (c % 3 == 0) and ((a % 5 == 0) or (b % 5 == 0) or (d % 5 == 0)):
  print("True")
elif (d % 3 == 0) and ((a % 5 == 0) or (b % 5 == 0) or (c % 5 == 0)):
  print("True")
else:
  print("False")

# 18 - misol
purchase_price = int(input("Enter the price of the purchase:>>> "))
if 1000 <= purchase_price < 2000:
  discount = purchase_price * 0.05
  print(f"Discount = {discount}")
  print(f"General account = {purchase_price - discount} UAH")
elif 2000 <= purchase_price <= 5000:
  discount = purchase_price * 0.1
  print(f"Discount = {discount}")
  print(f"General account = {purchase_price - discount} UAH")
else:
  print(f"Discount = {0}")
  print(f"General account = {purchase_price} UAH")

# 19 - misol
work_experience = int(input("Enter the number of work experience years:>>> "))
salary = int(input("Enter the salary:>>> "))
if 5 < work_experience < 10:
  bonus = salary * 0.02
  print(f"Bonus = {bonus}")
  print(f"General salary = {salary + bonus}")
elif 10 < work_experience < 20:
  bonus = salary * 0.1
  print(f"Bonus = {bonus}")
  print(f"General salary = {salary + bonus}")
else:
  print(f"Bonus = {0}")
  print(f"General salary = {salary}")

# 20 - misol , 14 - misol  
# 1
X = True
Y = True
Z = True
a = X and not(not Y or Z) or Y
print(a)  # True

# 2 
X = False
Y = False
Z = False
a = X and not(not Y or Z) or Y
print(a)  # false

# 3
X = True
Y = True
Z = False
a = X and not(not Y or Z) or Y
print(a)  # true

# 4
X = True
Y = False
Z = True
a = X and not(not Y or Z) or Y
print(a)  # false

# 5
X = True
Y = False
Z = False
a = X and not(not Y or Z) or Y
print(a)  #  false

# 6
X = False
Y = True
Z = False
a = X and not(not Y or Z) or Y
print(a)  # true

# 7
X = False
Y = True
Z = True
a = X and not(not Y or Z) or Y
print(a) # true

# 8
X = False
Y = False
Z = True
a = X and not(not Y or Z) or Y
print(a)  # false

# 21 - misol 
ish_tajribasi = int(input("Ish tajribangizni kiriting:>>> "))
if ish_tajribasi <= 2:
    koeffitsient = 11
    print(f"Koeffitsient = {koeffitsient}")
elif 2 < ish_tajribasi <= 5:
    koeffitsient = 12
    print(f"Koeffitsient = {koeffitsient}")
else:
    koeffitsient = 13
    print(f"Koeffitsient  = {koeffitsient}")

# 22 - misol , 13 - misol
t = int(input("Enter the time(from 0 to 24) of the conversation.:>>> "))
dt = int(input("Enter the duration(in minuts) of conversation:>>> "))
cost_minut = int(input("Enter the price per minute of the call:>>> "))
day = int(input("Enter the day of the week(from 1 to 7):>>> "))
if (day == 1) or (day == 2) or (day == 3) or (day == 4) or (day == 5):
  if (0 <= t <= 8) or (22 <= t <= 24):
    discount = cost_minut * dt * 0.1
    print(f"\nCost = {cost_minut * dt} sent")
    print(f"Discount = {discount} sent")
    print(f"General cost = {cost_minut * dt - discount} sent")
  else:
      print(f"\nIn {t} time on  {day} is not discount")
elif (day == 6) or (day == 7):
  if 8 < t < 22:
    discount = cost_minut * dt * 0.05
    print(f"\nCost = {cost_minut * dt} sent")
    print(f"Discount = {discount} sent")
    print(f"General cost = {cost_minut * dt - discount} sent")
  elif (0 <= t <= 8) or (22 <= t <= 24):
    discount = cost_minut * dt * 0.15
    print(f"\nCost = {cost_minut * dt} sent")
    print(f"Discount = {discount} sent")
    print(f"General cost = {cost_minut * dt - discount} sent")

# 23 - misol , 13 - misol 
dt = int(input("Enter the duration(in minuts) of conversation:>>> "))
location = int(input("Enter the location of conversataion:>>> "))
day = int(input("Enter the day of the week(from 1 to 7):>>> "))
location = location.lower().strip()
if location == "ukraina":
    cost_minut = 0.35
    if (day == 1) or (day == 2) or (day == 3) or (day == 4) or (day == 5):
       discount = cost_minut * dt * 0
       print(f"\ncount = {cost_minut * dt} UAH")
       print(f"Discount = {discount} UAH")
       print(f"General count = {cost_minut * dt - discount} UAH")
    elif (day == 6) or (day == 7):
       discount = cost_minut * dt * 0.1
       print(f"\ncount = {cost_minut * dt} UAH")
       print(f"Discount = {discount} UAH")
       print(f"General count = {cost_minut * dt - discount} UAH")
elif location == "rossiya":
   cost_minut = 0.9
   if (day == 1) or (day == 2) or (day == 3) or (day == 4) or (day == 5):
      discount = cost_minut * dt * 0
      print(f"\ncount = {cost_minut * dt} UAH")
      print(f"Discount = {discount} UAH")
      print(f"General count = {cost_minut * dt - discount} UAH")
   elif (day == 6) or (day == 7):
       discount = cost_minut * dt * 0.1
       print(f"\ncount = {cost_minut * dt} UAH")
       print(f"Discount = {discount} UAH")
       print(f"General count = {cost_minut * dt - discount} UAH")
else:
   print("There is no information about location You enter (404)")

# 24 - misol , 14 - misol 
# 1
A = True
B = True
C = True
D = A and not B or not(A or not C)
print(D)  # false

# 2 
A = False
B = False
C = False
D = A and not B or not(A or not C)
print(D)  # false

# 3
A = True
B = True
C = False
D = A and not B or not(A or not C)
print(D)  # false

# 4
A = True
B = False
C = True
D = A and not B or not(A or not C)
print(D)  # true

# 5
A = True
B = False
C = False
D = A and not B or not(A or not C)
print(D)  # true

# 6
A = False
B = True
C = False
D = A and not B or not(A or not C)
print(D)  # false

# 7
A = False
B = True
C = True
D = A and not B or not(A or not C)
print(D) # true

# 8
A = False
B = False
C = True
D = A and not B or not(A or not C)
print(D)  # true

# 25 - misol 
a = int(input("Son kiriting:>>> "))
b = int(input("Son kiriting:>>> "))
c = int(input("Son kiriting:>>> "))
d = int(input("Son kiriting:>>> "))
if ((a % 7 == 0) or (b % 7 == 0) or (c % 7 == 0) or (d % 7 == 0)) and (a % 2 != 0):
    print("True")
elif ((a % 7 == 0) or (b % 7 == 0) or (c % 7 == 0) or (d % 7 == 0)) and (b % 2 != 0):
    print("True")
elif ((a % 7 == 0) or (b % 7 == 0) or (c % 7 == 0) or (d % 7 == 0)) and (c % 2 != 0):
    print("True")
elif ((a % 7 == 0) or (b % 7 == 0) or (c % 7 == 0) or (d % 7 == 0)) and (d % 2 != 0):
    print("True")
else:
    print("False")

# 26 - misol 
n = int(input("Son kiriting:>>> "))
if n % 5 != 0:
    if(n % 2 == 0) and (n % 3 == 0):
        print(f"{n} soni 2 va 3 ga bo'linadi")
    else:
        print(f"{n} soni 2 va 3 ga bo'linmaydi")
else:
    print(f"{n} soni 5 ga bo'linadi")

# 27 - misol 
print("ax^2 + bx + c = 0")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
D = b ** 2 - 4 * a * c 
if a > 0:
    if D > 0:
       x_1 = (- b + D) / (2 * a) 
       x_2 = (- b - D) / (2 * a) 
       print ("2 ta yechim bor x_1 = {x_1} va x_2 = {x_2}")
    elif D < 0:
        print("yechimi yuq")
    elif D == 0:
        x = -b / a
        print("1 ta yechim bor x = {x}") 
elif D > 0:
    x_1 = (- b + D) / (2 * a) 
    x_2 = (- b - D) / (2 * a) 
    print ("2 ta yechim bor x_1 = {x_1} va x_2 = {x_2}")
elif D < 0:
    print("yechimi yuq")
elif D == 0:
    x = -b / a
    print("1 ta yechim bor x = {x}") 

# 28 - misol
valyuta_turi = input("Valyuta turi:>>> ")
omonat_miqdori = int(input("Omonat miqdori kiriting:>>> "))
valyuta_turi = valyuta_turi.lower().strip()
if valyuta_turi == ("uah"):
    if omonat_miqdori <= 5000:
        yillik_tulov = omonat_miqdori * 0.2
        print(f"Yillik to'lov {yillik_tulov} foiz stavkasi 20 %")
    elif omonat_miqdori > 5000:
        print(f"{omonat_miqdori} miqdorga yillik to'lov belgilanmagan")
elif valyuta_turi == "aqsh":
    if omonat_miqdori <= 5000:
        yillik_tulov = omonat_miqdori * 0.12
        print(f"Yillik to'lov {yillik_tulov} foiz stavkasi 12 %")
    elif omonat_miqdori > 5000:
        print(f"{omonat_miqdori} miqdorga yillik to'lov belgilanmagan")
elif valyuta_turi == "evro":
    if omonat_miqdori <= 5000:
        yillik_tulov = omonat_miqdori * 0.1
        print(f"Yillik to'lov {yillik_tulov} foiz stavkasi 10 %")
    elif omonat_miqdori > 5000:
        print(f"{omonat_miqdori} miqdorga yillik to'lov belgilanmagan")
else: 
    print("Kiritilgan valyuta turida omonat mavjud emas(404)")

# 29 - misol , 23 - misol 
# 1
A = True
B = True
C = True
D = not(A and not B) or (A or not C)
print(D)  # true

# 2 
A = False
B = False
C = False
D = not(A and not B) or (A or not C)
print(D)  # true

# 3
A = True
B = True
C = False
D = not(A and not B) or (A or not C)
print(D)  # true

# 4
A = True
B = False
C = True
D = not(A and not B) or (A or not C)
print(D)  # true

# 5
A = True
B = False
C = False
D = not(A and not B) or (A or not C)
print(D)  # true

# 6
A = False
B = True
C = False
D = not(A and not B) or (A or not C)
print(D)  # true

# 7
A = False
B = True
C = True
D = not(A and not B) or (A or not C)
print(D)  # true

# 8
A = False
B = False
C = True
D = not(A and not B) or (A or not C)
print(D)  # true

# 30 - misol 
a = int(input("Son kiriting:>>> "))
b = int(input("Son kiriting:>>> "))
c = int(input("Son kiriting:>>> "))
d = int(input("Son kiriting:>>> "))
if ((a % 5 == 0) or (b % 5 == 0) or (c % 5 == 0) or (d % 5 == 0)) and (a % 2 == 0):
    print("True")
elif ((a % 5 == 0) or (b % 5 == 0) or (c % 5 == 0) or (d % 5 == 0)) and (b % 2 == 0):
    print("True")
elif ((a % 5 == 0) or (b % 5 == 0) or (c % 5 == 0) or (d % 5 == 0)) and (c % 2 == 0):
    print("True")
elif ((a % 5 == 0) or (b % 5 == 0) or (c % 5 == 0) or (d % 5 == 0)) and (d % 2 == 0):
    print("True")  
elif (a % 5 == 0) or (b % 5 == 0) or (c % 5 == 0) or (d % 5 == 0):
    print("Kiritilgan sonlar qatorida juft son yuq")
else:
    print("Kiritilgan sonlar qatorida 5 ga bo'linadigani yuq")


