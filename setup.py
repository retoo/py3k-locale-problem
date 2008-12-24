 # -*- coding: utf-8 -*-

from distutils.core import setup
from distutils.extension import Extension

setup(name='py3k_locale_problem',
      version='1.0',
      py_modules=['py3k_locale_problem'],
      author="Reto Schüttel",
      url="http://github.com/retoo/py3k-locale-problem/wikis",
      author_email="reto@schuettel.ch",
      ext_modules=[Extension("py3k_locale_problem_ext", ['py3k_locale_problem_ext.c'])]
      )