file_name = "coffeeShopSales.txt"

# with open(file_name, "r") as f:
#     for line in f:
#         print(line, end='')
#
# with open(file_name, "r") as f:
#     header = f.readline()
#     print(header, header.split())
#     [print(line.split()) for line in f]
#     print('\n')


# 과제
with open(file_name, "r") as f:
    data_list = []
    header = f.readline()
    for k in f.readlines():
        coffee_dict = {}
        for j in range(0, len(header.split())):
            coffee_dict[header.split()[j]] = k.split()[j]
        data_list.append(coffee_dict)

    [print(data) for data in data_list]

with open(file_name, "r") as f:
    header = f.readline().split()
    data = [line.split() for line in f]

    espresso = []
    americano = []
    cafelatte = []
    cappucino = []

    for i in range(0, len(data)):
        espresso.append(int(data[i][1]))
        americano.append(int(data[i][2]))
        cafelatte.append(int(data[i][3]))
        cappucino.append(int(data[i][4]))

    total_sum = {"에스프레소": {"나흘전체": sum(espresso), "하루 평균": sum(espresso) / len(espresso)},
                 "아메리카노": {"나흘전체": sum(americano), "하루 평균": sum(americano) / len(americano)},
                 "카페라테": {"나흘전체": sum(cafelatte), "하루 평균": sum(cafelatte) / len(cafelatte)},
                 "카푸치노": {"나흘전체": sum(cappucino), "하루 평균": sum(cappucino) / len(cappucino)}}

    for i in range(0, 4):
        print("{} 판매량\n{}: {}, {}: {}".format(list(total_sum.keys())[i],
                                              list(list(total_sum.values())[i].keys())[0],
                                              list(list(total_sum.values())[i].values())[0],
                                              list(list(total_sum.values())[i].keys())[1],
                                              list(list(total_sum.values())[i].values())[1]))
