from chapter10.my_module2 import *
from chapter10.my_module1 import *

func1()
func2()  # 늦게 불러온 모듈에 있는 함수 호출
func3()


def func3():
    print("main")


func3()