import time
import sys
import os

from py3k_locale_problem_ext import convert

def run_tests():
  print(sys.version)
  # set LANG and LC_ALL to 'de_CH.UTF-8' on a OS X system to get the wrong behavior
  print("LANG: %s" % os.environ["LANG"])
  print("")

  print("""
  == strptime test ==

  When parsing date with strptime() Python usually ignores the locale and
  just assumes LANG=C.

  This test tries to parse the weekday 'Monday' and 'Montag'. With Python 3
  on OS X and a german locale only 'Montag' can be parsed.
  """)

  for name in ("Montag", "Monday"):
      try:
          t = time.strptime(name, "%A")
          print("Parsing '%s'. Result: %s" % (name, t))
      except ValueError:
          print("Parsing '%s'. Result: Unable to detect (Value Error)" % name)

  print("")
  print("""
  ==float() test ==

  Float's contstructor is pretty locale indepdendent, it will recognize 1.7 as
  a number regardless the version of Python or the plattform.

  """)
  for string in ("1.7", "1,7"):
      try:
          value = float(string)
          print("%s: %s" % (string, value))
      except ValueError:
          print("%s: Unable to detect (Value Error)" % string)

  print("")
  print("""
  == atof() test (using a C extension) =="

  In this test the libc function atof() is being used to convert the string to
  a float. In Python 2.5 the C extension's atof appears to ignore the LOCALE
  and always expects a '.' as the decimal delimiter. With Python 3.0 on
  a OS X box with german locales the atof epxects the german delimiter ','.
  """)
  for string in ("1.7", "1,7"):
        value = convert(string)
        print("%s: %s" % (string, value))

if __name__ == '__main__':
  run_tests()
