from cs50 import SQL
import cs50
import sys
import csv

# SAMPLE --> python import.py characters.csv

# OPEN CSV FILE (characters. csv)
# CREATE DB FILE
# TAKE DATA FROM EACH ROW IN CSV FILE
# INSERT IT INTO THE DB FILE


def main():
    # Checking That arguments written correctly
    if (len(sys.argv) != 2):
        print("ERROR")
        exit(1)

    # Making DB Connection
    db = SQL("sqlite:///students.db")

    # Opening CSV file
    with open(sys.argv[1], "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Neglecting first row which contains types of columns data
        for line in reader:
            fullname = line[0].split(" ")
            first = fullname[0]
            name_len = len(fullname)  # Getting number of names for a person
            if (name_len == 2):
                middle = None
                last = fullname[1]
            else:
                middle = fullname[1]
                last = fullname[2]
            house = line[1]
            birth = line[2]
            # Then we took all data from each line
            # Inserting data in the database
            db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",
                       first, middle, last, house, birth)


main()