students = []


def add_student():
    name = input("Enter Name: ")
    usn = input("Enter USN: ")
    age = input("Enter Age: ")
    branch = input("Enter Branch: ")

    student = {
        "Name": name,
        "USN": usn,
        "Age": age,
        "Branch": branch
    }

    students.append(student)
    print("\nStudent Added Successfully!\n")


def view_students():

    if len(students) == 0:
        print("\nNo Students Found.\n")
        return

    print("\n----------- Student List -----------")

    for student in students:
        print("Name   :", student["Name"])
        print("USN    :", student["USN"])
        print("Age    :", student["Age"])
        print("Branch :", student["Branch"])
        print("-----------------------------------")


def search_student():

    usn = input("Enter USN to Search: ")

    for student in students:
        if student["USN"] == usn:
            print("\nStudent Found")
            print(student)
            return

    print("Student Not Found")


def update_student():

    usn = input("Enter USN to Update: ")

    for student in students:

        if student["USN"] == usn:

            student["Name"] = input("Enter New Name: ")
            student["Age"] = input("Enter New Age: ")
            student["Branch"] = input("Enter New Branch: ")

            print("Student Updated Successfully!")
            return

    print("Student Not Found")


def delete_student():

    usn = input("Enter USN to Delete: ")

    for student in students:

        if student["USN"] == usn:
            students.remove(student)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found")


while True:

    print("\n====== Student Management System ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")