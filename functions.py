import json
def add_assigments(assignments):
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
                            with open("assignments.json", "w") as f:
                                json.dump(assignments, f, indent = 2)
        
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