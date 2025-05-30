"""List mashqlar"""
# # 1 - Listdan eng katta elementni o‘chiring.
# my_list = [1,2,3,4,5,5,6,7,7,8]
# print(my_list)
# my_list.remove(max(my_list))
# print(my_list)

# # 2 - Ikki listni birlashtirib yangi list hosil qiling (extend() ishlatmasdan).
# my_list_1 = [i for i in range(10)]
# my_list_2 = [i for i in range(10)]
# my_list_3 = my_list_1 + my_list_2
# print(my_list_3)

# # 3 - List ichidagi barcha elementlarni ketma-ket ikki marta chiqaruvchi kod yozing.
# my_list = [str(i) for i in range(16)]
# my_list_1 = [i * 2 for i  in my_list]
# print(my_list_1)

# # 4 - Faqat toq indeksdagi elementlarni ekranga chiqaring.
# my_list = [i for i in range(100)]
# my_list_1 = [my_list[i] for i in range(len(my_list)) if i % 2 == 0] # bu yerdagi shart bajariladi
# print(my_list_1)

# # 5 - List ichidan barcha manfiy sonlarni o‘chiring.
# my_list = [i for i in range(-19, 12, 1)]
# print(my_list)
# my_list_1 = [i for i in my_list if i > 0]
# print(my_list_1)

# # 6 - Elementlari bir xil bo‘lmagan ikkita listni qo‘shing va ularni tartiblang.
# my_list = [i for i in range(10)]
# my_list_1 = [i for i in range(10)]
# my_list.extend(my_list_1)
# my_list.sort()
# print(my_list)

# # 7 - List elementlarini alfavit tartibida saralang.
# my_list = ["abs", "asd", "ade", "adas", "aserv"]
# my_list.sort()
# print(my_list)

# # 8 - List ichidagi barcha satrlarni katta harflarga o‘tkazing.
# my_fruits = ["banana", "cherry", "apple","strawberry", "watermelon","melon"]
# my_fruits = [i.upper() for i in my_fruits]
# print(my_fruits)

# # 9 - Listdagi eng uzun so‘z uzunligini toping.
# my_fruits = ["banana", "cherry", "apple","strawberry", "watermelon1","melon"]
# max_item = len(my_fruits[0])
# for i in my_fruits:
#     if max_item < len(i):
#         max_item = len(i)
#         word = i
# print(f"Eng uzun so'z {word}, uzunligi {max_item}")

# # 10 - Berilgan listni indekslari bilan ekranga chiqaring.
# my_list = [i for i in range(10)]
# for index, value in enumerate(my_list):
#     print(f"index({index}): {value}")

# # 11 - Har bir element oldiga uning indeksini qo‘shib yangi list yarating.
# my_list = [i for i in range(10)]
# new_list = []
# for index, value in enumerate(my_list):
#     new_list.append(f"{index},{value}")
# print(new_list)

# # 12 - List ichidagi barcha elementlarni string sifatida chiqaruvchi kod yozing.
# my_list = [i for i in range(10)]
# for i in my_list:
#     print(str(i), end=", ")

# # 13 - List ichidagi string turidagi elementlarni alohida listga o‘tkazing.
# my_list = [i for i in range(10)]
# my_list_1 = ["asdassdd", "asear","AEWQR","WQRWQ"]
# my_list.extend(my_list_1)
# for i in my_list_1:
    