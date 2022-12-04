# 중복 x
# 삽입 / 삭제 : 0(1)

s= set()
s.add(10)
s.add(10)
s.add(50)
s.add(10)
s.add(70)
print(s)
# s.pop()     # 뺄 수 있음 pop 함수 / 어떤 값이 빠질지는 모름
#print(s)
s.remove(50)  # 어떤 값을 빼려면 remove 함수
print(s)