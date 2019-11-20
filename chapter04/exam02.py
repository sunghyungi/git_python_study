import random as rnd


def bubble_sort(random_list):
    for i in range(0, len(random_list)-1):
        for t in range(0, len(random_list)-1-i):
            if random_list[t]> random_list[t+1]:
                random_list[t], random_list[t+1] = random_list[t+1], random_list[t]
                # swap = random_list[t]
                # random_list[t] = random_list[t+1]
                # random_list[t+1] = swap

    return random_list
# todo


if __name__ == "__main__":
    random_list = []
    rnd.seed(1)
    for num in range(0, 10):
        random_list.append(rnd.randint(1, 46))

    print(random_list)

    sortedList = bubble_sort(random_list)
    print("정렬된 결과 {}".format(sortedList))


