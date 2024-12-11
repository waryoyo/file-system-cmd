import os
import time

def tail(file_path, num_lines=10, follow=False):
    """Simulates the behavior of the 'tail' command to display the last lines of a file.
    
    Args:
        file_path (str): The path to the file to read from.
        num_lines (int, optional): The number of lines to display (default: 10).
        follow (bool, optional): If True, follows the file for new content (default: False).
    """

    try:
        with open(file_path, 'r') as file:
            # Get file size for follow functionality (only needed for follow mode)
            file_size = os.path.getsize(file_path)

            # Read and store desired number of lines from the end
            lines = file.readlines()[-num_lines:]

            # Print the last lines
            print("".join(lines))

            # Follow the file for new content if follow=True
            if follow:
                print("\nFollowing the file for new content...")
                file.seek(file_size, os.SEEK_SET)  # Seek to the end of the file
                while True:
                    line = file.readline()
                    if not line:
                        time.sleep(0.1)  # Sleep briefly to avoid 100% CPU usage when waiting for new lines
                        continue  # Wait for new content to be appended
                    print(line, end='')  # Print line without extra newline
                    os.fsync(file.fileno())  # Flush output to ensure visibility

    except OSError as error:
        print(f"Error reading file '{file_path}': {error}")