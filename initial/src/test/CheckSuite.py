import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = """
            int a,b;
            int a;
            int main() {}
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,401))

    