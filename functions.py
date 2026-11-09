import json
from datetime import datetime
def add_assigments(assignments):
        name = input("Enter name of assignment \n")
        course_name = input("Enter course name \n")
        due = input("Enter due date (month-day-year) \n") 
        assignment_info = {"Name": name,
                          "Course": course_name,
                          "Due Date": due,
                          "Completed": False,
                          "Grade": None
                                    }
        assignments.append(assignment_info)
        save_assignments(assignments)
        print("Assignment Added")  

def remove_assigments(assignments):
        
        if len(assignments) == 0:
                    print("No assignments to remove!")
        
        else:
                    for number, assignment in enumerate(assignments, start=1):
                        print(number, assignment["Name"])
        
                    try:
                        remove_number = int(input("What number do you want to remove? \n"))
        
                        if 1 <= remove_number <= len(assignments):
                            assignments.pop(remove_number - 1)
                            save_assignments(assignments)
        
                            print("Assignment removed!")
        
                        else:
                            print("Assignment not found, try again!")
        
                    except ValueError:
                        print("Invalid input! Please enter a number.")

def view_assigments(assignments):
    print("Current Assignments:")
    print()
    for number, assignment in enumerate(assignments, start = 1):
         print(number, assignment['Name'])
         print(assignment['Course'])
         print(assignment['Due Date'])
         print(assignment['Completed']) 
         print()

def mark_assignments_complete(assignments):
          
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
                          change_status = int(input("Which assignment do you want to mark complete?\n"))
                          if 1<= change_status <= len(assignments):
                              assignments[change_status - 1]["Completed"] = True
                              save_assignments(assignments)
                              print(f"Assignment {change_status} marked as done!")
                          else:
                              print("Assignment not found")
                          repeat = input("Do you have another assignment to mark complete? Y/N\n").lower()
                          if repeat != "y":
                              break
                      except ValueError:
                          print("invalid input! Please enter a number.")  

def save_assignments(assignments):
     with open("assignments.json", "w") as f:
        json.dump(assignments, f, indent = 2)

def days_remaining(assignments):
      try:
        Current_Date = datetime.now().date()
        incomplete_assignments = [
        x for x in assignments if not x["Completed"]
    ]
        if len(incomplete_assignments) == 0:
            print("No incomplete assignments!")
            return
        sorted_assignments = sorted(assignments, key = lambda x: datetime.strptime(x["Due Date"]," %m-%d-%Y"))
        for number, assignment in enumerate(sorted_assignments, start=1):
                if assignment["Completed"] == True:
                    continue
                else:
                    Due_Date = datetime.strptime(assignment['Due Date'], "%m-%d-%Y").date()
                    Remaining_Time = Due_Date - Current_Date
                    print(number, assignment["Name"])
                    if Remaining_Time.days == 0:
                        print("Due today!")
                    elif Remaining_Time.days < 0:
                        overdue_date = abs(Remaining_Time.days)
                        print(f"Overdue by {overdue_date} Days!")
                    else:
                        print(f"Due in {Remaining_Time.days} Days")
      except ValueError:
           print("Invalid entry!")
        
def view_grades(assignments):
     print("----Grade Tracker ----")
     print()
     print("1. Add Grade")
     print("2. Update Grade")
     print("3. View Grades")
     print("4. Calculate Average")
     print("5. Return to Menu")

     while True:
        for number, assignment in enumerate(assignments, start=1):
            print(number, assignment["Name"])
        choice = int(input("Select an option, 1-4 \n"))
        if choice == 1:
             select = int(input("Which assignment do you want to grade? \n"))
             if 1 <= select <= len(assignments):
                  new_grade = float(input("Enter a grade 0-100: \n"))
                  if 0 <= new_grade <= 100:
                    assignment[select - 1]["Grade"] = new_grade
                    save_assignments(assignments)
                    print("Grade Saved")
                  else:
                    print("Invalid Grade")
             else:
                print("Not an assignment!")
        elif choice == 2:
             update = int(input("Which assignments grade do you want to update? \n"))
             if 1 <= update <= len(assignments):
                  updated_grade = float(input("Enter your updated grade: \n"))
                  if 0 <= updated_grade <= 100:
                       assignment[update-1]["Grade"] = updated_grade
                       save_assignments(assignments)
                       print("Grade Updated")
                  else:
                       print("Invalid Grade, Try again!")
             else:
                  print("Not an Assignment!")
        elif choice == 3:
             for number, assignment in enumerate(assignments, start =1):
                  grade = assignment.get("Grade")  
                  if grade is None:
                    print(f"{number}. {assignment["Name"]}: No Grade Yet")
                  else:
                    print(f"{number}. {assignment["Name"]}: {grade}%")
                
                    