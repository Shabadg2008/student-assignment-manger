import json
try:
    with open("assignments.json", "r") as f:
                assignments = json.load(f)
except FileNotFoundError:
    assignments = []
     
print("----------STUDENT ASSIGNMENT MANAGER----------")

while True:
    print("1. Add Asignment")
    print("2. Remove Asignment")
    print("3. View Assignments")
    print("4. Mark Assignments Complete")
    print("5. Check Grades")
    print("6. View Upcoming Deadlines")
    print("7. Exit")


    choice = (input("Select a number \n"))

    if choice == "7":
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
         with open("assignments.json", "w") as f:
             json.dump(assignments, f, indent = 2)
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
                    with open("assignments.json", "w") as f:
                        json.dump(assignments, f, indent = 2)

                    print("Assignment removed!")

                else:
                    print("Assignment not found, try again!")

            except ValueError:
                print("Invalid input! Please enter a number.")

    elif choice == "4":
        while True:
            if len(assignments) == 0:
                print("No assignments to mark complete!")
                break
            else:
                for number, assignment in enumerate(assignments, start=1):
                    print()
                    print(number, assignment["Name"])
                    print(assignment['Completed'])

                try:
                    change_status = int(input("Which assignment do you want to mark complete?"))
                    if 1<= change_status <= len(assignments):
                        assignments[change_status - 1]["Completed"] = True
                        with open("assignments.json", "w") as f:
                            json.dump(assignments, f, indent = 2)
                        print(f"Assignment {change_status} marked as done!")
                    else:
                        print("Assignment not found")
                    repeat = input("Do you have another assignment to mark complete? Y/N").lower()
                    if repeat != "y":
                        break
                except ValueError:
                    print("invalid input! Please enter a number.")                    
        


