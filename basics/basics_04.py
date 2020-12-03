a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print("ID - a:", id(a))
print("ID - b:", id(b))
b = a
print("ID - a:", id(a))
print("ID - b:", id(b))
b.append(10)
print(a)
print(b)