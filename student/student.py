import csv
import os

FILE_NAME = "students.csv"

def header():
    print("\n--- STUDENT REPORT CARD MANAGEMENT SYSTEM ---\n")

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    student_class = input("Enter Class: ")
    s1 = int(input("Enter marks for Subject 1: "))
    s2 = int(input("Enter marks for Subject 2: "))
    s3 = int(input("Enter marks for Subject 3: "))

    total = s1 + s2 + s3
    percentage = round(total / 3, 2)
    grade = calculate_grade(percentage)

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, student_class, s1, s2, s3, total, percentage, grade])

    print("✅ Student record added successfully.\n")

def display_students():
    if not os.path.exists(FILE_NAME):
        print("⚠️ No student records found.")
        return

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        print("\nAll Student Records:\n")
        for row in reader:
            print(row)

def search_student():
    roll = input("Enter roll number to search: ")
    found = False
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == roll:
                print("\n🎯 Student Found:\n", row)
                found = True
                break
    if not found:
        print("❌ Student not found.")

def update_student():
    roll = input("Enter roll number to update: ")
    records = []
    found = False

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == roll:
                print("Old record:", row)
                name = input("Enter New Name: ")
                student_class = input("Enter New Class: ")
                s1 = int(input("Enter new marks for Subject 1: "))
                s2 = int(input("Enter new marks for Subject 2: "))
                s3 = int(input("Enter new marks for Subject 3: "))
                total = s1 + s2 + s3
                percentage = round(total / 3, 2)
                grade = calculate_grade(percentage)
                row = [roll, name, student_class, s1, s2, s3, total, percentage, grade]
                found = True
            records.append(row)

    if found:
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(records)
        print("✅ Student record updated.")
    else:
        print("❌ Student not found.")

def delete_student():
    roll = input("Enter roll number to delete: ")
    records = []
    found = False

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != roll:
                records.append(row)
            else:
                found = True

    if found:
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(records)
        print("🗑 Student record deleted.")
    else:
        print("❌ Student not found.")

def menu():
    while True:
        header()
        print("1. Add Student Record")
        print("2. Display All Records")
        print("3. Search Student")
        print("4. Update Student Record")
        print("5. Delete Student Record")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid input. Try again.")

# Run the menu
menu()
