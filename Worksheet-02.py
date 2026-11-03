'''
#Worksheet-2 Sessions-3
#Lists
#Lists - basic
units = ["Introduction to Programming", "Calculus I", "Data Structures and Algorithms", "Linear Algebra", "Physics I", "Chemistry I", "Bloggy I", "Microeconomics", "Macroeconomics", "Psychology I", "History I", "English Composition I", "Introduction to Philosophy", "Calculus II", "Discrete Mathematics"]
print(units) 

'''

#List-sorted-Permanent sorting
units = ["Introduction to Programming", "Calculus I", "Data Structures and Algorithms", "Linear Algebra", "Physics I", "Chemistry I", "Bloggy I", "Microeconomics", "Macroeconomics", "Psychology I", "History I", "English Composition I", "Introduction to Philosophy", "Calculus II", "Discrete Mathematics"]
units.sort()
print(units) 

'''
#Temporary sorting
units = ["Introduction to Programming", "Calculus I", "Data Structures and Algorithms", "Linear Algebra", "Physics I", "Chemistry I", "Bloggy I", "Microeconomics", "Macroeconomics", "Psychology I", "History I", "English Composition I", "Introduction to Philosophy", "Calculus II", "Discrete Mathematics"]
units.sort()
units=sorted(units)
print(units)

3. Lists - reverse() 
# list-reverse-Permanent sorting
units = ["Introduction to Programming", "Calculus I", "Data Structures and Algorithms", "Linear Algebra", "Physics I", "Chemistry I", "Bloggy I", "Microeconomics", "Macroeconomics", "Psychology I", "History I", "English Composition I", "Introduction to Philosophy", "Calculus II", "Discrete Mathematics"]
units.sort()
units.sort(reverse=True)
print(units)

# list-reverse-Temporary sorting
units = ["Introduction to Programming", "Calculus I", "Data Structures and Algorithms", "Linear Algebra", "Physics I", "Chemistry I", "Bloggy I", "Microeconomics", "Macroeconomics", "Psychology I", "History I", "English Composition I", "Introduction to Philosophy", "Calculus II", "Discrete Mathematics"]
units.sort()
units=sorted(units,reverse=True)
print(units)


#Lists - sort() 
#Lists-Create useable coding(1.1) 

units. sort()
print(units)

print("The following courses are available for expression of interest if the students meet the prerequisites:")

#1.2 Remove the  2nd course from the list?
units = ["Introduction to Programming", "Calculus I", "Data Structures and Algorithms", "Linear Algebra", "Physics I", "Chemistry I", "Bloggy I", "Microeconomics", "Macroeconomics", "Psychology I", "History I", "English Composition I", "Introduction to Philosophy", "Calculus II", "Discrete Mathematics"]
units.sort()
del units[2]
print(“After del:”,units)

#Message announcement after removing one of the course from the list?

print(“Dear student the course title Data Structures and Algorithms is replace by a new course”)

#Replace with New course in the list?
units = ["Introduction to Programming", "Calculus I", "Data Structures and Algorithms", "Linear Algebra", "Physics I", "Chemistry I", "Bloggy I", "Microeconomics", "Macroeconomics", "Psychology I", "History I", "English Composition I", "Introduction to Philosophy", "Calculus II", "Discrete Mathematics"]
units.sort()
units.insert(2,"Nurshing")
print(units)

#Print the messages showing both the original course and the new course, with a message to confirm the withdrawn course and new course. 

print(“Original units:”,units)

#3. Three new courses added to the list?
units = ["Introduction to Programming", "Calculus I", "Data Structures and Algorithms", "Linear Algebra", "Physics I", "Chemistry I", "Bloggy I", "Microeconomics", "Macroeconomics", "Psychology I", "History I", "English Composition I", "Introduction to Philosophy", "Calculus II", "Discrete Mathematics"]
units.sort()
units.insert(0,"apple")
print(units)

units.insert(6,"orange")
print(units)

units.append(“Banana”)
print(units)

print(“Dear student Available courses for this semester are apple,orange and Banana 
due to technical and room availability issues ”)

#4. Use pop() to remove four courses from your list one at a time. 
units = ["Introduction to Programming", "Calculus I", "Data Structures and Algorithms", "Linear Algebra", "Physics I", "Chemistry I", "Bloggy I", "Microeconomics", "Macroeconomics", "Psychology I", "History I", "English Composition I", "Introduction to Philosophy", "Calculus II", "Discrete Mathematics"]
units.sort()
units= units.pop(7)
print("After pop:", units)
print("Popped item:", units)


#Tuples and Loops 
units=[(1, "Introduction to Programming"),(2, "Calculus I"), (3, "Data Structures and Algorithms"),(4, "Linear Algebra"),(5, "Physics I")]
units_names=[]
units_id=[]
print("Unit List:")
print()

for unit in units:
    unit_id, unit_name = unit
    print("ID ,Course Name")
    
    print(f"{unit_id:},{unit_name}")
    print()

#Session-4

#1 A .List of Departments 

departments = [[1, “Computer Science”],[2, “Mathematics”],[3, “Computer Science”],[4,”Mathematics”], [5, “Physics”],[6, “Chemistry”], [7, “Biology”],[8, “Economics”],[9,”Economics”], [10, “Psychology”],[11, “History”],[12, “English”], [13, “Philosophy”], [14, “Mathematics”], [15, “Computer Science”]]

#B. Loops 

while True:
    num=input(“Enter course_id, quit or 0”)
    if(num== “quit” or num== “0”):
        exit()
        
    else:
            print(num)
#C. Conditional statements 

while True:
    num=input("Enter course_ID, quit or 0")
    if (int(num)==courses[0]):
        print(courses[1])
        var=True
        break
    else:
        break
if (var==False):
    print(f"courses with id {num} not found")

#D.Search for department

while True:
    num = input("Enter a course ID (1–15) quit or 0")

    if num.lower() == "quit" or num == "0":
        print("Course ID is out of range (1-15), try again.")
        break

    if not num.isdigit():
        print(f"The value '{num}' has been used to exit.")
        break

    course_id = int(num)

    if 1 <= course_id <= 15:
        found = False
        for course in departments:
            if course[0] == course_id:
                print(f"Course ID {course_id} is in the {course[1]} department.")
                found = True
                break
        if not found:
            print("Course ID not found in the list.")
        break

    else:
        print(f"The value '{course_id}' has been used to exit.")
        break

#2. Creating a Course Information Retrieval System 

courses = [[1, "Introduction to Programming", "Computer Science", "None"],
[2, "Calculus I", "Mathematics", "None"],
[3, "Data Structures and Algorithms", "Computer Science", "Introduction to Programming"],
[4, "Linear Algebra", "Mathematics", "None"],
[5, "Physics I", "Physics", "None"],
[6, "Chemistry I", "Chemistry", "None"],
[7, "Biology I", "Biology", "None"],
[8, "Microeconomics", "Economics", "None"],
[9, "Macroeconomics", "Economics", "Microeconomics"],
[10, "Psychology I", "Psychology", "None"],
[11, "History I", "History", "None"],
[12, "English Composition I", "English", "None"],
[13, "Introduction to Philosophy", "Philosophy", "None"],
[14, "Calculus II", "Mathematics", "Calculus I"],
[15, "Discrete Mathematics", "Computer Science", "Introduction to Programming"]]


def retrieve_course_info(course_id):
    for course in courses:
        if course[0] == course_id:
            return course  
    return None 

while True:
    num= input("Enter a course ID (1-15) to retrieve course information")

    if num.lower() == "quit" or num == "0":
        print("Exiting the program. Goodbye!")
        break

    if not num.isdigit():
        print(f"The value '{num}' is invalid.enter a number between 1 and 15.")
        continue

    course_id = int(num)

    if 1 <= course_id <= 15:
        course_info = retrieve_course_info(course_id)
        if course_info:
            
            print(f"Course ID: {course_info[0]}")
            print(f"Course Name: {course_info[1]}")
            print(f"Department: {course_info[2]}")
            print(f"Prerequisites: {course_info[3]}")
        else:
            print(f"Course ID {course_id} not found.")
    else:
        print(f"Course ID {course_id} is out of range. Please enter a valid ID between 1 and 15.")

'''