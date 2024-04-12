from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='sibikanna',
    author_email='sibikanna.dp@gmail.com',
    install_requires=["generativeai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)