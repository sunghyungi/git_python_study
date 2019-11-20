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
    country_capital = {"영국": "런던", "프랑스": "파리", "스위스": "베른", "호주": "캔버라", "덴마크": "코펜하겐"}

    print(country_capital)

    print(type(country_capital))

    print(country_capital["프랑스"])

    list1 = ['a', 'b', 'c']

    tuple1 = (1, 2, 3, 4)

    set1 = {'가', '나'}
    data_dict = {"lst": list1, "tpl": tuple1, "set": set1}

    for key, value in data_dict.items():
        print("{} -> {}".format(key, value))

    for key in data_dict.keys():
        print("key {} -> {}".format(key, data_dict[key]))

    country_capital["독일"] = "베를린"
    print(country_capital)
    country_capital["호주"] = "멜버른"
    print(country_capital)
    del country_capital["호주"]
    print(country_capital)

    dict_app()