import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        # Get full path of file
        full_path = os.path.join(working_directory, file_path)
        
        # Get absolute path
        abs_target = os.path.abspath(full_path)
        abs_working_dir = os.path.abspath(working_directory)
        
        # Check if the working directory is in the file path
        if not abs_target.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        # Check if file_path is not a file:
        if not os.path.isfile(abs_target):
            return f'Error: File "{file_path}" not found.'
        
        # Check if file ends with .py
        if not abs_target.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'

        # Use subprocess.run to execute the python file.
        init_args = ['python3', f'{abs_target}']
        # if args provided
        if args:
            init_args += args
        
        completed_process = subprocess.run(init_args, timeout=30, capture_output=True,cwd=abs_working_dir)
        
        # Return a string
        stdout = completed_process.stdout.decode("utf-8")
        stderr = completed_process.stderr.decode("utf-8")
        
        return_string = f"STDOUT: {stdout}\nSTDERR: {stderr}\n"
        
        # If the process exits with a non-zero code, include "Process exited with code X"
        if completed_process.returncode != 0:
            return_string += f'Process exited with code {completed_process.returncode}'
            
        # If no output is produced.
        #if not completed_process.stdout.strip():
        #    return "No output produced"
        
        return return_string
        
        
    except Exception as e:
        return f"Error: {e}"