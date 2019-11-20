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