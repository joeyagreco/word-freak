import setuptools

from _version import __version__ as version

with open("README.md") as f:
    readMe = f.read()

with open("LICENSE") as f:
    license_ = f.read()

setuptools.setup(
    name="wordfreak",
    version=version,
    author="Joey Greco",
    author_email="joeyagreco@gmail.com",
    description="Word Freak is a Python library that extracts word frequencies from files.",
    long_description_content_type="text/markdown",
    long_description=readMe,
    license=license_,
    packages=setuptools.find_packages(exclude=("test", "docs")),
    install_requires=["PyPDF2",
                      "docx2txt",
                      "setuptools"]
)
