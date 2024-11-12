import os
import ast

def get_python_files(root_dir):
    python_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip virtual environments and hidden directories
        dirnames[:] = [d for d in dirnames if not d.startswith('.') and d != '__pycache__' and d != 'venv']
        for filename in filenames:
            if filename.endswith('.py'):
                python_files.append(os.path.join(dirpath, filename))
    return python_files

def file_uses_rootmodel(file_content):
    try:
        tree = ast.parse(file_content)
        for node in ast.walk(tree):
            # Check for class definitions using RootModel
            if isinstance(node, ast.ClassDef):
                for base in node.bases:
                    if (isinstance(base, ast.Name) and base.id == 'RootModel') or \
                       (isinstance(base, ast.Subscript) and isinstance(base.value, ast.Name) and base.value.id == 'RootModel'):
                        return True
            # Check for other usages of RootModel
            if isinstance(node, ast.Name) and node.id == 'RootModel':
                return True
    except SyntaxError:
        pass  # Skip files with syntax errors
    return False

def file_imports_rootmodel(file_content):
    try:
        tree = ast.parse(file_content)
        for node in ast.walk(tree):
            # Check for 'from pydantic import RootModel'
            if isinstance(node, ast.ImportFrom):
                if node.module == 'pydantic' and any(alias.name == 'RootModel' for alias in node.names):
                    return True
            # Check for 'import pydantic'
            if isinstance(node, ast.Import):
                if any(alias.name == 'pydantic' for alias in node.names):
                    return True  # Assuming 'RootModel' could be accessed via 'pydantic.RootModel'
        return False
    except SyntaxError:
        pass
    return False

def add_rootmodel_import(file_content):
    lines = file_content.split('\n')
    import_added = False

    # Find the last import statement
    last_import_index = -1
    for i, line in enumerate(lines):
        stripped_line = line.strip()
        if stripped_line.startswith('from') or stripped_line.startswith('import'):
            last_import_index = i
        elif stripped_line and not stripped_line.startswith('#'):
            # Stop at the first non-import and non-comment line
            break

    # Check if there's an existing 'from pydantic import' statement
    for i, line in enumerate(lines[: last_import_index + 1]):
        if line.strip().startswith('from pydantic import'):
            if 'RootModel' not in line:
                # Append 'RootModel' to the existing import
                if line.strip().endswith(')'):
                    # Handle multi-line imports
                    j = i
                    while not lines[j].strip().startswith(')'):
                        j += 1
                    lines[j] = lines[j].replace(')', ', RootModel)')
                else:
                    lines[i] = line.rstrip() + ', RootModel'
            import_added = True
            break

    if not import_added:
        # Insert 'from pydantic import RootModel' after the last import
        insert_index = last_import_index + 1
        lines.insert(insert_index, 'from pydantic import RootModel')

    return '\n'.join(lines)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if file_uses_rootmodel(content) and not file_imports_rootmodel(content):
        print(f'Updating {filepath}')
        new_content = add_rootmodel_import(content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

def main():
    root_dir = '.'  # Change this if your project root is not the current directory
    python_files = get_python_files(root_dir)
    for filepath in python_files:
        process_file(filepath)

if __name__ == '__main__':
    main()

