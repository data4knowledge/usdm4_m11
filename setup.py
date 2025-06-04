from setuptools import setup, find_packages

setup(
    name="usdm4_m11",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "usdm4",
        "usdm_excel",
        "usdm_info",
        "d4k_ms_base",
        "raw_docx",
        "python-dateutil",
    ],
    author="Original Author",
    author_email="author@example.com",
    description="A package for processing M11 protocol documents and converting them to USDM format",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/usdm4_m11",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
