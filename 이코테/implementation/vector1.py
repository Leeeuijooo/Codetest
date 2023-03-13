# # 동 북 서 남
# dx = [0,-1,0,1]
# dy = [1,0,-1,0]

# x, y = 2, 2
# for i in range (4):
#     #다음 위치
#     nx = x + dx[i]
#     ny = y + dy[i]
    
#     print(nx, ny)
    
n = int(input())
x, y = 1, 1
plans = input().split()

## L R U D 분류
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move = ['L','R','U','D']

# 이동 계획 확인
for plan in plans:
    # 이동 후 좌표 계산
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
        # 공간 벗어 날때?
    if nx < 1 or ny <1 or ny > n or nx > n :
        continue
    x, y = nx, ny
print(x, y)