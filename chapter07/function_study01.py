# 1. 리스트로전달, 2. 튜플 3. 딕셔너리
def my_student_info_list(student_info):
    print("========list========\n")
    for i in range(0, len(student_info)):
        print("{:02}번 학생".format(i + 1))
        print("***************************")
        print("* 학생이름:", student_info[i][0])
        print("* 학급번호:", student_info[i][1])
        print("* 전화번호:", student_info[i][2])
        print("***************************")
    print()


def my_student_info_tuple(student_info):
    print("========tuple========\n")
    for i in range(0, len(student_info)):
        print("{:02}번 학생".format(i + 1))
        print("***************************")
        print("* 학생이름:", student_info[i][0])
        print("* 학급번호:", student_info[i][1])
        print("* 전화번호:", student_info[i][2])
        print("***************************")
    print()


def my_student_info_dict(student_info):
    print("========dict========\n")
    for i in student_info.keys():
        print("{:02}번 학생".format(i))
        print("***************************")
        print("* 학생이름:", student_info[i]["학생 이름"])
        print("* 학급번호:", student_info[i]["학급 번호"])
        print("* 전화번호:", student_info[i]["전화 번호"])
        print("***************************")
    print()


if __name__ == "__main__":
    student_info1 = [["현아", "01", "01-235-6789"], ["진수", "02", "01-333-6789"]]

    my_student_info_list(student_info1)

    student_info2 = (("현아", "01", "01-235-6789"), ("진수", "02", "01-333-6789"))

    my_student_info_tuple(student_info2)

    student_info3 = {1: {"학생 이름": "현아", "학급 번호": "01", "전화 번호": "01-235-6789"},
                     2: {"학생 이름": "진수", "학급 번호": "02", "전화 번호": "01-333-6789"}}

    my_student_info_dict(student_info3)
