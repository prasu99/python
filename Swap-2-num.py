
With temp variable

a = input("a = ")
b = input("b = ")
x = a
a = b
b = x
print("a = " + str(a) + " ,b = " + str(b))

without temp variable

a = input("a = ")
b = input("b = ")
a, b = b, a
print("a = " + str(a) + " ,b = " + str(b))



