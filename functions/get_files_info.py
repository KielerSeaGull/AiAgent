import os
from google.genai import types


def get_files_info(working_directory, directory=".") -> str:
    working_dir_abs: str = os.path.abspath(working_directory)
    target_dir: str = os.path.normpath(os.path.join(working_dir_abs, directory))
    valid_target_dir: bool = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    file_infos: list = []
    try:
        with os.scandir(target_dir) as dir:
            for entry in dir:
                formatted_file_info: str = f'- {entry.name}: file_size={entry.stat().st_size} bytes, is_dir={entry.is_dir()}'
                file_infos.append(formatted_file_info)

        return '\n'.join(file_infos)
    except:
        return "Error: Scandir(target_dir) doesn't work"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)