from programming_language import ProgrammingLanguage

def string_to_bool(s):
    return s.strip().lower() in ['true', 'yes', '1']

def main():
    with open("languages.csv", "r") as file:
        header = file.readline()
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(',')
                name = parts[0].strip()
                year = int(parts[1].strip())
                reflection = string_to_bool(parts[2])
                pointer_arithmetic = string_to_bool(parts[3])
                language = ProgrammingLanguage(name, year, reflection, pointer_arithmetic)
                print(language)

if __name__ == '__main__':
    main()
