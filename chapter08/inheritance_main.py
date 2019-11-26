from chapter08.inheritance_study import Bicycle, FoldingBicycle

if __name__ == "__main__":
    myBicycle = Bicycle(wheel_size=26, color="red")
    myFoldBicycle = FoldingBicycle(state="folding", wheel_size=30, color="blue")

    cycle_list = [myBicycle, myFoldBicycle]

    [print(cycle) for cycle in cycle_list]
    [cycle.move() for cycle in cycle_list]
    [cycle.stop() for cycle in cycle_list]


