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
            for assign in assignments:
                print(assignment_info['Name'])
                print(assignment_info['Course'])
                print(assignment_info['Due Date'])
                print(assignment_info['Completed'])     

        
