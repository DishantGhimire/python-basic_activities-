
today_date = input("Enter today's date in 'Year month date' format in BS").strip()
year, month, date = today_date.split(" ")
user_choice = input("What to do?\n1. Add birthdate: PRESS 0\n2. Check whose birthday is today? PRESS 1\n")
nested_dict = {
    "99999": {"pname": "ram", "dobmonth": 11, "dobdate": 30},
}
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
    elif user_choice == '1':
        for roll_no, new_student in nested_dict.items():
            if new_student['dobmonth'] == int(month) and new_student['dobdate'] == int(date):
                print(f"Today is {new_student['pname']}'s birthday! His roll number is {roll_no}")
    else:
        print("Today is no one's birthday ")
else:
    print("Invalid input. Please enter either 0 or 1.")
