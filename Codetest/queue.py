from collections import deque
from this import d #안전성은 보장 못하지만 속도는 빠름
# from queue import Queue 멀티 쓰래드 환경 / 
dq = deque()
dq.append(123)
dq.appendleft(456)
dq.appendleft(789)
print(dq)

print(dq.pop())
print(dq.popleft())

