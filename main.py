# Task 1: import custom module & use functions of college.py file.
print("Task 1: import custom module & use functions")
import college
student_list = ["Ali", "Sara", "Ahmed", "Fatima", "Hassan"]
college.welcome()
college.display_students(student_list)
print("Total number of students:", college.total_students(student_list))

# Task 2: Lists
print("Task 2: Lists")
# Create a list containing at least five student names.
student_list  = ["Ali", "Sara", "Ahmed", "Fatima", "Hassan"]

# Display all students.
print("student list:", student_list )

# Add one new student.
student_list .append("Zainab")
print("updated student list:", student_list )

# Remove one student.
student_list .remove("Ahmed")
print("updated student list:", student_list )

# Update one student's name.
student_list[0] = "Muhammad Ali"
# Display the updated list.
print("updated student list:",student_list)

# Display the total number of students using the custom module.
print("Total number of students:", college.total_students(student_list))

# Task 3: Tuples

print("Task 3: Tuples")

# Tuple that stores Roll Number, Department, and Semester
student_info = (230, "Computer Science", 5)

# Display each value separately using indexing.
print("Roll Number :", student_info[0])
print("Department  :", student_info[1])
print("Semester    :", student_info[2])

# Try to modify one value and observe the error.
# student_info[2] = 6
print("trying to modify the tuple (student_info[2] = 6)")
print("error ouccured")
print("Explanation:")
print("Tuples are immutable (cannot add, remove, or modify elements once the tuple is created).")

# Task 4: Sets
print("Task 4: Set")

# Create a set containing club names.Include duplicate values intentionally.
clubs = {"Sports", "Drama", "Sports", "Debate", "Cricket", "Drama"}
 
# Display the set.
# no duplicate values in the set
print("Club set:", (clubs))
 
# Add one new club.
clubs.add("Music")
print("updated club set:", (clubs))
 
# Remove one club.
clubs.remove("Debate")
print("updated club set:", (clubs))
 
# Check whether a club exists using the 'in' operator.
if "Cricket" in clubs:
    print("Cricket club exist ")
else:
    print("No Cricket club exist")

# Task 5: Final Output

print("Task 5: FINAL OUTPUT ")
# Welcome message
college.welcome()
# Student list
print("student list:", student_list)
# Total students
print("Total number of students:", college.total_students(student_list))
# Student information (Tuple)
print("Student information")
print("Roll Number :", student_info[0])
print("Department  :", student_info[1])
print("Semester    :", student_info[2])
# Club names (Set)
print("Club set:", (clubs))