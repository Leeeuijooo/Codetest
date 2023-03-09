from re import A


def add (a,b):
    return a + b
result  = add(1,2)
print(result)

def add(a,b):
    	print("결과 : ", a+b)
add(b=2, a=1)

a = 0
def func():
    global a
    a += i
    
for i in range(10):
    func()
    
print(a)

array = [1,2,3,4]

def func():
    array = [5,6,7]
    array.append(8)
    print(array)
    
func()

array = [1,2,3,4]

def func():
    global array
    array.append(5)
    print(array)
    
func()

def oper(a, b):
    add_var = a + b
    sub_var = a - b
    return add_var,sub_var
a,b = oper(3,7)
print(a,b)