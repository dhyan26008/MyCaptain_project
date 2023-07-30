import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(['Name', 'Age', 'Contact_Number', 'Email_ID'])
        
        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True

    while condition:
        student_info = input("Enter student information in the following format (Name Age Contact_Number Email_ID): ")
        print("Entered information: " + student_info)

        student_info_list = student_info.split(" ")
        print("Entered split-up information: " + str(student_info_list))

        write_into_csv(student_info_list)

        condition_check = input("Do you want to enter information for another student (yes/no): ")
        if condition_check.lower() == "yes":
            condition = True
        elif condition_check.lower() == "no":
            condition = False
