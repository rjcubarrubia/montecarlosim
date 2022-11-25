from setuptools import setup

setup(name='montecarlosim',
      version='1.0',
      description='A Monte Carlo simulator package created for DS5100 course in UVA MSDS',
      url='https://github.com/rjcubarrubia/montecarlosim',
      author='RJ Cubarrubia',
      author_email='rcc7u@virginia.edu',
      license='MIT',
      packages= ['montecarlosim'],
      install_requires= ['numpy', 'pandas'])