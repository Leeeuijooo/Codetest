from collections import Counter

counter = Counter(['A','A','B','C','C','C'])

print(counter['A'])
print(counter['B'])
print(counter['C'])
print(dict(counter))
