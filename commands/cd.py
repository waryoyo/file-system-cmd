import os

def cd(path=None):
    """
    Simulates the behavior of the 'cd' command, with support for home directory fallback.

    Args:
        path (str, optional): The target directory to change to. Defaults to None.

    Behavior:
        - If `path` is None or empty, defaults to the user's home directory.
        - Prints meaningful messages for successful changes or errors.
    """
    # Default to the user's home directory if no path is provided
    if not path or not path.strip():
        path = os.path.expanduser("~")  # Get the user's home directory

    try:
        # Attempt to change the current working directory
        os.chdir(path)
        print(f"Directory successfully changed to: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Error: Directory '{path}' does not exist.")
    except NotADirectoryError:
        print(f"Error: '{path}' is not a directory.")
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
    except OSError as error:
        print(f"Error changing directory to '{path}': {error}")

