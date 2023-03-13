n = int(input())
data  = list(map(int, input().split()))

data.sort()

result = 0 ## 그룹 수
count = 0 ## 현재 그룹에 속한 모험가 수

for i in data:
    count += 1
    if count >= i: # 그룹 결성
        result += 1 # 그룹 수 하나 추가
        count = 0 # 현재 그룹에 포함된 모험가 수 초기화
print(result)
