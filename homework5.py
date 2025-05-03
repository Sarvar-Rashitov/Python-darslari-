# shart operatorlari 
# o'rta bosqich 
# 1- misol 
# a
a = int(input("Enter the number:>>> "))
b = int(input("Enter the number:>>> "))
if a > 0:
    if b > 0:
        orta_arifmetigi = (a +b) / 2
        print(f"o'rta arifmetigi = {orta_arifmetigi}")
    elif b < 0:
        b = - b
        orta_arifmetigi = (a + b) / 2
        print(f"o'rta arifmetigi = {orta_arifmetigi}")
else: 
    a = - a
    if b > 0:
        orta_arifmetigi = (a +b) / 2
        print(f"o'rta arifmetigi = {orta_arifmetigi}")
    elif b < 0:
        b = - b
        orta_arifmetigi = (a + b) / 2
        print(f"o'rta arifmetigi = {orta_arifmetigi}")

# b
if a > 0:
    if b > 0:
       modul =  (a * b) ** (1 / 2 )
       print(f"modullari ko`paytmasini kvadrat ildizini = {modul}")
    elif b < 0:
        b = - b
        modul =  (a * b) ** (1 / 2 )
        print(f"modullari ko`paytmasini kvadrat ildizini = {modul}")
else: 
    a = - a
    if b > 0:
       modul =  (a * b) ** (1 / 2 )
       print(f"modullari ko`paytmasini kvadrat ildizini = {modul}")
    elif b < 0:
        b = - b
        modul =  (a * b) ** (1 / 2 )
        print(f"modullari ko`paytmasini kvadrat ildizini = {modul}")

# 2 - misol
a = int(input("Enter the number:>>> "))
b = int(input("Enter the number:>>> ")) 
c= int(input("Enter the number:>>> ")) 
if a == b and b == c:
    print("The triangle is equilateral")
elif a == b or b == c or a == c:
    print("The triangle is isosceles")  
else:
    print("The triangle is scalene")

# 3 - misol
year = int(input("Enter the number year:>>> "))
if year % 4 == 0:
    if year > 0:
        print(f"{year} yil eramizdan avvalgi- kabisa yili")
    else:
        print(f"{year} yil eramizdagi kabisa yili")
else: 
    print("Kiritilgan yil kabisa yili emas")

# 4 - misol
xarid_qiymati = int(input("Xarid qiymatini kiriting:>>> "))
if xarid_qiymati > 100_000:
     discount = xarid_qiymati * 0.1
     print(f"chegirma = {discount}")
     print(f"Xarid qiymati = {xarid_qiymati - discount}")
else:
    print(f"{xarid_qiymati} xarid qiymatiga chegirma belgilanmagan ")

# 5 - misol 
vazn = int(input("Vazningizni  kiriting:>>> "))
tall = int(input("Bo'yingizni kiriting:>>> "))
# if vazn / tall < :
#     print("Ozg'inlik")
# elif vazn / tall > :
#     print("Semizlik")
# else:
#     print("normal")

# 6 - misol
print("Hozirgi zamonda ishlatilinayotgan klaviaturani kim yaratgan?")
a = "QWERTY"
b = "ASKOL"
c = "ALISEY"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
answer = input("Variantlardan birini kiriting!>>> ")
answer = answer.strip()
if answer == a:
    print("Javob to'gri")
else:
    print(f"Javob noto'g'ri /n To'g'ri javob {a}")

# 7 - misol 
xarid_qiymati = int(input("Xarid qiymatini kiriting:>>> "))
if xarid_qiymati > 500:
     discount = xarid_qiymati * 0.05
     print(f"chegirma = {discount}")
     print(f"Xarid qiymati = {xarid_qiymati - discount}")
elif xarid_qiymati > 1_000:
    discount = xarid_qiymati * 0.1
    print(f"chegirma = {discount}")
    print(f"Xarid qiymati = {xarid_qiymati - discount}")
else:
    print(f"{xarid_qiymati} xarid qiymatiga chegirma belgilanmagan ")

# 8 - misol
month = ["yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul","avgust", "sentabr", "oktabr", "noyabr", "dekabr"]
month_number = int(input("Oy raqamini kiriting:>>> "))
if month[month_number-1]:
    print(month[month_number-1])
else:
    print("Error")

# 9 -misol
a = int(input("Enter the number:>>> "))
b = int(input("Enter the number:>>> "))
c = int(input("Enter the number:>>> "))
if a > b and a > c:
    if b > c:
        print(f"{b} o'rtanchi son")
    else:
        print(f"{c} o'rtanchi son")
elif b > a and b > c:
    if a > c:
        print(f"{a} o'rtanchi son")
    else:
        print(f"{c} o'rtanchi son")
elif c > a and c > b:
    if a > b:
        print(f"{a} o'rtanchi son")
    else:
        print(f"{b} o'rtanchi son")

# 10 -misol
a = int(input("Enter the number:>>> "))
b = int(input("Enter the number:>>> "))
c = int(input("Enter the number:>>> "))
if a > b and a > c:
    if b > c:
        print(f"{c} kichkina son")
    else:
        print(f"{b} kichkina son")
elif b > a and b > c:
    if a > c:
        print(f"{c} kichkina son")
    else:
        print(f"{a} kichkina son")
elif c > a and c > b:
    if a > b:
        print(f"{b} kichkina son")
    else:
        print(f"{a} kichkina son")

# 11 - misol 
a = int(input("Uchburchak tomonini kiriting:>>> a = "))
b = int(input("Uchburchak tomonini kiriting:>>> b = "))
c = int(input("Uchburchak tomonini kiriting:>>> c = "))
if c ** 2 == a ** 2 + b ** 2:
    print("To'g'ri burchakli uchburchak")
elif c ** 2 > a ** 2 + b ** 2:
    print("O'tmas burchakli uchburchak")
else:
    print("O'tkir burchakli o'chburchak")

# 12 - misol
a = int(input("Enter the  number:>>> "))
b = int(input("Enter the  number:>>> "))
if a % b == 0:
    print(f"{a} soni {b} soniga qoldiqsiz bo'linadi")
elif b % a == 0:
    print(f"{b} soni {a} soniga qoldiqsiz bo'linadi ")
else:
    print("Sonlar bir-biriga karrali emas")

# 13 - misol 
a = int(input("Enter the number:>>> "))
b = int(input("Enter the number:>>> "))
c = int(input("Enter the number:>>> "))
if a > 0:
    if b > 0:
        if c > 0:
            c = c
        else:
            c = -c
    else:
        b = -b
        if c > 0:
            c = c
        else:
            c = -c
elif b > 0:
    if a > 0:
        if c > 0:
            c = c
        else:
            c = -c
    else:
        a = -a
        if c > 0:
            c = c
        else:
            c = -c

elif c > 0:
    if b > 0:
        if a > 0:
            a = a
        else:
            a = -a
    else:
        b = -b
        if a > 0:
            a = a
        else:
            a = -a
orta_arifmetik = (a + b + c) / 3
if a > orta_arifmetik:
    print(f"{a} katta {orta_arifmetik}")
elif b > orta_arifmetik:
    print(f"{b} katta {orta_arifmetik}")
elif c > orta_arifmetik:
    print(f"{c} katta {orta_arifmetik}")

# 14 - misol 
a = int(input("Enter the number:>>> "))
b = int(input("Enter the number:>>> "))
c = int(input("Enter the number:>>> "))
if a > b and a > c:
    if b > c:
        print(f"{a} > {b} > {c}")
    else:
        print(f"{a} > {c} > {b}") 
elif b > a and b > c:
    if a > c:
        print(f"{b} > {a} > {c}")
    else:
        print(f"{b} > {c} > {a}") 
elif c > a and c > b:
    if b > a:
        print(f"{c} > {b} > {a}")
    else:
        print(f"{c} > {a} > {b}") 
else:
    print("Kiritilgan sonlar ichida bir-birbiriga tenglari bor")

# 15 - misol 
a = int(input("Enter the number:>>> "))
if 9_999 >= a > 999:
    a_1000 = a // 1000
    a_delta = a - a_1000 * 1000
    a_100 = a_delta // 100
    x = a_delta - a_100 * 100
    print(x)
elif 9_999 < a <= 99_999:
    a_10000 = a // 10_000
    a_delta_1 = a  - a_10000 * 10_000  
    a_1000 = a_delta_1 // 1000
    a_delta = a - a_1000 * 1000
    a_100 = a_delta // 100
    x = a_delta - a_100 * 100  
    print(x)
elif 99_999 < a < 999_999:
    a_100_000 = a // 100_000
    a_delta_2 = a - a_100_000 * 100_000
    a_10000 = a_delta_2 // 10_000
    a_delta_1 = a  - a_10000 * 10_000  
    a_1000 = a_delta_1 // 1000
    a_delta = a - a_1000 * 1000
    a_100 = a_delta // 100
    x = a_delta - a_100 * 100  
    print(x)

# 16 - misol 
x = int(input("Enter the real number:>>> "))
if x <= 0:
    f_x = -x
    print(f_x)
elif x >= 2:
    f_x = 2
    print(f_x)
elif 0 < x < 2:
    f_x = x ** 2 
    print(f_x)

# yuqori bosqich 
# 1 - misol 
print("ax^2 + bx + c = 0")
a = int(input("a = "))
b = int(input("a = "))
c = int(input("a = "))
d = b ** 2 - 4 * a * c
if d > 0:
    x_1 = (-b + d ** (1/2)) / (2 * a)
    x_2 = (-b - d ** (1/2)) / (2 * a)
    print(f"Ikkta yechim bor x_1 = {x_1}, x_2 = {x_2}")
elif d == 0:
    x = - b / (2 * a)
else:
    print("tenglama ildizga ega emas")

# 2 - misol 
n = int(input("Ikki xonali son  kiriting:>>> "))
a = int(input("Raqam kiriting:>>> "))
if 9 < n < 99:
    if n % 5 == 0 or n // 10 == 5:
        print("Kiritilgan sonda 5 raqami mavjud")
    else:
        print("Kiritilgan sonda 5 raqami mavjud emas")
    if n - (n // 10) * 10 == a or n // 10 == a:
        print(f"Kiritilgan sonda {a} raqami bor")
    else:
        print(f"Kiritilgan sonda {a} yuq")
else:
    print("kiritilgan son ikkixonali emas")

# 3 - misol # 4 - misol 

# 5 - misol 
n = int(input("To'rt xonali son kiriting:>>> "))
n_1000 = n // 1000
n_100 = (n - n_1000 * 1000) // 100
n_10 = ((n - n_1000 *1000) - n_100 * 100) // 10
n_1 = (((n - n_1000 *1000) - n_100 * 100)-n_10 * 10)
if n_1 == n_10 == n_100 == n_1000:
    print(f"{n} soni polindrom")
elif n_1 == n_1000 and n_10 == n_100:
    print(f"{n} soni polindrom")
else:
    print("kiritilgan son polindrom emas")

# 6 - misol
n = int(input("Olti xonali son kirting:>>> "))
n_100_000 = n // 100_000
n_10_000 = (n - n_100_000 * 100_000) // 10_000
n_1000 = ((n - n_100_000 * 100_000) - n_10_000 * 10_000) // 1000 
n_100 = (((n - n_100_000 * 100_000) - n_10_000 * 10_000) - n_1000 * 1000) // 100 
n_10 = ((((n - n_100_000 * 100_000) - n_10_000 * 10_000) - n_1000 * 1000) - n_100 * 100) // 10
n_1 = (((((n - n_100_000 * 100_000) - n_10_000 * 10_000) - n_1000 * 1000) - n_100 * 100) - n_10 * 10)
if n_100_000 + n_10_000 + n_1000 == n_100 + n_10 + n_1:
    print(f'{n} son "omadli"')
else:
    print(f'{n} soni "omadli" emas')

# 7 - misol 
n = int(input("Uchxonali son kriting:>>> "))
n_100 = n // 100
n_10 = (n - n_100 * 100) // 10
n_1 = n - n_100 * 100 - n_10 * 10
if n_100 + n_10 + n_1 > 9:
    print(f"{n} son raqmlar yigindisi  ikkixonali son")
else:
    print(f"{n} son raqmlar yigindisi  ikkixonali son emas")
if n_100 * n_10 * n_1 > 999:
    print(f"{n} soni raqamlar ko'paytmasi to'rtxonali son")
else:
    print(f"{n} soni raqamlar ko'paytmasi to'rtxonali son emas")

# 8 - misol
n = int(input("To'rtxonali son kiriting:>>> "))
b = int(input("Son kiriting:>>> "))
n_1000 = n // 1000
n_100 = (n - n_1000 * 1000) // 100
n_10 = ((n - n_1000 *1000) - n_100 * 100) // 10
n_1 = (((n - n_1000 *1000) - n_100 * 100)-n_10 * 10)
if n_1000 * n_100 * n_10 * n_1 > b:
    print(f"{b} sonidan katta {n} soninig raqamlar ko'paytmasi")
else:
    print(f"{b} sonidan  {n} soninig raqamlar ko'paytmasi katta emas")
if (n_1000 + n_100 + n_10 + n_1) % 3 == 0:
    print(f"{n} raqamlari yig`indisi 3 ga karrai")
else:
    print(f"{n} raqamlari yig`indisi 3 ga karrai emas")

# 9 - misol
n = int(input("Uchxonali son kriting:>>> "))
n_100 = n // 100
n_10 = (n - n_100 * 100) // 10
n_1 = n - n_100 * 100 - n_10 * 10
if n_1 == n_10 == n_100:
    print(f"{n} barcha raqamlari bir xil")
else:
    print(f"{n} barcha raqamlari bir xil emas")

# b
if n_1 == n_10 or n_1 == n_100 or n_10 == n_100:
    print(f"{n} raqamlari orasida bir xillari bor")
else:
    print(f"{n} raqamlari orasida bir xillari yuq")

# 10 - misol 
n = int(input("To'rtxonali son kiriting:>>> "))
n_1000 = n // 1000
n_100 = (n - n_1000 * 1000) // 100
n_10 = ((n - n_1000 *1000) - n_100 * 100) // 10
n_1 = (((n - n_1000 *1000) - n_100 * 100)-n_10 * 10)
if n_1000 + n_100 == n_10 + n_1:
    print(f"{n} boshidagi 2 ta raqamlari yig`indisi oxirgi 2 ta raqami yig`indisiga teng")
else:
    print(f"{n} boshidagi 2 ta raqamlari yig`indisi oxirgi 2 ta raqami yig`indisiga teng emas")

# b
if (n_1000 + n_100 + n_10 + n_1) % 7 == 0:
    print(f"{n} raqamlari yig`indisi 7 ga karrai")
else:
    print(f"{n} raqamlari yig`indisi 7 ga karrai emas")

# 11 -misol
n = int(input("To'rtxonali son kiriting:>>> "))
a = int(input("Son kiriting:>>> "))
n_1000 = n // 1000
n_100 = (n - n_1000 * 1000) // 100
n_10 = ((n - n_1000 *1000) - n_100 * 100) // 10
n_1 = (((n - n_1000 *1000) - n_100 * 100)-n_10 * 10)
if (n_1000 * n_100 * n_10 * n_1) % 3 == 0:
    print(f"{n} raqamlari ko`paytmasi 3 ga karrali;")
elif (n_1000 * n_100 * n_10 * n_1) % a == 0:
    print(f"{n} raqamlari ko`paytmasi {a} ga karrali;")
else:
    print(f"{n} raqamlari ko`paytmasi 3 ga karrali emas;")  