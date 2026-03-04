"""
FIFA 2022 World Cup Data Analysis
Setup configuration for package distribution
"""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="fifa2022-analysis",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="FIFA 2022 World Cup Data Analysis with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/fifa2022-analysis",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.10.0",
            "black>=21.0",
            "flake8>=3.9.0",
            "isort>=5.0.0",
            "mypy>=0.910",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=0.5.0",
        ],
        "viz": [
            "seaborn>=0.11.0",
            "plotly>=5.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "fifa2022-analysis=fifa2022_analysis.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.csv", "*.json", "*.yaml"],
    },
    project_urls={
        "Bug Reports": "https://github.com/yourusername/fifa2022-analysis/issues",
        "Source": "https://github.com/yourusername/fifa2022-analysis",
        "Documentation": "https://github.com/yourusername/fifa2022-analysis/tree/main/docs",
    },
    keywords=[
        "fifa",
        "world cup",
        "football",
        "soccer",
        "data analysis",
        "visualization",
        "pandas",
        "numpy",
        "matplotlib",
        "sports analytics",
    ],
)
