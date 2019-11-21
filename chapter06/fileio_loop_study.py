file_path = '/home/shk/다운로드/github/git_python_study/chapter06/two_times_table.txt'


def file_write():
    global file_path
    f = open(file_path, 'w')
    for num in range(1, 6):
        format_string = "2 x {0} = {1}\n".format(num, 2 * num)
        f.write(format_string)
    f.close()


def file_read():
    global file_path
    f = open(file_path)
    line1 = f.readline()
    line2 = f.readline()
    f.close()
    print(line1, line2)


def file_read2():
    f = open(file_path)
    line = f.readline()
    while line:
        print(line, end="")
        line = f.readline()
    f.close()


def file_read3():
    global file_path
    f = open(file_path)
    lines = f.readlines()
    f.close()
    print(lines)


def file_read4():
    global file_path
    f = open(file_path)
    for line in f:
        print(line, end="")
    f.close()


def with_fileio():
    global file_path
    print('===', with_fileio.__name__, '===')
    try:
        with open(file_path, 'r') as f:
            for line in f:
                print(line, end="")
    except FileNotFoundError as e:
        print("해당 파일이 존재하지 않음", e, sep='\n')


# 4개의 함수를 정의
if __name__ == "__main__":
    file_write()
    file_read()
    file_read2()
    file_read3()
    file_read4()
    with_fileio()