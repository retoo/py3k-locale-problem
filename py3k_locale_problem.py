import time
import sys
import os

from py3k_locale_problem_ext import convert

def run_tests():
  print(sys.version)
  print("LANG: %s" % os.environ["LANG"])
  print("")

  print("strptime test:")
  for name in ("Montag", "Monday"): 
      try:
          t = time.strptime(name, "%A")
          print("%s: %s" % (name, t))
      except ValueError:
          print("%s: Unable to detect (Value Error)" % name)
          
  print("")
  print("float() test:")
  for string in ("1.9", "1,9"):
      try:
          value = float(string)
          print("%s: %s" % (string, value))
      except ValueError:
          print("%s: Unable to detect (Value Error)" % string)

  print("")
  print("atof() test (using a C extension):")
  for string in ("1.9", "1,9"):
        value = convert(string)
        print("%s: %s" % (string, value))

if __name__ == '__main__':
  run_tests()
