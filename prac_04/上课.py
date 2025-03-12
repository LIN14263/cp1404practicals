"""names=["Ada","Alan","Bill","John"]
print(",".join(names))
name_to_remove=input("who do you want to remove? ")
while name_to_remove!="":
    try:
        names.remove(name_to_remove)
    except ValueError:
        print("Name not in the list!")
    print(names)
    name_to_remove=input("who do you want to remove? ").title()

print("good try!")"""




with open ("numbers.txt", "r") as input_file:
    numbers=input_file.readlines()
    sum_of_numbers=0
    for number in numbers:
        sum_of_numbers+=float(number)
    print(f"Total sum is {sum_of_numbers}")
    print(float(sum_of_numbers))
    print(int(sum_of_numbers))
    print(float("hello")
