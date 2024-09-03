from setuptools import setup, find_packages

setup(
    name="python_project_template",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hello=hello.app.main:main',
        ],
    },
)
