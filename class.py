import json
def save_to_file(nested_dict, students_birthdays):
    with open(filename, 'w') as file:
        json.dump(nested_dict, file)

def load_from_file(students_birthdays):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

filename = "students_birthdays.json"
nested_dict = load_from_file(filename)

while True:
    today_date = input("Enter today's date in 'Year month date' format in BS (enter 'exit' to stop): ").strip().lower()
    if today_date == 'exit':
        save_to_file(nested_dict, filename)
        break

    year, month, date = today_date.split(" ")

    user_choice = input("What to do?\n1. Add birthdate: PRESS 0\n2. Check whose birthday is today? PRESS 1\n")

    if user_choice in ['0', '1']:
        if user_choice == '0':
            roll_no = input("Enter the roll number: ")
            name = input("Enter first name: ")
            dob_month = int(input("Enter his/her birth month: "))
            dob_date = int(input("Enter his/her birth date: "))
            new_student = {
                "pname": name,
                "dobmonth": dob_month,
                "dobdate": dob_date
            }
            nested_dict[roll_no] = new_student
            print(f"New student with roll no {roll_no} added.")
            save_to_file(nested_dict, filename)  # Save the updated dictionary to the file
        elif user_choice == '1':
            birthday_students = [
                (roll_no, student) for roll_no, student in nested_dict.items()
                if student['dobmonth'] == int(month) and student['dobdate'] == int(date)
            ]
            if birthday_students:
                for roll_no, student in birthday_students:
                    print(f"Today is {student['pname']}'s birthday! Student's roll number is {roll_no}")
            else:
                print("Today is no one's birthday.")
        else:
            print("Invalid input. Please enter either 0 or 1.")
    else:
        print("Invalid input. Please enter either 0 or 1.")
