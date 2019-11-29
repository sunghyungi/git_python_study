import numpy as np

file_name = "Gettysburg_Address.txt"


def f1(x):
    return x[0]


with open(file_name, "r") as f:
    header = f.readline()
    list_s = []
    list_c = []
    for i in f.readlines():
        list_s.extend(i.split())
    for j in range(0, len(list_s)):
        if list_c.count([list_s.count(list_s[j]), list_s[j].strip(',.')]) == 0 and list_s.count(list_s[j]) > 2:
            if list_s[j] != '-' and list_s[j] != ',' and list_s[j] != '.':
                list_c.append([list_s.count(list_s[j]), list_s[j].strip(',.')])

    list_c.sort(key=f1, reverse=True)
    [print(i) for i in list_c]


def operation(x, y, o):
    mul = lambda x, y: x * y
    sum = lambda x, y: x + y
    div = lambda x, y: x / y
    min = lambda x, y: x - y


    x = int(x)
    y = int(y)

    if o == "1":
        print("{} + {} ={}".format(x, y, sum(x, y)))
    elif o == "2":
        print("{} - {} ={}".format(x, y, min(x, y)))
    elif o == "3":
        print("{} * {} ={}".format(x, y, mul(x, y)))
    elif o == "4":
        print("{} / {} ={}".format(x, y, round(div(x, y), 5)))
    else:
        print("잘못 입력하셨습니다.")


def solution(array, commands):
    answer = []
    for i in range(0, len(commands)):
        array2 = list(array[commands[i][0] - 1:commands[i][1]])
        array2.sort()
        answer.append(array2[commands[i][2]-1])
    return answer


if __name__ == "__main__":

    x = input("x를 입력하세요")
    y = input("y를 입력하세요")
    o = input("연산을 선택하세요 (1)+ (2)- (3)* (4)/")

    operation(x, y, o)

    array1 = np.array([1, 5, 2, 6, 3, 7, 4])
    commands1 = np.array([[2, 5, 3], [4, 4, 1], [1, 7, 3]])

    count = 0
    while True:
        count = count+1
        print("나무꾼이 나무를 {}번 찍습니다".format(count))

        if count == 10:
            print("나무가 넘어갑니다.")
            break

    answer1 = solution(array1, commands1)
    print("answer = {}".format(answer1))