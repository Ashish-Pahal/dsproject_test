from setuptools import find_packages, setup
from typing import List

Hyphen_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements 
    '''
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace('\n', '') for req in requirements]

        if Hyphen_E_DOT in requirements:
            requirements.remove(Hyphen_E_DOT)

    return requirements

setup(
name= 'dsproject_test',
version= '0.0.1',
author= 'Ashish Pahal',
author_email= 'ashishpayal07@gmail.com',
packages= find_packages(),
install_requirements= get_requirements('requirements.txt')
)