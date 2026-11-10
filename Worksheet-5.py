#Worksheet 5
#Session 9
#Exercise-1
'''

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def write_summary(self):
    """Write a short summary about Python into the file (only if it's a .txt file)."""
        if self.filename.endswith(".txt"):
            try:
                with open(self.filename, 'w') as file:
                    file.write("Python is easy to learn and powerful.\n")
                    file.write("It supports object-oriented programming.\n")
                    file.write("You can handle files and exceptions in Python.\n")
                    file.write("Python is widely used in data science and web development.\n")
                print(f"Summary successfully written to '{self.filename}'.\n")
            except (IOError, PermissionError) as e:
                print(f"Error writing to file: {e}")
        else:
            print("Skipping writing because the file is not a .txt summary file.\n")

# --- Execution / Test Cases ---
if __name__ == "__main__":
    
# Test with a valid .txt file
    txt_manager = FileManager("python_summary.txt")
    txt_manager.write_summary()

# Test with a non-.txt file to trigger the else block
    csv_manager = FileManager("data.csv")
    csv_manager.write_summary() 


    def read_entire_file(self):
        """Read the entire content of the file at once and print it."""
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
                print("9.1.a - Entire File Content:\n")
                print(content)
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
        except PermissionError:
            print(f"Error: Permission denied to read '{self.filename}'.")

    def read_file_line_by_line(self):
        """Read the file line by line into a list and print each line."""
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                print("9.1.b - File Content Line by Line:\n")
                for line in lines:
                    print(line.strip()) 
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
        except PermissionError:
            print(f"Error: Permission denied to read '{self.filename}'.") 



# Main program
if __name__ == "__main__":
    # Choose file to work with: summary.txt or students.csv
    filename = "summary.txt"  
# change to "students.csv" to test with that file

    manager = FileManager(filename)

# Write summary if using summary.txt
    manager.write_summary()

# Perform both types of read operations
    manager.read_entire_file()
    manager.read_file_line_by_line() 

#Exercise 2
with open("learning_students.txt", "w") as file:
    file.write("Every learner must complete their assignments on time. "
               "A good learner always seeks to learn more. "
               "Learners are the future leaders.")
with open("learning_students.txt", "r") as file:
    for line in file:
        modified_line = line.replace("learner", "student").replace("Learners", "Students")
        print(modified_line)

#Exercise 3
def get_numeric_input(prompt):
    while True:
        try:
            return float(input(prompt))  
# You can change to int() if integers only
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def main():
    print("Enter two numbers to add them together.")
    num1 = get_numeric_input("Enter the first number: ")
    num2 = get_numeric_input("Enter the second number: ")
    total = num1 + num2
    print(f"The sum of {num1} and {num2} is {total}.")

if __name__ == "__main__":
    main()


#Exercise 4

def read_file(filename):
    try:
        with open(filename, "r") as file:
            print(f"\nContents of {filename}:")
            print(file.read())
    except FileNotFoundError:
        print(f"Error: {filename} was not found. Please check the file location.")

def main():
    read_file("students_c1.txt")
    read_file("students_c2.txt")

if __name__ == "__main__":
    main()


#Exercise 5

import json
filename = "favourite_number.json"
try:
    favourite_number = int(input("Enter your favourite number: "))
    with open(filename, "w") as file:
        json.dump(favourite_number, file)
    print("Your favourite number has been saved.")
except ValueError:
    print("Invalid input. Please enter a valid number.")

try:
    with open(filename, "r") as file:
        fav = json.load(file)
        print(f"\nYour favourite number is {fav}! That's a great choice.")
except FileNotFoundError:
    print(f"Could not find the file {filename}.")
except json.JSONDecodeError:
    print("Error reading the favourite number from the file.")
Exercise 6

import json
filename = "user_profile.txt"

# 9.6.a.1 – Collect and save student ID
user_profiles = {}
student_id = input("Enter Student ID: ").strip()
user_profiles[student_id] = {} 
 # Initialize with empty data

# Save to file
with open(filename, "w") as file:
    json.dump(user_profiles, file)
print("Student ID saved to file.")

# 9.6.a.2 – Load the saved data from the file
try:
    with open(filename, "r") as file:
        loaded_profiles = json.load(file)
except FileNotFoundError:
    print(f"Error: {filename} not found.")
    loaded_profiles = {}

# 9.6.a.3 – Add DOB and email for the student
if student_id in loaded_profiles:
    dob = input("Enter Date of Birth (YYYY-MM-DD): ").strip()
    email = input("Enter Email Address: ").strip()
    
    loaded_profiles[student_id]["dob"] = dob
    loaded_profiles[student_id]["email"] = email

# Save updated data back to the file
    with open(filename, "w") as file:
        json.dump(loaded_profiles, file, indent=4)
    
    print("Student profile updated and saved.")
else:
    print(f"Student ID {student_id} not found in the loaded profiles.")

# Optional: Display the updated profile
print("\nCurrent Data:")
print(json.dumps(loaded_profiles, indent=4))

#Session 10
#Exercises 1.
#a.	Student_function.py (folder)
import csv

def get_student_info(filename):
    result = []
    try:
        with open(filename, mode='r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 3:
                    first_name = row[1].strip()
                    last_name = row[2].strip()
                    student_id = row[0].strip()
                    message = f"Hello {first_name} {last_name}, your student id is {student_id}."
                    result.append(message)
    except FileNotFoundError:
        return ["File not found."]
    return result

#b. test_studentinfo.py (folder)
import unittest
from student_functions import get_student_info

class TestStudentInfo(unittest.TestCase):
    def test_get_student_info(self):
        # Create a sample test file
        test_filename = 'test_students.csv'
        with open(test_filename, 'w') as f:
            f.write("1001,Alice,Smith,sd1001@uni123st.edu.au\n")
            f.write("1002,Bob,Johnson,sd1002@uni123st.edu.au\n")

        expected_output = ["Hello Alice Smith, your student id is 1001.","Hello Bob Johnson, your student id is 1002."]

        result = get_student_info(test_filename)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()

#Exercise 2:

Employee.py
class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        self.annual_salary += amount

test_employee.py
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_default_raise(self):
        emp = Employee("John", "Doe", 50000)
        emp.give_raise()
        self.assertEqual(emp.annual_salary, 55000)

    def test_custom_raise(self):
        emp = Employee("Jane", "Smith", 60000)
        emp.give_raise(10000)
        self.assertEqual(emp.annual_salary, 70000)

if __name__ == '__main__':
    unittest.main()

#Thereafter, we have to open the terminal and run 
python test_studentinfo.py
python test_employee.py


'''