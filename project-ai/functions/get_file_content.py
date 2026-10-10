import os
from config import MAX_CHARS

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads the content of a file ",
        "parameters": {
            "required": ["file_path"],
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path to the file to read ",
                },
            },
        },
    },
}

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        target_path = os.path.abspath(os.path.join(working_directory, file_path))
        working_path = os.path.abspath(working_directory)
        if os.path.commonpath([working_path,target_path]) != working_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(target_path,"r") as f:
            content = f.read(MAX_CHARS)
            extra = f.read(1)
            if extra != "":
                content += f'[...File "{file_path}" truncated at "{MAX_CHARS}" characters]'
            return content
    except Exception as e:
        return f"Error: {e}"