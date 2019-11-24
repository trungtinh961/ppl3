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

    def test_TypeMismatchStmt_int_return_floatlit(self):
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

    def test_TypeMismatchStmt_int_return_bool(self):
        input = """
            int a,b;
            float c;            
            int main(int a, boolean b) {                
                do {
                    if (a == 2) {
                        b = false;
                    }
                } while b;
                return true;
            }
        """
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_TypeMismatchStmt_float_return_bool(self):
        input = """
            int a,b;
            float c;            
            float main(int a, boolean b) {                
                do {
                    if (a == 2) {
                        b = false;
                    }
                } while b;
                return b;
            }
        """
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_TypeMismatchStmt_float_return_string(self):
        input = """
            int a,b;
            float c;            
            float main(int a, boolean b) {                
                do {
                    if (a == 2) {
                        b = false;
                    }
                } while b;
                return "ppl";
            }
        """
        expect = "Type Mismatch In Statement: Return(StringLiteral(ppl))"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_TypeMismatchStmt_int_return_arraycell(self):
        input = """
            int a,b;
            float c;            
            int main(int a, boolean b) {
                float c[5];            
                do {
                    if (a == 2) {
                        b = false;
                    }
                } while b;
                return c[1];
            }
        """
        expect = "Type Mismatch In Statement: Return(ArrayCell(Id(c),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_TypeMismatchStmt_float_return_array_func(self):
        input = """
            int a,b;
            float foo() {
                return 9.99;
            }          
            float[] main(int a, boolean b) {             
                do {
                    if (a == 2) {
                        b = false;
                    }
                } while b;
                return foo();
            }
        """
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_TypeMismatchStmt_float_array_return_array_int(self):
        input = """
            int a,b;         
            float[] main(int a, boolean b) {             
                int c[5];
                do {
                    if (a == 2) {
                        b = false;
                    }
                } while b;
                return c;
            }
        """
        expect = "Type Mismatch In Statement: Return(Id(c))"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_TypeMismatchStmt_float_array_return_bool(self):
        input = """
            int a,b;         
            float[] main(int a, boolean b) {             
                int c[5];
                do {
                    if (a == 2) {
                        b = false;
                    }
                } while b;
                return true;
            }
        """
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_TypeMismatchStmt_float_array_return_string(self):
        input = """
            int a,b;         
            float[] main(float d[], boolean b) {             
                int c[5];
                do {
                    if (a == 2) {
                        b = false;
                    }
                } while b;
                return "ppl";
            }
        """
        expect = "Type Mismatch In Statement: Return(StringLiteral(ppl))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_TypeMismatchExpr_array_expr2(self):
        input = """
           int main(float a[], boolean b) {             
                a[2.3] = 1;
                return 0;
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLiteral(2.3))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_TypeMismatchExpr_array_expr1(self):
        input = """
           int main(float a[], boolean b) {             
                a[2] = 1 + b[0];
                return 0;
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_TypeMismatchExpr_binary_bool_and(self):
        input = """
           int main(boolean a, int b) {             
                boolean c;
                c = true != a;
                c = b && true;
                return 0;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(b),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_TypeMismatchExpr_binary_bool_or(self):
        input = """
           int main(int a[], boolean b) {             
                boolean c;
                b = !true;
                c = b || 1;
                return 0;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,Id(b),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_TypeMismatchExpr_binary_int_basic(self):
        input = """
           int main(int a[], float b) {             
                a[0] = 1 + 2 - 3 * 4 / 5 + b;
                return 0;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(a),IntLiteral(0)),BinaryOp(+,BinaryOp(-,BinaryOp(+,IntLiteral(1),IntLiteral(2)),BinaryOp(/,BinaryOp(*,IntLiteral(3),IntLiteral(4)),IntLiteral(5))),Id(b)))"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_TypeMismatchExpr_binary_mod(self):
        input = """
           int main(int a[], float b, int c) {             
                a[0] = b % c;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(b),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_TypeMismatchExpr_binary_eq(self):
        input = """
           int main(float a[], int b, float c) {
                if (b == c) {
                    a[0] = b % c;
                }
                return 0;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(b),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_TypeMismatchExpr_binary_neq(self):
        input = """
           int main(float a, int b, float c) {
                do {
                    a = a + 1.9;
                } while (b != c);
                return 1;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,Id(b),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_TypeMismatchExpr_binary_less_greater(self):
        input = """
           int main(float a, int b, float c) {
                do {
                    a = a + 1.9;
                } while (b >= c) && (a <= 10.15) || b;
                return 1;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,BinaryOp(&&,BinaryOp(>=,Id(b),Id(c)),BinaryOp(<=,Id(a),FloatLiteral(10.15))),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,445))


    def test_TypeMismatchExpr_assign_LHS_arraypointer(self):
        input = """
           int main(float a[], int b, int c) {
                do {
                    a = b + 1.9;
                } while (b != c);
                return 1;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(+,Id(b),FloatLiteral(1.9)))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_TypeMismatchExpr_assign_LHS_array(self):
        input = """
           int main(float a, int b, int c) {
                int arr[5];
                do {
                    arr = a + 1.9;
                } while (b != c);
                return 1;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(arr),BinaryOp(+,Id(a),FloatLiteral(1.9)))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_TypeMismatchExpr_assign_LHS_array(self):
        input = """
           int main(float a, int b, int c) {
                int arr[5];
                do {
                    arr = a + 1.9;
                } while (b != c);
                return 1;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(arr),BinaryOp(+,Id(a),FloatLiteral(1.9)))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_TypeMismatchExpr_assign_int_float(self):
        input = """
           int main(float a, int b, int c) {
                for(b = 1; b >= 0; b = b + 1) {
                    c = a + 2;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(c),BinaryOp(+,Id(a),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_TypeMismatchExpr_assign_int_bool(self):
        input = """
           int main(float a, int b, float c) {
                for(b = 1; b >= 0; b = b + 1) {
                    c = true;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(c),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_TypeMismatchExpr_assign_bool_int(self):
        input = """
           int main(float a, int b, boolean c) {
                for(b = 1; b >= 0; b = b + 1) {
                    c = b * 10;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(c),BinaryOp(*,Id(b),IntLiteral(10)))"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_TypeMismatchExpr_assign_string_int(self):
        input = """
           int main(float a, int b, string c) {
                for(b = 1; b >= 0; b = b + 1) {
                    c = b * 10;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(c),BinaryOp(*,Id(b),IntLiteral(10)))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_TypeMismatchExpr_assign_bool_arraypointer(self):
        input = """
            int[] foo(int a) {
                int b[5];
                return b;
            }
            void main(float a, int b, int c) {
                int x[5], y[5];
                boolean d;
                for(b = 1; b >= 0; b = b + 1) {
                    foo(2)[3+c] = x[y[2]] +3;
                    d = foo(2)[1];
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(d),ArrayCell(CallExpr(Id(foo),[IntLiteral(2)]),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,452))


    def test_TypeMismatchExpr_funcall_less_param(self):
        input = """
            int foo(int a, int b){
                string str;
                boolean flag;
                return a + b * 100;
            }
            void main(float a, int b, boolean c) {
                if (c && false) {
                    foo(b);
                }
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_TypeMismatchExpr_funcall_many_param(self):
        input = """
            int foo(int a, int b){
                string str;
                boolean flag;
                return a + b * 100;
            }
            void main(float a, int b, boolean c) {
                int x, y;
                if (c && false) {
                    foo(b,1,2);
                }
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(b),IntLiteral(1),IntLiteral(2)])"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_TypeMismatchExpr_funcall_pass_lhs(self):
        input = """
            int foo(int a, int b){
                string str;
                boolean flag;
                return a + b * 100;
            }
            void main(float a, int b, boolean c) {
                int x, y;
                if (c && false) {
                    foo(x*y/10+15*20*1.3, foo(1,2));
                }
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[BinaryOp(+,BinaryOp(/,BinaryOp(*,Id(x),Id(y)),IntLiteral(10)),BinaryOp(*,BinaryOp(*,IntLiteral(15),IntLiteral(20)),FloatLiteral(1.3))),CallExpr(Id(foo),[IntLiteral(1),IntLiteral(2)])])"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_TypeMismatchExpr_funcall_pass_lhs_bool_string(self):
        input = """
            int foo(boolean a, string b){
                string str;
                boolean flag;
                return 10;
            }
            void main(float a, int b, boolean c) {
                int x, y;
                if (c && false) {
                    foo(true && (c || (x > y)), foo(true,"2"));
                }
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[BinaryOp(&&,BooleanLiteral(true),BinaryOp(||,Id(c),BinaryOp(>,Id(x),Id(y)))),CallExpr(Id(foo),[BooleanLiteral(true),StringLiteral(2)])])"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_TypeMismatchExpr_funcall_pass_lhs_array(self):
        input = """
            int[] foo(int a[], int b){
                string str;
                boolean flag;
                return a;
            }
            void main(float a, int b, boolean c) {
                int x[5], y[10];
                if (c && false) {
                    foo(foo(x,b),c);
                }
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[CallExpr(Id(foo),[Id(x),Id(b)]),Id(c)])"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_TypeMismatchExpr_funcall_pass_lhs_array_pass_arraypointer(self):
        input = """
            float[] foo(int a[], int b[]){
                string str;
                float c[3];
                str = "PPL 3";
                boolean flag;
                flag = true || false;
                return c;
            }
            void main(int argc, int argv[]) {
                int x[0], y[5];
                float a[10];
                if (true && false) {
                    foo(foo(x,y),a);
                }
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[CallExpr(Id(foo),[Id(x),Id(y)]),Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_functionNotReturn_int(self):
        input = """
            int main(int array[]) {
                int max,i,length;
                max = array[0];
                for (i; i < length; i=i+1) {
                    if (max < array[i])
                        max = array[i];
                }
                putInt(max);
            }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_functionNotReturn_return_in_ifStmt(self):
        input = """
            int main() {
                int a, b, c, min;
                min = a;
                if (min > b) {
                    min = b;
                    return 0;
                }
                if (min > c) {
                    min = c;
                    return 1;
                }
                putInt(min);
            }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_functionNotReturn_else_not_return(self):
        input = """
            int main() {
                float a,b;
                if (a < b) {
                    putString("a less than b");
                    return 0;
                }
                else putString("a greater than b");
            }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_functionNotReturn_if_return(self):
        input = """
            boolean canWork() {
                int energy;
                if (energy == 0) return false;
            }
            void main() {
                if (!canWork())
                    putString("ppl so hard!");
                return;
            }
        """
        expect = "Function canWork Not Return "
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_functionNotReturn_if_nested(self):
        input = """
            int main(int a, int b){
                if (true) {
                    if (a == b) {
                        return 0;
                    }
                }
                else return 1;
            }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_functionNotReturn_return_in_for(self):
        input = """
            float[] main() {
                int a,b;
                float d[5];
                boolean c;
                for(a;c;b) {
                    return d;
                }
            }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_functionNotReturn_return_in_dowhile(self):
        input = """
            boolean[] foo() {
                int a,b;
                boolean d[5];
                boolean c;
                do {
                    return d;
                } while c && d[0] || d[1];
            }
            int main(){
                if (foo()[0]) putString("ppl very hard !!");
            }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_breakNotInLoop_in_func(self):
        input = """
            void main(){
                int i,j;
                for (i = 0; i < 10; i = i + 1) {
                    for (j = 10; j >= 0; j = j - 1) {
                        if (i == j) putIntLn(i);
                        break;
                    }
                }
                break;
            }  
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_breakNotInLoop_in_if(self):
        input = """
            int main(){
                int i,j;
                for (i = 0; i < 10; i = i + 1) {
                    for (j = 10; j >= 0; j = j - 1) {
                        if (i == j) return 0;
                        else return 1;
                    }
                }
                if (i == j) break;
                return j;
            } 
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_breakNotInLoop_in_dowhile(self):
        input = """
            int main(){
                int i,a;
                for (i = 0; i < 10; i = i + 1){
                    if (i == a % getInt()) break;
                    else continue;
                do 
                    break;
                while (i == 0);                
                }
                break;
                return 0;
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_continueNotInLoop_in_main(self):
        input = """
            int i;
            int f() {
                return 200;
            }
            void main () {
                int main ;
                main = f();
                putIntLn (main);
                {
                    int i;
                    int main;
                    int f;
                    main = f = i = 100;
                    putIntLn(i);
                    putIntLn(main);
                    putIntLn(f);
                }
                putIntLn(main);
                continue;
            } 
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_continueNotInLoop_in_else(self):
        input = """
            int[] foo(boolean a, float b){
                int c[5],d[10];
                if (c[0] >= 10) return c;
                else {
                    continue;
                    return d;
                }
            }
            int main() {
                putIntLn(foo(a>=b,00.E2019)[10]);
                return 0;
            }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_UnreachableFunction_explicit(self):
        input = """
            float foo() {
                return getFloat();
            }
            void main(){
                putString("ppl nearly done!!");
            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_unreachableFunction_callby_another(self):
        input = """
            boolean IsPrime(int number)
            {
                int i;
                for (i = 2; i < number; i = i + 1)
                {
                    if (number % i == 0 && i != number)
                        return false;
                }
                return true;
            }
            void foo(){
                putBool(IsPrime(15));
            }
            void main(){
                putBool(IsPrime(15));
            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_unreachableFunction_call_byself(self):
        input = """
            boolean IsPrime(int number)
            {
                int i;
                for (i = 2; i < number; i = i + 1)
                {
                    if (number % i == 0 && i != number)
                        return false;
                }
                return true;
            }
            void foo(){
                putBool(IsPrime(15));
                foo();
            }
            void main(){
                putBool(IsPrime(15));
            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_unreachableFunction_call_Indirect(self):
        input = """
            float[] foo1() {
                float a[10];
                foo2();
                return a;
            }
            int foo2() {
                if (1 == 5) return 1;
                else return 2;
            }
            void foo3() {
                putString("only 25 test!");
            }
            void main(){
                boolean flag;
                if (flag) {
                    foo1();
                }
                else foo1();
            }
        """
        expect = "Unreachable Function: foo3"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_notLeftValue_func_lhs(self):
        input = """
            void foo() {
                putString("only 24 test left!");
            }
            int main() {
                int i,a[10];
                putString("In cac so le:\\n");
                for(foo() = 1; i <= 10; i=i+1) {
                    if(i%2 != 0)
                        putInt(i);
                }
                return 0;
            }
        """
        expect = "Not Left Value: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_notLeftValue_add_op(self):
        input = """
            int main() {
                int year;
                year + 2 = 2016;                
                if (((year % 4 == 0) && (year % 100!= 0)) || (year%400 == 0))
                    putString("la mot nam nhuan");
                else
                    putString("khong phai la nam nhuan");                    
                return 0;
            }
        """
        expect = "Not Left Value: BinaryOp(+,Id(year),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_notLeftValue_intlit(self):
        input = """
            int tinhgiaithua(int i) {
                if(i <= 1)
                {
                    return 1;
                }
                return i * tinhgiaithua(i - 1);
            }
            int  main() {
                int i;
                10 = i;
                putString("Gia tri giai thua la");
                putInt(tinhgiaithua(i));            
                return 0;
            }
        """
        expect = "Not Left Value: IntLiteral(10)"
        self.assertTrue(TestChecker.test(input,expect,477))

    # def test_notLeftValue_(self):
    #     input = """
            
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,475))

    # def test_notLeftValue_(self):
    #     input = """
            
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,475))











