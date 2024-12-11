import os

def rm(file_path, force=False, interactive=False):
    """Simulates the behavior of the 'rm' command to remove a file or directory.

    Args:
        file_path: The path to the file or directory to be removed.
        force (optional): If True, removes the file or directory without prompting for confirmation. Defaults to False.
        interactive (optional): If True, prompts the user for confirmation before removing the file or directory. Defaults to False.
    """

    # Check if the file or directory exists
    if not os.path.exists(file_path):
        print(f"Error: '{file_path}' does not exist.")
        return

    # Handle interactive confirmation (prompt the user before removal)
    if interactive:
        confirmation = input(f"Are you sure you want to remove '{file_path}' (y/N)? ")
        if confirmation.lower() != 'y':
            print("Removal canceled.")
            return

    # Handle standard confirmation (if not forced or interactive)
    if not force and not interactive:
        print(f"Warning: This will permanently remove '{file_path}'. Are you sure? (y/N)")
        confirmation = input().lower()
        if confirmation != 'y':
            print("Removal canceled.")
            return

    # Try to remove the file or directory
    try:
        if os.path.isfile(file_path):  # If it's a file, remove it
            os.remove(file_path)
            print(f"File '{file_path}' removed successfully.")
        elif os.path.isdir(file_path):  # If it's a directory, remove it (only if empty)
            os.rmdir(file_path)
            print(f"Directory '{file_path}' removed successfully.")
        else:
            print(f"Error: '{file_path}' is neither a file nor an empty directory.")
    except OSError as error:
        print(f"Error removing '{file_path}': {error}")

