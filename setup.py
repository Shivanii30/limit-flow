from setuptools import setup, find_packages

setup(
    name="limit-flow",
    version="0.1.0",
    description="Adaptive rate limiting middleware for Python APIs",
    author="Shivani Kshirsagar",
    packages=find_packages(),
    install_requires=[
        "redis",
        "fastapi"
    ],
    python_requires=">=3.8",
)