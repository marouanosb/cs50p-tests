import csv

def main():
    students = read_from_file()
    for s in sorted(students, key=lambda student: student["mark"], reverse=True):
        print(f'{s["firstname"]}, {s["familyname"]}, {s["year"]}, {s["mark"]}')

def read_from_file():
    students = []
    with open("list.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students


if __name__=="__main__":
    main()