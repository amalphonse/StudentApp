student_list = []

def create_student():
    #ask user for student name
    # create the dictionary
    # return the dictionary
    name = input("Enter student name: ")
    student_data = {
        "name": name,
        "scores": []
    }
    return student_data

# print(create_student())
#stu = create_student()

def append_scores(student, mark):
    #Append scores to the student dictionary
    student['scores'].append(mark)

def calculate_avg(student):
    number = len(student['scores'])
    if number ==0:
        return 0
    total = sum(student['scores'])
    return total/number

#print(calculate_avg(stu))
#append_scores(stu,5)
#append_scores(stu,10)
#append_scores(stu,7)
#print(calculate_avg(stu))

def student_details(student):
    print("{}, average score: {}".format(student['name'],calculate_avg(student)
                                         ))

def print_student_list(students):
    for i,student in enumerate(students):
        print("ID {}".format(i))
        student_details(student)


def menu():
    selection = input("Enter 'p' to print student list,"
                      "'s' to add a new student to the list,"
                      "'a' to add he scores for the student,"
                      "'q' to exit.")
    while selection != 'q':
        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input("Enter the student ID to add a mark to: "))
            student = student_list[student_id]
            new_score = int(input("Enter the score for the student: "))
            append_scores(student, new_score)
        selection = input("Enter 'p' to print student list,"
                      "'s' to add a new student to the list,"
                      "'a' to add he scores for the student,"
                      "'q' to exit.")


menu()
