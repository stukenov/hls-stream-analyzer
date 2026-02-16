from setuptools import setup

setup(
    name="hls-analyse",
    version="1.0.0",
    url="https://github.com/epiclabs-io/hls-analyzer",
    license="MIT",
    author="epiclabs-io",
    description="Analyzer for HTTP Live Streams (HLS) content",
    python_requires=">=3.7",
    install_requires=[
        "iso8601>=0.1.11"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Multimedia :: Video",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
