import os
import argparse
import os
import subprocess

all_files = []


def build_file_tree(root_dir, file_extensions):
    tree = []
    for item in sorted(os.listdir(root_dir), key=lambda x: os.path.isdir(os.path.join(root_dir, x))):
        full_path = os.path.join(root_dir, item)
        if os.path.isdir(full_path):
            # Recursively build the file tree for the subdirectory
            subdir_tree = build_file_tree(full_path, file_extensions)
            if subdir_tree:
                # Only add the subdirectory to the tree if it contains any matching files
                tree.append({item: subdir_tree})
        else:
            # Check if the file name matches any of the supplied regexes
            for file_extension in file_extensions:
                if item.endswith(file_extension):
                    # Check if the file is ignored by Git
                    if subprocess.run(["git", "check-ignore", "--quiet", full_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 1:
                        tree.append(item)
                        all_files.append(os.path.join(root_dir, item))
                        break
    return tree


def print_directory_tree(tree, indent=""):
    for i, item in enumerate(tree):
        is_last_item = i == len(tree) - 1
        # If item is a dict, it's a folder
        if isinstance(item, dict):
            for key in item:
                print(
                    f"{indent}├── {key}/") if not is_last_item else print(f"{indent}└── {key}/")
                print_directory_tree(item[key], indent + "    ")
        else:
            print(f"{indent}├── {item}") if not is_last_item else print(
                f"{indent}└── {item}")


def print_file_contents(path):
    with open(path) as f:
        print()
        print(path)
        print("```")
        print(f.read())
        print("```")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="directory path")
    parser.add_argument("file_extensions", nargs="+",
                        help="file extensions to search for")
    parser.add_argument("--tree-only", action="store_true",
                        help="print only directory tree, not the file contents")
    args = parser.parse_args()

    tree = build_file_tree(args.directory, args.file_extensions)
    print(f"{os.path.basename(args.directory)}/")
    print_directory_tree(tree)

    if not args.tree_only:
        for file in all_files:
            print_file_contents(file)


if __name__ == "__main__":
    main()
