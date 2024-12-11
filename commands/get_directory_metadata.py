import os
import datetime

def get_directory_metadata(dir_path):
    """Retrieves metadata about a directory.

    Args:
        dir_path: The path to the directory.

    Returns:
        A dictionary containing the following metadata:
          - num_files: Number of files in the directory.
          - num_dirs: Number of subdirectories in the directory.
          - total_size: Total size of the directory and its contents in bytes.
          - creation_time: Creation time of the directory as a datetime object.
    """

    if not os.path.exists(dir_path):
        raise FileNotFoundError(f"Directory '{dir_path}' not found.")
    
    if not os.path.isdir(dir_path):
        raise NotADirectoryError(f"'{dir_path}' is not a directory.")

    num_files, num_dirs, total_size = 0, 0, 0

    for root, dirs, files in os.walk(dir_path):
        num_files += len(files)
        num_dirs += len(dirs)
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)

    # Convert creation time to datetime object
    creation_time = datetime.datetime.fromtimestamp(os.path.getctime(dir_path))

    metadata = {
        "num_files": num_files,
        "num_dirs": num_dirs,
        "total_size": total_size,
        "creation_time": creation_time
    }

    return metadata
