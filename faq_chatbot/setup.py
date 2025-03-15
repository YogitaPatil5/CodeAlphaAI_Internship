from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="faq-chatbot",
    version="1.0.0",
    author="Yogita Patil",
    author_email="yogitarajput.04@gmail.com",
    description="A modular FAQ chatbot with NLP capabilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = "https://github.com/YogitaPatil5/CodeAlphaAI_Internship"
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "nltk>=3.5",
        "scikit-learn>=0.24.0",
    ],
    entry_points={
        "console_scripts": [
            "faq-chatbot=faq_chatbot.__main__:main",
        ],
    },
)