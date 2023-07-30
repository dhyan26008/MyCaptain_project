def add_student(student_data, roll_no, name, age, grade):
    student_data[roll_no] = {
        'name': name,
        'age': age,
        'grade': grade
    }

def display_student(student_data, roll_no):
    if roll_no in student_data:
        student = student_data[roll_no]
        print(f"Roll No: {roll_no}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Grade: {student['grade']}")
    else:
        print("Student not found.")

def update_student(student_data, roll_no, name, age, grade):
    if roll_no in student_data:
        student_data[roll_no]['name'] = name
        student_data[roll_no]['age'] = age
        student_data[roll_no]['grade'] = grade
        print("Student information updated.")
    else:
        print("Student not found.")

def delete_student(student_data, roll_no):
    if roll_no in student_data:
        del student_data[roll_no]
        print("Student record deleted.")
    else:
        print("Student not found.")

def main():
    student_data = {} 

    while True:
        print("\nSchool Administration Program")
        print("1. Add Student")
        print("2. Display Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            roll_no = int(input("Enter Roll No: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ")
            add_student(student_data, roll_no, name, age, grade)
        elif choice == 2:
            roll_no = int(input("Enter Roll No: "))
            display_student(student_data, roll_no)
        elif choice == 3:
            roll_no = int(input("Enter Roll No: "))
            name = input("Enter New Name: ")
            age = int(input("Enter New Age: "))
            grade = input("Enter New Grade: ")
            update_student(student_data, roll_no, name, age, grade)
        elif choice == 4:
            roll_no = int(input("Enter Roll No: "))
            delete_student(student_data, roll_no)
        elif choice == 5:
            print("Exiting School Administration Program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
