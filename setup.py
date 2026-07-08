"""
Setup script for the NetworkSecurity package.The setup.py file is an essential component of the package, providing metadata and configuration for building, distributing, and installing the package. It defines the package name, version, author information, dependencies, and other relevant details required for proper installation and usage of the NetworkSecurity packaging and
distributing python projects.It is used by setuptools to define the package structure, dependencies, and other metadata necessary for building and distributing the package. The setup.py file is typically executed using the command line to install the package or create distribution archives. It serves as a central point for managing the package's configuration and ensuring that it can be easily installed and used by others in the Python ecosystem.  

"""


from setuptools import setup, find_packages
from typing import List

def get_reqiuirements()->List[str]:
    """
    This function will return the list of requirements
    """
    requirement_lst :List[str] = []
    try:
        with open("requirements.txt","r") as file:
            # read lines from the file
            lines  = file.readlines()
            # process each line
            for line in lines:
                requirements  = line.strip()
                ## ignore empty lines and comments (-e .)
                if requirements and requirements != "-e .":
                    requirement_lst.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Muhammed Jahsh V",
    author_email="jahshvrd@gmail.com",
    packages=find_packages(),
    install_requires=get_reqiuirements(),
)