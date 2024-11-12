from setuptools import setup, find_packages

setup(
    name="NextGen-Search-LLM-and-Agents",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask>=2.0.0",
        "requests>=2.25.0",
        "numpy>=1.21.0",
        "transformers>=4.0.0",
        "torch>=1.9.0"
    ],
    entry_points={
        'console_scripts': [
            'nextgen-search=app:main',  
        ],
    },
    author="Raghav Tigadi",
    author_email="raghavtigadi@gmail.com.com",
    description="An advanced search engine with LLMs and agent-based architecture for intelligent search results.",
    url="https://github.com/ragztigadi/NextGen-Search-LLM-and-Agents",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
