# 리스트 컴프리헨션, if 추가
numbers = [1, 2, 3, 4, 5]
square = [i ** 2 for i in numbers]
print(square)

square2 = [i ** 2 for i in numbers if i >= 3]
print(square2)

print([i ** 2 for i in range(1, 6) if i >= 3])


