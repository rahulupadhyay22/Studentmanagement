#student disctionary
student_grades = {}

#add new student
def add_student(name, grade):
    student_grades[name] = grade
    print(f"added {name} with a {grade}")

#update a student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} with marks are updated {grade}")
        
    else:    
        print(f"{name} not found")  
        
#delete a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} is has been deleted")
    else:
        print(f"{name} not found")
        
#view all students
def view_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} has {grade}")
    else:
        print("No students found")

#search a student
def search_student(name):
    if name in student_grades:
        print(f"{name} has {student_grades[name]}")
    else:
        print(f"{name} not found")


#main function for options
def main():
    while True:
        print("\nstudent management system")
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. View students")
        print("5. Search student")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            add_student(name, grade)
        elif choice == 2:
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            update_student(name, grade)
        elif choice == 3:
            name = input("Enter student name: ")
            delete_student(name)
        elif choice == 4:
            view_students()
        elif choice == 5:
            name = input("Enter student name: ")
            search_student(name)
        elif choice == 6:
            print("Exiting... Thank you for using the system")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()