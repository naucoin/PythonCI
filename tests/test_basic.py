# nosetests --nocapture -v tests/test_basic.py

import sys, os
print('test_sitk: Python = %s, version = %s' % (sys.executable, sys.version))
import logging
from nose_parameterized import parameterized
from itertools import product

testCases = ["A", "B"]
features = ["one", "two", "three", "four"]

class TestBasic:

  def generate_scenarios():
    global testCases
    global features

    for testCase in testCases:
      for feature in features:
        yield testCase, feature

  @parameterized.expand(generate_scenarios())
  def test_scenario(self, testCase, featureClassName):
    print("")

    logging.debug('test_scenario: testCase = %s, featureClassName = %s', testCase, featureClassName)

def teardown_module():
  print("")

