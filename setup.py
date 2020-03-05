from setuptools import find_packages, setup

setup(name='SpykeTorch',
      version='0.1.0',
      install_requires=['numpy', 'torch>=1.1', 'torchvision', 'matplotlib'],
      packages=find_packages())
