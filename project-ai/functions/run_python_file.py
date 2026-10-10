import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Execute a python file ",
        "parameters": {
            "required": ["file_path"],
            "type": "object",
            "properties": {
                "args": {
                    "type":"array",
                    "description":"optional command line arguments for Python file",
                    "items":{
                        "type":"string",
                    }
                },
                "file_path": {
                    "type": "string",
                    "description": "The path to the file to execute ",
                },
            },
        },
    },
}
def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:

    try:
        target_path = os.path.abspath(os.path.join(working_directory, file_path))
        working_path = os.path.abspath(working_directory)
        if os.path.commonpath([working_path,target_path]) != working_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path) :
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_path]
        if args:
            command.extend(args)

        result = subprocess.run(
            command,
            cwd=working_path,
            capture_output=True,
            text=True,
            timeout=30,
        )
        output = ""
        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}\n"
        if result.stdout:
            output += f"STDOUT:\n{result.stdout}"
        if result.stderr:
            output += f"STDERR:\n{result.stderr}"
        if not result.stdout and not result.stderr:
            output += "No output produced"
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"