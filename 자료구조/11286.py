# 11286 절댓값 힙

# 절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

# 테스트 케이스

#배열에 정수 x (x ≠ 0)를 넣는다.
#배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
#프로그램은 처음에 비어있는 배열에서 시작하게 된다.

# 입력

# 첫째 줄에 연산의 개수 N(1≤N≤100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다.
# 만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다.
# 입력되는 정수는 -2^31보다 크고, 2^31보다 작다.

# 우선순위 큐를 이용해야 함

# arr = [ 1,2,6,4,13]
# arr.sort()
# print(arr)
# arr1 = [(3,4),(3,1),(8,50),(8,7)]
# arr1.sort()
# print(arr1)

# <우선순위큐에 튜플을 넣는 풀이>
import heapq as hq
import sys 
input = sys.stdin.readline # 빠른 입출력을 위해 선언 
pq = []
N = int(input())
for _ in range(N):
    x  = int(input())
    if x:
        hq.heappush(pq,(abs(x),x))
    else:
        print(hq.heappop(pq)[1] if pq else 0) # 삼항 연산



# import heapq as hq
# import sys 
# input = sys.stdin.readline # 빠른 입출력을 위해 선언 
# min_heap = [] # 1, 2, 3, 8 ,13 ,99, 242 / 양수를 보관
# max_heap = [] # -1, -4, -10, -1042  절댓값이 작을 수록 큼 / 양수와는 다르게 / 음수를 보관
# N = int(input())
# for _ in range(N):
#     x  = int(input())
    
#     if x:
#         if x>0:
#             hq.heappush(min_heap,x)
#         else:
#             hq.heappush(max_heap,x)
#     else:
#         min_heap[0] abs(max_heap[0])