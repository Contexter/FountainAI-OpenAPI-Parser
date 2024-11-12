import os
import py_compile

def check_incomplete_imports(root_dir=".", verbose=False):
    print("Starting scan of repository for incomplete imports...")
    import_errors = []
    non_import_errors = []

    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(subdir, file)
                try:
                    py_compile.compile(file_path, doraise=True)
                except Exception as e:
                    error_message = str(e)
                    if "ImportError" in error_message or "ModuleNotFoundError" in error_message:
                        import_errors.append((file_path, error_message))
                    else:
                        non_import_errors.append((file_path, error_message))

    # Output summary for import-related errors
    if import_errors:
        print("\nIncomplete Imports Detected:")
        for file_path, message in import_errors:
            print(f"File: {file_path}\n  Issue: {message}")
    else:
        print("No incomplete imports found.")

    # Optional verbose output for non-import errors
    if verbose and non_import_errors:
        print("\nOther Issues Detected:")
        for file_path, message in non_import_errors:
            print(f"File: {file_path}\n  Issue: {message}")

    print("\nScan completed.")

# Run the function with verbose output disabled by default
check_incomplete_imports(verbose=False)

