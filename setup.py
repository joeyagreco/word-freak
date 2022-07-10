from pathlib import Path

import setuptools

thisDirectory = Path(__file__).parent
longDescription = (thisDirectory / "README.md").read_text()

with open("LICENSE") as f:
    license = f.read()

setuptools.setup(
    name="wordfreak",
    version="0.0.9",
    author="Joey Greco",
    author_email="joeyagreco@gmail.com",
    description="Word Freak is a Python library that extracts word frequencies from files.",
    long_description=longDescription,
    license=license,
    packages=setuptools.find_packages(exclude=("test", "docs")),
    install_requires=["PyPDF2",
                      "docx2txt",
                      "setuptools"]
)
