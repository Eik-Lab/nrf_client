from setuptools import setup, find_packages


install_requires = ["requests", "orjson", "python-dotenv"]


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="NRFClient",
    version="0.0.1a",
    author="Uzair Aftab",
    url="https://github.com/Eik-Lab/nrf_client",
    packages=find_packages(),
    install_requires=install_requires,
    description="Get started with the nrf client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    download_url="https://github.com/Eik-Lab/nrf_client",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
