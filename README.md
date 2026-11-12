# Student Assignment Manager

A command-line assignment management application built with Python. This project helps students organize coursework, track deadlines, manage assignment completion, and monitor grades.

## Features

- **Assignment Management:** Add, view, and remove assignments.
- **Deadline Tracking:** Calculate how many days remain until an assignment is due, identify overdue assignments, and sort upcoming deadlines.
- **Completion Tracking:** Mark assignments as completed.
- **Grade Tracking:** Add, update, and view assignment grades.
- **Grade Average:** Calculate the average across graded assignments.
- **Data Persistence:** Save and load assignments using a JSON file.
- **Input Validation:** Handle invalid inputs, including incorrect dates, assignment selections, and grades.

## Technologies Used

- Python
- JSON
- Python Datetime Library

## How to Run

1. Install Python
2. Clone this repository:

   ```bash
   git clone https://github.com/Shabadg2008/REPOSITORY-NAME.git
   ```

3. Navigate to the project directory.
4. Run the main Python file:

   ```bash
   python "Assignment Tracker.py"
   ```

Replace `REPOSITORY-NAME` with the actual repository name and adjust the main filename if necessary.

## How It Works

The application uses a menu-driven command-line interface where users can manage assignments and grades.

Each assignment contains:

- Assignment name
- Course name
- Due date
- Completion status
- Grade (if available)

Assignment information is stored locally in `assignments.json`, allowing data to persist between sessions.

## What I Learned

Through this project, I practiced:

- Organizing Python code into reusable functions
- Working with lists and dictionaries
- Reading and writing JSON files
- Handling exceptions with `try/except`
- Validating user input
- Working with dates using `datetime`
- Sorting data using `sorted()` and lambda functions
- Using Git and GitHub for version control

## Future Improvements

- Search and filter assignments by course
- Calculate grade averages for individual courses
- Add automated unit tests
- Develop a graphical user interface

## Project Status

Core features completed.
