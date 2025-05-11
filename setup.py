from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mkpdf",
    version="0.1.0",
    author="tikisan",
    author_email="s2501082@sendai-nct.jp",
    description="様々な形式の画像をPDFに変換するPythonライブラリ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tikipiya/mkpdf",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        "Pillow>=10.2.0",
        "reportlab>=4.1.0",
        "click>=8.0.0",
        "tqdm>=4.65.0",
    ],
    entry_points={
        "console_scripts": [
            "mkpdf=mkpdf.cli:main",
        ],
    },
) 