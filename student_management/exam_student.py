# list, tuple, dict, set에서 하나를 선택하여 하나를 선택하여 아래 프로그램을 작성하시오.
# --> dictionary + 하나
# student_management 패키지를 추가
# 학생 정보는 : 학생번호, 학생명, 국어, 영어, 수학, 총점, 평균
# 출력 결과 : 1, 김승영, 90, 90, 90, 270, 90.0
# 1. 학생목록, 2. 학생추가 3. 학생 수정, 4. 학생 삭제, 5. 종료 메뉴 추가
# 2. 프로그램 수행 시 먼저 student_list.txt 파일을 읽어와 수행
# 3. 각각 메뉴별 수행되도록 작성
# 4. 종료 시 학생 목록이 student_list.txt에 저장
# 5. 프린트하여 제출
# {"학생번호":"01", "학생명":"김승영", "국어":90, "영어":90, "수학":90, "총점":270, "평균":90}
import sys


def ListOfStudent():
    try:
        print("학생번호  학생명   국어   영어   수학   총점    평균")
        for i in student_list[0:len(student_list)]:
            print(i)
    except e:
        print("학생 정보 검색에 실패하였습니다.", e, sep="\n")
    finally:
        select = input("검색이 종료되었습니다. 메뉴로 돌아가시겠습니까?[y/n]\n")
        while True:
            if select == "y":
                return
            elif select == "n":
                ExitProgram()
            else:
                select = input("잘못 입력하셨습니다. 메뉴로 돌아가시겠습니까?[y/n]\n")


def AddStudent():
    while True:
        try:
            print("학생 정보를 추가하겠습니다.")
            data1 = input("학생번호? ")
            for i in range(0, len(student_list)):
                if student_list[i][0] == data1:
                    print("학생번호가 중복됩니다.")
                    return
            data2 = input("학생명? ")
            data3 = int(input("국어성적? "))
            data4 = int(input("영어성적? "))
            data5 = int(input("수학성적? "))
            total = data3 + data4 + data5
            avg = round(total / 3, 1)
            list = [data1, data2, str(data3), str(data4), str(data5), str(total), str(avg)]
            print(list)
            student_list.append(list)
        except e:
            print("학생 정보 추가에 실패하였습니다.", e, sep="\n")
        finally:
            select = input("학생 추가가 종료되었습니다. 메뉴로 돌아가시겠습니까?[y/n]\n")
            while True:
                if select == "y":
                    return
                elif select == "n":
                    ExitProgram()
                else:
                    select = input("잘못 입력하셨습니다. 메뉴로 돌아가시겠습니까?[y/n]\n")


def UpdateStudent():
    try:
        count = 0
        num = input("수정하실 학생 번호를 입력하세요.")
        for i in range(0, len(student_list)):
            if student_list[i][0] == num:
                count = 1
                print("{} 학생의 정보를 수정하겠습니다.".format(student_list[i][1]))
                student_list[i][1] = input("학생명? ")
                student_list[i][2] = input("국어성적? ")
                student_list[i][3] = input("영어성적? ")
                student_list[i][4] = input("수학성적? ")
                total = int(student_list[i][2]) + int(student_list[i][3]) + int(student_list[i][4])
                avg = round(total / 3, 1)
                student_list[i][5] = str(total)
                student_list[i][6] = str(avg)
                print(student_list[i])
        if count == 0:
            print("해당 학번의 학생이 없습니다.")
    except e:
        print("학생 정보 수정에 실패하였습니다.", e, sep="\n")
    finally:
        select = input("추가가 종료되었습니다. 메뉴로 돌아가시겠습니까?[y/n]\n")
        while True:
            if select == "y":
                return
            elif select == "n":
                ExitProgram()
            else:
                select = input("잘못 입력하셨습니다. 메뉴로 돌아가시겠습니까?[y/n]\n")


def DelStudent():
    try:
        count = 0
        num = input("삭제하실 학생 번호를 입력하세요.")
        for i in range(0, len(student_list)):
            if student_list[i][0] == num:
                count = 1
                a = input("{} 학생의 정보를 삭제하겠습니다.[y/n]".format(student_list[i][1]))
                if a == "y":
                    del student_list[i]
        if count == 0:
            print("해당 학번의 학생이 없습니다.")
    except e:
        print("학생 정보 수정에 실패하였습니다.", e, sep="\n")
    finally:
        select = input("삭제가 종료되었습니다. 메뉴로 돌아가시겠습니까?[y/n]\n")
        while True:
            if select == "y":
                return
            elif select == "n":
                ExitProgram()
            else:
                select = input("잘못 입력하셨습니다. 메뉴로 돌아가시겠습니까?[y/n]\n")


def ExitProgram():
    print("프로그램을 종료하겠습니다.")
    f = open("/home/shk/다운로드/github/git_python_study/student_management/student_list.txt", "w")
    for i in range(0, len(student_list)):
        for j in range(0, 7):
            f.write("{} ".format(student_list[i][j]))
        f.write("\n")
    f.close()
    sys.exit(0)


if __name__ == "__main__":
    student_list = []
    # 학생 정보 리스트에 추가
    try:
        f = open("/home/shk/다운로드/github/git_python_study/student_management/student_list.txt", "r")
        line = f.readline()
        while line:
            student_list.append(line.split())
            line = f.readline()
    except FileNotFoundError as e:
        print("해당 파일이 존재하지 않음", e, sep="\n")
    finally:
        f.close()
        print(student_list)

    while True:
        print("=========학생관리시스템=========")
        print("1. 학생 목록")
        print("2. 학생 추가")
        print("3. 학생 수정")
        print("4. 학생 삭제")
        print("5. 종료")
        print("=============================")
        num = input("번호를 입력하세요.\n")

        if num == "1":
            ListOfStudent()
        elif num == "2":
            AddStudent()
        elif num == "3":
            UpdateStudent()
        elif num == "4":
            DelStudent()
        elif num == "5":
            ExitProgram()
