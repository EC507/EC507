import os
import argparse

def lowercase_folders(path):
    # Example Usage: python repo_formatter.py lowercase_folders ../assignments/
    count = 0
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    # Sort in reverse to avoid issues with renaming
    for folder in sorted(folders, reverse=True):
        count += 1
        full_path = os.path.join(path, folder)
        new_name = folder.lower()
        new_full_path = os.path.join(path, new_name)
        if new_full_path != full_path:
            if os.path.exists(new_full_path):
                print(f"Skipping '{folder}' because '{new_name}' already exists.")
                continue
            os.rename(full_path, new_full_path)
    print(f"Total folders processed: {count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a function on a folder")
    parser.add_argument("function", help="Function name to run")
    parser.add_argument("path", help="Path to folder")
    args = parser.parse_args()

    # Map function names to actual functions
    functions = {
        "lowercase_folders": lowercase_folders,
        # Add more mappings here if you add more functions
    }

    if args.function in functions:
        functions[args.function](args.path)
    else:
        print(f"Function '{args.function}' not found. Available: {list(functions.keys())}")

