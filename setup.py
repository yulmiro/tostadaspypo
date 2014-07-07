from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='tostadaspypo',
      version=version,
      description="ejemplos de conjuntos de tostadas pypo",
      long_description="""\
ejemplos de conjuntos de tostadas pypo""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='package python egg conjuntos tostadas pypo',
      author='yuliana miquilareno',
      author_email='yulianamiquilareno@gmail.com',
      url='https://github.com/yulmiro/tostadaspypo',
      license='GPL 2v',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
