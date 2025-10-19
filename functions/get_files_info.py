import os

def get_files_info(working_directory, directory="."):
    try:
        # normalize directory relative to working_directory
        if directory in (working_directory, os.path.basename(os.path.abspath(working_directory))):
            directory = "."
        if os.path.isabs(directory):
            # force absolute to be under working_directory by stripping leading slash
            directory = directory.lstrip(os.sep) or "."
         
        # Get full path of directory
        full_path = os.path.join(working_directory, directory)
        
        # Get absolute path
        abs_target = os.path.abspath(full_path)
        abs_working_dir = os.path.abspath(working_directory)
        
        # Check if the working directory is in the full path
        if not abs_target.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        # Check if directory argument is a directory
        if not os.path.isdir(abs_target):
            return f'Error: "{directory}" is not a directory'
        
        # Build and return a string of the contents in the directory
        list_of_dir = []
        
        for item in os.listdir(abs_target):
            joined = os.path.join(abs_target, item)
            list_of_dir.append(f"- {item}: file_size={os.path.getsize(joined)}, is_dir={os.path.isdir(joined)}")
        
        returned_string = "\n".join(list_of_dir)
        
        return returned_string
    
    except Exception as e:
        return f"Error: {e}"
    
    
    