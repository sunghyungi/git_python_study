import random as rnd
from chapter04.exam02 import bubble_sort


def binary_list():
    rnd.seed(1)
    num = []
    while len(num) < 20:
        num.append(rnd.randint(1, 100))
    return num


def binary_search(binary_num, search_num):
    left = 0
    right = len(binary_num)-1

    while True:
        mid = (left + right) // 2

        if binary_num[mid] == search_num:
            print("{}를 찾았습니다.".format(search_num))
            break;
        elif binary_num[mid] > search_num:
            right = mid -1
        elif binary_num[mid] < search_num:
            left = mid + 1

        if (right < left):
            print("{}가 존재하지 않습니다.".format(search_num))
            break


if __name__ == "__main__":
    binary_num = bubble_sort(binary_list())
    print(binary_num)

    binary_search(binary_num, 4)