
n = 1260
count = 0
# 큰 단위의 화폐부터 차례로 확인
array = [500, 100, 50, 10]

for coin in array:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin
    
print(count)

n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k ## 10 , 3이었을때 target은  9가됨   ## 스킬 : 나누어 떨어지는 수가 n 과 가까운 값을 찾고자 할때
    result += (n-target)   ## result 는 1이됨
    n = target ## n = 9
    # N 이 K보다 작을 때 (더 이상 나눌 수 없을때 반복문 탈출)
    if n < k: ## 아니라면
        break
    result += 1 ## result는 2
    n //= k ## n = 3

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1) ## result  = 2
print(result)

    