# unreliable_car_test.py
from unreliable_car import UnreliableCar


def main():
    # 创建一个30%可靠性的车
    car = UnreliableCar("Old Clunker", 100, 30)

    # 测试100次驾驶，每次10公里
    total_distance = 0
    for _ in range(100):
        distance_driven = car.drive(10)
        total_distance += distance_driven

    # 打印结果
    print(f"Total distance driven: {total_distance}km")
    print(f"Final state: {car}")

    # 检查可靠性（30%可靠的车应该大约行驶30次左右）
    if 20 <= total_distance / 10 <= 40:
        print("Reliability seems to be working as expected!")
    else:
        print("Something might be wrong with reliability.")


if __name__ == "__main__":
    main()