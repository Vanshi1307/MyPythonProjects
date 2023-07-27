import csv
import os

FILE_NAME = "students.csv"

def load_students_from_csv():
    students = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            students = [student for student in reader]
    return students

def save_students_to_csv(students):
    with open(FILE_NAME, "w", newline="") as csvfile:
        fieldnames = ["Name", "Age", "Grade"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

def display_menu():
    print("\n===== School Administration Program =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Exit")

def add_student(students):
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grade = input("Enter student's grade: ")

    students.append({"Name": name, "Age": age, "Grade": grade})
    save_students_to_csv(students)
    print("Student added successfully!")

def view_students(students):
    if not students:
        print("No students found.")
        return

    print("\n===== List of Students =====")
    for i, student in enumerate(students, 1):
        print(f"{i}. Name: {student['Name']}, Age: {student['Age']}, Grade: {student['Grade']}")

def main():
    students = load_students_from_csv()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
