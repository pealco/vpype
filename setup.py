from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="vpype",
    version="0.1.0",
    description="Vector pipeline for generative art",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Antoine Beyeler",
    url="https://github.com/abey79/vpype",
    license=license,
    packages=find_packages(exclude=("examples", "tests")),
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        vpype=vpype:cli
    '''
)