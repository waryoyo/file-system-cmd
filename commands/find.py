import os
import fnmatch

def find(path=".", name=None, file_type=None, max_depth=None, print_results=True):
    """Simulates the behavior of the 'find' command to search for files and directories.

    Args:
        path (str): The root directory to start the search from (default: current directory).
        name (str, optional): The name or pattern of the file/directory to search for (supports wildcards like '*').
        file_type (str, optional): The type of file to search for ('f' for files, 'd' for directories).
        max_depth (int, optional): The maximum depth of the search (default: unlimited).
        print_results (bool): If True, prints the results to the console. Defaults to True.

    Returns:
        List[str]: A list of paths matching the search criteria.
    """
    if not os.path.exists(path):
        print(f"Error: Path '{path}' does not exist.")
        return []

    matches = []

    def is_depth_exceeded(current_path, root_path):
        if max_depth is None:
            return False
        return os.path.relpath(current_path, root_path).count(os.sep) >= max_depth

    for root, dirs, files in os.walk(path):
        if is_depth_exceeded(root, path):
            dirs[:] = []

        items = []
        if file_type == "f":
            items = files
        elif file_type == "d":
            items = dirs
        else:
            items = files + dirs

        for item in items:
            if name is None or fnmatch.fnmatch(item, name):
                matches.append(os.path.join(root, item))

    if print_results:
        for match in matches:
            print(match)

    return matches