#입력데이터
data = input()
#첫번쨰 문자부터 시작
result = int(data[0])

for i in range(1, len(data)):
    a = int(data[i])
    if a <= 1 or result <= 1:
        result += a
    else:
        result *= a
print(result)
