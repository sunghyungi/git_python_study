def string_split():
    coffee_menu = "에스프레소 아메리카노 카페라떼 카푸치노"
    print(type(coffee_menu.split()))
    coffee_list = coffee_menu.split()
    [print(coffee) for coffee in coffee_list]
    print()

    coffee_menu2 = "에스프레소,아메리카노,카페라떼,카푸치노"
    coffee_list2 = coffee_menu2.split(',')
    [print(coffee) for coffee in coffee_list2]
    print()
    [print(coffee) for coffee in coffee_menu2.split(',', 2)]
    print()

    coffee_menu3 = "에스프레소 \n 아메리카노 \n 카페라떼 \n 카푸치노"
    coffee_list3 = coffee_menu3.split()
    [print(coffee) for coffee in coffee_list3]
    print()

    for t in coffee_list:
        if t == "카페라떼":
            print("라떼존재")
    print()


def string_strip():
    python_str01 = "    Python             "
    python_str02 = "aaaaPythonaaaaaaaaaa"
    python_str03 = "aabbPythonbbaaaaaa"
    python_str04 = "aaaBallaaa"
    python_str05 = "\n This is very \n fast. \n \n"
    print(python_str01.strip())
    print(python_str02.strip('a'))
    print(python_str03.strip('ab'))
    print(python_str04.strip('a'))
    print("중간에 공백은 제거 불가능", python_str05.strip(), sep='\n')


if __name__ == "__main__":
    string_split()
    string_strip()
    print('\n')

    address_list = ["서울시", "서초구", "반포대로", "201(반포동)"]
    print(address_list)
    a = " "
    print(a.join(address_list))
    print(" ".join(address_list))
    print("*^^*".join(address_list))
    print()

    str_f = "Python code"
    print("찾는 문자열 위치:", str_f.find("Python"))
    print("찾는 문자열 위치:", str_f.find("code"))
    print("찾는 문자열 위치:", str_f.find("n"))
    print("찾는 문자열 위치:", str_f.find("easy"))

    str_f2 = "Python study code"
    print(str_f2.find("study", 6, 12))
    print(str_f2.find("code", 6, 12))

    print(str_f2.count('o'))
    print(str_f2.count('Python'))
    print(str_f2.count("code", 0, 10))

    print("Python으로 시작?", str_f2.startswith("Python"))
    print(".로 끝?", str_f2.endswith("."))
    print("end로 끝?", str_f2.endswith("code"))
    print("study로 시작?", str_f2.startswith("study", 7, 15))
    print()

    str_f3 = "[Python] [Python] code Python"
    print(str_f3.replace('Python', 'QT'))
    print(str_f3.replace('Python', 'QT', 2))
    print(str_f3)
    print(str_f3.replace('[', '').replace(']', ''))
    print()

    print('Python'.isalpha())
    print('Ver. 3.x'.isalpha())
    print()
    print('12345'.isdigit())
    print('12345abc'.isdigit())
    print()
    print('   '.isspace())
    print('  1  '.isspace())
    print()
    print('PYTHON'.isupper())
    print('Python'.isupper())
    print('python'.islower())
    print('Python'.islower())
    print()
    print('PYTHON'.lower())
    print('Python'.upper())
    print('Python' == 'python')
    print('Python'.lower() == 'python')