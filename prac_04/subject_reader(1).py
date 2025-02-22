FILENAME = "subject_data.txt"


def main():
    datas = load_data()
    display_data(datas)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    datas = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        datas.append(parts)
        print("----------")
    input_file.close()
    return datas

def display_data(datas):
    for i in datas:
        course, name, number = i
        print(f"{course:<6} is taught by {name:<12} and has {number:<3} students")



main()