from setuptools import setup

with open('README.md') as f:
    page_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

page_description = '''#Sample python package
Folder structure to create a python package
To use this structure it is necessary to create real modules
'''

setup(
    name="dummy_python_package",
    version="0.0.1",
    author="robinson_enedino",
    author_email="robinsonbrz@gmail.com",
    description="Sample Python package",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/robinsonbrz/dummy-python-package"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
