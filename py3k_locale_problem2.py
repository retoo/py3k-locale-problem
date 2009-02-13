import time
import sys
import os
import locale

from py3k_locale_problem_ext import print_locale

def run_tests():
  print(sys.version)
  print("Python: LC_NUMMERIC: %s" % repr(locale.getlocale(locale.LC_NUMERIC)))
  print("C Extension: LC_ALL")

  print_locale()

if __name__ == '__main__':
  run_tests()
