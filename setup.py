from setuptools import setup, find_packages
import sys, os

version = '0.1'
README = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
              'README.rst')).read()

setup(name='story_parser',
      version=version,
      description="A Given/When/Then BDD stories parser",
      long_description=README,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='bdd story parser',
      author='Hugo Lopes Tavares',
      author_email='hltbra@gmail.com',
      url='http://github.com/hugobr/story_parser',
      license='MIT',
      packages=['story_parser',],
      package_data={'':['README.rst', 'INSTALL', 'LICENSE', ]},
      package_dir={'story_parser': 'src',},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
