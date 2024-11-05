# Student Management System

This is a simple Python program that allows you to manage a dictionary of students and their grades. The program provides functions to add, update, delete, view, and search for students within the system.

## Features

- **Add a Student**: Add a new student and their grade to the system.
- **Update a Student**: Update the grade of an existing student.
- **Delete a Student**: Remove a student from the system.
- **View All Students**: View all students and their grades.
- **Search for a Student**: Find a student and view their grade.
- **Exit**: Exit the program.

## Program Structure

The program is structured as follows:

- `add_student(name, grade)`: Adds a new student to the `student_grades` dictionary.
- `update_student(name, grade)`: Updates the grade for an existing student.
- `delete_student(name)`: Deletes a student from the dictionary.
- `view_students()`: Displays all students and their grades.
- `search_student(name)`: Searches for a specific student by name and displays their grade.

### Main Loop

The main function provides an interactive menu with options to add, update, delete, view, and search for students, or exit the program.

## Usage

1. Run the program.
2. Choose from the menu options:
    - `1`: Add a student by entering their name and grade.
    - `2`: Update an existing student's grade.
    - `3`: Delete a student from the system.
    - `4`: View all students currently in the system.
    - `5`: Search for a student by name.
    - `6`: Exit the program.

## Requirements
- Python 3.x
  
## Running the Program
```bash
python app.py
