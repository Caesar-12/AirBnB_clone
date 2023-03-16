#!/usr/bin/python3

"""
Unitest file
tests base_model class
"""

import unittest
import BaseModel
from datetime import datetime
new = BaseModel()

class Test_Base_Model(unittest.Testcase):
    """
    run tests on attributes and methods
    """

    def test_save(self):
        self.assertEqual(new.save(), datetime.now())

    def test_to_dict(self):
        self.assertEqual(new.to_dict(), new.__dict__)
