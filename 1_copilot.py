#list of three students named Jon, Kim and Lee

students = ['Jon', 'Kim', 'Lee']

# change Jon to John

students[0] = 'John'    

# add two more students after initial creation

students.append('Sara')
students.append('Miko')


#function to print ‘Hi name’ for each student in the list

def greet_students(students):
    for student in students:
        print(f"Hi {student}")

    # print total count
    
    print(f"Total students: {len(students)}")

#call the function

greet_students(students)