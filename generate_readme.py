# Script to generate a ReadME file
# Author: Libhongo Mko

def generate_readme():
    readme_content = """
# My Project

This is a sample project generated using Python.

## Description

This project demonstrates how to make an API request to GitHub and retrieve user information.

## Installation

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.

## Usage

1. Run the Python script `app-load-testing-ag.py`.
2. The script will make an API request to GitHub and retrieve user information.
3. The response status code, headers, and body will be printed.

"""

    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)

if __name__ == "__main__":
    generate_readme()
