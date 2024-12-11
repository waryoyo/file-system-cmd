import os
import stat
import datetime

def get_file_metadata(file_path):
    """Retrieves metadata about a file or directory.

    Args:
        file_path: The path to the file or directory.

    Returns:
        A dictionary containing the following metadata:
          - file_size: File size in bytes.
          - creation_time: Creation time as a datetime object.
          - modification_time: Modification time as a datetime object.
          - permissions: File permissions in octal format (e.g., '0755').
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")

    stat_info = os.stat(file_path)

    # Convert timestamps to datetime objects
    creation_time = datetime.datetime.fromtimestamp(stat_info.st_ctime)
    modification_time = datetime.datetime.fromtimestamp(stat_info.st_mtime)

    # Get file permissions in octal format
    permissions = oct(stat_info.st_mode & 0o777)  # Mask to get just the permission bits

    metadata = {
        "file_size": stat_info.st_size,
        "creation_time": creation_time,
        "modification_time": modification_time,
        "permissions": permissions
    }

    return metadata
