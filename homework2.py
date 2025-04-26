import math
# 2 - darajali misollar 
# 1 - misol 
y =  int(input("y = "))
f =  int(input("f = "))
g =  (math.exp(2 * y) + math.sin(f)) / math.log(3.8 * y + f)
print(f"g =  (math.exp(2 * y) + math.sin(f))/math.log(3.8 * y + f) = {g}")

# 2 - misol 
y =  int(input("y = "))
d =  int(input("d = "))
f =  math.log(d) + (3.5 * (d ** 2) + 1) / math.cos(2 * y)
print(f"f =  math.log(d) + (3.5 * (d ** 2) + 1)/math.cos(2 * y) = {f}")

# 3 - misol
y =  int(input("y = "))
k =  int(input("k = "))
u = (math.log(k - y) + y ** 4) / (math.exp(y) + 2.355 * k ** 2)
print(f"u = (math.log(k - y) + y ** 4) / (math.exp(y) + 2.355 * k ** 2) = {u}")

# 4 - misol 
y =  int(input("y = "))
w =  int(input("w = "))
g = (9.33 * w ** 3 + math.sqrt(w)) / (math.log(y + 3.5) + math.sqrt(y))
print("Natija: " , g)

# 5 - misol
y = int(input("Son kiriting:>>> "))
t = int(input("Son kiriting:>>> "))
a = int(input("Son kiriting:>>> "))
d = (7.8 * a ** 2 + 3.52 * t) / (math.log(a + 2 * y) + math.exp(y))
print("Natija:>>> " , d)

# 6 - misol 
y = int(input("Son kiriting:>>> "))
r = int(input("Son kiriting:>>> "))
t = int(input("Son kiriting:>>> "))
w = (4 * t ** 3 + math.log(r)) / (math.exp(y + r) + 7.2 * math.sin(r))
print("Natija:>>> " , w)

# 7 - misol 
y = int(input("Son kiriting:>>> "))
n = int(input("Son kiriting:>>> "))
h = (y ** 2 - 0.8 * y + math.sqrt(y)) / (23.1 * n ** 2 + math.cos(n))
print("Natija:>>> " , h)

# 8 - misol
y = int(input("Son kiriting:>>> "))
k = int(input("Son kiriting:>>> "))
r = (math.sqrt(math.sin(y) ** 2 + 6.835)) / (math.log(y + k) + 3 * y ** 2)

print("Natija:>>> " , r)
#  9- misol 
y =  int(input("y = "))
q =  int(input("q = "))
e = (math.log(0.7 * y + 2 * q)) / math.sqrt(3 * y ** 2 + 0.5 * y + 4)
print("Natija: " ,e)

# 10 - misol 
t = int(input("Son kiriting:>>> "))
y = int(input("Son kiriting:>>> "))
l = int(input("Son kiriting:>>> "))
k = (2 * math.pow(t , 2) + 3 * l + 7.2) / (math.log(y) + math.exp(2 * l))
print("Natija:>>> " , k)

# 3 - darajali misollar 

# 1 - misol 
x = int(input("Son kiriting:>>> "))
a = int(input("Son kiriting:>>> "))
c = int(input("Son kiriting:>>> "))
l = (math.sqrt(math.exp(x) - math.cos(pow(x , 2) * pow(a , 5)) ** 4) + math.atan(a - x ** 5) ** 4) / math.e * math.sqrt(abs(a + x * c ** 4))
print("Natija:>>> " , l)

# 2 - misol
x = int(input("Son kiriting:>>> "))
t = int(input("Son kiriting:>>> "))
c = int(input("Son kiriting:>>> "))
l = math.ctan(c) ** 2 + (2 * x ** 2 + 5) / (math.sqrt(c + t))
print("Natija:>>> " , l)

# 3 - misol 
y = int(input("Son kiriting:>>> "))
h = int(input("Son kiriting:>>> "))
a = (math.tan(y ** 3 - h ** 4) + h ** 2) / (math.sin(h) ** 3 + y)
print("Natija:>>> ", a)

# 4 - misol 
x = int(input("Son kiriting:>>> "))
y = int(input("Son kiriting:>>> "))
f = (math.sqrt((2 + y) ** 2 + math.pow(math.sin(y + 5) , 1/7))) / (math.log(x + 1) - y ** 3)
print("Natija:>>> ", f)

# 5 - misol 
x = int(input("Son kiriting:>>> "))
y = int(input("Son kiriting:>>> "))
z = int(input("Son kiriting:>>> "))
c = int(input("Son kiriting:>>> "))
g = (math.tan(x ** 4 - 6) + math.cos(z + x * y ) ** 3) / (math.cos(pow(x,3) * pow(c,2)) ** 4)
print("Natija:>>> ", g)

# 6 - misol 
x = int(input("Son kiriting:>>> "))
y = int(input("Son kiriting:>>> "))
t = int(input("Son kiriting:>>> "))
p = (math.sin(x) ** 3 + math.log(2 * y + 3 * x)) / (math.pow(t, math.e) + math.sqrt(x))
print("Natija:>>> ", p)

# 7 - misol 
x = int(input("Son kiriting:>>> "))
y = int(input("Son kiriting:>>> "))
a = int(input("Son kiriting:>>> "))
b = int(input("Son kiriting:>>> "))
t = (math.sqrt(x + b - a) + math.log(y)) / (math.atan(b + a))
print("Natija:>>> ", t)

# 8 -misol
t = int(input("Son kiriting:>>> "))
y = int(input("Son kiriting:>>> "))
s = (4.351 * y ** 3 + 2 * t * math.log(t)) / (math.sqrt(math.cos(2 * y) + 4.351))
print("Natija:>>> ", s)

# 9 - misol 
x = int(input("Son kiriting:>>> "))
y = int(input("Son kiriting:>>> "))
r = int(input("Son kiriting:>>> "))
a = int(input("Son kiriting:>>> "))
b = int(input("Son kiriting:>>> "))
k = int(input("Son kiriting:>>> "))
d = (math.pow(k , a * r * x) + a * math.sqrt(6) - math.cos(3 * a * b)) / (math.sin(a * math.asin(x) + math. log(y)) ** 2)
print("Natija:>>> ", d)

# 10 - misol
x = int(input("Son kiriting:>>> "))
y = int(input("Son kiriting:>>> "))
a = int(input("Son kiriting:>>> "))
b = int(input("Son kiriting:>>> "))
c = int(input("Son kiriting:>>> "))
u = (math.tan(y) ** 3 + math.sin(x * math.sqrt(b - c)) ** 5) / math.sqrt(a - b + c)
print("Natija:>>> " , u)