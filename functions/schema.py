import os
from google.genai import types

# for get_files_info
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

# for get_files_content
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads file and returns content as a string with a max of 10000 characters",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file which your trying to read and return as a string"
            ),
        },
    ),
)

# for write_file
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Checks if a file exists, and if it doesnt it creates the fool at the file path and then puts the content in, if it does it overwrites the file with content",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file which your trying to overwrite or creat"
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content which your writing into the file"
            )
        },
    ),
)

# run_python_file
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file using the command line, by putting the working directory, file path and args which is whats written in the command line",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file which your trying to run"
            ),
        },
    ),
)
