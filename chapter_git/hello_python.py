def add(a, b):
    return a + b


def div(a, b):
    return a / b


def mul(a, b):
    return a * b


def dict_app():
    fruit_code = {'사과': 101, '배': 102, '딸기': 103, '포도': 104, '바나나': 105}
    print(fruit_code)
    print(fruit_code.keys())
    print(fruit_code.values())
    print(fruit_code.items())
    print(list(fruit_code.keys()))
    print(list(fruit_code.values()))
    print(list(fruit_code.items()))
    fruit_code2 = dict(오렌지=106, 수박=107)
    fruit_code.update(fruit_code2)
    print(fruit_code)
    fruit_code2.clear()
    print(fruit_code2)
    print(type(fruit_code2))


if __name__ == "__main__":
    print("{} {}".format('hello python', 'hi pycharm'))
    x = 10
    y = 5
    print("add({}, {}) = {}".format(x, y, add(x, y)))
    print("mul({}, {}) = {}".format(x, y, mul(x, y)))
    print("div({}, {}) = {}".format(x, y, div(x, y)))

    dict_app()
