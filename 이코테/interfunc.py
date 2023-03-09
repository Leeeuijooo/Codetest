#sum
result = sum([1,2,3,4,5])
print(result)

# mix max
min_result = min(1,2,3,4)
max_result = max(1,2,3,4)
print(min_result,max_result)

# eval()
result = eval("(3+5)*7")
print(result)

# sorted()
result = sorted([2,5,3,6,7])
reverse_result  = sorted([2,5,3,6,7], reverse=True)
print(result)
print(reverse_result)

# sorted with key
array = [('lee', 11),('eui', 2),('joo', 35)]
print(sorted(array, key = lambda x : x[1], reverse=True))
