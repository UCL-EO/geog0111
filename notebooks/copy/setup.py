import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup = {
    'url':'https://github.com/UCL-EO/geog0111',
    'version':'1.0.1',
    'name':'geog0111',
    'description':'UCL Geography MSc notes',
    'author':'Prof. P. Lewis',
    'author_email':'p.lewis@ucl.ac.uk',
    'license':'MIT',
    'keywords':'scientific computing',
    'long_description':long_description,
    'long_description_content_type':"text/markdown",
    'packages':setuptools.find_packages(),
    'classifiers':[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    'python_requires':'>=3.6',
}


setuptools.setup(**setup) 

