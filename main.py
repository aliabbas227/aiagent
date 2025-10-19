import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.schema import schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file
from call_function import call_function
import sys

def main():
    # Get info from dotenv
    load_dotenv()                   
    api_key = os.environ.get("GEMINI_API_KEY")
    
    # Creates the client using your api key
    client = genai.Client(api_key=api_key)
    
    # Checks if there is an input in the command line
    if len(sys.argv) == 1:
        print("Error, no prompt was written.")
        sys.exit(1)
        
    # Creates list of message to keep for conversation.
    user_prompt = sys.argv[1]
    verbose = "--verbose" in sys.argv
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]
    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, go through the process and when your done, respond with a "Final response:" explaining the answer.

You can perform the following operations:
- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths must be relative to the working directory. Do not specify the working directory in function calls; it is injected automatically.

If there is a missing directory instead of None put a '.'

Only print the result of the functions after you've finished the entire process
"""
    
    # Create available functions using type.tool
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file
        ]
    )
    
    # Generates a response using the client.
    try:
        for i in range(0, 20): 
            response = client.models.generate_content(
                model='gemini-2.0-flash-001', contents=messages, config=types.GenerateContentConfig(tools= [available_functions], system_instruction=system_prompt)
            )

            if response.candidates:
                for candidate in response.candidates:
                    messages.append(candidate.content)
            
            if response.function_calls:
                for fc in response.function_calls:
                    result = call_function(fc, verbose=verbose)
                    fr = result.parts[0].function_response.response
                    
                    calls = types.Content(role= "user", parts= [types.Part(function_response= result.parts[0].function_response)], )
                    messages.append(calls)
                    
                    if not fr:
                        raise Exception("IDK")                    
        
            if "Final response:" in response.text:
                print(response.text)
                break
              
    except Exception as e:
        print(f"Error {e}")
    
    
    # Print tokens is --verbose is added
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    
    
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")


if __name__ == "__main__":
    main()
