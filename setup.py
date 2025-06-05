from setuptools import setup,find_packages
from typing import List
HIPPEN_E_DOT='-e.'

def get_requirements(file_name:str)->List[str]:
    """
    input:file_name--str
    this function returns the requirements in a form of list
    output:list[requirements]
    """
    requirements=[]

    with open(file_name,'r') as file:
        requirements=file.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HIPPEN_E_DOT in requirements:
            requirements.remove(HIPPEN_E_DOT)
        return requirements

setup(
    name='Descriptive Answer Evalution System',
    version='0.1.1',
    author='rishendra',
    author_email='mrishe6@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)

