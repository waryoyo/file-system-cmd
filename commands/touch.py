import os
import time

def execute(arg):
    # Remove leading/trailing spaces from the argument
    arg = arg.strip()   

    # Check if the argument is empty (no file name provided)
    if not arg:
        print("Error: Missing file name. Usage: touch <file_name>")
        return   

    try:
        # Check if the file already exists
        if os.path.exists(arg):
            # Update the file's access and modification timestamps
            os.utime(arg, None)
            print(f"File '{arg}' modified successfully (timestamp updated).")
        else:
            # If file doesn't exist, create it in append mode (so it won't overwrite existing content)
            with open(arg, 'a'):
                # Update the timestamps to the current time
                os.utime(arg, None)
            print(f"File '{arg}' created and timestamp set.")
    
    except OSError as e:
        # Handle any OS-related errors and print a message
        print(f"Error: Unable to create or modify file '{arg}'. {e}")
