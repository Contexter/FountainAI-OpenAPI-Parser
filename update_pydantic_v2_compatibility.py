import re

def update_config(filename):
    with open(filename, "r") as file:
        content = file.read()

    # Replace allow_population_by_field_name with populate_by_name
    new_content = content.replace(
        "allow_population_by_field_name", "populate_by_name"
    )

    if content != new_content:
        print(f"Updated config setting in {filename}")
    else:
        print(f"No config setting updates needed in {filename}")

    with open(filename, "w") as file:
        file.write(new_content)

def update_schema_field(
    filename, class_names, old_field="schema", new_field="schema_data"
):
    with open(filename, "r") as file:
        lines = file.readlines()

    updated_lines = []
    within_class = None

    for line in lines:
        # Detect the start of a class and check if it's one of the target classes
        class_match = re.match(r"class\s+(\w+)\(BaseModel\):", line)
        if class_match:
            class_name = class_match.group(1)
            within_class = class_name if class_name in class_names else None

        # If within a target class, replace `schema` field with `schema_data`
        if within_class and re.search(rf"\b{old_field}\s*:", line):
            updated_line = line.replace(old_field, new_field)
            updated_lines.append(updated_line)
            print(
                f"Updated '{old_field}' to '{new_field}' in class '{within_class}' in {filename}"
            )
        else:
            updated_lines.append(line)

    with open(filename, "w") as file:
        file.writelines(updated_lines)

def main():
    filename = "fountainai_openapi_parser/models.py"
    update_config(filename)
    update_schema_field(filename, ["MediaType", "Parameter", "Header"])

if __name__ == "__main__":
    main()
