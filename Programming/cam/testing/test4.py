
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

one = sum(len(i) for i in lista)
two = sum(map(len, lista)) 

print(one)
print(two)


dicta = {2: 4, 7: 3}

print(7 in dicta)


a = 3

b = a

print(a, b)

a = 1

print(a, b)
