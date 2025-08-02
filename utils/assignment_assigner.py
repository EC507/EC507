import json
import random
import os

def load_assignments(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        random.shuffle(data)
        return data

def index_students():
    students = []
    root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assignment_folder = os.path.join(root_folder, 'assignments')
    for student in os.listdir(assignment_folder):
        if student!="sunit":
            student_path = os.path.join(assignment_folder, student)
            if os.path.isdir(student_path):
                students.append(student)
    return students

def assign_random_students(assignments, students):
    for a_id in range(len(assignments)):
        print(assignments[a_id])

    # for assignment in assignments:
    #     assignment['students'] = random.sample(students, k=min(len(students), assignment['max_students']))
    # return assignments

def assignment1():
    root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(root_folder, 'assignments_master', 'module1.json')
    assignments = load_assignments(file_path)
    students = index_students()
    assign_random_students(assignments, students)
    print(assignments)

    # students = [...]  # Load or define your list of students
    # assigned = assign_random_students(assignments, students)
    # print(assigned)


assignment1()