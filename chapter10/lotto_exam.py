import random


def checkNum(num):
    count = 0
    for i in num[0]:
        for j in lottoNum[0]:
            if i == j:
                count += 2
    if num[1] == lottoNum[1]:
        count += 1

    if count >= 12:
        rank = "1등"
    elif count == 11:
        rank = "2등"
    elif count == 10:
        rank = "3등"
    elif count >= 8:
        rank = "4등"
    elif count >= 6:
        rank = "5등"
    else:
        rank = "꽝"

    return rank


def randomNum():
    number = set()
    while len(number) < 7:
        number.add(random.randint(1, 45))

    lotto_num = [[list(number)[i] for i in range(0, 6)], list(number)[6]]
    return lotto_num


def countNum(num):
    count = 0
    bonus = 0
    for i in num[0]:
        for j in lottoNum[0]:
            if i == j:
                count += 1
    if num[1] == lottoNum[1]:
        bonus += 1

    print("일반 번호 {}개 보너스 번호 {}개 맞추셨습니다.".format(count, bonus))


if __name__ == "__main__":
    random.randint(1, 45)
    lottoNum = [[19, 23, 28, 37, 42, 45], 2]

    a = randomNum()
    print(a)
    countNum(a)
    a_rank = checkNum(a)
    print("이번주 당신의 로또는 {}입니다.".format(a_rank))

    b = randomNum()
    print(b)
    countNum(b)
    b_rank = checkNum(b)
    print("이번주 당신의 로또는 {}입니다.".format(b_rank))


