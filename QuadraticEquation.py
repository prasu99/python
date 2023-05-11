
import cmath
a = input("a = ")
b = input("b = ")
c = input("c = ")

d = (int(b)*int(b)) - (4*int(a)*int(c))

sol1 = (-int(b)-cmath.sqrt(d))/(2*int(a))
sol2 = (-int(b)+cmath.sqrt(d))/(2*int(a))

print('The solution are {1} and {0}'.format(sol1,sol2))

