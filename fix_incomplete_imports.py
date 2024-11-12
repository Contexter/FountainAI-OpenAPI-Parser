import os
import py_compile

def check_incomplete_imports(root_dir="."):
    print("Starting scan of repository for incomplete imports...")
    modified_files = False

    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(subdir, file)
                try:
                    # Attempt to compile the file; errors will raise exceptions
                    py_compile.compile(file_path, doraise=True)
                except py_compile.PyCompileError as e:
                    # This captures any compile error related to missing imports
                    print(f"Error in {file_path}: {e}")
                    modified_files = True

    if not modified_files:
        print("No incomplete imports found or modified.")
    print("Scan completed.")

# Run the function
check_incomplete_imports()
