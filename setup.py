from setuptools import setup

setup(
    name="wiki-forecast",
    version="0.3.2",
    description="Forecasting models for wikipedia page views",
    entry_points={"console_scripts": ["wiki-forecast=wikicast.__main__:cli"]},
    install_requires=[
        "click",
        "pyspark >= 2.4.0",
        "networkx",
        "matplotlib",
        "pandas",
        "graphframes",
    ],
    packages=["wikicast"],
)
