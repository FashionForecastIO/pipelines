from setuptools import find_packages, setup

setup(
    name="pipelines",
    packages=find_packages(exclude=["*tests"]),
    install_requires=[
        "dagster",
        "dagster-postgres",
        "requests",
        "ruff",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
