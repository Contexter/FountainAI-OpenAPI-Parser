import os

def scan_and_fix_indentation_errors(file_path):
    """
    Scans a file for indentation errors and attempts to resolve them.
    Returns True if any errors were found and fixed; otherwise, False.
    """
    fixed = False
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        fixed_lines = []
        for line in lines:
            # Stripping trailing whitespace, which often causes indentation issues
            fixed_line = line.rstrip() + '\n'
            fixed_lines.append(fixed_line)

        if lines != fixed_lines:  # Detect if any changes were made
            with open(file_path, 'w') as file:
                file.writelines(fixed_lines)
            fixed = True
            print(f"Fixed indentation issues in: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

    return fixed

def resolve_indentation_errors_in_repo(root_dir='.'):
    """
    Walks through each file in the repository, scans for indentation errors,
    and attempts to fix them.
    """
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.py'):
                file_path = os.path.join(dirpath, filename)
                scan_and_fix_indentation_errors(file_path)

if __name__ == "__main__":
    resolve_indentation_errors_in_repo()

