import os
from .config import *

def get_file_content(working_directory, file_path):
    try:
        # Get full path of file
        full_path = os.path.join(working_directory, file_path)
        
        # Get absolute path
        abs_target = os.path.abspath(full_path)
        abs_working_dir = os.path.abspath(working_directory)
        
        # Check if the working directory is in the file path
        if not abs_target.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        # Check if file_path is not a file:
        if not os.path.isfile(abs_target):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        # Read file and return contents as string with max 10000 characters
        with open(abs_target, 'r') as f:
            file_content_string = f.read(MAX_CHARS) + (f'...File "{file_path}" truncated at 10,000 characters')
        
        # Return the string
        return file_content_string
        
    except Exception as e:
        return f"Error: {e}"