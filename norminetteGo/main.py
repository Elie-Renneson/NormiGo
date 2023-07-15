import re
import sys

def is_snake_case(name):
    words = name.split("_")
    
    if len(words) == 1:
        # For single-word variables, it should be all lowercase
        return words[0].islower()
    else:
        # For multi-word variables, all words should be lowercase
        for word in words:
            if not word.islower() and not word.isdecimal():
                return False
        return words[0][0].islower()


def check_go_program(file_path):
    with open(file_path, 'r') as file:
        source_code = file.read()

    lines = source_code.split('\n')
    errors = []

    # Check variable assignment format and value assignment after declaration
    for line in lines:
        line = line.strip()
        if line.startswith("var"):
            parts = line.split()
            if len(parts) != 3:
                errors.append(f"Invalid variable assignment format: {line}")
        elif ":=" in line:
            errors.append(f"Invalid assignment operator ':=' found: {line}")

    # Rule 3: Verify variable name follows Snake Case
    variable_name_pattern = r'\bvar\s+(\w+)\s+'
    variable_names = re.findall(variable_name_pattern, source_code)
    for variable_name in variable_names:
        if not is_snake_case(variable_name):
            errors.append(f"Variable name '{variable_name}' does not follow Snake Case")

    # Rule 4: Verify the usage of printf instead of println or print
    printf_pattern = r'\b(print(ln)?)\b'
    printf_matches = re.findall(printf_pattern, source_code)
    if printf_matches:
        errors.append("Found usage of 'println' or 'print', use 'printf' instead")

    return errors

# Example usage:
if len(sys.argv) < 2:
    print("Please provide the file path as an argument.")
    sys.exit(1)

file_path = sys.argv[1]

errors = check_go_program(file_path)
if errors:
    for error in errors:
        print(f"Error: {error}")
else:
    print("The Go program follows the specified rules.")
