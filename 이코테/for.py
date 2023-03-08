result = 0
array = (1,2,3,4,5)

for x in array:
    result += x
print(result)

### 연속적인 값을 차례대로 순회할 때는 range()

result = 0
# i 는 1부터 9까지의 모든 값을 순회
for i in range(1,10):
    result += i
print(result)


result = 0
for i in range(1,10):
    if i % 2 == 0:
        continue
    result += i
print(result)

### 1부터 5까지의 정수를 차레대로 출력
i = 1
while True:
    print("현재 i 의 값:", i)
    if i == 5:
        break
    i += 1

scores = [90,85,77,65,44]
for i in range(5):
    if scores[i] >= 80:
        print(i+ 1,'번 학생은 합격')
        
scores = [90,85,77,65,44]
cheat = {2,4}

for i in range(5):
    if i + 1 in cheat:
        continue
    if scores[i] >= 80:
        print(i+1, "번 학생은 합격")
        
for i in range(2,10):
    for j in range(1,10):
        print(i,"x",j, "=", i*j)
    print()
        
        
