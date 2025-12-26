import os, subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path: str = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_path: bool = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs

        if not valid_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not target_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_path]
        if args:
            command.extend(args)
        process = subprocess.run(command,
                                 cwd=working_dir_abs,
                                 capture_output=True,
                                 text=True,
                                 timeout=30
                                 )
        output_string = ""
        if process.returncode != 0:
            output_string += f"Process exited with code {process.returncode}"
        if not process.stdout and not process.stderr:
            output_string += "No output produced"
        else:
            if process.stdout:
                output_string += f"STDOUT: {process.stdout}"
            if process.stderr:
                output_string += f"STDERR: {process.stderr}"
        return output_string

    

    except Exception as e:
        return f"Error: executing Python file: {e}"
