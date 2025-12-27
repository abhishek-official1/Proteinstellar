"""
Proteinstellar - Computational Therapeutics through AlphaFold
Setup script for local installation
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="proteinstellar",
    version="1.0.0",
    author="Proteinstellar Contributors",
    author_email="your.email@example.com",
    description="Computational therapeutics platform for protein structure prediction and analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR_USERNAME/proteinstellar",
    project_urls={
        "Bug Tracker": "https://github.com/YOUR_USERNAME/proteinstellar/issues",
        "Documentation": "https://github.com/YOUR_USERNAME/proteinstellar/blob/main/docs/getting_started.md",
        "Source Code": "https://github.com/YOUR_USERNAME/proteinstellar",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0,<2.0.0",
        "biopython>=1.79",
        "ipython>=7.0.0",
        "ipywidgets>=7.6.0",
        "jupyter>=1.0.0",
        "matplotlib>=3.3.0",
        "py3Dmol>=2.0.0",
        "scipy>=1.7.0",
        "pandas>=1.3.0",
        "requests>=2.26.0",
    ],
    extras_require={
        "dev": [
            "black>=22.0.0",
            "flake8>=4.0.0",
            "isort>=5.10.0",
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
        ],
        "colabfold": [
            "pydrive2>=1.15.0",
        ],
    },
    keywords="protein-folding alphafold bioinformatics structural-biology drug-discovery",
)
