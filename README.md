# Directory Tree Printer

This project provides a command line tool that recursively prints the contents of a directory tree, including the names of all files in the tree with specified file extensions. It also prints the contents of these files.

## Installation

To install the dirtree command line tool, clone this repository and run the following command from the root directory:

```
pip install .
```

## Usage

To print the directory tree for a specified directory and file extensions, run the following command:

```
dirtree /path/to/directory file_extension1 file_extension2 ...
```

For example:

```
dirtree /path/to/directory .py .txt
```

This will print the directory tree for the specified directory, including all files with the .py or .txt extensions, along with the contents of these files e.g.

```
/path/to/directory/
├── setup.py
└── dirtree/
    ├── print_directory_tree.py
    └── __init__.py
```

## Development

To develop or modify this project, clone this repository and install the dependencies using the following command:

```
pip install -r requirements.txt
```

The print_directory_tree.py script contains the main implementation of the dirtree command line tool. It can be run from the command line using the python command, for example:

```
python print_directory_tree.py /path/to/directory .py .txt
```

## Credits

This project was created by Stephan Cilliers. Majority of the code and readme was written by ChatGPT.
