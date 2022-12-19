from setuptools import setup

setup(
    name="dirtree",
    version="1.0",
    author="Stephan Cilliers",
    author_email="stephan@stephancill.co.za",
    description="Prints a directory dirtree with the contents of specified file types.",
    packages=["dirtree"],
    entry_points={
        "console_scripts": [
            "dirtree = dirtree.print_directory_tree:main"
        ]
    }
)