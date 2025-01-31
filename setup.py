from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')
    return requirements
    
setup(
    name='TAGSim',
    version='1.0',    
    install_requires=read_requirements(),
    description='Implementation of TAGSim: Topic-Informed Attention-Guided Similarity',
    url='https://github.com/vipul124/TAGSim',
    packages=find_packages(),
    include_package_data=True
)
