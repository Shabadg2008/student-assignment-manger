print("----------STUDENT ASSIGNMENT MANAGER----------")
assignments = []
while True:
    print("1. Add Asignment")
    print("2. Remove Asignment")
    print("3. View Assignments")
    print("4. Check Grades")
    print("5. View Upcoming Deadlines")
    print("6. Exit")


    choice = (input("Select a number \n"))

    if choice == "6":
        print("Goodbye")
        break

    elif choice == "1":
         name = input("Enter name of assignment \n")
         course_name = input("Enter course name \n")
         due = input("Enter due date (month-day-year) \n") 
         assignment_info = {"Name": name,
                            "Course": course_name,
                            "Due Date": due,
                            "Completed": False
                            }
         assignments.append(assignment_info)
         print("Assignment Added")

    elif choice =="3":
            print("Current Assignments:")
            print()
            for number, assignment in enumerate(assignments, start = 1):
                print(number, assignment['Name'])
                print(assignment['Course'])
                print(assignment['Due Date'])
                print(assignment['Completed']) 
                print()

    elif choice == "2":
        if len(assignments) == 0:
            print("No assignments to remove!")

        else:
            for number, assignment in enumerate(assignments, start=1):
                print(number, assignment["Name"])

            try:
                remove_number = int(input("What number do you want to remove? \n"))

                if 1 <= remove_number <= len(assignments):
                    assignments.pop(remove_number - 1)
                    print("Assignment removed!")

                else:
                    print("Assignment not found, try again!")

            except ValueError:
                print("Invalid input! Please enter a number.")

