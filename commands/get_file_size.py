import os

class FileNotFoundErrorCustom(Exception):
    """Custom exception for when the file is not found."""
    pass

def get_file_size(file_path: str) -> int:
    """Retrieves the size of a file in bytes.

    Args:
        file_path (str): The path to the file.

    Returns:
        int: The size of the file in bytes.

    Raises:
        FileNotFoundErrorCustom: If the file does not exist.
        IsADirectoryError: If the path is a directory, not a file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundErrorCustom(f"Error: File '{file_path}' not found.")
    
    if os.path.isdir(file_path):
        raise IsADirectoryError(f"Error: '{file_path}' is a directory, not a file.")

    return os.path.getsize(file_path)
