import os
from .config import *

def write_file(working_directory, file_path, content):
    try:
        # Get full path of file
        full_path = os.path.join(working_directory, file_path)
            
        # Get absolute path
        abs_target = os.path.abspath(full_path)
        abs_working_dir = os.path.abspath(working_directory)
            
        # Check if the working directory is in the file path
        if not abs_target.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        # Check if file_path is not a file, If file path doesn't exist, write it.:
        if not os.path.isfile(abs_target):
            with open(abs_target, "w") as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

        # Overwrite contents of the file with the contents argument.
        with open(abs_target, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
            
    except Exception as e:
        return f"Error: {e}"
    