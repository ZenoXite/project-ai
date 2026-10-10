from functions.get_file_content import get_file_content

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

main_content = get_file_content("calculator", "main.py")
calculator_content = get_file_content("calculator", "pkg/calculator.py")
missing_content = get_file_content("calculator", "pkg/does_not_exist.py")
outside_content = get_file_content("calculator", "/bin/cat")


print(main_content)
print(calculator_content)
print(missing_content)
print(outside_content)