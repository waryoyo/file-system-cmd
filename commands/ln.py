import os

def ln(source, link_name=None, symbolic=True):
    """Simulates the behavior of the 'ln' command to create links between files or directories.

    Args:
        source (str): The path to the source file or directory.
        link_name (str, optional): The name of the link to be created. Defaults to None, which uses the source filename.
        symbolic (bool, optional): Boolean flag indicating whether to create a symbolic link (default: True).
    """
    
    if not os.path.exists(source):
        print(f"Error: Source '{source}' does not exist.")
        return

    # If no link name is provided, use the base name of the source file
    if link_name is None:
        link_name = os.path.basename(source)

    try:
        if symbolic:
            # Create a symbolic link
            os.symlink(source, link_name)
            print(f"Symbolic link '{link_name}' created pointing to '{source}'.")
        else:
            # Hard link creation (ensure the OS supports it)
            try:
                os.link(source, link_name)
                print(f"Hard link '{link_name}' created pointing to '{source}'.")
            except OSError as error:
                print(f"Error: Unable to create a hard link. {error}")
                print("Note: Hard links may not be supported on your filesystem.")
    except OSError as error:
        print(f"Error creating link '{link_name}' to '{source}': {error}")
