from unittest import result


def add (a,b):
    return a + b

## 일반적인 add() 메서드 사용
print(add(1,2))

## 람다 표현식으로 구현
print((lambda a,b : a +b )(1,2))

array = [('lee', 11),('eui', 2),('joo', 35)]

def kkey(x):
    return x[1]

print(sorted(array, key = kkey))

## 람다함수로 구현했을 때
print(sorted(array, key = lambda x: x[1]))

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a,b : a+b ,list1, list2)

print(list(result))