from setuptools import setup, find_packages
import sys, os

version = '1.2'
long_description = """The raisin.restish package is a part of Raisin, the web application
used for publishing the summary statistics of Grape, a pipeline used for processing and
analyzing RNA-Seq data."""

setup(name='raisin.restish',
      version=version,
      description="A package used in the Raisin web application",
      long_description=long_description,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Natural Language :: English',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Operating System :: POSIX :: Linux'],
      keywords='RNA-Seq pipeline ngs transcriptome bioinformatics ETL',
      author='Maik Roder',
      author_email='maikroeder@gmail.com',
      url='http://big.crg.cat/services/grape',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      namespace_packages = ['raisin'],
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
main = raisin.restish.wsgiapp:make_app

[paste.app_install]
main = paste.script.appinstall:Installer
      """,
      test_suite="raisin.restish.tests",
      tests_require=['WebTest'],
      )
