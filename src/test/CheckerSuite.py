import unittest
from TestUtils import TestChecker
from AST import *
from Visitor import Visitor
from StaticError import *
from abc import ABC

class CheckerSuite(unittest.TestCase):
    pass