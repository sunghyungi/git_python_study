def func1():
    print("func1 in my_module1 ")


def func2():
    print("func2 in my_module1 ")


# main 을 지정 안할 경우 import 한 모듈 안에서도 자동 출력
if __name__ == "__main__":
    print("=== my_module1 ===")
    func1()
    func2()
else:
    print("임포트")


