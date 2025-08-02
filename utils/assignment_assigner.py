import json
import random
import os
import uuid
import shutil
from common_texts.assignment_1 import common_text as common_text_a1


def load_assignments(file_path):
    with open(file_path) as f:
        return json.load(f)
    
def index_students():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    folder = os.path.join(root, 'assignments')
    return [s for s in os.listdir(folder) if s != "sunit" and os.path.isdir(os.path.join(folder, s))]

def place_assignment(student_id, assignment_name, content):
    root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    student_folder = os.path.join(root_folder, 'assignments', student_id)
    assignment_path = os.path.join(student_folder, assignment_name)
    try:
        with open(assignment_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"Error placing assignment for {student_id}: {e}")

def assign_students(assignments, students, assignment_name):
    updated_assignments = []
    for a_id, assignment in enumerate(assignments):
        if a_id < len(students) and 'student_id' not in assignment.keys():
            assignment['assignment_id'] = str(uuid.uuid4())
            assignment['student_id'] = students[a_id]
            txt = (
                f"{common_text_a1()}\n\n\n\n"
                f"Title: {assignment.get('title', '')}\n\n"
                f"Description: {assignment.get('description', '')}\n\n"
                f"Unique ID: {assignment['assignment_id']}\n"
            )
            place_assignment(assignment['student_id'], assignment_name, txt)
        updated_assignments.append(assignment)
    root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(root_folder, 'assignments_master', 'module1_c.json')
    with open(file_path, 'w') as file:
        json.dump(updated_assignments, file, indent=4)

def assignment1():
    # Copy the editable assignment file if it doesn't exist
    root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if not os.path.exists(os.path.join(root_folder, 'module1_c.json')):
        shutil.copy(os.path.join(root_folder, 'assignments_master', 'module1.json'), 
                    os.path.join(root_folder, 'assignments_master', 'module1_c.json'))
    
    file_path = os.path.join(root_folder, 'assignments_master', 'module1_c.json')
    
    assignments = load_assignments(file_path)
    
    students = index_students()

    assign_students(assignments, students, "assignment1")

    # # print(assignments)

    # students = [...]  # Load or define your list of students
    # assigned = assign_random_students(assignments, students)
    # print(assigned)


assignment1()