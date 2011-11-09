from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='nostrils',
      version=version,
      description="Notify user of test failures while nosetests is running",
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
          # -*- Extra requirements: -*-
      ],
      entry_points={'nose.plugins':['nostrils=nostrils:Nostrils']}
      )
