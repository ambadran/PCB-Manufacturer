
a = [2, 4, 6, 8]

one = 3
two = 7

a.insert(1, two)
a.insert(3, one)

if a.index(one) < a.index(two):
    b = a[a.index(one)+1:a.index(two)]
    c = a[a.index(two)+1:]
    c.extend(a[:a.index(one)])

else:
    b = a[a.index(two)+1:a.index(one)]
    c = a[a.index(one)+1:]
    c.extend(a[:a.index(two)])


print(a)
print(b)
print(c)
