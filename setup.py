from setuptools import setup, find_packages

setup(
    name="Sagital Brain",
    version="0.1.0",
    packages=find_packages(),
    install_requires=['numpy', 'pytest'],
    entry_points={
        'console_scripts': [
            'sagital_brain = sagital_brain.command:process'
    ]}
)