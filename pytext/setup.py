# Import required functions
from setuptools import setup,find_packages

# Call setup function
setup(
    author="<Mehdi RABBAI>",
    description="Text analysis package",
    name="pytext",
    packages=find_packages(include=["pytext","pytext.*"]),
    version="0.1.0",
)
