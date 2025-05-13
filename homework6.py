import random
"""Takrorlanuvchi Algoritmlash 
Boshlang'ich bosqich
"""
# # 1 - misol 
# a = int(input("Son kiriting:>>> "))
# b = int(input("Son kiriting:>>> "))
# for i in range(a,b):
#     print(i, end=", ")

# # 2 - misol 
# a = int(input("Son kiriting:>>> "))
# b = int(input("Son kiriting:>>> "))
# n = 0 
# for i in range(b - 1, a, -1):
#     n +=1
#     print(i, end=", " )
# print(n)

# # 3 - misol
# a = int(input("Son kiriting:>>> "))
# n = int(input("Son kiriting:>>> "))
# s = 1
# for i in range(n):
#     s *= a
# print(s)

# # 4 - misol
# a = int(input("Son kiriting:>>> "))
# n = int(input("Son kiriting:>>> "))
# b = 1
# for i in range(1, n + 10):
#     b *= a
#     print(f"{a}^{i}={b}")

# # 5 - misol 
# a = int(input("Son kiriting:>>> "))
# n = int(input("Son kiriting:>>> "))
# s = 1
# summa = 1
# for i in range(n):
#     s *= a
#     summa +=s
#     print(s)
# print(summa) 

# # 6 - misol 
# a = int(input("Son kiriting:>>> "))
# n = int(input("Son kiriting:>>> "))
# summa = 0
# for i in range(n):
#     sum= 1 / (i+1)
#     summa += sum
#     if summa > a:
#         print(i+1)
# print(summa) 

# # 7 - misol 
# n = int(input("Son kiriting:>>> "))
# summa = 1
# for i in range(n):
#     summa *= (i + 1)
# print(summa)

# # 8 - misol 
# n = int(input("Son kiriting:>>> "))
# summa = 2
# for i in range(n):
#     summa *= (1 / (i + 1))
# print(summa)    

# # 9 - misol 
# x = int(input("Son kiriting:>>> "))
# n = int(input("Son kiriting:>>> "))
# summa = 1
# for i in range(n):
#     summa += (x / (i + 1))
#     x *= x
# print(summa)

# # 10 - misol 
# x = int(input("Son kiriting:>>> "))
# n = int(input("Son kiriting:>>> "))
# summa = 0
# for i in range(n):
#     summa += (((-1) ** i) * (x ** (2 * i + 1))) /(2 * i + 1)
# print(summa)

# # 11 - misol 
# x = int(input("Son kiriting:>>> "))
# n = int(input("Son kiriting:>>> "))
# summa = 1
# for i in range(n):
#     summa += (((-1) ** (i + 1)) * (x ** (2 * (i + 1)))) / (2 * (i + 1))
# print(summa)

# # 12 - misol 
# x = int(input("Son kiriting:>>> "))
# n = int(input("Son kiriting:>>> "))
# summa = 0
# for i in range(n):
#     summa += (((-1) ** (i)) * (x ** (i + 1))) / (i + 1)
# print(summa)

# # 13 - misol 
# n = int(input("Son kiriting:>>> "))
# for i in range(10, n + 1):
#     if i % 5 == 0:
#         print( i, end=", ")

# # 14 - misol 
# for i in range(11, 100):
#     print("{}^{}={}".format(i , 2 , i ** 2))

# # 15 - misol 
# n = int(input("Son kiriting:>>> "))
# summa = 1
# daraja = 1
# for i in range(n):
#     summa *= (i + 1)
#     daraja *= 2
# print(summa)
# print(daraja)

# # 16 - misol 
# n = int(input("Son kiriting:>>> "))
# a = []
# for i in range(10, n):
#     if i < 100:
#         a.append(i)
# print(max(a))

# # 17 - misol 
# N = int(input("N ni kiriting (N > 10): "))
# for son in range(10, N + 1):
#     # Raqamlar yig'indisi
#     yigindi = 0
#     vaqtinchalik = son
#     while vaqtinchalik > 0:
#         raqam = vaqtinchalik % 10
#         yigindi += raqam
#         vaqtinchalik //= 10
#     # Birinchi raqam (eng chapdagi raqam)
#     birinchi_raqam = int(str(son)[0])  # sonni matnga aylantirib, 1-chi raqamni olami
#     print(f"{son}: Birinchi raqam = {birinchi_raqam}, Raqamlar yig'indisi = {yigindi}")  
          
# # 18 - misol 
# son = int(input("Son kiriting: "))
# asl_son = son         # Asl sonni saqlab qo‘yamiz
# teskari = 0
# while son > 0:
#     raqam = son % 10
#     teskari = teskari * 10 + raqam
#     son = son // 10
# if asl_son == teskari:
#     print("Bu son palindrom.")
# else:
#     print("Bu son palindrom emas.")

# # 19 - misol 
# summa = 0
# for i in range(12, 81):
#     summa += i ** 2
# print(summa)

# # 20 - misol
# summa = 0
# for i in range(22, 89):
#     summa -= i ** 2
# print(summa)

# # 21 - misol
# a = int(input("Son kiriting:>>> "))
# n = int(input("Son kiriting:>>> "))
# b = 0 
# for i in range(1, n + 1):
#     b += (i ** 2)
# print("{} - {} = {}".format(b, a ** 2, b-a)) 

# # 22 - misol 
# n = int(input("Son kiriting:>>> "))
# a = []
# for i in range(10, n):
#     if i < 100:
#         a.append(i)
# print(min(a))
     
# # 23 - misol 
# a = int(input("Son kiriting:>>> "))
# n = int(input("Son kiriting:>>> "))
# b = 1 
# for i in range(n):
#     b *= a 
# print(b)
    
# # 24 - misol
# n = int(input("Son kiriting:>>> "))
# faktorial = 1
# for i in range(1, n):
#     faktorial *= i  
# print("N! = {}".format(faktorial))

# # 25 - misol 
# n = int(input("Son kiriting:>>> "))
# summa = 0
# for i in range(n):
#     summa += (i ** 2)
# print("1 dan n gacha bolgan sonlar kvadratlari yig'indisi = {}".format(summa))

# # 26 - misol 
# n = int(input("Son kiriting:>>> "))
# summa = 0
# for i in range(n):
#     if i %  2 == 0:
#         summa += (i ** 2) 
#     else:
#         summa += (i ** 3)
# print(summa)

# # 27 - misol 
# n = int(input("Son kiriting:>>> "))
# summa = 1 
# for i in range(n):
#     if i % 5 != 0:
#         print(i , end=", ")
#         summa += i
#     if i % 3 == 0:
#         print(i , end=", ")
#         summa += i
# print(summa)

# # 28 - misol 
# n = int(input("Son kiriting:>>> "))
# for i in range(n):
#     if i % 5 == 0:
#         print(i, end=", ")

# # 29 - misol
# n = int(input("Son kirting:>>> "))
# a  = 1
# b = 0
# for i in range(n):
#    a *= 2
#    if n == a:
#       print("{} = {} ^ {}".format(n, 2, i)) 
# else:                                            # for tashqarida else yozsa bo'larkan 
#     print("Error")   

# # 30 - misol ?
# n = int(input("Son kirting:>>> "))
# print("{} = ".format(n), end="")
# for i in range(1, int(n ** (1/2))):
#     if n % i == 0:
#         print("{}".format(i), end=" * ")

# # 31 - misol 
# # Berilgan oraliqdagi tub sonalrni ajratib olish
# n  = int(input("Son kiriting:>>> "))
# for i in range(2, n): 
#     tub = True
#     for j in range(2, int(i ** 0.5) + 1):  
#         if i % j == 0:
#             tub = False
#             break
#     if tub:
#         print(i, end=' ')

# # 32 - misol
# m = int(input("Son kiriting:>>> "))
# n = int(input("Son kiriting:>>> "))
# summa = 0 
# for i in range(m,n):
#     summa += (i ** 2)
# print(summa)

# # 33 - misol 
# m  = int(input("Son kiriting:>>> "))
# n  = int(input("Son kiriting:>>> "))
# summa = 0 
# for i in range(m, n):
#     if i % 2 != 0:
#         summa += (i ** 2)
# print(summa)

# # 34 - misol 
# summa = 1
# for i in range(-80,80):
#     if i % 7 == 0:
#         if i % 2 != 0:
#             summa *= i
# print(summa)

# # 35 - misol
# summa = 0
# for i in range(-100,100):
#     if i % 9 == 0 and i > 0:
#         summa += i
# print(summa)

# # 36 - misol
# n = int("(100,800) oralig'ida bo'lgan natural son kiriting:>>> ")
# k = 0
# for i in range(n,800):
#     k += 1
# print(k)

# # 37 - misol 
# n = int(input("Son kiriting:>>> "))
# for i in range(1, n):
#     for j in range(1, n):
#         if i % j != 0:
#             print("{} va {} sonlar o'zaro tub".format(i, j))

# # 38 - misol
# p = int(input("Birinchi sonni kiriting:>>> "))
# q = int(input("Birinchi son bilan o'zaro tub bo'lgan son kiriting:>>> "))
# print("{} = ".format(q), end="")
# for i in range(1, int(q ** (1/2))):
#     if q % i == 0:
#         print("{}".format(i), end=" * ")

# # 39 - misol 
# n = int(input("Son kirting:>>> "))
# print("{} = ".format(n), end="")
# for i in range(1, int(n ** (1/2))):
#     if n % i == 0:
#         print("{}".format(i), end=" * ")

# # 40 - misol
# n = int(input("Natural son kiriting:>>> "))
# for i in range(n):
#     count = 0
#     for j in range(1, n):
#         if i % j == 0:
#             count +=1
#     if count == 2:
#         print(i, end=", ")

# # 41 - misol
# m = int(input("Son kiriting:>>> "))
# n = int(input("Son kiriting:>>> "))
# summa = 1
# for i in range(m,n):
#     if i % 2 == 0:
#         summa *= (i ** 2) 
# print(summa)

# # 42 - misol 
# n = int(input("Son kiriting:>>> "))
# summa = 0 
# a = 1
# for i in range(1,n):
#     a *= i * (i + 1)
#     summa += a 
# print(summa)

# # 43 - misol 
# n = int(input("Son kiriting:>>> "))
# summa = 1
# for i in range(1,n):
#     summa /= (i ** 3)
# print(summa)

# # 44 - misol
# m = int(input("Son kiriting:>>> "))
# n = int(input("Son kiriting:>>> ")) 
# summa = 1
# for i in range(m,n):
#     summa /= i
# print(summa ** 2)

# # 45 - misol
# for i in range(-20,20):
#     if i % 5 == 0 and i < 0:
#         summa += i
# print(summa)

# # 46 - misol
# summa = 0
# for i in range(0,100):
#     if i % 4 == 0:
#         summa += i
# print(summa)

# # 47 - misol
# n = int(input("Son kiriting:>>> "))
# summa = 1
# for i in range(1,n):
#     summa /= (i ** 2)
# print(summa)

# # 48 - misol
# for i in range(100,200):
#     if i % 2 != 0:
#         print(i, end=", ")

# # 49 - misol
# m = int(input("Son kiriting:>>> "))
# n = int(input("Son kiriting:>>> "))
# summa = 1
# for i in range(m,n):
#     summa *= (i ** 3)
# print(summa)

# # 50 - misol
# m = int(input("Son kiriting:>>> "))
# n = int(input("Son kiriting:>>> "))
# summa = 0
# for i in range(1,n):
#     if m <= summa:
#         break
#     summa += (i ** 2)
#     print(i)

# # 51 - misol
# m = int(input("Son kiriting:>>> "))
# n = int(input("Son kiriting:>>> "))
# summa = 1
# for i in range(m,n):
#     if i % 2 != 0:
#         summa *= (i ** 2)
# print(summa)

# # 52 - misol
# m = int(input("Son kiriting:>>> "))
# n = int(input("Son kiriting:>>> "))
# summa = 1
# for i in range(m,n):
#     if i % 2 == 0:
#         summa *= (i ** 2)
# print(summa)


"""O'rta bosqich"""
# # 1 - misol
# for i in range(1,21):
#     print(f"{i} dyuym = {i * 2.54} sm")

# # 2 - misol
# for i in range(2,101):
#     if i % 5 == 0 and i % 2 == 2:
#         print(i, end=", ")

# # 3 - misol
# for i in range(-500, 500):
#     yuzlik_xona = (abs(i) - (abs(i) // 100) * 100) // 10
#     if yuzlik_xona % 2 == 0:
#         print(i, end=", ")

# # 4 - misol 
# summa = 0
# for i in range(-99,99):
#     if abs(i) % 2 != 0:
#         summa += abs(i)
# print(summa)

# # 5 - misol
# for i in range(0, 700):
#     yuzlik_xona = (abs(i) - (abs(i) // 100) * 100) // 10
#     if yuzlik_xona % 2 != 0:
#         print(i, end=", ")

# # 6 - misol
# n = int(input("Son kiriting:>>> "))
# for i in range(n, 2, -1):
#     if n % i == 0:
#         print(i, end=", ")

# # 7 - misol
# x = int(input("Birinchi sonni kiriting:>>> ")) 
# y = int(input("Ikkinchi sonni kiriting:>>> ")) 
# if x % y == 0:
#     EKUB = y
# elif y % x == 0:
#     EKUB = x
# for i in range(int(y * 0.5), 1, -1):
#     if x % i == 0 and y % i == 0:
#         EKUB = i
#         break
# print("EKUB({0}, {1}) = {2}".format(x, y, i))

# # 8 - misol
# x=int(input("Birinchi sonni kiriting:>>> "))
# y=int(input("Ikkinchi sonni kiriting:>>> "))
# if x > y:
#     z = x
# else:
#     z = y
# while(True):
#     if((z % x == 0) and (z % y == 0)):
#         EKUK = z
#         break
#     z += 1
# print("EKUK({}, {}) = {}".format(x, y, z))

# # 9 - misol
# son = int(input("Butun musbat son kiriting: "))
# if son == 0:
#     raqamlar_soni = 1
# else:
#     raqamlar_soni = 0
#     while son > 0:
#         son = son // 10
#         raqamlar_soni += 1
# print("Raqamlar soni:", raqamlar_soni)


# # 10 - misol 
# m = int(input("Son kirting:>>> "))
# for i in range(1,1000):
#     if i > 99 and i % 2 != 0:
#         print(f"({i} ^ 3) * {m} = {(i ** 3) * m}")

# # 11 - misol
# m = int(input("Son kirting:>>> "))
# for i in range(1,1000):
#     if i > 99 and i % 5 == 0:
#         print(f"({i} ^ 2) / {m} = {(i ** 2) / m}")

"""# 12 - misol
n = int(input("Son kiriting:>>> "))
m = int(input("Son kiriting:>>> "))
"""

# # 13 - misol 
# summa = 1
# a = 1
# b = 0
# # for i in range(10):
# #     a *= 2
# #     summa += a
# # print(summa) 
# for i in range(11):
#     b += i
#     summa *= b
# print(summa)

# # 14 - misol
# m = int(input("Son kiriting:>>> "))
# for i in range(1,1000):
#     if i < 100:
#         yuzlik_xona = i // 10
#         if yuzlik_xona % 2 != 0:
#             print(f"{i} / {m} = {i / m}")
#     if i > 99:
#         yuzlik_xona = (i - (i // 100) * 100) // 10
#         if yuzlik_xona % 2 != 0:
#             print(f"{i} / {m} = {i / m}")

# # 15 - misol
# n = 0 
# for i in range(100_000, 1_000_000):
#     birinchi_raqam = i // 100_000
#     ikkinchi_raqam = (i- birinchi_raqam * 100_000) // 10_000
#     uchinnchi_raqam = (i- birinchi_raqam * 100_000 - ikkinchi_raqam * 10_000) // 1000
#     tortichi_raqam = (i- birinchi_raqam * 100_000 - ikkinchi_raqam * 10_000 - uchinnchi_raqam * 1000) // 100
#     beshinchi_raqam = (i- birinchi_raqam * 100_000 - ikkinchi_raqam * 10_000 - uchinnchi_raqam * 1000 - tortichi_raqam * 100) // 10
#     oltinchi_raqam = i- birinchi_raqam * 100_000 - ikkinchi_raqam * 10_000 - uchinnchi_raqam * 1000 - tortichi_raqam * 100 - beshinchi_raqam * 10
#     if birinchi_raqam == oltinchi_raqam and ikkinchi_raqam == beshinchi_raqam and uchinnchi_raqam == tortichi_raqam:
#         if birinchi_raqam + ikkinchi_raqam + uchinnchi_raqam == 13:
#             n += 1
# print(n)

"""# 16 - misol
"""

# # 17 - misol
# guess = [] 
# ortacha_boy = 0
# guess_number = int(input("O'quvchilar sonini kiriting:>>> "))
# for i in range(1,guess_number + 1):
# #     guess.append(int(input(f"{i} - o'quvchi bo'y uzinligizni kiriting:>>> ")))
# # print(f"O'rtacha bo'y uzinligi {sum(guess) // guess_number} ga teng")
#     ortacha_boy += int(input(f"{i} - o'quvchi bo'y uzinligizni kiriting:>>> ")) 
# print(f"O'rtacha bo'y uzinligi { ortacha_boy / guess_number} ga teng")

"""# 18 - misol
"""

# # 19 - misol
# n = int(input("Son kiriting:>>> "))
# raqam = int(input("Kiritilgan son oxiridan oldingi qarab sanlgnada, nechinchi raqamini chiqazib beri:>>> "))
# print("10 dan kotta son kiriting!") if n < 10 else print(end="")
# vaqtinchalik_son = n
# i = 1
# while n > 0 :
#     if i == raqam:
#         raqam_value = vaqtinchalik_son % 10 
#         print(raqam_value)
#         break
#     vaqtinchalik_son //= 10 
#     i += 1

# # 20 - misol
# m = int(input("Son kiriting:>>> "))
# for i in range(1, 1000):
#     minglik_xona = i // 100
#     yuzlik_xona = (i - (i // 100) * 100) // 10
#     if yuzlik_xona % 2 == 0:
#         print(f"{i} % {m} = {i % m}")

# # 21 - misol
# n  = int(input("Son kiriting:>>> "))
# summa = 0
# for i in range(n):
#     summa += 1 / (i + 1)
# print(summa)

# # 22 - misol
# vaqt = int(input("Vaqtni kiriting:>>> "))
# summa = 0
# n = 1
# for i in range(vaqt):
#     n *= 2
#     summa += n
# print(summa)

# # 23 - misol
# n = int(input("Son kiritig:>>> "))
# for i in range(n):
#     count = 0
#     for j in range(n):
#         if i % j == 0:
#             count +=1
#     if count == 2:
#         print(i, end=", ")

# # 24 -misol
# N = int(input("N sonini kiriting: "))
# a, b = 1, 1  # Fibonachchi ketma-ketlikning boshlang'ich qiymatlari
# print("Fibonachchi sonlari:", a, end=" ")
# while b < N:
#     print(b, end=" ")
#     a, b = b, a + b

# # 25 - misol
# for i in range(1, 1000):
#     if i > 99:
#         oxirgi_xona = i % 10
#         orta_xona = (i // 10) % 10
#         if oxirgi_xona == orta_xona:
#             print(i, end=", ")

# # 26 - misol
# for i in range(1, 1000):
#     if i > 99:
#         oxirgi_xona = i % 10
#         orta_xona = (i // 10) % 10
#         biriinchi_xona = i // 100
#         if oxirgi_xona == orta_xona == biriinchi_xona:
#             print(i, end=", ") 

# # 27 - misol
# for i in range(1, 1000):
#     if i > 99 and i % 2 != 0:
#         oxirgi_xona = i % 10
#         orta_xona = (i // 10) % 10
#         biriinchi_xona = i // 100
#         if biriinchi_xona == orta_xona or orta_xona == oxirgi_xona or biriinchi_xona == oxirgi_xona:
#             print(i, end=", ") 

"""# # 28 - misol 
# i = 0
# while 1000 > i:
#     i += 1

# 29 - misol 
"""
# # 30 - misol
# m = int(input("Son kiriting(0, 99):>>> "))
# for i in range(0,100):
#     if i > m:
#         print("{} kotta birinchi son {} unig kvadrati {}".format(m, i, i ** 2))
#         break


""" Yuqori bosqich 
"""
"""# 1 - misol
n = int(input("Son kirting:>>> "))
"""
# # 4 - misol
# for i in range(10,100):
#     if i // 10 == i % 10:
#         print(i , end=", ")

# # 5 - misol
# for i in range(100):
#     i = i ** 2
#     if i // 10 == i % 10 and 100 > i >=10:
#         print(i , end=", ")
#     if 1000 > i > 99 and i // 100 == i % 10:
#         print(i, end=", ")
#     if 10_000 > i > 999 and i // 1000 == i % 10 and (i - (i // 1000) * 1000) // 100 == (i // 10) % 10:
#         print(i, end=", ") 

# # 6 - misol
# sonlar = []
# summa = []
# for i in range(10):
#     sonlar.append(int(input("Son kiriting:>>> ")))
# for j in sonlar:
#     if j == 0:
#         break
#     if j > 0:
#         summa.append(j)
# print(sum(summa))

# # 7 - misol
# sonlar = []
# summa = []
# for i in range(10):
#     sonlar.append(int(input("Son kiriting:>>> ")))
# for j in sonlar:
#     if j == 0:
#         break
#     if j < 0:
#         summa.append(j)
# print(sum(summa))

# # 8 - misol
# sonlar = []
# summa = 1
# for i in range(10):
#     sonlar.append(int(input("Son kiriting:>>> ")))
# for j in sonlar:
#     if j < 0:
#         break
#     summa *= j
# print(summa)

# # 9 - misol
# sonlar = []
# summa = 1
# for i in range(10):
#     sonlar.append(int(input("Son kiriting:>>> ")))
# for j in sonlar:
#     if j == 0:
#         break
#     summa *= j
# print(summa)

# # 10 - misol
# n = int(input("Natural son kiriting:>>> "))
# boluvchilar = 0
# print("{} = ".format(n), end="")
# for i in range(1, n):
#     if n % i == 0:
#         boluvchilar += i
#         print(i, end=" + ")
# print()
# if boluvchilar == n:
#     print("{} haqiqiy son".format(n))
# else:
#     print("{} haqiqiy son emas".format(n))

# 11 - misol
"""9 bilan bir xil"""

# # 12 - misol
# sonlar = []
# interval = []
# for i in range(10):
#     sonlar.append(int(input("Son kiriting:>>> ")))
# for j in sonlar:
#     if j == 0:
#         break
#     if -5 < j < 5:
#        interval.append(j) 
# print(interval)

# # 13 - misol
# sonlar = []
# interval = []
# for i in range(10):
#     sonlar.append(int(input("Son kiriting:>>> ")))
# for j in sonlar:
#     if j < 0:
#         break
#     if 3 < j < 13:
#        interval.append(j) 
# print(interval)

# # 14 - misol
# n = int(input("Son kiriting:>>> "))
# m = int(input("Son kiriting:>>> "))
# summa = 0
# for i in range(1, n):
#     for j in range(m):
#         i *= i
#     summa += i
# print(summa)

# # 15 - misol
# n = int(input("Son kiriting:>>> "))
# a, b = 1, 1
# print(a, end=", ")
# while b < n:
#     print(b, end=", ")
#     a, b = b, a+b

# # # 16 - misol
# a = int(input("Stipendiyangiz miqdorini kiriting:>>> "))
# b = int(input("Oylik xarajatlar:>>> "))
# for i in range(10):
#     delta += b - a 
#     b += b * 0.03
# delta += b-a
# print("Mablag' = ", delta)
# print("Stipendiya umumiy miqdori = ", a * 10)

# # 17 - misol
# s = int(input("Student jamg'armasi:>>> "))
# a = int(input("Har oylik stipendiya:>>> "))
# b = int(input("Oylik xarajatlar:>>> "))
# delta = b - a
# for i in range(1, 10):
#     b += b * 0.03
#     delta += b - a
#     s -= delta
#     if s <= 0:
#         print("Talaba {} oy yashay oladi".format(i))

# # 18 - misol
# depozit = int(input("Depozit summasini kiriting:>>> "))
# depozit_muddati = int(input("Depozit muddatini kiriting(yillarda):>>> "))
# summa = depozit
# for i in range(depozit_muddati - 1):
#     depozit += depozit * 0.06
#     summa = depozit
# print("{} muddatda depozit {} aylanadi".format(depozit_muddati, summa))

# # 19 - misol
# n = int(input("n sonini kiriting (n < 9999): "))
# m = int(input("m sonini kiriting: "))
# yigindi = 0
# soni = 0
# while n > 0 and soni < m:
#     raqam = n % 10
#     yigindi += raqam
#     n = n // 10
#     soni += 1
# print("Oxirgi", m, "ta raqam yig'indisi:", yigindi)

# # 20 - misol
# for i in range(1000,10000):
#   birinchi_xona = i // 1000
#   ikkinchi_xona = (i // 100) % 10
#   uchunchi_xona = (i // 10) % 10
#   tortinchi_xona = i % 10
#   if birinchi_xona == ikkinchi_xona or birinchi_xona == uchunchi_xona or birinchi_xona == tortinchi_xona or ikkinchi_xona == uchunchi_xona or ikkinchi_xona == tortinchi_xona or uchunchi_xona == tortinchi_xona:
#     print(end="")
#   else:
#     print(i, end=", ")

# # 21 - misol
# n = int(input("Son kiriting:>>> "))
# boluvchilar = 0
# print(f"{n} = ", end="")
# if 1000 > n > 99:
#   for j in range(2, int(n/2)):
#       if n % j == 0:
#         boluvchilar += j ** 3
#         print(f"{j} ^ 3" , end=" + ")
# elif 999 < n < 10_000:
#   for i in range(2, int(n/2)):
#     if n % i == 0:
#       boluvchilar += i ** 3
#       print(f"{i} ^ 3" , end=" + ")
# else:
#   print("Uchxonali yoki to'rtxonali son kiriting!")
# print()
# if boluvchilar == n:
#     print("{} soni Armstrong".format(n))
# else:
#     print("{} soni Armstrong soni emas".format(n))

# # 22 - misol
# ball = 0
# for i in range(10):
#   a = random.randrange(1,10)
#   b = random.randrange(1,10)
#   print(f"{a} * {b} = ", end="")
#   c = int(input())
#   if a * b == c:
#     ball += 1
# print()
# if ball == 10:
#   print("A'lo")
# elif ball == 9 or ball == 8:
#   print("Yaxshi")
# elif ball == 7 or ball == 6:
#   print("Qoniqarli")
# else:
#   print("Yomon")

# # 23 - misol
# count = 0
# for i in range(1, 1000):
#   for j in range(1, 501):
#     if i % j == 0:
#       count += 1
#   if count == 5:
#     print(i, end=", ")

# # 24 - misol
# for son in range(1, 10000):
#     if son % 7 == 0:  
#         yigindi = 0
#         n = son
#         while n > 0:
#             raqam = n % 10
#             yigindi += raqam
#             n = n // 10
#         if yigindi % 7 == 0:
#             print(son , end=", ")

# # 25 - misol 
# # Foydalanuvchidan natural sonni olish
# n = int(input("Natural son kiriting: "))
# # Har bir raqam (0 dan 9 gacha) necha marta uchraganini saqlash uchun ro'yxat
# sanoq = [0] * 10  # 10 ta raqam uchun boshlang‘ich qiymatlar: [0, 0, ..., 0]
# # Raqamlarni bitta-bitta ajratib chiqamiz
# while n > 0:
#     raqam = n % 10        # Oxirgi raqamni olish
#     sanoq[raqam] += 1      # Shu raqamni sanash
#     n = n // 10            # Oxirgi raqamni olib tashlash
# # Natijani chiqarish
# for i in range(10):
#     if sanoq[i] > 0:
#         print(f"{i} raqami {sanoq[i]} marta uchradi.")

