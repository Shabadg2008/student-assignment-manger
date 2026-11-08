import json
from functions import add_assigments, remove_assigments, mark_assignments_complete, view_assigments, days_remaining, view_grades
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
         add_assigments(assignments)

    elif choice =="3":
            view_assigments(assignments)

    elif choice == "2":
        remove_assigments(assignments)

    elif choice == "4":
        mark_assignments_complete(assignments)        

    elif choice == "6":
        days_remaining(assignments)

    elif choice == "5":
         view_grades(assignments)                    
        


