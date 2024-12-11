import os

def rename_directory(dir_path, new_name):
    """Renames a directory.

    Args:
        dir_path: The path to the directory to be renamed.
        new_name: The new name for the directory.

    Returns:
        True if the rename was successful, False otherwise.
    """

    try:
        # Get the parent directory where the directory is located
        parent_dir = os.path.dirname(dir_path)

        # Create the full path for the new directory name
        new_dir_path = os.path.join(parent_dir, new_name)

        # Check if the new directory name already exists
        if os.path.exists(new_dir_path):
            print(f"Error: A directory named '{new_name}' already exists.")
            return False

        # Rename the directory
        os.rename(dir_path, new_dir_path)
        return True

    except OSError as error:
        print(f"Error renaming directory: {error}")
        return False
    
if rename_directory(old_dir_name, new_dir_name): # type: ignore
    print("Directory renamed successfully.")
else:
    print("Directory renaming failed.")
