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


    def test_Undeclared_Id_param(self):
        input = """
            int a,b;
            void foo(float a, int b) {}
            int main(int a, int b) {                
                {
                    foo(c,b);
                }
                return 0;
            }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_Undeclared_Id_binary(self):
        input = """
            int a,b;            
            int main(int a, int b) {                
                {
                    c = a + b;
                }
                return 0;
            }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_Undeclared_Id_unary(self):
        input = """
            int a,b;            
            int main(boolean a, boolean b) {                
                c = b && a;
                return 0;
            }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_Undeclared_Id_for(self):
        input = """
            int a,b;            
            int main(int a, float b) {                
                for (c = 1; c > 0; c = c + 1) {
                    a = b + 1;
                }
                return 0;
            }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_Undeclared_Id_if(self):
        input = """
            int a,b;            
            int main(boolean a, boolean b) {                
                if (c > a + b) {
                    c = a + 1;
                }
                return 0;
            }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,417))


    def test_Undeclared_Id_dowhile(self):
        input = """
            int a,b;            
            int main(float a, int b) {                
                do
                    a = b + 1;
                    c = a * 2;
                while(true);
                return 0;
            }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_TypeMismatchStmt_if_param(self):
        input = """
            int a,b;            
            int main(float a, boolean b) {                
                if (a) {
                    b = true;
                }
                return 0;
            }
        """
        expect = "Type Mismatch In Statement: If(Id(a),Block([BinaryOp(=,Id(b),BooleanLiteral(true))]))"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_TypeMismatchStmt_if_glo(self):
        input = """
            int a,b;
            string flag;            
            int main(float a, boolean b) {                
                if (flag) {
                    b = true;
                }
                else {
                    b = false;
                }
                return 0;
            }
        """
        expect = "Type Mismatch In Statement: If(Id(flag),Block([BinaryOp(=,Id(b),BooleanLiteral(true))]),Block([BinaryOp(=,Id(b),BooleanLiteral(false))]))"
        self.assertTrue(TestChecker.test(input,expect,420))


    def test_TypeMismatchStmt_for_expr1(self):
        input = """
            int a,b;
            string flag;            
            int main(float a, boolean b) {                
                for (a = a + 1.3; b; 1) {
                    b = false;
                }
                return 0;
            }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(a),BinaryOp(+,Id(a),FloatLiteral(1.3)));Id(b);IntLiteral(1);Block([BinaryOp(=,Id(b),BooleanLiteral(false))]))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_TypeMismatchStmt_for_expr2(self):
        input = """
            int a,b;
            string flag;            
            int main(int a, boolean b) {                
                for (a = 10; flag = "ppl"; 1) {
                    b = false;
                }
                return 0;
            }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(a),IntLiteral(10));BinaryOp(=,Id(flag),StringLiteral(ppl));IntLiteral(1);Block([BinaryOp(=,Id(b),BooleanLiteral(false))]))"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_TypeMismatchStmt_for_expr3(self):
        input = """
            int a,b;
            string flag;            
            int main(int a, boolean b) {                
                for (a = 10; b = true; flag = "ppl") {
                    b = false;
                }
                return 0;
            }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(a),IntLiteral(10));BinaryOp(=,Id(b),BooleanLiteral(true));BinaryOp(=,Id(flag),StringLiteral(ppl));Block([BinaryOp(=,Id(b),BooleanLiteral(false))]))"
        self.assertTrue(TestChecker.test(input,expect,423))


    def test_TypeMismatchStmt_dowhile(self):
        input = """
            int a,b;
            string flag;            
            int main(int a, boolean b) {                
                do {
                    if (a == 2) {
                        b = false;
                    }
                } while flag;
                return 0;
            }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([If(BinaryOp(==,Id(a),IntLiteral(2)),Block([BinaryOp(=,Id(b),BooleanLiteral(false))]))])],Id(flag))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_TypeMismatchStmt_return_void_have_expr(self):
        input = """
            int a,b;
            string flag;            
            void main(int a, boolean b) {                
                do {
                    if (a == 2) {
                        b = false;
                    }
                } while b;
                return 0;
            }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_TypeMismatchStmt_int_return_void(self):
        input = """
            int a,b;
            string flag;            
            int main(int a, boolean b) {                
                do {
                    if (a == 2) {
                        b = false;
                    }
                } while b;
                return ;
            }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_TypeMismatchStmt_int_return_float(self):
        input = """
            int a,b;
            float c;            
            int main(int a, boolean b) {                
                do {
                    if (a == 2) {
                        b = false;
                    }
                } while b;
                return c;
            }
        """
        expect = "Type Mismatch In Statement: Return(Id(c))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_TypeMismatchStmt_int_return_float(self):
        input = """
            int a,b;
            float c;            
            int main(int a, boolean b) {                
                do {
                    if (a == 2) {
                        b = false;
                    }
                } while b;
                return 1.34567;
            }
        """
        expect = "Type Mismatch In Statement: Return(FloatLiteral(1.34567))"
        self.assertTrue(TestChecker.test(input,expect,428))