"""
Create pii-manager as a Python package
"""


import io
import sys
import re

from setuptools import setup, find_packages

from src.pii_manager import VERSION

PKGNAME = "pii-manager"
GITHUB_URL = "https://github.com/bigscience-workshop/pii-manager"

# --------------------------------------------------------------------

PYTHON_VERSION = (3, 8)

if sys.version_info < PYTHON_VERSION:
    sys.exit(
        f'**** Sorry, {PKGNAME} {VERSION} needs at least Python {".".join(map(str, PYTHON_VERSION))}'
    )


def requirements(filename="requirements.txt"):
    """Read the requirements file"""
    with io.open(filename, "r") as f:
        return [line.strip() for line in f if line and line[0] != "#"]


def long_description():
    """
    Take the README and remove markdown hyperlinks
    """
    with open("README.md", "rt", encoding="utf-8") as f:
        desc = f.read()
        desc = re.sub(r"^\[ ([^\]]+) \]: \s+ \S.*\n", r"", desc, flags=re.X | re.M)
        return re.sub(r"\[ ([^\]]+) \]", r"\1", desc, flags=re.X)


# --------------------------------------------------------------------


setup_args = dict(
    name=PKGNAME,
    version=VERSION,
    author="Paulo Villegas",
    author_email="paulo.vllgs@gmail.com",
    description="Text Anonymization of PII",
    long_description_content_type="text/markdown",
    long_description=long_description(),
    license="Apache",
    url=GITHUB_URL,
    download_url=f"{GITHUB_URL}/tarball/v{VERSION}",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    extras_require={
        "test": ["pytest", "nose", "coverage"],
    },
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "pii-manage = pii_manager.app.manage:main",
            "pii-task-info = pii_manager.app.task_info:main",
        ]
    },
    include_package_data=False,
    package_data={},
    cmdclass={},
    keywords=["Big Science Workshop, PII"],
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
)

if __name__ == "__main__":
    # Add requirements
    setup_args["install_requires"] = requirements()
    # Setup
    setup(**setup_args)
