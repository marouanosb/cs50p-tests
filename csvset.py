import csv

def main():
    while True:
        firstname = input("Name: ")
        familyname = input("Family: ")
        year = input("Year: ")
        mark = input("Mark: ")
        write_to_file(firstname,familyname,year,mark)
        print("written to file!")

def write_to_file(firstname,familyname,year,mark):
    with open ("list.csv","a") as file:
        writer = csv.DictWriter(file, fieldnames=["firstname","familyname","year","mark"])
        writer.writerow({"firstname": firstname, "familyname": familyname, "year": year, "mark": mark})


if __name__=="__main__":
    main()