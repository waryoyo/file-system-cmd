import os
import shutil

def mv(source, destination):
    """
    Simulates the behavior of the 'mv' command to move or rename files/directories.

    Args:
        source (str): Path to the source file or directory.
        destination (str): Path to the destination file or directory (or new name for rename).

    Returns:
        bool: True if the operation was successful, False otherwise.
    """

    # Strip leading/trailing whitespace from arguments
    source = source.strip()
    destination = destination.strip()

    # Check if the source exists
    if not os.path.exists(source):
        print(f"Error: Source '{source}' does not exist.")
        return False

    # If destination is a directory, move source into it
    if os.path.isdir(destination):
        destination = os.path.join(destination, os.path.basename(source))

    try:
        # Use shutil.move for robust handling of moves and renames
        shutil.move(source, destination)
        print(f"'{source}' has been moved/renamed to '{destination}' successfully.")
        return True
    except FileNotFoundError:
        print(f"Error: Destination '{destination}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied while moving to '{destination}'.")
    except OSError as error:
        print(f"Error: Unable to move/rename '{source}' to '{destination}'. {error}")
    return False