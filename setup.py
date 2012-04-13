from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='nostrils',
      version=version,
      description="Gather test-line mapping from test runs.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='nose plugin',
      author='Kevin Qiu',
      author_email='kevin.jing.qiu@gmail.com',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'nose',
      ],
      entry_points={'nose.plugins':['nostrils=nostrils:Nostrils'],
          }
      )
