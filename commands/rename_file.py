import os

def rename_file(file_path, new_name):
    """Renames a file.

    Args:
        file_path: The path to the file to be renamed.
        new_name: The new name for the file.

    Returns:
        True if the rename was successful, False otherwise.
    """

    try:
        # Get the directory of the file to be renamed
        dir_path = os.path.dirname(file_path)

        # Create the new full file path
        new_file_path = os.path.join(dir_path, new_name)

        # Check if the new file already exists
        if os.path.exists(new_file_path):
            print(f"Error: A file named '{new_name}' already exists.")
            return False

        # Rename the file
        os.rename(file_path, new_file_path)
        return True

    except OSError as error:
        print(f"Error renaming file: {error}")
        return False
        
if rename_file(old_name, new_name): # type: ignore
    print("File renamed successfully.")
else:
    print("File renaming failed.")
