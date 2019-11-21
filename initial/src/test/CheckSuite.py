import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    # def test_no_entry_point(self):
    #     input = """
    #         int a,b;
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test_redeclared_variable(self):
    #     input = """
    #         int a,b;
    #         int a;
    #         int main() {
    #             return 0;
    #         }
    #     """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_redeclared_variable_after_main(self):
    #     input = """
    #         int a,b;            
    #         int main() {
    #             return 0;
    #         }
    #         int a;
    #     """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input,expect,403))
    
    # def test_redeclared_function(self):
    #     input = """
    #         int a,b;
    #         int a() {}
    #         int main() {
    #             return 0;
    #         }
    #     """
    #     expect = "Redeclared Function: a"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_redeclared_parameter(self):
    #     input = """
    #         int a,b;
    #         int c(int a, int a) {}
    #         int main(int a) {
    #             return 0;
    #         }
    #     """
    #     expect = "Redeclared Parameter: a"
    #     self.assertTrue(TestChecker.test(input,expect,405))

    # def test_redeclared_local_level2(self):
    #     input = """
    #         int a,b;
    #         int main(int a, int b) {                
    #             int b;
    #             return 0;
    #         }
    #     """
    #     expect = "Redeclared Variable: b"
    #     self.assertTrue(TestChecker.test(input,expect,406))

    # def test_redeclared_local_level3(self):
    #     input = """
    #         int a,b;
    #         int main(int a, int b) {                
    #            {
    #                 int a,b,c;
    #                 int a;
    #             }
    #             return 0;
    #         }
    #     """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input,expect,407))

    # def test_redeclared_local_level4(self):
    #     input = """
    #         int a,b;
    #         int main(int a, int b) {                
    #             {
    #                 int a,b,c;
    #                 {
    #                     int a,b,c;
    #                     int a;
    #                 }
    #             }
    #             return 0;
    #         }
    #     """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input,expect,408))

    # def test_Undeclared_function_level_2(self):
    #     input = """
    #         int a,b;
    #         int main(int a, int b) {                
    #             {
    #                 int a,b,c;
    #                 {
    #                     int a,b,c;
    #                     foo();
    #                 }
    #             }
    #             return 0;
    #         }
    #     """
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,409))

    # def test_Undeclared_functionStmt(self):
    #     input = """
    #         int a,b;
    #         int main(int a, int b) {                
    #             {
    #                 foo();
    #             }
    #             return 0;
    #         }
    #     """
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,410))

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


    def test_unrecha_funct_(self):
        """test unrechable function declared"""
        input = """
        float tfloat;
        float foo2(){
            float tfloat;
            return 1.e-3;
        }
        boolean foo(){
            return true;
        }
        boolean foo1(){
            return false;
        }
        int main(int argc, string args, boolean argv, float flo){
            if(1==1){
                return 0;
            }
            else{
                if(true){
                    foo();
                }
                else{
                    foo1();
                }
                return 0;
            }
        }
        """
        expect = "Unreachable Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,424))
        
    def test_unrecha_funct_2(self):
        """test unrechable function declared 2nd"""
        input = """
        float tfloat;
        float foo2(){
            float tfloat;
            boolean boo;
            foo1(foo());
            boo = foo() && foo1(foo());
            return 1.e-3;
        }
        boolean foo(){
            return foo1(foo());
        }
        boolean foo1(boolean b){
            return false;
        }
        int main(int argc, string args, boolean argv, float flo){
            if(1==1){
                return 0;
            }
            else{
                if(true){
                    foo();
                }
                else{
                    foo1(foo());
                }
                return 0;
            }
        }
        """
        expect = "Unreachable Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,425))
        
    def test_left_value_failed2(self):
        """test left value content id"""
        input = """
        float tfloat;
        float foo2(){
            float tfloat;
            boolean boo;
            return 1.e-3;
        }
        int main(int argc, string args, boolean argv, float flo){
            foo2();
            int c,b;
            b + c = 1;
            return 0;
        }
        """
        expect = "Not Left Value: BinaryOp(+,Id(b),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,428))
        
    
        
    # def test_left_value_failed5(self):
    #     """test left value content expression with call """
    #     input = """
    #     float tfloat[4];
    #     float foo2(){
    #         float tfloat;
    #         boolean boo;
    #         return 1.e-3;
    #     }
    #     int main(int argc, string args, boolean argv, float flo){
    #         //argc + tfloat[1] = 10.0;
    #         int some;
    #         foo2() + some = 0;
    #         return 0;
    #     }
    #     """
    #     expect = "Not Left Value: BinaryOp(+,CallExpr(Id(foo2),[]),Id(some))"
    #     self.assertTrue(TestChecker.test(input,expect,431))
        
    # def test_stmt_miss_mat1ch(self):
    #     """test left value statement return"""
    #     input = """
    #     float tfloat[4];
    #     float foo2(){
    #         float tfloat;
    #         boolean boo;
    #         return true;
    #     }
    #     int main(int argc, string args, boolean argv, float flo){
    #         //argc + tfloat[1] = 10.0;
    #         foo2();
    #         return 0;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
    #     self.assertTrue(TestChecker.test(input,expect,432))
        
    # def test_stmt_m2iss_mat1ch(self):
    #     """test left value exp string type"""
    #     input = """
    #     float tfloat[4];
    #     float foo2(){
    #         float tfloat;
    #         boolean boo;
    #         return 1.0;
    #     }
    #     int main(int argc, string args, boolean argv, float flo){
    #         //argc + tfloat[1] = 10.0;
    #         foo2();
    #         "str" = 0;
    #         return 0;
    #     }
    #     """
    #     expect = "Not Left Value: StringLiteral(str)"
    #     self.assertTrue(TestChecker.test(input,expect,433))
        
    # def test_stmt_miss2_mat1ch(self):
    #     """test left value exp booleantype"""
    #     input = """
    #     float tfloat[4];
    #     float foo2(){
    #         float tfloat;
    #         boolean boo;
    #         return 1.0;
    #     }
    #     int main(int argc, string args, boolean argv, float flo){
    #         //argc + tfloat[1] = 10.0;
    #         foo2();
    #         true = 0;
    #         return 0;
    #     }
    #     """
    #     expect = "Not Left Value: BooleanLiteral(true)"
    #     self.assertTrue(TestChecker.test(input,expect,434))
        
    # def test_stmt_miss3_mat1ch(self):
    #     """test left value expression corresponding bool->int"""
    #     input = """
    #     float tfloat[4];
    #     float foo2(){
    #         float tfloat;
    #         boolean boo;
    #         return 1.0;
    #     }
    #     int main(int argc, string args, boolean argv, float flo){
    #         //argc + tfloat[1] = 10.0;
    #         foo2();
    #         argc = true;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(=,Id(argc),BooleanLiteral(true))"
    #     self.assertTrue(TestChecker.test(input,expect,435))
        
    # def test_stmt_miss4_mat1ch(self):
    #     """test left value expression corresponding float->int"""
    #     input = """
    #     float tfloat[4];
    #     float foo2(){
    #         float tfloat;
    #         boolean boo;
    #         return 1.0;
    #     }
    #     int main(int argc, string args, boolean argv, float flo){
    #         //argc + tfloat[1] = 10.0;
    #         foo2();
    #         argc = flo;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(=,Id(argc),Id(flo))"
    #     self.assertTrue(TestChecker.test(input,expect,436))
        
    # def test_stmt_miss5_mat1ch(self):
    #     """test left value expression corresponding (expression float)->int"""
    #     input = """
    #     float tfloat[4];
    #     float foo2(){
    #         float tfloat;
    #         boolean boo;
    #         return 1.0;
    #     }
    #     int main(int argc, string args, boolean argv, float flo){
    #         //argc + tfloat[1] = 10.0;
    #         foo2();
    #         int x;
    #         x = 1 + 2 + 3 + 4 + 5 + 6 -1.3;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(=,Id(x),BinaryOp(-,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),IntLiteral(5)),IntLiteral(6)),FloatLiteral(1.3)))"
    #     self.assertTrue(TestChecker.test(input,expect,437))
        
    # def test_stmt_miss6_mat1ch(self):
    #     """test left value Statement corresponding return float[]->int[]"""
    #     input = """
    #     float tfloat[4];
    #     float foo2(){
    #         float tfloat;
    #         boolean boo;
    #         return 1.0;
    #     }
    #     int[] main(int argc, string args, boolean argv, float flo){
    #         //argc + tfloat[1] = 10.0;
    #         foo2();
    #         return tfloat;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Return(Id(tfloat))"
    #     self.assertTrue(TestChecker.test(input,expect,438))
        
    # def test_stmt_miss7_mat1ch(self):
    #     """test left value Statement corresponding return int[]->float[]"""
    #     input = """
    #     float tfloat[4];
    #     float foo2(){
    #         float tfloat;
    #         boolean boo;
    #         return 1.0;
    #     }
    #     float[] main(int argc[], string args, boolean argv, float flo){
    #         //argc + tfloat[1] = 10.0;
    #         foo2();
    #         int a[5];
    #         return a;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Return(Id(a))"
    #     self.assertTrue(TestChecker.test(input,expect,439))
        
    # def test_stmt_miss8_mat1ch(self):
    #     """test left value Statement corresponding float->float[]"""
    #     input = """
    #     float tfloat[4];
    #     float foo2(){
    #         float tfloat;
    #         boolean boo;
    #         return 1.0;
    #     }
    #     float[] main(int argc[], string args, boolean argv, float flo){
    #         //argc + tfloat[1] = 10.0;
    #         foo2();
    #         int a[5];
    #         return 1.1/1.0-10;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Return(BinaryOp(-,BinaryOp(/,FloatLiteral(1.1),FloatLiteral(1.0)),IntLiteral(10)))"
    #     self.assertTrue(TestChecker.test(input,expect,440))
    


    