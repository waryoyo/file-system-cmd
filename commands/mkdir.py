import os
import shutil

def execute(arg, edit_dir=None):
    """Simulates the behavior of the 'mkdir' command to create a directory or edit an existing one.

    Args:
        arg (str): The name or path of the directory to create.
        edit_dir (str, optional): New name or path to rename or move the directory.
    """
    # Strip leading/trailing whitespace from the arguments
    arg = arg.strip()
    if edit_dir:
        edit_dir = edit_dir.strip()

    # Check if the directory name is provided
    if not arg:
        print("Error: Missing directory name. Usage: mkdir <directory_name>")
        return

    try:
        if edit_dir:
            # Edit (rename or move) the directory
            if not os.path.exists(arg):
                print(f"Error: Source directory '{arg}' does not exist.")
                return
            shutil.move(arg, edit_dir)
            print(f"Directory '{arg}' renamed/moved to '{edit_dir}' successfully.")
        else:
            # Create the directory
            os.makedirs(arg, exist_ok=True)
            print(f"Directory '{arg}' created successfully.")
    except OSError as e:
        # Handle OS-related errors (e.g., permission issues, invalid characters)
        print(f"Error: Unable to process directory '{arg}'. {e}")
