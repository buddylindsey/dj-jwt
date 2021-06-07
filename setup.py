from setuptools import find_packages, setup

from djjwt import __version__ as VERSION

PACKAGE_NAME = "dj-jwt"

with open("README.md", "r") as fh:
    long_description = fh.read()


def parse_requirements(filename):
    """Load requirements from a pip requirements file."""
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


if __name__ == "__main__":
    setup(
        name=PACKAGE_NAME,
        version=VERSION,
        packages=find_packages(),
        install_requires=parse_requirements("requirements/base.txt"),
        url="https://github.com/buddylindsey/dj-jwt",
        author="Buddy Lindsey",
        author_email="buddy@buddylindsey.com",
        maintainer="Buddy Lindsey",
        description="Library to give vanilla Django jwt auth.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        python_requires=">=3.7",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Natural Language :: English",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Framework :: Django",
            "Framework :: Django :: 3.0",
        ],
        project_urls={
            "Documentation": "https://github.com/buddylindsey/dj-jwt",
            "Source": "https://github.com/buddylindsey/dj-jwt",
        },
    )
