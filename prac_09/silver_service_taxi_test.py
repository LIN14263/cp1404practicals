# silver_service_taxi_test.py
from silver_service_taxi import SilverServiceTaxi


def main():
    # 创建一个fanciness为2的豪华出租车
    taxi = SilverServiceTaxi("Limo", 100, 2)

    # 驾驶18公里
    taxi.drive(18)

    # 检查费用是否正确（应为$48.80）
    fare = taxi.get_fare()
    print(f"Taxi details: {taxi}")
    print(f"Fare for 18km: ${fare:.2f}")
    assert fare == 48.8, f"Expected $48.80, got ${fare}"
    print("Fare test passed!")


if __name__ == "__main__":
    main()