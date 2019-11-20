# 로또번호생성기를 작성하고 당첨번호에 따라 순위를 구하는 프로그램 작성

import random as rnd
from chapter04.exam02 import bubble_sort


def lotto_generator():
    # rnd.seed(1)
    lotto_num = set()
    while len(lotto_num) < 6:
        lotto_num.add(rnd.randint(1, 46))

    return lotto_num


if __name__ == "__main__":

    set_lotto = bubble_sort(list(lotto_generator()))
    print("로또 번호 : {}".format(set_lotto))