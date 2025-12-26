import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        work_dir_abs: str = os.path.abspath(working_directory)
        target_file_path: str = os.path.normpath(os.path.join(work_dir_abs, file_path))

        valid_path: bool = os.path.commonpath([work_dir_abs, target_file_path]) == work_dir_abs
        if not valid_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        
        with open(target_file_path, "r") as f:
            file_content: str = f.read(MAX_CHARS)
            #reads 1 Element after the first MAX_CHARS elements
            if f.read(1):
                file_content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        
        return file_content

    except Exception as e:
        return f"Error: {e}"
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Retrieves the content (at most {MAX_CHARS} characters) of a specified file within the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory",
            ),
        },
        required=["file_path"],
    ),
)


    




