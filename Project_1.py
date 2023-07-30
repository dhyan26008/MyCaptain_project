import csv

class Student:
    def __init__(self, name, age, contact_number, email_id):
        self.name = name
        self.age = age
        self.contact_number = contact_number
        self.email_id = email_id


def write_into_csv(student_info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(['Name', 'Age', 'Contact_Number', 'Email_ID'])
        
        writer.writerow(student_info_list)


def main():
    condition = True

    while condition:
        print("\nSchool Administration Program")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            contact_number = input("Enter student's contact number: ")
            email_id = input("Enter student's email ID: ")

            student = Student(name, age, contact_number, email_id)

            # Convert student object attributes to a list to write into CSV
            student_info_list = [student.name, student.age, student.contact_number, student.email_id]
            write_into_csv(student_info_list)

            print("Student added successfully!")
        elif choice == '2':
            try:
                with open('student_info.csv', 'r') as csv_file:
                    reader = csv.reader(csv_file)
                    for row in reader:
                        print(f"Name: {row[0]}, Age: {row[1]}, Contact Number: {row[2]}, Email ID: {row[3]}")
            except FileNotFoundError:
                print("No student records found.")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
