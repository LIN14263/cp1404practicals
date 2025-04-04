# taxi_test.py
from taxi import Taxi


def main():
    # 1. 创建一个新的Taxi对象
    my_taxi = Taxi("Prius 1", 100)

    # 2. 驾驶40公里
    my_taxi.drive(40)

    # 3. 打印出租车详情和当前费用
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # 4. 重置计价器并驾驶100公里
    my_taxi.start_fare()
    my_taxi.drive(100)

    # 5. 再次打印详情和当前费用
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


if __name__ == "__main__":
    main()