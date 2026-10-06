import re

FILE_NAME = "students.txt"


def add_student():
    try:
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        email = input("Enter Email: ")

        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if not re.match(pattern, email):
            raise ValueError("Invalid Email!")

        with open(FILE_NAME, "a") as file:
            file.write(f"{name},{age},{email}\n")

        print("Student added successfully!")

    except ValueError as e:
        print("Error:", e)


def read_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

            if not data:
                print("No student records found.")
                return

            print("\nStudent Records:")
            print("----------------")

            for record in data:
                name, age, email = record.strip().split(",")

                print("Name:", name)
                print("Age:", age)
                print("Email:", email)
                print("----------------")

    except FileNotFoundError:
        print("No student records found.")


while True:
    print("\n===== Student Record Manager =====")
    print("1. Add Student")
    print("2. Read Students")
    print("3. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            read_students()

        elif choice == 3:
            print("Thank you!")
            break

        else:
            print("Invalid Choice! Please enter 1, 2 or 3.")

    except ValueError:
        print("Please enter a valid number.")