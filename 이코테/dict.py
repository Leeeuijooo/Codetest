data = dict()
data['a'] = 'apple'
data['b'] = 'banana'
data['c'] = 'cola'

print(data)

if 'a' in data:
    print('존재')
    
# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
value_list = data.values()
print(key_list)
print(value_list)
# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])

print(data['a'])    
    
# for value in value_list:
#     print(data[value])

a = dict()
a['이의'] = 97
a['이주'] = 98
print(a)

b = {
    '이의' : 97,
    '이주' : 98
}

b_list = b.keys()
print(b_list)

b_list = list(b.keys())
print(b_list)