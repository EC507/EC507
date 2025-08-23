import json
import os
import uuid
import shutil
import logging
from typing import List, Dict, Any
from common_texts.assignment_1 import common_text as common_text_a1

# Enhanced logging setup
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_assignments(file_path: str) -> List[Dict[str, Any]]:
    try:
        with open(file_path) as f:
            assignments = json.load(f)
            logger.debug(f"Loaded {len(assignments)} assignments from {file_path}")
            return assignments
    except Exception as e:
        logger.error(f"Failed to load assignments from {file_path}: {e}")
        return []

def index_students() -> List[str]:
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    folder = os.path.join(root, 'assignments')
    
    if not os.path.exists(folder):
        logger.error(f"Assignments folder does not exist: {folder}")
        return []
        
    students = [s for s in os.listdir(folder) 
               if s != "sunit" and os.path.isdir(os.path.join(folder, s))]
    logger.debug(f"Found {len(students)} students: {students}")
    return students

def place_assignment(student_id: str, assignment_name: str, content: str) -> bool:
    root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    student_folder = os.path.join(root_folder, 'assignments', student_id)
    assignment_path = os.path.join(student_folder, assignment_name)
    
    # Create student folder if it doesn't exist
    if not os.path.exists(student_folder):
        try:
            os.makedirs(student_folder)
            logger.info(f"Created student folder for {student_id}")
        except Exception as e:
            logger.error(f"Failed to create student folder for {student_id}: {e}")
            return False
    
    # Check if assignment already exists
    if os.path.exists(assignment_path):
        logger.warning(f"Assignment already exists for student {student_id}. Skipping.")
        return False
        
    try:
        with open(assignment_path, 'w', encoding='utf-8') as file:
            file.write(content)
        logger.info(f"Created new assignment for student {student_id}")
        return True
    except Exception as e:
        logger.error(f"Error placing assignment for {student_id}: {e}")
        return False

def assign_students(assignments: List[Dict], students: List[str], assignment_name: str) -> List[Dict]:
    if not assignments:
        logger.error("No assignments to process")
        return []
        
    if not students:
        logger.error("No students to assign")
        return assignments

    updated_assignments = []
    assignments_made = 0
    available_students = students.copy()
    
    logger.debug(f"Starting assignment process with {len(assignments)} assignments and {len(students)} students")
    
    for assignment in assignments:
        # Skip if already assigned
        if 'student_id' in assignment:
            logger.debug(f"Assignment already has student {assignment['student_id']}")
            updated_assignments.append(assignment)
            continue
            
        # Check if we have students left
        if not available_students:
            logger.warning("Ran out of available students")
            updated_assignments.append(assignment)
            continue
            
        # Assign to next available student
        student_id = available_students.pop(0)
        assignment['assignment_id'] = str(uuid.uuid4())
        assignment['student_id'] = student_id
        
        txt = (
            f"{common_text_a1()}\n\n\n\n"
            f"Title: {assignment.get('title', '')}\n\n"
            f"Description: {assignment.get('description', '')}\n\n"
            f"Unique ID: {assignment['assignment_id']}\n"
        )
        
        if place_assignment(student_id, assignment_name, txt):
            assignments_made += 1
            logger.debug(f"Successfully assigned to student {student_id}")
        
        updated_assignments.append(assignment)

    if assignments_made > 0:
        root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(root_folder, 'assignments_master', 'module1_c.json')
        try:
            with open(file_path, 'w') as file:
                json.dump(updated_assignments, file, indent=4)
            logger.info(f"Successfully assigned {assignments_made} new assignments")
        except Exception as e:
            logger.error(f"Failed to save assignments: {e}")
    else:
        logger.warning("No new assignments were made")

    return updated_assignments

def assignment1():
    root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_path = os.path.join(root_folder, 'assignments_master', 'module1_c.json')
    source_path = os.path.join(root_folder, 'assignments_master', 'module1.json')
    
    # Verify source file exists
    if not os.path.exists(source_path):
        logger.error(f"Source file does not exist: {source_path}")
        return
    
    # Create tracking file if needed
    if not os.path.exists(target_path):
        try:
            shutil.copy(source_path, target_path)
            logger.info("Created new assignments tracking file")
        except Exception as e:
            logger.error(f"Failed to create tracking file: {e}")
            return
    
    assignments = load_assignments(target_path)
    if not assignments:
        return
        
    students = index_students()
    if not students:
        return
        
    assign_students(assignments, students, "assignment1")

if __name__ == "__main__":
    assignment1()