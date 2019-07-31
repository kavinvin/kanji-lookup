import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
    setuptools.setup(
        name='kanji',
        version='0.1.0',
        scripts=['kj'] ,
        author="Kavin Ruengprateepsang",
        author_email="kavinvin.vin@gmail.com",
        description="A program to lookup kanji",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/kavinvin/kj",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
    )
