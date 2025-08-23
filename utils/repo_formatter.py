import os
import argparse
from pathlib import Path

def lowercase_folders(path: str) -> None:
    """
    Rename all folders in the given path to lowercase.
    
    Args:
        path: Directory path to process
    """
    try:
        root_path = Path(path)
        if not root_path.is_dir():
            raise NotADirectoryError(f"'{path}' is not a directory")

        # Get all folders and sort in reverse to avoid renaming conflicts
        folders = [f for f in root_path.iterdir() if f.is_dir()]
        folders.sort(reverse=True)
        
        processed = 0
        for folder in folders:
            new_name = folder.name.lower()
            new_path = folder.parent / new_name

            # Compare actual string values instead of paths
            if folder.name != new_name:
                try:
                    # Use a temporary name first to handle case-sensitive renaming on Windows
                    temp_path = folder.parent / (folder.name + "_temp")
                    folder.rename(temp_path)
                    temp_path.rename(new_path)
                    processed += 1
                    print(f"Renamed '{folder.name}' to '{new_name}'")
                except OSError as e:
                    print(f"Error renaming '{folder.name}': {e}")

        print(f"Total folders processed: {processed}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    folder_name = os.path.dirname(__file__)
    root_folder = os.path.dirname(folder_name)
    assignments_folder = os.path.join(root_folder, 'assignments')
    print(assignments_folder)
    lowercase_folders(assignments_folder)