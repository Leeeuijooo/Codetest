# from queue import PriorityQueue
# Thread safe 

import heapq
# 빈 배열을 만든다
pq=[]
heapq.heappush(pq,6)
heapq.heappush(pq,12)
heapq.heappush(pq,0)
heapq.heappush(pq,-5)
heapq.heappush(pq,8)
print(pq)
while pq:
    print(pq[0]) #최상단에 있는 루트 노드의 값을 출력하려면 0번째 인덱스를 출력하면 됨
    heapq.heappop(pq) # 그냥 출력하는 것
    




