import unittest
from TestUtils import TestChecker
from AST import *
from Visitor import Visitor
from StaticError import *
from abc import ABC

class CheckerSuite(unittest.TestCase):
    def test_0(self):
        input = """
        x: integer = 3;
        x: string;
        main: function void(){}
    """

        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 400))