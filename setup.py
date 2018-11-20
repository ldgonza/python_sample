import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_sample",
    version="0.0.1",
    author="Leonardo González",
    author_email="ldgonza@gmail.com",
    description="Sample, empty, python project used to set up new projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ldgonza/python_sample",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],

    install_requires=[]
)
