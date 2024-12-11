import os

def chmod(path, mode, recursive=False):
    """Simulates the behavior of the 'chmod' command to change file/directory permissions.

    Args:
        path (str): The path to the file or directory whose permissions need to be changed.
        mode (str): An octal string representing the desired permissions (e.g., '0755').
        recursive (bool, optional): If True, changes permissions recursively for directories. Defaults to False.

    Returns:
        bool: True if the permissions were changed successfully, False otherwise.
    """
    try:
        # Convert octal string to integer for permission setting
        permission_mode = int(mode, 8)

        if recursive and os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for item in dirs + files:
                    os.chmod(os.path.join(root, item), permission_mode)
            print(f"Permissions for '{path}' and its contents changed to '{mode}' recursively.")
        else:
            os.chmod(path, permission_mode)
            print(f"Permissions for '{path}' changed to '{mode}'.")
        return True

    except (ValueError, OSError) as error:
        print(f"Error changing permissions for '{path}': {error}")
        return False
    