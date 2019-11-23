import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="esteganew",
    version="1.0",
    author="JuanPab3 and naso071699",
    author_email="juanpab.sierra@urosario.edu.co",
    description="Steganographic tool, for images.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JuanPab3/esteganew",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
