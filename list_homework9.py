"""List vazifalar"""
# # 1 - mashq
# my_list = [i for i in range(10)]
# for i in my_list:




# # 2 - mashq
# my_list = [i for i in range(100)]
# summa = max(my_list) + min(my_list)
# print(summa)

# # 3 - mashq
# my_list = [i for i in range(100)]
# my_list_1 = [i for i in my_list if i // 10 != 0] 
# summa = sum(my_list_1)
# print(summa)

# # 4 - mashq
# my_list = [i for i in range(100)]
# my_list_1 = [i for i in my_list if i % 2 != 0]
# my_list_2 = [i for i in my_list if i % 2 == 0]
# orta_arifmetik_1 = sum(my_list_1) / len(my_list_1) 
# orta_arifmetik_2 = sum(my_list_2) / len(my_list_2)
# print(f"toq >>> {orta_arifmetik_1} ")
# print(f"juft >>> {orta_arifmetik_2} ")
# if orta_arifmetik_1 > orta_arifmetik_2:
#     print(f"{orta_arifmetik_1} > {orta_arifmetik_2}") 
# elif orta_arifmetik_2 > orta_arifmetik_1:
#     print(f"{orta_arifmetik_1} < {orta_arifmetik_2}") 
# else:
#     print(f"{orta_arifmetik_1} = {orta_arifmetik_2}") 

# # 5 - mashq
# my_list  = [i for i in range(100)]
# for i in my_list:
#     count = 0
#     if i % 2 != 0:
#         count += 1
#     if count == len(my_list) + 1:
#         print(True)
#     else:
#         print(False)

# # 6 - mashq
# my_list = [i for i in range(100)]
# my_list_1 = [i for i in my_list if 9 < i < 100 and i %  3 == 0]    
# print(my_list_1)

# # 7 - mashq
# my_list = [i for i in range(-100, 123,1)]
# my_list_1 = [i for i in my_list if i < 0]
# my_list_2 = []
# for i in my_list:
#     for j in my_list_1:
#         if i == -j:
#             my_list_2.append(i)
#             my_list_2.append(j)
# print(my_list_2)

# # 8 - mashq
# my_list = [i for i in range(100)]
# my_list.append(range(10))
# for i in my_list: 
#     for j in my_list:
#         if i == j:
#             print("Sonlar orasida takrorlanish mavjud")

# # 9 - mashq
# my_list = [i for i in range(10)]+*+
# my_list.append(range(-10,0,1))
# summa = 0
# for i in my_list: 
#     if i < 0:
#         break   
#     summa += i 
# print(summa)

# # 10 - mashq
# s_n = [i for i in range(100)]
# a = int(input("son kiriting:>>> "))
# b = int(input("son kiriting:>>> ")) 
# a_b = []
# for i in s_n:
#     if a < i < b:
#         a_b.append(i)
# else:
#     print("BU ORALIQQA TEGISHLI ELEMENT MAVJUD EMAS")
# print(a_b)

# # 11 - mashq
# my_list =[i for i in range(-100, 100, 1)]
# my_list_1 = [i for i in my_list if i < 0]
# my_list_2 = [i for i in my_list if i > 0]
# print(max(my_list_1))
# print(min(my_list_2))

# # 12 - mashq
# my_list = [range(10), 0, range(10,16), 0, range(18,23)]
# my_list_1 = []
# for i in len(my_list):
#     if my_list[i] == 0:
#         my_list_1.append(my_list[i])




# # 13 - mashq
# my_list = [i for i in range(100)]
# my_list_1 = [i for i in  len(my_list) if i % 2 != 0]
# print(sum(my_list_1))

# 14 - mashq
# my_list = [i for i in range(100)]
# my_list_1 = [i for i in  len(my_list) if i % 2 == 0]
# print(sum(my_list_1))

# # 15 - mashq
# my_list = [i for i in range(100)]
# my_list_1 = [i for i in my_list if i % 10 == 0]
# print(my_list_1)

# # 16 - mashq
# my_list = list(range(100), range(-100, 10,1))
# my_list_1 = [i for i in my_list if i < 0]
# print(my_list_1)

# # 17 - mashq
# my_list = list(range(10, 1, -1), range(23, 34))
# my_list_1 = []
# min_item = my_list[0]
# for i in my_list:
#     for j in my_list:
#         if i < j:
#             min_item = i

# # 18 - mashq
# my_list = [i for i in range(100)]
# my_list_1 = [i for i in my_list if i == 7]
# print(my_list_1)

# # 19 - mashq
# Z = list(range(100), range(-100,19,1))
# R_0 = [i for i in Z if i > 0]
# R = [i for i in Z if i < 0]
# R.extend(R_0)
# print(R)

# # 20 - mashq
# C = list(range(-100,10,1))
# min_item = min(C)
# index = C.index(min_item)
# print(f"index = {index}, min value = {min_item}")

# # 21 - mashq
# C = list(range(-100,10,1))
# max_item = max(C)
# index = C.index(max_item)
# print(f"index = {index}, min value = {max_item}")

# # 22 - mashq
# x_vektor = list(range(4), -1, range(6,9), -4, range(12,24), -2, range(10))
# for i in x_vektor:
#     count = 0
#     if i < 0:
#         count += 1
#         print(f"index = {x_vektor.index(i)}, value = {i}")
#         if count == 3:
#             break

# # 23 - mashq
# my_list = [i for i in range(10)]
# min_item = min(my_list)
# max_item = max(my_list)
# index_max = my_list.index(max_item)
# index_min = my_list.index(min_item)
# my_list.remove(index_min)
# my_list.insert(index_min, max_item)
# my_list.remove(index_max)
# my_list.insert(index_max, min_item)
# print(my_list)

# # 24 - mashq
# x_vektor = list(range(4), -1, range(6,9), -4, range(12,24), -2, range(10))
# min_item = 
# for i in x_vektor:

#     count = 0
#     count += 1
#     print(f"index = {x_vektor.index(i)}, value = {i}")
#     if count == 3:
#         break




# 25 - mashq
my_list = [i for i in range(100)]
v = int(input("Son kiriting:>>> "))
my_list.sort()
