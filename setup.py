from setuptools import setup

long_description = open("README.md").read()

# Version info -- read without importing
_locals = {}
with open("glitch_forge/_version.py") as fp:
    exec(fp.read(), None, _locals)
version = _locals["__version__"]


setup(
    name="glitch_forge",
    version=version,
    description="",
    long_description=long_description,
    author="Lukas Ukelis",
    author_email="lukasukelis@gmail.com",
    project_urls={
        "Source": "https://github.com/LukasUkelis/GlitchForge",
        "Issues": "https://github.com/LukasUkelis/GlitchForge/issues",
    },
    packages=["glitch_forge"],
    python_requires=">=3.10",
    install_requires=["PyQt6>=6.8.1"],
)
