import os
def write_file(working_directory: str, file_path: str, content: str) -> str:
    target_path = os.path.abspath(os.path.join(working_directory, file_path))
    working_path = os.path.abspath(working_directory)
    if os.path.commonpath([working_path,target_path]) != working_path:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(target_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    parent_dir = os.path.dirname(target_path)
    try:
        os.makedirs(parent_dir, exist_ok=True)
        with open(target_path,"w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"