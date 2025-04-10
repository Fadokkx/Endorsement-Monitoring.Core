from setuptools import setup, find_packages

setup(
    name="extracaorelatorioprocsmcc",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "selenium==4.10.0",
        "webdriver-manager==3.8.6",
        "python-dotenv==1.0.0"
    ],
)