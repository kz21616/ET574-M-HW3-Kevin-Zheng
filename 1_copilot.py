# list of three students named Jon, Kim and Lee
students = ["Jon", "Kim", "Lee"]

# add two more students after the list was created
students.append("Sara")
students.append("Miko")

# function to print ‘Hi name’ for each student in the list
# and then report how many students there are
def greet_students(student_list):
    for student in student_list:
        print(f"Hi {student}!")
    print(f"Total students: {len(student_list)}")

# call the function
greet_students(students)