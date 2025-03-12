def get_numbers():
    input_str = input("Enter numbers separated by commas: ")
    numbers = [float(x.strip()) for x in input_str.split(',')]
    return numbers

def square_numbers(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2
    return numbers

def display_numbers(numbers):
    output_str = "..".join(str(x) for x in numbers)
    print(output_str)

def main():
    numbers = get_numbers()
    square_numbers(numbers)
    display_numbers(numbers)

if __name__ == "__main__":
    main()

    