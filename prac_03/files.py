"""
name ← Prompt user "Enter your name: "
Open "name.txt" for writing as file
    Write name to file
Close file

Open "name.txt" for reading as file
    name ← Read from file
    Print "Hi " + name + "!"
Close file

Open "numbers.txt" for reading as file
    number_1 ← Convert first line read from file to integer
    number_2 ← Convert second line read from file to integer
    Print number_1 + number_2
Close file

total ← 0
Open "numbers.txt" for reading as file
    For each line in file
        total ← total + Convert line to integer
    End for
    Print total
"""
name = input("Enter your name：")
with open("name.txt", "w") as file:
    file.write(name)

with open("name.txt", "r") as file:
    name = file.read()
    print(f"Hi {name}!")


with open("numbers.txt", "r") as file:
    number_1 = int(file.readline())
    number_2 = int(file.readline())
    print(number_1 + number_2)


total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line)
print(total)
