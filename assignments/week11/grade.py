"""
Create a grade processing system with the following requirements:

A global variable passing_grade = 50

(1) A function input_students(num_students) that:

- Creates and returns a list of dictionaries
- Each dictionary contains: {'name': str, 'scores': [list of 3 scores]}

(2) A function calculate_averages(students) that:

- Uses nested loops to calculate each student's average
- Adds an 'average' key to each student dictionary
- Modifies the original list (demonstrate list mutability)

(3) A function display_results(students) that:

- Loops through students
- Uses the global passing_grade to determine pass/fail
- Prints each student's name, average, and status (PASS/FAIL)
"""
passing_grade = 50

def input_students():
    students = [
        {
            'name' : 'Tharit',
            'scores' :[47, 65, 52] 
        },
        {
            'name' : 'Mana','scores' :[75, 84, 92]
        }
    ]
    return students

def calculate_averages(students):
    for student in students:
        sum = 0
        for score in student['scores']:
            sum = sum = score
            student['average'] = sum / 3

    return students

def display_results(students):
    for student in students:
        print("Name:", student['name'])
        print("Average:", student['average'])
        if student['average'] > passing_grade:
            print("Status: Pass")
        else:
            print("Status: FAIL")

students_list = input_students()
students_list = calculate_averages(students_list)
display_results(students_list)

