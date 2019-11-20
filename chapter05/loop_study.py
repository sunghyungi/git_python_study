
for i in [0, 1, 2, 3, 4, 5]:
    print(i, end=' ')

print()
for i in range(1, 10):
    print(i, end=" ")

print()
for i in range(0, 10, 2):
    print(i, end=' ')

print()
print("{} {}".format(range(0, 10), list(range(0, 10))))

x_list = ['x1', 'x2']
y_list = ['y1', 'y2']

print("x y")
for x in x_list:
    for y in y_list:
        print(x, y)


# gugudan
def gugu(num):
    for i in range(1, 10):
        print("{} * {} = {:2}".format(num, i, num * i))
    print()


def gugudan():
    for i in range(2, 10):
        print("======{}단======".format(i))
        for j in range(1, 10):
            print("{} * {} = {:2}".format(i, j, i * j))
        print()
    print()


def gugudan_land():
    for i in range(1, 10):
        for j in range(2, 10):
            print("{} * {} = {:2}".format(j, i, i * j), end='\t')
        print()


gugu(2)  # 2단

gugudan()  # 전체의 구구단

gugudan_land()  # 2단 3단

names = ['James', 'Robert', 'Lisa', 'Mary']
scores = [95, 96, 97, 94]

# zip
for name, score in zip(names, scores):
    print(name, score)
