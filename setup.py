from setuptools import setup, find_packages


install_requires = ["requests", "orjson", "dotenv"]


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="de_wrapper",
    version="0.0.1a",
    author="Disruptive Engineering, Balder Grenness Klanderud",
    url="https://github.com/Uzaaft/de-wrapper",
    packages=find_packages(),
    install_requires=install_requires,
    description="Get started with the DNB PSD2 API. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    download_url="https://github.com/uzaaft/de-wrapper/archive/master.zip",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
