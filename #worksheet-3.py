#worksheet-3
#Student Course Enrollment.
Course_enrollments={1:["ICT101"],2:["ICT102"],3:["ICT103"],4:["ICT104"],5:["ICT105"]}
for num, info in Course_enrollments.items():
    print(f"student ID {num}:")
    for Course in info:
        print(Course)

#Class Schedule.(Whole list)
departments={"computer science":["CS101", "introduction to computer science"],"Mathematics":["MATH101", "Calculus I"]," Physics":["PHY101", "General Physics I"], "Chemistry":["CHEM101", "General Chemistry"], "computer Hardware":["ICT105", "hardware"]}
print("Printing whole list")
for dep, courses in departments.items():
    print(f"department {dep} has these courses registered:{courses}")

# Individual list 
print("Print individual items in list")
for dep, courses in departments.items():
    print(f"department {dep}has these courses registered:")
    for c in courses:
        print(c)
#Lecturer Assignments.
lecturer_assignments = {"Pema": ["CS101", "MATH101"], "Mr.Dorji": ["PHY101", "CHEM101"], "Dr.Tashi": ["ICT105"]}
for lecturer,courses in lecturer_assignments.items():
    print(f"{lecturer} teaches the following courses:{courses}")

#Session 6 (User input loop).
class_list = []
while True:
    student_name = input("Enter student's name (or type 'exit' to finish): ")
    if student_name.lower() == 'exit':
        break
    class_list.append(student_name)
    print(f"{student_name} has been added to the class.")

print("\nClass list:")
for student in class_list:
    print(student)

#Locate rooms that can support the number of users. 
rooms = [{"room": "101", "capacity": 15, "floor": 0, "location": "Building A"},
    {"room": "102", "capacity": 15, "floor": 0, "location": "Building A"},
    {"room": "103", "capacity": 20, "floor": 0, "location": "Building A"},
    {"room": "104", "capacity": 20, "floor": 0, "location": "Building A"}]

min_students = int(input("Enter the minimum number of seats required: "))
print("\nRooms that can support the number of students:")
for room in rooms:
    if room["capacity"] >= min_students:
        print(f"Room {room['room']} - Capacity: {room['capacity']}, Floor: {room['floor']}, Location: {room['location']}")

# Exit program loop
class_list = []

while True:
    student_name = input("Enter student's name ('quit', 'exit', or '0' to stop): ")
    if student_name.lower() in ['quit', 'exit', '0']:
        print("\nExiting program...")
        break
    class_list.append(student_name)
    print(f"{student_name} has been added to the class.")

print("\nFinal class list:")
for student in class_list:
    print(student)
print(f"Total students: {len(class_list)}")
print(f"Exit parameter: {student_name}")


#Using an active variable to control the loop
class_list = []
active = True

while active:
    student_name = input("Enter student's name ('stop' to end): ")
    if student_name.lower() == 'stop':
        active = False
    else:
        class_list.append(student_name)
        print(f"{student_name} has been added to the class.")

print("\nFinal class list:")
for student in class_list:
    print(student)
print(f"Total students: {len(class_list)}")


#Exiting when reaching max capacity using 
class_list = []
max_cap = int(input("Enter the maximum number of students allowed: "))

while True:
    if len(class_list) >= max_cap:
        print("Maximum capacity reached.")
        break
    student_name = input("Enter student's name: ")
    class_list.append(student_name)
    print(f"{student_name} has been added to the class.")

print("\nFinal class list:")
for student in class_list:
    print(student)
print(f"Total students: {len(class_list)} (Max capacity: {max_cap})")

#Infinite Loop – exit
print("Start typing (exit)...")
line_count = 0

try:
    while True:
        user_input = input()
        print(user_input)
        line_count += 1
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
    print(f"Total lines entered: {line_count}")


# END OF WORKSHEET 3. THANK YOU. 

Nar get_shapepoly()
