from cs50 import SQL
import sys


# Sample --> python roster.py Gryffindor
# Sample Test --> Lavender Brown, born 1979


# TAKE THE HOUSE NAME FROM ARGV
# EXECUTE SQL COMMAND TO SELECT ALL NAMES FROM THIS HOUSE
# SORTING RESULT BY LAST NAME
# FOR MUTUAL LAST NAME, SORT BY FIRST NAME


def main():
    # Checking That arguments written correctly
    if (len(sys.argv) != 2):
        print("ERROR")
        exit(1)

    housename = sys.argv[1]

    db = SQL("sqlite:///students.db")
    data = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last, first", housename)
    # data result is a list of dicts, each dict contains entire one-person data needed
    for i in range(len(data)):  # iteratimg over this list of dicts which has a person data in each dict
        person = data[i]
        print(person["first"], end=" ")
        if person["middle"] == None:
            pass
        else:
            print(person["middle"], end=" ")
        print(person["last"] + ",", end=" ")
        print("born", person["birth"])


main()