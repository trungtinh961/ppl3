import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):

    def test_no_entry_point_no_main(self):
        input = """
            int a,b;
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_no_entry_point_var(self):
        input = """
            int a,b;
            float main;
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_no_entry_point_array(self):
        input = """
            int a,b;
            float main[5];
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclared_glo_var(self):
        input = """
            int a,b;
            int a;
            int main() {
                return 0;
            }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_glo_var_after_main(self):
        input = """
            int a,b;            
            int main() {
                return 0;
            }
            int a;
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclared_function(self):
        input = """
            int a,b;
            float a() {
                return 0;
            }
            int main() {
                return 0;
            }
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,405))
    
    def test_redeclared_var(self):
        input = """
            int a,b;
            int c(int a, float b) {
                return 0;
            }
            float c;
            int main(int a) {
                return 0;
            }
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclared_param(self):
        input = """
            int a,b;
            int c(int a, float b, string c, boolean a) {
                return 0;
            }
            int main(int a) {
                return 0;
            }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclared_local_level2(self):
        input = """
            int a,b;
            int main(int a, int b) {                
                int b;
                return 0;
            }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_redeclared_local_level3(self):
        input = """
            int a,b;
            int main(int a, int b) {                
                {
                    int a,b,c;
                    int a;
                }
                return 0;
            }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_redeclared_local_level4(self):
        input = """
            int a,b;
            int main(int a, int b) {                
                {
                    int a,b,c;
                    {
                        int a,b,c;
                        int a;
                    }
                }
                return 0;
            }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_Undeclared_function_level_4(self):
        input = """
            int a,b;
            int main(int a, int b) {                
                {
                    int a,b,c;
                    {
                        int a,b,c;
                        foo();
                    }
                }
                return 0;
            }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_Undeclared_function_level_3(self):
        input = """
            int a,b;
            int main(int a, int b) {                
                {
                    foo();
                }
                return 0;
            }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,412))

    # def test_TypeMismatchInStmt_nonePara(self):
    #     input = """
    #         int a,b;
    #         int foo(int a) {
    #             return 0;
    #         }
    #         int main(int a, int b) {                
    #             {
    #                 foo();
    #             }
    #             return 0;
    #         }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
    #     self.assertTrue(TestChecker.test(input,expect,411))

    # def test_TypeMismatchInStmt_manyPara(self):
    #     input = """
    #         int a,b;
    #         int foo(int a) {
    #             return 0;
    #         }
    #         int main(int a, int b) {                
    #             {
    #                 foo(a,b);
    #             }
    #             return 0;
    #         }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a),Id(b)])"
    #     self.assertTrue(TestChecker.test(input,expect,412))

    # def test_TypeMismatchInStmt_partype_floatint(self):
    #     input = """
    #         int a,b;
    #         int foo(int a) {
    #             return 0;
    #         }
    #         int main(float a, int b) {                
    #             foo(a);
    #             return 0;
    #         }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])"
    #     self.assertTrue(TestChecker.test(input,expect,413))

    # def test_TypeMismatchInStmt_partype_intbool(self):
    #     input = """
    #         int a,b;
    #         int foo(int a) {
    #             return 0;
    #         }
    #         int main(boolean a, int b) {                
    #             foo(a);
    #             return 0;
    #         }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])"
    #     self.assertTrue(TestChecker.test(input,expect,414))

    # def test_Undeclared_IdLHS(self):
    #     input = """
    #         int a,b;
    #         int main(float a, int b) {                
    #             c = a + b
    #         }
    #     """
    #     expect = "Undeclared Identifier: c"
    #     self.assertTrue(TestChecker.test(input,expect,415))

    # def test_Undeclared_IdRHS(self):
    #     input = """
    #         int a,b;
    #         int main(float a, int b) {                
    #             a = c + b
    #         }
    #     """
    #     expect = "Undeclared Identifier: c"
    #     self.assertTrue(TestChecker.test(input,expect,416))