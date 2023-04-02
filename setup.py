from setuptools import setup, find_packages

setup(
    name="auto-cr",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'click',
        'openai',
        'setuptools',
        'wheel',
    ],
    entry_points={
        'console_scripts': [
            'auto-cr=cli.main:hello',
        ],
    },
)
