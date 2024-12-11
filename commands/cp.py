import os

def cp(source, destination):
    """Simulates the behavior of the 'cp' command to copy a file.

    Args:
        source: The path to the source file.
        destination: The path to the destination file (or directory for directory copy).
    """

    # Check if the source exists
    if not os.path.exists(source):
        print(f"Error: Source file '{source}' does not exist.")
        return

    # If the source is a directory, raise an error (currently only handles files)
    if os.path.isdir(source):
        print(f"Error: Source '{source}' is a directory. Only file copying is supported.")
        return

    # Check if the destination is a directory (for copying the file into a directory)
    if os.path.isdir(destination):
        # Create a filename with the same name as the source file in the destination directory
        destination = os.path.join(destination, os.path.basename(source))

    try:
        # Open the source and destination files in binary mode
        with open(source, 'rb') as source_file, open(destination, 'wb') as dest_file:
            # Read and write the file contents in chunks for efficiency
            for data in iter(lambda: source_file.read(1024), b''):
                dest_file.write(data)
        print(f"File '{source}' copied to '{destination}' successfully.")
    except OSError as error:
        print(f"Error copying file '{source}' to '{destination}': {error}")
