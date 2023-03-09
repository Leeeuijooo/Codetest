import math

def lcm(a,b):
    return a * b // math.gcd(a,b)


a = 10
b = 40

print(math.gcd(10,40))
print(lcm(10, 40))

