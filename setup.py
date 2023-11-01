import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="fetch-downloader",
    version="0.0.1",
    author="Caleb Smith",
    author_email="me@calebmsmith.com",
    description=("A youtube downloader package."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fyresmith/fetch",
    project_urls={
        "Bug Tracker": "https://github.com/fyresmith/fetch/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pytube"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "fetchtube = fetchtube.cli:main",
        ]
    }
)
