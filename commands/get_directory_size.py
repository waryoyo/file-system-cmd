import os

def get_directory_size(dir_path):
    """Calculates the total size of a directory and its contents in bytes.

    Args:
        dir_path: The path to the directory.

    Returns:
        The total size of the directory in bytes.

    Raises:
        FileNotFoundError: If the directory doesn't exist.
        NotADirectoryError: If the provided path is not a directory.
    """
    if not os.path.exists(dir_path):
        raise FileNotFoundError(f"Directory '{dir_path}' not found.")
    
    if not os.path.isdir(dir_path):
        raise NotADirectoryError(f"'{dir_path}' is not a directory.")
    
    total_size = 0
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    
    return total_size
