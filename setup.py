from setuptools import setup, find_packages
import sys, os

version = '1.0.1'

setup(name='big.restish',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      namespace_packages = ['big'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'restish',
          'WebError',
      ],
      entry_points="""
      # -*- Entry points: -*-
[paste.app_factory]
main = big.restish.wsgiapp:make_app

[paste.app_install]
main = paste.script.appinstall:Installer
      """,
      test_suite="big.restish.tests",
      tests_require=['WebTest'],
      )
