file_name = "coffeeShopSales.txt"

with open(file_name, "r") as f:
    for line in f:
        print(line, end='')

with open(file_name, "r") as f:
    header = f.readline()
    print(header, header.split())
    [print(line.split()) for line in f]
    print('\n')


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
