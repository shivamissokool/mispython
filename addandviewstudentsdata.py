# Initialize an empty list to store student data
students = []

def add_student():
    """Function to add a student to the list"""
    scholar_number = input("Enter the scholar number: ")
    name = input("Enter the student's name: ")
    # Add the student's data as a dictionary to the list
    students.append({"scholar_number": scholar_number, "name": name})
    print("Student added successfully!")

def view_students():
    """Function to view all students in the list"""
    if not students:
        print("No students data available.")
        return
    
    print("\nList of Students:")
    for student in students:
        print(f"Scholar Number: {student['scholar_number']}, Name: {student['name']}")

def main():
    """Main function to display the menu and handle user input"""
    while True:
        print("\nStudent Data Management")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
