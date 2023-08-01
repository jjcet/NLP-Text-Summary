import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


__version__ = "0.0.0"

REPO_NAME = "NLP-Text-Summary"
AUTHOR_USER_NAME = "jjcet"
SRC_REPO = "TextSummary"
AUTHOR_EMAIL = "dycjh@example.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jjcet/{}".format(REPO_NAME),
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
    
