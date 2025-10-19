from google.genai import types
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file
import os

def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    function_args = function_call_part.args
    
    # if verbose is true, print function name and args, else just print the name
    if verbose == True:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")
    
    # Based on the name, call the function and capture the result.
    functions = {"get_file_content": get_file_content, "get_files_info": get_files_info, "run_python_file": run_python_file,"write_file": write_file}
    copy_function_args = function_call_part.args.copy()
    copy_function_args["working_directory"] = "./calculator"
    
    
    fn = functions.get(function_name)
    
    # If name not found explain the error
    if fn is None:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
        
    # If name found call function and return result with a description.
    else:
        result = fn(**copy_function_args)
        
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": result},
                )
            ],
        )
    
    
