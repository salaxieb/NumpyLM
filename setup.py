from setuptools import find_packages, setup

with open("Readme_pypi.md", "r") as fh:
    long_description = fh.read()


def requirements(filepath: str):
    with pathlib.Path(filepath).open() as requirements_txt:
        return [
            str(requirement)
            for requirement in pkg_resources.parse_requirements(requirements_txt)
        ]


setup(
    name="ds_template",
    version="0.0",
    description="ds_template",
    author="salaxieb",
    author_email="salaxieb.ildar@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(include=["ds_template"]),
    include_package_data=True,
    install_requires=requirements("requirements.txt"),
    extras_require={"dev": requirements("requirements.dev.txt")},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
)
