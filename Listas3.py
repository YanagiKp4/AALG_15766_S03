a=[2*x for x in range(1,10+1)]
print(a)

b = [(2*x)+1 for x in range(1,10+1)]
print(b)

c = [2*n +1 for n in range(0,5)]
print(c)

print([n for n in range(1,10,2)])

print([0 if x % 3 == 0 else x for x in range(1, 10, 2)])

print([x if i != 1 and i != 4 else 0 for i, x in enumerate([1, 2, 5, 7, 9])])
