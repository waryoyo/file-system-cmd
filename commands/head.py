import os


def head(file_path, num_lines=5):
    """
    Simulates the behavior of the 'head' command to display the first lines of a file.

    Args:
        file_path (str): The path to the file to read from.
        num_lines (int, optional): The number of lines to display (default: 5).
    """
    if num_lines <= 0:
        print("Error: Number of lines must be greater than 0.")
        return

    # Check if file exists before proceeding
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return

    try:
        with open(file_path, 'r') as file:
            print(f"--- First {num_lines} lines of '{file_path}' ---")
            for i, line in enumerate(file):
                if i >= num_lines:  # Stop after printing the required number of lines
                    break
                print(line, end='')  # Print lines without adding extra newlines
    except PermissionError:
        print(f"Error: Permission denied for reading the file '{file_path}'.")
    except Exception as error:
        print(f"Error reading file '{file_path}': {error}")
