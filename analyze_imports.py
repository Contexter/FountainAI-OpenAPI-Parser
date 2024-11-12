# scripts/analyze_imports.py
import os
import importlib
import re
    from collections import defaultdict

def find_imports_in_file(file_path):
    """Extract import statements from a given Python file."""
    imports = set()
    with open(file_path, "r") as file:
        for line in file:
            match = re.match(r'^\s*(from|import)\s+([\w.]+)', line)
            if match:
                imports.add(match.group(2))
    return imports

def build_dependency_graph(base_path):
    """Build a dependency graph based on import statements."""
    dependency_graph = defaultdict(set)
    files = []

    for root, _, filenames in os.walk(base_path):
        for filename in filenames:
            if filename.endswith(".py"):
                file_path = os.path.join(root, filename)
                module_name = os.path.relpath(file_path, base_path).replace("/", ".").replace("\\", ".").rstrip(".py")
                files.append((module_name, file_path))
                imports = find_imports_in_file(file_path)
                dependency_graph[module_name].update(imports)

    return dependency_graph, files

def detect_circular_dependencies(dependency_graph):
    """Detect circular dependencies in the dependency graph."""
    circular_dependencies = []

    def visit(node, path):
        if node in path:
            circular_dependencies.append(path[path.index(node):] + [node])
            return
        if node not in dependency_graph:
            return
        for neighbor in dependency_graph[node]:
            visit(neighbor, path + [node])

    for node in dependency_graph:
        visit(node, [])

    return circular_dependencies

def resolve_circular_imports(base_path, circular_dependencies):
    """Provide suggestions to break circular imports."""
    for cycle in circular_dependencies:
        print(f"Circular import detected: {' -> '.join(cycle)}")
        print("Suggested fix:")
        for i, module in enumerate(cycle[:-1]):
            next_module = cycle[i + 1]
            print(f"  - In '{module}', consider lazy-importing '{next_module}' inside a function.")

def main():
    base_path = "fountainai_openapi_parser"  # Set this to your base directory for the parser

    # Step 1: Build dependency graph
    dependency_graph, files = build_dependency_graph(base_path)

    # Step 2: Detect circular dependencies
    circular_dependencies = detect_circular_dependencies(dependency_graph)

    # Step 3: Print and suggest fixes for circular dependencies
    if circular_dependencies:
        resolve_circular_imports(base_path, circular_dependencies)
    else:
        print("No circular dependencies detected.")

if __name__ == "__main__":
    main()

