# taxi_simulator.py
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == "q":
            print(f"Total trip cost: ${total_bill:.2f}")
            print("Taxis are now:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            break

        elif choice == "c":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            try:
                taxi_choice = int(input("Choose taxi: "))
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid taxi choice")

        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = int(input("Drive how far? "))
                    if distance > 0:
                        current_taxi.drive(distance)
                        fare = current_taxi.get_fare()
                        total_bill += fare
                        print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                        current_taxi.start_fare()  # 重置计价器
                    else:
                        print("Distance must be positive")
                except ValueError:
                    print("Invalid distance")

        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")


if __name__ == "__main__":
    main()