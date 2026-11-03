'''
#Session 7 
#Exercise 1: Student Registration 
# Define the function
def course_enrollment(student_id, first_name, last_name, course_id, course_name, action=None):
    if action == 'Add':
        print(f"Student {first_name} {last_name} {student_id} has been successfully added to {course_name} {course_id}")
    else:
        print(f"Echo: Student {first_name} {last_name} {student_id} registered for {course_name} {course_id}")

course_enrollment("S1234", "Alice", "Brown", "CSE101", "Introduction to Computer Science")

course_enrollment("S5678", "Bob", "Smith", "CSE102", "Data Structures", action='Add')


#Student Action 
#Modified function to handle Echo, Amend, and Delete

def course_enrollment(student_id, first_name, last_name, course_id, course_name, action="Echo"):
    if action == 'Amend':
        print(f"Amend: Student {first_name} {last_name} {student_id} updated enrollment in {course_name} {course_id}).")
    elif action == 'Delete':
        print(f"Delete: Student {first_name} {last_name} {student_id} removed from {course_name} {course_id}")
    else:
        print(f"Echo: Student {first_name} {last_name} {student_id} registered for {course_name} {course_id}")

course_enrollment("S2001", "Charlie", "Davis", "CS103", "Algorithms")

course_enrollment("S2002", "Diana", "Evans", "CS104", "Databases", action="Amend")

course_enrollment("S2003", "Ethan", "Ford", "CS105", "Operating Systems", action="Delete")

#Exercise 2 
#Student Course List 

'''
def collect_courses(student_id, student_name):
    print(f"\nWelcome {student_name} (ID: {student_id})") 

#Collect 4 course IDs
    
    courses = []
    for i in range(4):
        course_id = input(f"Enter Course {i + 1} ID: ")
        courses.append(course_id)

#Ask for semester and year
    semester = input("Enter Semester (e.g., Semester 1): ")
    year = input("Enter Year (e.g., 2025): ")

    # Display summary
    print("\n--- Course Enrollment Summary ---")
    print(f"Student ID: {student_id}")
    print(f"Student Name: {student_name}")
    print("Enrolled Courses:")
    for course in courses:
        print(f"- {course}")
    print(f"Semester: {semester}")
    print(f"Year: {year}\n")
sid = input("Enter Student ID: ")
name = input("Enter Student Name: ")
collect_courses(sid, name)

'''
2.
def store_course_info(student_id, student_name, **courses):
    print(f"\n- Student Course Details -")
    print(f"Student ID: {student_id}")
    print(f"Student Name: {student_name}")
    
    # Display the courses from keyword arguments
    if courses:
        print("Courses Enrolled:")
        for course_id, course_name in courses.items():
            print(f"- {course_id}: {course_name}")
    else:
        print("No courses were provided.")
        
store_course_info("S2022", "Nar", ICT101="Introduction of Computer", ICT102="Applied Communication", MTH104="Discrete Mathematics", ENG101="English Communication")

#Exercise 3 
#Tkinter calculator 

import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math error", "Cannot divide by zero.")

# Create the main window
root = tk.Tk()
root.title("Basic Calculator")

# Create and place widgets
tk.Label(root, text="Enter first number:").grid(row=0, column=0, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, pady=5)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, pady=5)

# Operation buttons
tk.Button(root, text="Add", command=lambda: calculate("add")).grid(row=2, column=0, pady=5)
tk.Button(root, text="Subtract", command=lambda: calculate("subtract")).grid(row=2, column=1, pady=5)
tk.Button(root, text="Multiply", command=lambda: calculate("multiply")).grid(row=3, column=0, pady=5)
tk.Button(root, text="Divide", command=lambda: calculate("divide")).grid(row=3, column=1, pady=5)

# Result display
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()


#Session 6
#Student Profile-User Class
class User:
    def __init__(self, first_name, last_name, email, username, date_of_birth, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.date_of_birth = date_of_birth
        self.location = location

    def describe_user(self):
        print(f"User Profile Summary:")
        print(f" Name: {self.first_name} {self.last_name}")
        print(f" Username: {self.username}")
        print(f" Email: {self.email}")
        print(f" Date of Birth: {self.date_of_birth}")
        print(f" Location: {self.location}")
        print("-" * 40)

    def greet_user(self):
        print(f"Welcome back, {self.first_name}!\n")


# Create several user instances
user1 = User("Dorji", "Pema", "dorji.pema@example.com", "DorjiP", "2001-03-15", "Bhutan")
user2 = User("Tshering", "Dema", "Tshering.dema@example.com", "TsheringD", "2000-08-22", "Melbourne")
user3 = User("Clara", "Nguyen", "clara.nguyen@example.com", "clarang", "2002-01-10", "Brisbane")


# Call methods for each user
for user in [user1, user2, user3]:
    user.describe_user()
    user.greet_user()


#Login Attempts 
# Test login attempts
class User:
    def __init__(self, first_name, last_name, email, username, date_of_birth, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.date_of_birth = date_of_birth
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Profile Summary:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Username: {self.username}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Welcome, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
print("=== User Login Attempts Demo ===")

user1 = User("Nar", "Galey", "nar.bdr@example.com", "NarG", "2000-03-15", "Bhutan")

user1.greet_user()
user1.describe_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"Login attempts after 3 tries: {user1.login_attempts}")

user1.reset_login_attempts()
print(f"Login attempts after reset: {user1.login_attempts}")


#Student Profile - Classroom 

class Classroom:
    def __init__(self, classroom_name, classroom_location, seats_in_class):
        self.classroom_name = classroom_name
        self.classroom_location = classroom_location
        self.seats_in_class = seats_in_class

    def describe_classroom(self):
        print("\nClassroom Details:")
        print(f"Name: {self.classroom_name}")
        print(f"Location: {self.classroom_location}")
        print(f"Seats Available: {self.seats_in_class}")

    def checksize_classroom(self, enrolled_students):
        if self.seats_in_class >= enrolled_students:
            print(f"The classroom has enough seats for {enrolled_students} students.")
        else:
            print(f"Not enough seats! {enrolled_students} students need seating, but only {self.seats_in_class} seats are available.")

# --- Creating one classroom instance and using it ---
print("=== Single Classroom Instance ===")
classroom1 = Classroom("ICT Lab 1", "Building A, Room 101", 30)

# Print individual attributes
print(f"\nName: {classroom1.classroom_name}")
print(f"Location: {classroom1.classroom_location}")
print(f"Seats: {classroom1.seats_in_class}")

# Call methods
classroom1.describe_classroom()
classroom1.checksize_classroom(enrolled_students=25)

# --- Creating multiple classroom instances ---
print("\n=== Multiple Classroom Instances ===")
classroom2 = Classroom("ICT Lab 2", "Building B, Room 202", 40)
classroom3 = Classroom("Lecture Hall 1", "Main Block, Room 1", 100)
classroom4 = Classroom("Seminar Room", "Annex Building, Room 10", 20)

classroom2.describe_classroom()
classroom3.describe_classroom()
classroom4.describe_classroom()


#Enrolled Students 
# Define the Classroom class with enrollment tracking
class Classroom:
    def __init__(self, classroom_name, classroom_location, seats_in_class):
        self.classroom_name = classroom_name
        self.classroom_location = classroom_location
        self.seats_in_class = seats_in_class
        self.students_enrolled = 0  # Default value
        self.audit_log = []  # To store historical enrollment updates

    def describe_classroom(self):
        print(f"Classroom Name: {self.classroom_name}")
        print(f"Location: {self.classroom_location}")
        print(f"Seats in Class: {self.seats_in_class}\n")

    def checksize_classroom(self):
        if self.students_enrolled <= self.seats_in_class:
            print(f"Seats are sufficient for {self.students_enrolled} enrolled students.")
        else:
            print(f"Not enough seats for {self.students_enrolled} students!")
        print()
# Method to set number of enrolled students
    def set_number_enrolled(self, number):
        self.students_enrolled = number
        print(f"Students enrolled set to: {self.students_enrolled}\n")

# Method to update number of enrolled students and log changes
    def update_number_enrolled(self, number, updated_by="System"):
        self.students_enrolled = number
        log_entry = {
            "new_value": number,
            "updated_by": updated_by
        }
        self.audit_log.append(log_entry)
        print(f"Updated enrolled students to: {number} by {updated_by}\n")

# Show the audit log
    def show_audit_log(self):
        print("Audit Log of Enrollment Changes:")
        for entry in self.audit_log:
            print(entry)
        print()
classroom = Classroom("ICT105", "Block A - Room 101", 30)

# Print default enrolled students
print(f"Initial enrolled students: {classroom.students_enrolled}")

# Change value directly
classroom.students_enrolled = 20
print(f"Manually updated enrolled students: {classroom.students_enrolled}")

# Use set_number_enrolled
classroom.set_number_enrolled(25)

# Use update_number_enrolled
classroom.update_number_enrolled(28, updated_by="Admin")
classroom.update_number_enrolled(30, updated_by="Instructor")

# Check if seats are enough
classroom.checksize_classroom()

# Display audit log
classroom.show_audit_log()


#Classroom Equipment 
# Base class
class Classroom:
    def __init__(self, classroom_name, classroom_location, seats_in_class):
        self.classroom_name = classroom_name
        self.classroom_location = classroom_location
        self.seats_in_class = seats_in_class

    def describe_classroom(self):
        print(f"Classroom Name: {self.classroom_name}")
        print(f"Location: {self.classroom_location}")
        print(f"Seats in Class: {self.seats_in_class}\n")

# Subclass that inherits from Classroom
class Equipment(Classroom):
    def __init__(self, classroom_name, classroom_location, seats_in_class, devices):
        # Initialize base class attributes
        super().__init__(classroom_name, classroom_location, seats_in_class)
        # New attribute for the subclass
        self.devices = devices

    def display_devices(self):
        print(f"Devices in {self.classroom_name}:")
        if self.devices:
            for device in self.devices:
                print(f"- {device}")
        else:
            print("No devices listed.")
        print()


#Create an instance and test 
equipment_classroom = Equipment(
    classroom_name="ICT Lab",
    classroom_location="Building B - Room 202",
    seats_in_class=35,
    devices=["Projector", "Smart Board", "25 Laptops", "Wi-Fi Router"]
)

equipment_classroom.describe_classroom()
equipment_classroom.display_devices()


'''