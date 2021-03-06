from setuptools import setup, find_packages

setup(name='trainer',
      version='0.1',
      packages=find_packages(),
      description='lstm nn with keras on gcloud ml-engine',
      author='Daniel Strausz',
      author_email='danst.1199@gmail.com',
      license='MIT',
      install_requires=[
          'keras',
          'h5py'
      ],
      zip_safe=False)
