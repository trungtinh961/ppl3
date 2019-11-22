# import unittest
# from TestUtils import TestChecker
# from AST import *

# class CheckSuite(unittest.TestCase):
#     # def test_no_entry_point(self):
#     #     input = """
#     #         int a,b;
#     #     """
#     #     expect = "No Entry Point"
#     #     self.assertTrue(TestChecker.test(input,expect,401))

#     # def test_redeclared_variable(self):
#     #     input = """
#     #         int a,b;
#     #         int a;
#     #         int main() {
#     #             return 0;
#     #         }
#     #     """
#     #     expect = "Redeclared Variable: a"
#     #     self.assertTrue(TestChecker.test(input,expect,402))

#     # def test_redeclared_variable_after_main(self):
#     #     input = """
#     #         int a,b;            
#     #         int main() {
#     #             return 0;
#     #         }
#     #         int a;
#     #     """
#     #     expect = "Redeclared Variable: a"
#     #     self.assertTrue(TestChecker.test(input,expect,403))
    
#     # def test_redeclared_function(self):
#     #     input = """
#     #         int a,b;
#     #         int a() {}
#     #         int main() {
#     #             return 0;
#     #         }
#     #     """
#     #     expect = "Redeclared Function: a"
#     #     self.assertTrue(TestChecker.test(input,expect,404))

#     # def test_redeclared_parameter(self):
#     #     input = """
#     #         int a,b;
#     #         int c(int a, int a) {}
#     #         int main(int a) {
#     #             return 0;
#     #         }
#     #     """
#     #     expect = "Redeclared Parameter: a"
#     #     self.assertTrue(TestChecker.test(input,expect,405))

#     # def test_redeclared_local_level2(self):
#     #     input = """
#     #         int a,b;
#     #         int main(int a, int b) {                
#     #             int b;
#     #             return 0;
#     #         }
#     #     """
#     #     expect = "Redeclared Variable: b"
#     #     self.assertTrue(TestChecker.test(input,expect,406))

#     # def test_redeclared_local_level3(self):
#     #     input = """
#     #         int a,b;
#     #         int main(int a, int b) {                
#     #            {
#     #                 int a,b,c;
#     #                 int a;
#     #             }
#     #             return 0;
#     #         }
#     #     """
#     #     expect = "Redeclared Variable: a"
#     #     self.assertTrue(TestChecker.test(input,expect,407))

#     # def test_redeclared_local_level4(self):
#     #     input = """
#     #         int a,b;
#     #         int main(int a, int b) {                
#     #             {
#     #                 int a,b,c;
#     #                 {
#     #                     int a,b,c;
#     #                     int a;
#     #                 }
#     #             }
#     #             return 0;
#     #         }
#     #     """
#     #     expect = "Redeclared Variable: a"
#     #     self.assertTrue(TestChecker.test(input,expect,408))

#     # def test_Undeclared_function_level_2(self):
#     #     input = """
#     #         int a,b;
#     #         int main(int a, int b) {                
#     #             {
#     #                 int a,b,c;
#     #                 {
#     #                     int a,b,c;
#     #                     foo();
#     #                 }
#     #             }
#     #             return 0;
#     #         }
#     #     """
#     #     expect = "Undeclared Function: foo"
#     #     self.assertTrue(TestChecker.test(input,expect,409))

#     # def test_Undeclared_functionStmt(self):
#     #     input = """
#     #         int a,b;
#     #         int main(int a, int b) {                
#     #             {
#     #                 foo();
#     #             }
#     #             return 0;
#     #         }
#     #     """
#     #     expect = "Undeclared Function: foo"
#     #     self.assertTrue(TestChecker.test(input,expect,410))

#     # def test_TypeMismatchInStmt_nonePara(self):
#     #     input = """
#     #         int a,b;
#     #         int foo(int a) {
#     #             return 0;
#     #         }
#     #         int main(int a, int b) {                
#     #             {
#     #                 foo();
#     #             }
#     #             return 0;
#     #         }
#     #     """
#     #     expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
#     #     self.assertTrue(TestChecker.test(input,expect,411))

#     # def test_TypeMismatchInStmt_manyPara(self):
#     #     input = """
#     #         int a,b;
#     #         int foo(int a) {
#     #             return 0;
#     #         }
#     #         int main(int a, int b) {                
#     #             {
#     #                 foo(a,b);
#     #             }
#     #             return 0;
#     #         }
#     #     """
#     #     expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a),Id(b)])"
#     #     self.assertTrue(TestChecker.test(input,expect,412))

#     # def test_TypeMismatchInStmt_partype_floatint(self):
#     #     input = """
#     #         int a,b;
#     #         int foo(int a) {
#     #             return 0;
#     #         }
#     #         int main(float a, int b) {                
#     #             foo(a);
#     #             return 0;
#     #         }
#     #     """
#     #     expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])"
#     #     self.assertTrue(TestChecker.test(input,expect,413))

#     # def test_TypeMismatchInStmt_partype_intbool(self):
#     #     input = """
#     #         int a,b;
#     #         int foo(int a) {
#     #             return 0;
#     #         }
#     #         int main(boolean a, int b) {                
#     #             foo(a);
#     #             return 0;
#     #         }
#     #     """
#     #     expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])"
#     #     self.assertTrue(TestChecker.test(input,expect,414))

#     # def test_Undeclared_IdLHS(self):
#     #     input = """
#     #         int a,b;
#     #         int main(float a, int b) {                
#     #             c = a + b
#     #         }
#     #     """
#     #     expect = "Undeclared Identifier: c"
#     #     self.assertTrue(TestChecker.test(input,expect,415))

#     # def test_Undeclared_IdRHS(self):
#     #     input = """
#     #         int a,b;
#     #         int main(float a, int b) {                
#     #             a = c + b
#     #         }
#     #     """
#     #     expect = "Undeclared Identifier: c"
#     #     self.assertTrue(TestChecker.test(input,expect,416))

#     def test_entry_width_Ovar(self):
#         """Test no entry with vardecl"""
#         input = """
#         int main, entry[10];
#         int mai1n(int argv, string argc){
#             return 0;
#         }
#         string str, s;
#         float tfloat;
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,400))

#     def test_entry_with_OFunc(self):
#         """Test noentry with funcdecl"""
#         input = """
#         string foo2(){return "10051999";}
#         int mai1n(int argv, string argc){
#             return 0;
#         }
#         float foo(){return 10051999;}
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,401))

#     def test_entry_with_FaV(self):
#         """test no entry with small vardecl-funcdecl"""
#         input = """
#         int main, entry[10];
#         string foo2(){return "10051999";}
#         int mai1n(int argv, string argc){
#             return 0;
#         }
#         string str, s;
#         float tfloat;
#         float foo(){return 10051999;}
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,402))

#     def test_entry_with_more_type1(self):
#         """test no entry with vardecl-funcdecl"""
#         input = """
#         int main, entry[10];
#         string foo2(){return "10051999";}
#         int mai1n(int argv, string argc){
#             return 0;
#         }
#         string str, s;float tfloat;float foo(){return 10051999;}
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,403))

#     def test_entry_with_more_type2(self):
#         """test no entry with vardecl-funcdecl"""
#         input = """
#         int main, entry[10];
#         string foo2(){return "10051999";}
#         int mai1n(int argv, string argc){
#             return 0;
#         }
#         string str, s; float tfloat;float foo(){return 10051999;}
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,404))

#     def test_entry_with_more_type3(self):
#         """test no entry with vardecl-funcdecl"""
#         input = """
#         int main, entry[10];float tfloat;
#         string foo2(){return "10051999";}
#         int mai1n(int argv, string argc){
#             return 0;
#         }
#         string str, s;float foo(){return 10051999;}
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,405))

#     def test_global_var_rede(self):
#         """test redecl global scope"""
#         input = """
#         int main1, entry[10];
#         float tfloat;
#         float main1;
#         string foo2(){return "10051999";}
#         int main(int argv, string argc){
#             return 0;
#         }
#         """
#         expect = "Redeclared Variable: main1"
#         self.assertTrue(TestChecker.test(input,expect,406))

#     def test_global_vWF_rede(self):
#         """test Redeclared function main"""
#         input = """
#         int main1, entry[10];
#         float tfloat;
#         float main;
#         string foo2(){return "10051999";}
#         int main(int argv, string argc){
#             return 0;
#         }
#         """
#         expect = "Redeclared Function: main"
#         self.assertTrue(TestChecker.test(input,expect,407))

#     def test_global_vWF1_rede(self):
#         """test redeclared function in global scope"""
#         input = """
#         int main1, entry[10];
#         float tfloat;
#         string foo2(){return "10051999";}
#         int main(int argv, string argc){
#             return 0;
#         }
#         void foo2(){}
#         """
#         expect = "Redeclared Function: foo2"
#         self.assertTrue(TestChecker.test(input,expect,408))

#     def test_global_vWF2_rede(self):
#         """test redeclared array scope"""
#         input = """
#         int main1, entry[10], entry;
#         float tfloat;
#         string foo2(){return "10051999";}
#         int main(int argv, string argc){
#             return 0;
#         }
#         void foo2(){}
#         """
#         expect = "Redeclared Variable: entry"
#         self.assertTrue(TestChecker.test(input,expect,409))

#     def test_global_para_rede(self):
#         """test redeclared parameter in main"""
#         input = """
#         float tfloat;
#         string foo2(){return "10051999";}
#         int main(int argv, string argc, boolean argv){
#             return 0;
#         }
#         """
#         expect = "Redeclared Parameter: argv"
#         self.assertTrue(TestChecker.test(input,expect,410))

#     def test_global_para_rede_1dift(self):
#         """test redeclared parameter in main 2"""
#         input = """
#         float tfloat;
#         string foo2(){return "10051999";}
#         int main(int argv, string argc, boolean argv){
#             return 0;
#         }
#         """
#         expect = "Redeclared Parameter: argv"
#         self.assertTrue(TestChecker.test(input,expect,411))

#     def test_global_para_rede_2dift(self):
#         """test redeclared another type parameter in main"""
#         input = """
#         float tfloat;
#         string foo2(){return "10051999";}
#         int main(int argc, string argc, boolean argv, float flo){
#             return 0;
#         }
#         """
#         expect = "Redeclared Parameter: argc"
#         self.assertTrue(TestChecker.test(input,expect,412))

#     def test_global_para_rede_3dift(self):
#         """test redeclared param inside"""
#         input = """
#         float tfloat;
#         string foo2(){return "10051999";}
#         int main(int argc, string flo, boolean argv, float flo){
#             return 0;
#         }
#         """
#         expect = "Redeclared Parameter: flo"
#         self.assertTrue(TestChecker.test(input,expect,413))

#     def test_global_val_rede(self):
#         """test redeclared local scope main"""
#         input = """
#         float tfloat;
#         string foo2(){
#             float tfloat;
#             return "10051999";
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             int argc, argc[2];
#             foo2();
#             return 0;
#         }
#         """
#         expect = "Redeclared Variable: argc"
#         self.assertTrue(TestChecker.test(input,expect,414))

#     def test_undecl_val_inside(self):
#         """test undeclared identifier only"""
#         input = """
#         float tfloat;
#         float foo2(){
#             float tfloat;
#             return 0.0;
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             flo = foo2();
#             Long;
#             return 0;
#         }
#         """
#         expect = "Undeclared Identifier: Long"
#         self.assertTrue(TestChecker.test(input,expect,415))

#     def test_undecl_val_outside(self):
#         """test undeclared identifier in expression"""
#         input = """
#         float tfloat;
#         float foo2(){
#             float tfloat;
#             return 1.e-3;
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             flo = foo2();
#             argc = argc + Trai;
#             return 0;
#         }
#         """
#         expect = "Undeclared Identifier: Trai"
#         self.assertTrue(TestChecker.test(input,expect,416))

#     def test_undecl_val_inde(self):
#         """test undeclared function in expression"""
#         input = """
#         float tfloat;
#         float foo2(){
#             float tfloat;
#             return 1.e-3;
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             argc = argc + foo(1);
#             return 0;
#         }
#         """
#         expect = "Undeclared Function: foo"
#         self.assertTrue(TestChecker.test(input,expect,417))

#     def test_not_return(self):
#         """test typemismatch in experssion call only"""
#         input = """
#         float tfloat;
#         float foo2(){
#             float tfloat;
#             return 1.e-3;
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             int foo2;
#             foo2();
#             return 0;
#         }
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo2),[])"
#         self.assertTrue(TestChecker.test(input,expect,418))

#     def test_not_retur1n(self):
#         """test function not return in path if only"""
#         input = """
#         float tfloat;
#         float foo2(){
#             float tfloat;
#             return 1.e-3;
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             foo2();
#             if(1==1){
#                 return 0;
#             }
#             for(1;true;1)
#                 return 0;
#         }
#         """
#         expect = "Function main Not Return "
#         self.assertTrue(TestChecker.test(input,expect,419))

#     def test_not_inloop1(self):
#         """test continue ouside loop"""
#         input = """
#         float tfloat;
#         float foo2(){
#             float tfloat;
#             return 1.e-3;
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             argc = argc + 1;
#             if(true){
#                 if (false){
#                     if(argc == 0){
#                         continue;
#                     }
#                 }
#             }
#             return 0;
#         }
#         """
#         expect = "Continue Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,420))

#     def test_not_inloop2(self):
#         """test break outside loop"""
#         input = """
#         float tfloat;
#         float foo2(){
#             float tfloat;
#             return 1.e-3;
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             if(1==1){
#                 return 0;
#             }
#             else{
#                 if(true){

#                 }
#                 else{
#                     break;
#                 }
#             }
#         }
#         """
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,421))

#     def test_not_inloop3(self):
#         """test continue ouside loop 2nd"""
#         input = """
#         float tfloat;
#         float foo2(){
#             float tfloat;
#             return 1.e-3;
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             if(1==1){
#                 return 0;
#             }
#             else{
#                 if(true){

#                 }
#                 else{
#                     continue;
#                 }
#             }
#         }
#         """
#         expect = "Continue Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,422))

#     def test_not_inloop4(self):
#         """test continue ouside loop 3rd"""
#         input = """
#         float tfloat;
#         float foo2(){
#             float tfloat;
#             return 1.e-3;
#         }
#         int main(int a, string args, boolean argv, float b){
#             b  = a*10/5+1;
#             continue;
#         }
#         """
#         expect = "Continue Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,423))

#     def test_unrecha_funct_(self):
#         """test unrechable function declared"""
#         input = """
#         float tfloat;
#         float foo2(){
#             float tfloat;
#             return 1.e-3;
#         }
#         boolean foo(){
#             return true;
#         }
#         boolean foo1(){
#             return false;
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             if(1==1){
#                 return 0;
#             }
#             else{
#                 if(true){
#                     foo();
#                 }
#                 else{
#                     foo1();
#                 }
#                 return 0;
#             }
#         }
#         """
#         expect = "Unreachable Function: foo2"
#         self.assertTrue(TestChecker.test(input,expect,424))
        
#     def test_unrecha_funct_2(self):
#         """test unrechable function declared 2nd"""
#         input = """
#         float tfloat;
#         float foo2(){
#             float tfloat;
#             boolean boo;
#             foo1(foo());
#             boo = foo() && foo1(foo());
#             return 1.e-3;
#         }
#         boolean foo(){
#             return foo1(foo());
#         }
#         boolean foo1(boolean b){
#             return false;
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             if(1==1){
#                 return 0;
#             }
#             else{
#                 if(true){
#                     foo();
#                 }
#                 else{
#                     foo1(foo());
#                 }
#                 return 0;
#             }
#         }
#         """
#         expect = "Unreachable Function: foo2"
#         self.assertTrue(TestChecker.test(input,expect,425))
        
#     def test_unrecha_funct_3(self):
#         """test unrechable function declared 3rd"""
#         input = """
#         float tfloat;
#         float foo2(){
#             float tfloat;
#             boolean boo;
#             foo1(foo());
#             boo = foo() && foo1(foo());
#             return 1.e-3;
#         }
#         boolean foo(){
#             return foo1(foo());
#         }
#         boolean foo1(boolean b){
#             return false;
#             float tfloat;
#             tfloat = foo2();
#         }
#         string nothing(){
#             return "Long";
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             return 0;
#         }
#         """
#         expect = "Unreachable Function: nothing"
#         self.assertTrue(TestChecker.test(input,expect,426))
        
#     def test_left_value_failed1(self):
#         """test left value content constraint"""
#         input = """
#         float tfloat;
#         float foo2(){
#             float tfloat;
#             boolean boo;
#             return 1.e-3;
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             foo2();
#             1+1=2;
#             return 0;
#         }
#         """
#         expect = "Not Left Value: BinaryOp(+,IntLiteral(1),IntLiteral(1))"
#         self.assertTrue(TestChecker.test(input,expect,427))
        
#     def test_left_value_failed2(self):
#         """test left value content id"""
#         input = """
#         float tfloat;
#         float foo2(){
#             float tfloat;
#             boolean boo;
#             return 1.e-3;
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             foo2();
#             int c,b;
#             b + c = 1;
#             return 0;
#         }
#         """
#         expect = "Not Left Value: BinaryOp(+,Id(b),Id(c))"
#         self.assertTrue(TestChecker.test(input,expect,428))
        
#     def test_left_value_failed3(self):
#         """test left value content type failed"""
#         input = """
#         float tfloat;
#         float foo2(){
#             float tfloat;
#             boolean boo;
#             return 1.e-3;
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             foo2();
#             main() = 0;
#             return 0;
#         }
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(main),[])"
#         self.assertTrue(TestChecker.test(input,expect,429))
        
#     def test_left_value_failed4(self):
#         """test left value content expression simple"""
#         input = """
#         float tfloat[4];
#         float foo2(){
#             float tfloat;
#             boolean boo;
#             return 1.e-3;
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             argc + tfloat[1] = 10.0;
#             //foo2() = 0;
#             return 0;
#         }
#         """
#         expect = "Not Left Value: BinaryOp(+,Id(argc),ArrayCell(Id(tfloat),IntLiteral(1)))"
#         self.assertTrue(TestChecker.test(input,expect,430))
        
#     def test_left_value_failed5(self):
#         """test left value content expression with call """
#         input = """
#         float tfloat[4];
#         float foo2(){
#             float tfloat;
#             boolean boo;
#             return 1.e-3;
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             //argc + tfloat[1] = 10.0;
#             int some;
#             foo2() + some = 0;
#             return 0;
#         }
#         """
#         expect = "Not Left Value: BinaryOp(+,CallExpr(Id(foo2),[]),Id(some))"
#         self.assertTrue(TestChecker.test(input,expect,431))
        
#     def test_stmt_miss_mat1ch(self):
#         """test left value statement return"""
#         input = """
#         float tfloat[4];
#         float foo2(){
#             float tfloat;
#             boolean boo;
#             return true;
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             //argc + tfloat[1] = 10.0;
#             foo2();
#             return 0;
#         }
#         """
#         expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
#         self.assertTrue(TestChecker.test(input,expect,432))
        
#     def test_stmt_m2iss_mat1ch(self):
#         """test left value exp string type"""
#         input = """
#         float tfloat[4];
#         float foo2(){
#             float tfloat;
#             boolean boo;
#             return 1.0;
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             //argc + tfloat[1] = 10.0;
#             foo2();
#             0 = 0;
#             return 0;
#         }
#         """
#         expect = "Not Left Value: IntLiteral(0)"
#         self.assertTrue(TestChecker.test(input,expect,433))
        
#     def test_stmt_miss2_mat1ch(self):
#         """test left value exp booleantype"""
#         input = """
#         float tfloat[4];
#         float foo2(){
#             float tfloat;
#             boolean boo;
#             return 1.0;
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             //argc + tfloat[1] = 10.0;
#             foo2();
#             1 = 0;
#             return 0;
#         }
#         """
#         expect = "Not Left Value: IntLiteral(1)"
#         self.assertTrue(TestChecker.test(input,expect,434))
        
#     def test_stmt_miss3_mat1ch(self):
#         """test left value expression corresponding bool->int"""
#         input = """
#         float tfloat[4];
#         float foo2(){
#             float tfloat;
#             boolean boo;
#             return 1.0;
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             //argc + tfloat[1] = 10.0;
#             foo2();
#             argc = true;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(=,Id(argc),BooleanLiteral(true))"
#         self.assertTrue(TestChecker.test(input,expect,435))
        
#     def test_stmt_miss4_mat1ch(self):
#         """test left value expression corresponding float->int"""
#         input = """
#         float tfloat[4];
#         float foo2(){
#             float tfloat;
#             boolean boo;
#             return 1.0;
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             //argc + tfloat[1] = 10.0;
#             foo2();
#             argc = flo;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(=,Id(argc),Id(flo))"
#         self.assertTrue(TestChecker.test(input,expect,436))
        
#     def test_stmt_miss5_mat1ch(self):
#         """test left value expression corresponding (expression float)->int"""
#         input = """
#         float tfloat[4];
#         float foo2(){
#             float tfloat;
#             boolean boo;
#             return 1.0;
#         }
#         int main(int argc, string args, boolean argv, float flo){
#             //argc + tfloat[1] = 10.0;
#             foo2();
#             int x;
#             x = 1 + 2 + 3 + 4 + 5 + 6 -1.3;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(=,Id(x),BinaryOp(-,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),IntLiteral(5)),IntLiteral(6)),FloatLiteral(1.3)))"
#         self.assertTrue(TestChecker.test(input,expect,437))
        
#     def test_stmt_miss6_mat1ch(self):
#         """test left value Statement corresponding return float[]->int[]"""
#         input = """
#         float tfloat[4];
#         float foo2(){
#             float tfloat;
#             boolean boo;
#             return 1.0;
#         }
#         int[] main(int argc, string args, boolean argv, float flo){
#             //argc + tfloat[1] = 10.0;
#             foo2();
#             return tfloat;
#         }
#         """
#         expect = "Type Mismatch In Statement: Return(Id(tfloat))"
#         self.assertTrue(TestChecker.test(input,expect,438))
        
#     def test_stmt_miss7_mat1ch(self):
#         """test left value Statement corresponding return int[]->float[]"""
#         input = """
#         float tfloat[4];
#         float foo2(){
#             float tfloat;
#             boolean boo;
#             return 1.0;
#         }
#         float[] main(int argc[], string args, boolean argv, float flo){
#             //argc + tfloat[1] = 10.0;
#             foo2();
#             int a[5];
#             return a;
#         }
#         """
#         expect = "Type Mismatch In Statement: Return(Id(a))"
#         self.assertTrue(TestChecker.test(input,expect,439))
        
#     def test_stmt_miss8_mat1ch(self):
#         """test left value Statement corresponding float->float[]"""
#         input = """
#         float tfloat[4];
#         float foo2(){
#             float tfloat;
#             boolean boo;
#             return 1.0;
#         }
#         float[] main(int argc[], string args, boolean argv, float flo){
#             //argc + tfloat[1] = 10.0;
#             foo2();
#             int a[5];
#             return 1.1/1.0-10;
#         }
#         """
#         expect = "Type Mismatch In Statement: Return(BinaryOp(-,BinaryOp(/,FloatLiteral(1.1),FloatLiteral(1.0)),IntLiteral(10)))"
#         self.assertTrue(TestChecker.test(input,expect,440))
        
#     def test_stmt_miss9_mat1ch(self):
#         """test left value Statement corresponding for condition"""
#         input = """
#         float tfloat[4];
#         float foo2(){
#             float tfloat;
#             boolean boo;
#             return 1.0;
#         }
#         float[] main(int argc[], string args, boolean argv, float flo){
#             //argc + tfloat[1] = 10.0;
#             foo2();
#             for(1;1;1)
#                 argc[1] = -10;
#         }
#         """
#         expect = "Type Mismatch In Statement: For(IntLiteral(1);IntLiteral(1);IntLiteral(1);BinaryOp(=,ArrayCell(Id(argc),IntLiteral(1)),UnaryOp(-,IntLiteral(10))))"
#         self.assertTrue(TestChecker.test(input,expect,441))
        
#     def test_stmt_miss10_mat1ch(self):
#         """test left value Statement corresponding for condition"""
#         input = """
#         float tfloat[4];
#         float foo2(){
#             float tfloat;
#             boolean boo;
#             return 1.0;
#         }
#         float[] main(int argc[], string args, boolean argv, float flo){
#             //argc + tfloat[1] = 10.0;
#             foo2();
#             for(10;false;true){
#                 argc[1] = 0;
#                 }
#         }
#         """
#         expect = "Type Mismatch In Statement: For(IntLiteral(10);BooleanLiteral(false);BooleanLiteral(true);Block([BinaryOp(=,ArrayCell(Id(argc),IntLiteral(1)),IntLiteral(0))]))"
#         self.assertTrue(TestChecker.test(input,expect,442))
        
#     def test_stmt_miss11_mat1ch(self):
#         """test left value exp corresponding string->array[int]"""
#         input = """
#         float tfloat[4];
#         float foo2(){
#             float tfloat;
#             boolean boo;
#             return 1.0;
#         }
#         float[] main(int argc[], string args, boolean argv, float flo){
#             //argc + tfloat[1] = 10.0;
#             foo2();
#             return tfloat;
#             do{
#                 int f;
#             }
#             while(argc[1] <= "10.1");
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(<=,ArrayCell(Id(argc),IntLiteral(1)),StringLiteral(10.1))"
#         self.assertTrue(TestChecker.test(input,expect,443))
        
#     def test_exp_miss12_mat1ch(self):
#         """test left value exp corresponding int->array[int]"""
#         input = """
#         float tfloat[4];
#         float[] main(int argc[], string args, boolean argv, float flo){
#             //argc + tfloat[1] = 10.0;
#             return tfloat;
#             do{
#                 int f;
#             }
#             while(argc[1] == 10.1);
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(==,ArrayCell(Id(argc),IntLiteral(1)),FloatLiteral(10.1))"
#         self.assertTrue(TestChecker.test(input,expect,444))
        
#     def test_stmt_miss13_mat1ch(self):
#         """test left value exp corresponding string->array[float]"""
#         input = """
#         float tfloat[4];
#         float[] main(int argc[], string args, boolean argv, float flo){
#             //argc + tfloat[1] = 10.0;
#             do{
#                 int f;
#             }
#             while(argv = true);
#             return args;
#         }
#         """
#         expect = "Type Mismatch In Statement: Return(Id(args))"
#         self.assertTrue(TestChecker.test(input,expect,445))
        
#     def test_exp_miss14_mat1ch(self):
#         """test left value exp corresponding boolean->array[int]"""
#         input = """
#         float tfloat[4];
#         float[] main(int argc[], string args, boolean argv, float flo){
#             //argc + tfloat[1] = 10.0;
#             do{
#                 int f;
#             }
#             while(argc[1] = true);
#             return args;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(argc),IntLiteral(1)),BooleanLiteral(true))"
#         self.assertTrue(TestChecker.test(input,expect,446))
        
#     def test_exp_miss15_mat1ch(self):
#         """test left value exp corresponding % with float"""
#         input = """
#         float tfloat[4];
#         void foo(){}
#         float[] main(int argc[], string args, boolean argv, float flo){
#             //argc + tfloat[1] = 10.0;
#             flo = argc[1] = argc[2] = argc[3];
#             foo();
#             do{
#                 int f;
#             }
#             while(argc[0]%10.1);
            
#             return tfloat;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(%,ArrayCell(Id(argc),IntLiteral(0)),FloatLiteral(10.1))"
#         self.assertTrue(TestChecker.test(input,expect,447))
        
#     def test_stmy_miss0_mat1ch(self):
#         """test left value exp corresponding if type"""
#         input = """
#         float tfloat[4];
#         void foo(){}
#         float[] main(int argc[], string args,
#          boolean argv, float flo){
#             //argc + tfloat[1] = 10.0;
#             return tfloat;
#             if(1 == 2){
#                 if (true == false){
#                     return tfloat;
#                 }

#             }
#             else {
#                 if (argc[1] + 10)
#                 {
#                     return tfloat;
#                 }
#             }
#             foo();
#         }
#         """
#         expect = "Type Mismatch In Statement: If(BinaryOp(+,ArrayCell(Id(argc),IntLiteral(1)),IntLiteral(10)),Block([Return(Id(tfloat))]))"
#         self.assertTrue(TestChecker.test(input,expect,448))
        
#     def test_stmt_miss0_mat1ch(self):
#         """test left value exp corresponding return string->float[]"""
#         input = """
#         float tfloat[4];
#         void foo(){}
#         float[] main(int argc[],
#          string args, boolean argv, float flo){
#             //argc + tfloat[1] = 10.0;
#             if(1 == 2){
#                 if (true == false){
#                     return tfloat;
#                 }
#             }
#             else {
#                 if (true)
#                 {
#                     return tfloat;
#                 }
#             }
#             foo();
#             return args;
#         }
#         """
#         expect = "Type Mismatch In Statement: Return(Id(args))"
#         self.assertTrue(TestChecker.test(input,expect,449))
        
#     def test_exp_mismatch(self):
#         """test left value exp corresponding ! with not booleantype"""
#         input = """
#         float tfloat[4];
#         void foo(){}
#         float[] main(int argc[], 
#         string args, boolean argv, float flo){
#             int a;
#             a = !true + !false + !1;
#             foo();
#             return tfloat;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(+,UnaryOp(!,BooleanLiteral(true)),UnaryOp(!,BooleanLiteral(false)))"
#         self.assertTrue(TestChecker.test(input,expect,450))
        
#     def test_exp_mismatch1(self):
#         """test left value exp corresponding - with not int & float"""
#         input = """
#         float tfloat[4];
#         void foo(){}
#         float[] main(int 
#         argc[], string args, boolean argv, float flo){
#             int a;
#             a = 1 -- 10 --20 -- 30.0 - -true;
#             foo();
#             return tfloat;
#         }
#         """
#         expect = "Type Mismatch In Expression: UnaryOp(-,BooleanLiteral(true))"
#         self.assertTrue(TestChecker.test(input,expect,451))
        
#     def test_exp_mismatch2(self):
#         """test left value exp corresponding string->array[float]"""
#         input = """
#         float tfloat[4];
#         void foo(){}
#         float[] main(int argc[], string args, boolean argv, float flo){
#             int a;
#             a = argc[0] + --10 --20 -- 30.0;
#             foo();
#             return tfloat;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(-,BinaryOp(-,BinaryOp(+,ArrayCell(Id(argc),IntLiteral(0)),UnaryOp(-,UnaryOp(-,IntLiteral(10)))),UnaryOp(-,IntLiteral(20))),UnaryOp(-,FloatLiteral(30.0))))"
#         self.assertTrue(TestChecker.test(input,expect,452))
        
#     def test_exp_mismatch3(self):
#         """test left value exp corresponding expwith string & int"""
#         input = """
#         float tfloat[4];
#         void foo(){}
#         float[] main(int argc[], string args, boolean argv, 
#         float flo){
#             int a;
#             a = args + -- 10 --20 -- 30.0;
#             foo();
#             return tfloat;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(+,Id(args),UnaryOp(-,UnaryOp(-,IntLiteral(10))))"
#         self.assertTrue(TestChecker.test(input,expect,453))

#     def test_exp_mis_somematch4(self):
#         """test left value exp corresponding string->float"""
#         input = """
#         float tfloat[4];
#         void foo(){}
#         float[] main(int argc[], 
#         string args, boolean argv, float flo){
#             int a;
#             flo = 1.1;
#             flo = 1.0;
#             flo = "LongDepTrai";
#             foo();
#             return tfloat;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(=,Id(flo),StringLiteral(LongDepTrai))"
#         self.assertTrue(TestChecker.test(input,expect,454))

#     def test_exp_mis_somematch5(self):
#         """test left value exp corresponding - with booleantype"""
#         input = """
#         float tfloat[4];
#         void foo(){}
#         float[] main(int argc[], 
#         string args, boolean argv, float flo){
#             int a;
#             flo = 1.1;
#             flo = 1.0;
#             flo = 1+2-3*4/5%-argv;
#             foo();
#             return tfloat;
#         }
#         """
#         expect = "Type Mismatch In Expression: UnaryOp(-,Id(argv))"
#         self.assertTrue(TestChecker.test(input,expect,455))

#     def test_exp_mismatc_someh6(self):
#         """test left value exp corresponding - with boolean"""
#         input = """
#         float tfloat[4];
#         void foo(){}
#         float[] main(int argc[], string args, 
#         boolean argv, float flo){
#             int a;
#             flo = 1.1;
#             flo = 1.0;
#             flo = 1+2-3*4/5%-!argv;
#             foo();
#             return args;
#         }
#         """
#         expect = "Type Mismatch In Expression: UnaryOp(-,UnaryOp(!,Id(argv)))"
#         self.assertTrue(TestChecker.test(input,expect,456))

#     def test_exp_mismat_somech7(self):
#         """test left value exp corresponding string + string"""
#         input = """
#         float tfloat[4];
#         void foo(){}
#         float[] main(int argc[], string args, boolean argv, float flo){
#             int a;
#             flo = 1.1;
#             flo = 1.0;
#             args = "Long" + 
#             "Is" +"Very"+"HandSome";
#             foo();
#             return args;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(+,StringLiteral(Long),StringLiteral(Is))"
#         self.assertTrue(TestChecker.test(input,expect,457))

#     def test_exp_mismat8ch_some(self):
#         """test left value exp corresponding boolean => int"""
#         input = """
#         float tfloat[4];
#         void foo(){}
#         float[] main(int 
#         argc[], string args, boolean argv, float flo){
#             int a;
#             flo = 1.1;
#             flo = 1.0;
#             argv = true;
#             argv = !(true&&false||true>=10);
#             foo();
#             return argv;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(true),IntLiteral(10))"
#         self.assertTrue(TestChecker.test(input,expect,458))

#     def test_exp_9mismatch_some(self):
#         """test left value exp corresponding boolean || int"""
#         input = """
#         float tfloat[4];
#         void foo(){}
#         float[] main(int argc[], string args, boolean argv, float flo){
#             int a;
#             flo = 1.1;
#             flo = 1.0;
#             argv = 1 < 2 -!(true||1.0);
#             foo();
#             return argv;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(||,BooleanLiteral(true),FloatLiteral(1.0))"
#         self.assertTrue(TestChecker.test(input,expect,459))

#     def test_exp10_mismatch_some(self):
#         """test left value exp corresponding operator - with boolean"""
#         input = """
#         float tfloat[4];
#         void foo(){}
#         float[] main(int argc[], string args, boolean argv, float flo){
#             int a;
#             flo = 1.1;
#             flo = 1.0;
#             argv = 1 < 2 -!(true||((((((((((!false))))))))))&&1);
#             foo();
#             return argv;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(&&,UnaryOp(!,BooleanLiteral(false)),IntLiteral(1))"
#         self.assertTrue(TestChecker.test(input,expect,460))

#     def test_exp11_mismatch_some(self):
#         """test left value exp corresponding arrayPointer => array"""
#         input = """
#         float tfloat[4];
#         //float[] foo(){return tfloat;}
#         float[] foo2(){return tfloat;}
#         float[] main(int argc[], string args, boolean argv, float flo){
#             float f[10];
#             f = foo2();
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(=,Id(f),CallExpr(Id(foo2),[]))"
#         self.assertTrue(TestChecker.test(input,expect,461))

#     def test_exp_mis12match_some(self):
#         """test left value exp corresponding string + string -> string"""
#         input = """
#         float tfloat[4];
#         //float[] foo(){return tfloat;}
#         //float[] foo2(){return tfloat;}
#         float[] main(int argc[], string args, boolean argv, float flo){
#             float f[10];
#             args = "123"+"234";
#             return tfloat;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(+,StringLiteral(123),StringLiteral(234))"
#         self.assertTrue(TestChecker.test(input,expect,462))

#     def test_exp_mis13match_some(self):
#         """test left value is intType"""
#         input = """
#         float tfloat[4];
#         //float[] foo(){return tfloat;}
#         float[] foo2(

#         ){
#             return tfloat;
#             }
#         int foo(){
#             return 1;
#         }
#         float[] main(int argc[], string args, boolean argv, float flo){
#             float f[10];
#             foo2()[2] = 123456;
#             foo() = 1;
#             return tfloat;
#         }
#         """
#         expect = "Not Left Value: CallExpr(Id(foo),[])"
#         self.assertTrue(TestChecker.test(input,expect,463))

#     def test_exp_mis14match_some(self):
#         """test left value is void type"""
#         input = """
#         float tfloat[4];
#         void test(){}
#         float[] main(int argc[], string args, boolean argv, float flo){
#             float f[10];
#             test() = 123321;
#             return tfloat;
#         }
#         """
        
#         expect = "Not Left Value: CallExpr(Id(test),[])"
#         self.assertTrue(TestChecker.test(input,expect,464))

#     def test_exp_mismatch15_some(self):
#         """test continue outside"""
#         input = """
#         float tfloat[4];
#         float[] Function(float a[], float b[]){return tfloat;}

#         float[] main(int argc[], string args, boolean argv, float flo){

#             Function(tfloat, Function(tfloat, tfloat));
            
#             continue;
#             return tfloat;
#         }
#         """
#         expect = "Continue Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,465))

#     def test_exp_mismatch16_some(self):
#         """test index is float"""
#         input = """
#         float tfloat[4];
#         void test(){}
#         //float[] foo2(){return tfloat;}
#         float[] main(int argc[], 
#         string args,
#          boolean argv, float flo){
#             float f[10];
#             f[argc[1]*10/3+1.1];
#             return tfloat;
#         }
#         """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(f),BinaryOp(+,BinaryOp(/,BinaryOp(*,ArrayCell(Id(argc),IntLiteral(1)),IntLiteral(10)),IntLiteral(3)),FloatLiteral(1.1)))"
#         self.assertTrue(TestChecker.test(input,expect,466))

#     def test_exp_mismatch17_some(self):
#         """test index is booleantype"""
#         input = """
#         float tfloat[4];
#         void test(){}
#         //float[] foo2(){return tfloat;}
#         float[] main(int argc[], string args, boolean argv, float flo){
#             float f[10];
#             f[!!!!!true];
#             return tfloat;
#         }
#         """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(f),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,BooleanLiteral(true)))))))"
#         self.assertTrue(TestChecker.test(input,expect,467))

#     def test_exp_mismatch18_some(self):
#         """test index is stringtype"""
#         input = """
#         float tfloat[4];
#         void test(){}
#         //float[] foo(){return tfloat;}
#         //float[] foo2(){return tfloat;}
#         float[] main(int argc[], string args, boolean argv, float flo){
#             float f[10];
#             f["LongLML"];
#             return tfloat;
#         }
#         """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(f),StringLiteral(LongLML))"
#         self.assertTrue(TestChecker.test(input,expect,468))

#     def test_exp_mismatch19_some(self):
#         """test mismatch expression call different length param"""
#         input = """
#         float tfloat[4];
#         void test(){}
#         float[] foo(){return tfloat;}
#         float[] foo2(){return tfloat;}
#         float[] main(int argc[], string args, boolean argv, float flo){
#             float f[10];
#             foo2(foo(3));
#             return tfloat;
#         }
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(3)])"
#         self.assertTrue(TestChecker.test(input,expect,469))
        
#     def test_exp_mismatch20_some(self):
#         """test mismatch expression call different length param"""
#         input = """
#         float tfloat[4];
#         void test(){}
#         float[] foo(){return tfloat;}
#         float[] foo2(){return tfloat;}
#         float[] main(int argc[], string args, boolean argv, float flo){
#             float f[10];
#             foo2(foo(),1,2,3);
#             return tfloat;
#         }
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo2),[CallExpr(Id(foo),[]),IntLiteral(1),IntLiteral(2),IntLiteral(3)])"
#         self.assertTrue(TestChecker.test(input,expect,470))
        
#     def test_deep_block_decl(self):
#         """test redeclared with scope 1st"""
#         input = """
#         int i;
#         float f;
#         string str;
#         boolean boo;
#         void main(int argc[], string args, boolean argv, float flo){
#             string str,str2;
#             {
#                 string str2;
#                 {
#                     boolean str2;
#                     {
#                         float str2;
#                     }
#                 }
#             }
#             int str;
#         }
#         """
#         expect = "Redeclared Variable: str"
#         self.assertTrue(TestChecker.test(input,expect,471))
        
#     def test_deep_block_return(self):
#         """test break with scope"""
#         input = """
#         int i;
#         float f;
#         string str;
#         boolean boo;
#         float main(int argc[], string args, boolean argv, float flo){
#             string str,str2;
#             {
#                 string str2;
#                 {
#                     boolean str2;
#                     {
#                         return 0;
#                     }
#                 }
#             }
#             break;
#         }
#         """
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,472))
        
#     def test_deep_block_if(self):
#         """test return with path"""
#         input = """
#         int i;
#         float f;
#         string str;
#         boolean boo;
#         float main(int argc[], string args, boolean argv, float flo){
#             if(true){
#                 if(false){
#                     if(true)
#                         return 0;

#                 }
#                 return 0;
#             }
#             else
#                 if(argv){
#                     return 0;
#                 }
#         }
#         """
#         expect = "Function main Not Return "
#         self.assertTrue(TestChecker.test(input,expect,473))
        
#     def test_deep_block_if2(self):
#         """test return with execute path 2rd"""
#         input = """
#         int i;
#         float f;
#         string str;
#         boolean boo;
#         int main(){
#             if(true){
#                 if(boo){
#                     {{return 0;}}
#                 }
#                 else{
#                     return 0;
#                 }
#             }
#             else{
#                 if(boo){
#                     return 0;
#                 }
#                 else{
#                     return 1;
#                 }
#             }
#             foo();
#         }
#         int foo(){
#             return 1.1;
#         }
#         """
#         expect = "Type Mismatch In Statement: Return(FloatLiteral(1.1))"
#         self.assertTrue(TestChecker.test(input,expect,474))
        
#     def test_deep_block_if3(self):
#         """test statement return string"""
#         input = """
#         int i;
#         float f;
#         string str;
#         boolean boo;
#         int main(){
#             if(true)
#                 if(true)
#                     if(true)
#                         if(true) return 1;
#                         else return 0;
#                     else return 0;
#                 else return 0;
#             else return 0;
#         }
#         int foo(){
#             return "string";
#         }
#         """
#         expect = "Type Mismatch In Statement: Return(StringLiteral(string))"
#         self.assertTrue(TestChecker.test(input,expect,475))
        
#     def test_deep_block_if4(self):
#         """test statement return execute path"""
#         input = """
#         int i;
#         float f;
#         string str;
#         boolean boo;
#         int main(){
#             if(true){
#                 if(true){
#                     return 0;
#                 }
#                 else{
#                     if(true){
#                         return 0;
#                     }
#                     else{
#                         return 0;
#                     }
#                 }
#             }
            
#             for(1;true;1)
#                 return 0;
#         }
#         """
#         expect = "Function main Not Return "
#         self.assertTrue(TestChecker.test(input,expect,476))
        
#     def test_deep_block_declared(self):
#         """test undeclared with scope"""
#         input = """
#         int i;
#         float f;
#         string str;
#         boolean boo;
#         int main(){
#             {
#                 int c;
#                 {
#                     int a;
#                     {
#                         return 0;
#                     }
#                     a;
#                 }
#                 c;
#             }
#             a;
#         }
#         """
#         expect = "Undeclared Identifier: a"
#         self.assertTrue(TestChecker.test(input,expect,477))
        
#     def test_deep_block_declared_twice(self):
#         """test statement value with scope"""
#         input = """
#         int i;
#         float f;
#         string str;
#         boolean boo;
#         int main(){
#             float c;
#             {
#                 int c;
#                 {
#                     boolean c;
#                     {
#                         string c;
#                         c = "Long Dep Trai";
#                     }
#                     !c;
#                 }
#                 c = c%10;
#             }
#             boo = !(c >= 10);
#             return c/1.1;
#         }
#         """
#         expect = "Type Mismatch In Statement: Return(BinaryOp(/,Id(c),FloatLiteral(1.1)))"
#         self.assertTrue(TestChecker.test(input,expect,478))
        
#     def test_deep_block_declared_tri(self):
#         """test statement return float->int"""
#         input = """
#         int i;
#         float f;
#         string str;
#         boolean boo;
#         int main(){
#             {
#                 int f; boolean i;
#                 {
#                     f = f%10;
#                 }
#                 i = true&&false||(10<=5);
#             }
#             return f/.1;
#         }
#         """
#         expect = "Type Mismatch In Statement: Return(BinaryOp(/,Id(f),FloatLiteral(0.1)))"
#         self.assertTrue(TestChecker.test(input,expect,479))
        
#     def test_deep_block_declared_4th(self):
#         """test statement return execute path true"""
#         input = """
#         int i;
#         float f;
#         string str;
#         boolean boo;
#         int main(){
#             int LongLML;
#             {
#                 int f; boolean i;
#                 {
#                     f = f%10;
#                 }
#                 i = true&&false||(10<=5);
#             }
#             return i;
#         }
#         float foo(){
#             if (true){
#                 return 0;
#             }
#             else{
#                 return 1;
#             }
#             LongLML = 10;
#         }
#         """
#         expect = "Undeclared Identifier: LongLML"
#         self.assertTrue(TestChecker.test(input,expect,480))
        
#     def test_deep_block_declared_5th(self):
#         """test break stmt outside loop deep block"""
#         input = """
#         int i;
#         float f;
#         string str;
#         boolean boo;
#         int main(){
#             int LongLML;
#             {
#                 int f; boolean i;
#                 {
#                     {{{{{{{{string str;return f;}}}}}}}}
#                 }
#                 i = true&&false||(10<=5);
#             }
#             break;
#         }
#         """
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,481))
        
#     def test_deep_block_do_1st(self):
#         """test deep do-while if-else"""
#         input = """
#         int i;
#         float f;
#         string str;
#         boolean boo;
#         int main(){
#             int str;
#             do 
#             do 
#             do 
#             if(true) return 0; else return 1; 
#             while(true);
#             while(true);
#             while(true);
#         }
#         int foo(){
#             return Long;
#         }
#         """
#         expect = "Undeclared Identifier: Long"
#         self.assertTrue(TestChecker.test(input,expect,482))
        
#     def test_deep_block_do_2rd(self):
#         """test function not return with float Epointer"""
#         input = """
#         int i;
#         float f;
#         string str;
#         boolean boo;
#         int main(){
#             int str;
#             do{
#                 if(false){
#                     if(true){
#                         if (1 <= 10){
#                             return 10;
#                         }
#                         else {
#                             continue;
#                         }
#                     }
#                     else{
#                         break;
#                     }
#                 }
#             }while(true);
#             return 1e4;
#         }
#         void foo(){
#             return ;
#         }
#         """
#         expect = "Type Mismatch In Statement: Return(FloatLiteral(10000.0))"
#         self.assertTrue(TestChecker.test(input,expect,483))
        
#     def test_deep_block_do_3nd(self):
#         """test continue stmt outside loop deep block"""
#         input = """
#         int i;
#         float f;
#         string str;
#         boolean boo;
#         int main(){
#             int str;
#             do{
#                 if(false){
#                     if(true){
#                         if (1 <= 10){
#                             return 10;
#                         }
#                         else {
#                             continue;
#                         }
#                     }
#                     else{
#                         break;
#                     }
#                 }
#             }while(true);
#             return 1;
#         }
#         void foo(){
#             continue;
#             return ;
#         }
#         """
#         expect = "Continue Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,484))
        
#     def test_deep_block_do_4th(self):
#         """test break stmt outside loop deep block"""
#         input = """
#         int i;
#         float f;
#         string str;
#         boolean boo;
#         int main(){
#             int str;
#             do{
#                 if(false){
#                     if(true){
#                         if (1 <= 10){
#                             return 10;
#                         }
#                         else {
#                             continue;
#                         }
#                     }
#                     else{
#                     }
#                 }
#             }while(true);
#             break;
#             return 1;
#         }
#         """
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,485))
        
#     def test_deep_block_do_5th(self):
#         """test stmt for expr"""
#         input = """
#         int i;
#         float f;
#         string str;
#         boolean boo;
#         int main(){
#             for(10;true;1e1){
#                 "haha";
#             }
#         }
#         """
#         expect = "Type Mismatch In Statement: For(IntLiteral(10);BooleanLiteral(true);FloatLiteral(10.0);Block([StringLiteral(haha)]))"
#         self.assertTrue(TestChecker.test(input,expect,486))
        
#     def test_unrechable_func_1st(self):
#         """test unrechable function recursive"""
#         input = """
#         void foo(){}
#         void foo1(){foo();}
#         void foo2(){foo1();}
#         void foo3(){foo2(); foo3();}
#         int main(){
#             do
#                 return 1;
#             while(true);
#         }
#         """
#         expect = "Unreachable Function: foo3"
#         self.assertTrue(TestChecker.test(input,expect,487))
        
#     def test_unrechable_func_2nd(self):
#         """test call exp  failed"""
#         input = """
#         void foo(){}
#         void foo1(){foo();}
#         void foo2(){foo2();}
#         void foo3(){foo3();}
#         int main(){
#             foo1();
#             foo3();
#             float foo3;
#             foo3();
#             do
#                 return 1;
#             while(true);
#         }
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo3),[])"
#         self.assertTrue(TestChecker.test(input,expect,488))
        
#     def test_unrechable_func_3rd(self):
#         """test call stmt failed"""
#         input = """
#         void foo(){}
#         void foo1(){foo();}
#         void foo2(boolean f){foo2(foo3());}
#         boolean foo3(){return foo3();}
#         int main(){
#             foo1();
#             float main;
#             main = 1e10-10e1;
#             string foo2;
#             foo2(true);
#             do
#                 return 1;
#             while(true);
#         }
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo2),[BooleanLiteral(true)])"
#         self.assertTrue(TestChecker.test(input,expect,489))

#     def test_all_check_1st(self):
#         """test large code example expression failed 1st"""
#         input = """
#         void println(string str){}
#         void save(int len){}
#         void main(){
#             int TimeRemaining,len,Per;
#                     println("How many incorrect times do you want to get? ");
#                     save(TimeRemaining);
#                     println("what minimum word lengh do you want? ");
#                     save(len);
#                     //fstream f;
#                     //f.open("input.txt",ios::in);
#                     string data;
#                     string List[255];
#                     int NumOfWord,n;
#                     List[-1] = "1005199"&&Per;
#                     NumOfWord=0;
#             }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(&&,StringLiteral(1005199),Id(Per))"
#         self.assertTrue(TestChecker.test(input,expect,490))

#     def test_all_check_2nd(self):
#         """test large code example expression failed 2nd"""
#         input = """
#         void println(string str){}
#         void save(int len){}
#         void getline(int l, int data){}
#         void main(){
#             int data,f,NumOfWord;
#             string List[255];
#             do{
#                         getline(f,data);
#                         if (data!=1) List[NumOfWord]=data;

#                     }while(data!=1);
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(List),Id(NumOfWord)),Id(data))"
#         self.assertTrue(TestChecker.test(input,expect,491))

#     def test_all_check_3rd(self):
#         """test large code example stmt failed 3rd"""
#         input = """
#         //void println(string str){}
#         //void save(int len){}
#         void getline(int l, int data){}
#         void main(){
#             int data,f,NumOfWord;
#             string List[255];
#             do{
#                 getline(f,data);
#             }while(data!=1);
#             for(1;true;1){
#                 return 0;
#             }
#         }
#         """
#         expect = "Type Mismatch In Statement: Return(IntLiteral(0))"
#         self.assertTrue(TestChecker.test(input,expect,492))

#     def test_all_check_4th(self):
#         """test large code example break failed 4th"""
#         input = """
#         //void println(string str){}
#         //void save(int len){}
#         void getline(int l, int data){}
#         void main(){
#             int data,f,NumOfWord;
#             string List[255];
#             do{
#                 getline(f,data);
#             }while(data!=1);
#             for(1;true;1){
#                 return;
#             }
#             if(true){
#                 break;
#             }
#         }
#         """
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,493))

#     def test_all_check_5th(self):
#         """test large code example return failed 5th"""
#         input = """
#         //void println(string str){}
#         //void save(int len){}
#         void getline(int l, int data){}
#         int main(){
#             int data,f,NumOfWord;
#             string List[255];
#             do{
#                 getline(f,data);
#             }while(data!=1);
#             for(1;true;1){
#                 boolean b;
#                 b = !true&&false||(10.1>10);
#             }
#             if(true){
#                 return 0;
#             }
#             for(1;true;1)
#                 return 0;
#         }
#         """
#         expect = "Function main Not Return "
#         self.assertTrue(TestChecker.test(input,expect,494))

#     def test_all_check_6th(self):
#         """test large code example declared failed 6th"""
#         input = """
#         //void println(string str){}
#         //void save(int len){}
#         void getline(int l, int data){}
#         int main(float flo){
#             int data,f,NumOfWord;
#             string List[255];
#             do{
#                 getline(f,data);
#             }while(data!=1);
#             for(1;true;1){
#                 boolean b;
#                 b = !true&&false||(10.1>10);
#             }
#             if(true){
#                 return 0;
#             }
#             else{
#                 return 0;
#             }
#             int flo;
#         }
#         """
#         expect = "Redeclared Variable: flo"
#         self.assertTrue(TestChecker.test(input,expect,495))

#     def test_all_check_7th(self):
#         """test large code example left expression failed 7th"""
#         input = """
#         //void println(string str){}
#         //void save(int len){}
#         void getline(int l, int data){}
#         int main(float flo){
#             int data,f,NumOfWord;
#             string List[255];
#             do{
#                 getline(f,data);
#             }while(data!=1);
#             for(1;true;1){
#                 boolean b;
#                 b = !true&&false||(10.1>10);
#             }
#             if(true){
#                 return 0;
#             }
#             else{
#                 return 0;
#             }
#             10.1=-10;
#         }
#         """
#         expect = "Not Left Value: FloatLiteral(10.1)"
#         self.assertTrue(TestChecker.test(input,expect,496))

#     def test_all_check_8th(self):
#         """test large code example left undeclared indentifier failed 8th"""
#         input = """
#         //void println(string str){}
#         //void save(int len){}
#         void getline(int l, int data){}
#         int main(float flo){
#             int data,f,NumOfWord;
#             string List[255];
#             do{
#                 getline(f,data);
#             }while(data!=1);
#             for(1;true;1){
#                 boolean b;
#                 b = !true&&false||(10.1>10);
#             }
#             if(true){
#                 return 0;
#             }
#             else{
#                 return 0;
#             }
#             floas;

#         }
#         """
#         expect = "Undeclared Identifier: floas"
#         self.assertTrue(TestChecker.test(input,expect,497))

#     def test_all_check_9th(self):
#         """test large code example left expression failed 7th"""
#         input = """
#         //void println(string str){}
#         //void save(int len){}
#         void getline(int l, int data){}
#         int main(float flo){
#             int data,f,NumOfWord;
#             string List[255];
#             do{
#                 getline(f,data);
#             }while(data!=1);
#             for(1;true;1){
#                 boolean b;
#                 b = !true&&false||(10.1>10);
#             }
#             if(true){
#                 return 0;
#             }
#             else{
#                 return 0;
#             }
#             flo + data = 10;
#         }
#         """
#         expect = "Not Left Value: BinaryOp(+,Id(flo),Id(data))"
#         self.assertTrue(TestChecker.test(input,expect,498))

#     def test_all_check_10th(self):
#         """test large code example left stmt return failed 7th"""
#         input = """
#         //void println(string str){}
#         //void save(int len){}
#         // void reduce
#         void getline(int l, int data){}
#         int main(float flo){
#             int data,f,NumOfWord;
#             string List[255];
#             do{
#                 getline(f,data);
#             }while(data!=1);
#             for(1;true;1){
#                 boolean b;
#                 b = !true&&false||(10.1>10);
#             }
#             if(true){
#                 return 0;
#             }
#             else{
#                 return 0;
#             }
#             return flo;
#         }
#         // This is the end of Assignment 3
#         // Share to be better 
#         """
#         expect = "Type Mismatch In Statement: Return(Id(flo))"
#         self.assertTrue(TestChecker.test(input,expect,499))

import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):

    #---Test Redeclared Variable/Function/Parameter
        
    def test0_RedeclaredVariable(self):
        """Redeclared Variable a"""
        input = """
        int main(){
            int a;
            {
                float a;
            }
            boolean a;
            return 0;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 400))
        
    def test1_RedeclaredVariable(self):
        """Redeclared Variable b"""
        input = """
        void main(float b){
            string b;
            return getInt();
        }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test2_RedeclaredVariable(self):
        """Redeclared Variable main"""
        input = """
        boolean foo(boolean foo){
            return foo;
        }
        void main(){
            return ;
        }
        string main;
        """
        expect = "Redeclared Variable: main"
        self.assertTrue(TestChecker.test(input, expect, 402))
    
    def test3_RedeclaredFunction(self):
        """Redeclared Function foo"""
        input = """
        boolean foo;
        int main(){
            return 0;
        }
        int foo(){
            return 0;
        }
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 403))
        
    def test4_RedeclaredFunction(self):
        """Redeclared Function a"""
        input = """
        int a(int b){
            return b;
        }
        string a(string b){
            return b;
        }
        void main(){}
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test5_RedeclaredFunction(self):
        """Redeclared Function main"""
        input = """
        int main1, arr[69];
        float f;
        float main;
        string foo2(){ return "surprise";}
        int main(){
            return 0;
        }
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test6_RedeclaredFunction(self):
        """Redeclared Function foo2"""
        input = """
        int foo1, a;
        string foo2(){return "surprise";}
        int main(){
            return 0;
        }
        void foo2(){return;}
        """
        expect = "Redeclared Function: foo2"
        self.assertTrue(TestChecker.test(input, expect, 406))
    
    def test7_RedeclaredParameter(self):
        """Redeclared Parameter: a"""
        input = """
        float foo(int a, float a){return a+b;}
        int main(){
            return 0;
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 407))
    
    def test8_RedeclaredParameter(self):
        """Redeclared Parameter: a"""
        input = """
        float foo(int a, float b){return a+b;}
        int main(int a[], float a[]){
            return 0;
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 408))
        
    def test9_RedeclaredParameter(self):
        """Redeclared Parameter: a"""
        input = """
        float foo(int a, float b){return a+b;}
        int main(int a[], string a){
            return 0;
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 409))

    #---Test Undeclared Identifier/Function
        
    def test10_UndeclaredIdentifier(self):
        """Undeclared Identifier: temp"""
        input = """
        int a[1], i;
        void main(){
            int i, a;
            for(i=1;i<10;i=i+1)
            {
                if(temp<10)
                    temp=temp+1;
            }
            return;
        }
        """
        expect = "Undeclared Identifier: temp"
        self.assertTrue(TestChecker.test(input, expect, 410))
        
    def test11_UndeclaredIdentifier(self):
        """Undeclared Identifier: res"""
        input = """
        int foo(int a[])
        {
            return a[0];
        }
        float main(){
            int arr[10];
            float f;
            f = 0;
            do f=f+foo(arr); res=f+1; while (foo(arr)+f)<100;
            return f;
            }
        """
        expect = "Undeclared Identifier: res"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test12_UndeclaredIdentifier(self):
        """Undeclared Identifier: exp"""
        input = """
        int a;
        float b;
        string c;
        int d[10];
        void main(){
            {
                if(exp)
                    return;
            }
            return;
        }
        """
        expect = "Undeclared Identifier: exp"
        self.assertTrue(TestChecker.test(input, expect, 412))
    
    def test13_UndeclaredIdentifier(self):
        """Undeclared Identifier: somethingjustlikethis"""
        input = """
        void main()
        {
            {
                int a,b;
                boolean c,d;
                a = 10 ;
                b = 5;
                c = true;
                d = c == (a>b);
            }
            {
                somethingjustlikethis = a+b; 
            }
            return;
        }
        """
        expect = "Undeclared Identifier: somethingjustlikethis"
        self.assertTrue(TestChecker.test(input, expect, 413))
        
    def test14_UndeclaredIdentifier(self):
        """Undeclared Identifier: i"""
        input = """
        int[] foo()
        {
            int a[5];
            return a;
        }
        void main()
        {
            do
                foo();
            while i;
            return;
        }
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test15_UndeclaredFunction(self):
        """Undeclared Function: foo2"""
        input = """
        int foo(int a, int b){ return a+b;}
        int main(){
                return a+b+foo2();
            }
        int a,b;
        """
        expect = "Undeclared Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test16_UndeclaredFunction(self):
        """Undeclared Function: multi"""
        input = """
        void main(){
            string str;
            str = "Chery Chery Lady\\n";
            int a;
            a = multi(10);
            return;
        }
        """
        expect = "Undeclared Function: multi"
        self.assertTrue(TestChecker.test(input, expect, 416))
    
    def test17_UndeclaredFunction(self):
        """Undeclared Function: foo1"""
        input = """
        int foo()
            {
                return 1;
            }
        int main()
        {
            int a;
            a=foo();
            return foo1();
        }
        """
        expect = "Undeclared Function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 417))
    
    def test18_UndeclaredFunction(self):
        """Undeclared Function: convertBoolean"""
        input = """
        void main(){
            int a;
            {a =1;}
            if(convertBoolean(a))
                return;
            else                
                return;
        }
        """
        expect = "Undeclared Function: convertBoolean"
        self.assertTrue(TestChecker.test(input, expect, 418))
        
    def test19_UndeclaredFunction(self):
        """Undeclared Function: foo2"""
        input = """
        int foo(int a){
            if((a%2)==0)
                a=a+1;
            else
                do 
                    a=a-1;
                while a > 0;
            return a;
        }
        void main(){
            int a,b[10],i;
            a=10;
            for(i=0;i<10;i=i+1)
                b[i]=foo(a)+foo2(a);                
            return;
        }
        """
        expect = "Undeclared Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,419))

    #---Test Type Mismatch In Statement
        
    def test20_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: If"""
        input = """
        void main(){
            int a;
            {a =1;}
            if(a)
                return;
            else                
                return;
        }
        """
        expect = "Type Mismatch In Statement: If(Id(a),Return(),Return())"
        self.assertTrue(TestChecker.test(input, expect, 420))
        
    def test21_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: If"""
        input = """
        int foo(int a){
            if((a%2)+1.0)
                a=a+1;
            else
                return a+1;
            return a;
        }
        void main(){              
            return;
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,BinaryOp(%,Id(a),IntLiteral(2)),FloatLiteral(1.0)),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),Return(BinaryOp(+,Id(a),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test22_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: If"""
        input = """
        void main(){
            int a;
            float b[10];
            foo(a,b);              
            return;
        }
        int[] foo(int a,float b[]) {
            int c[3];
            if(a*2) foo(a-1,b);
            else return c;
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(*,Id(a),IntLiteral(2)),CallExpr(Id(foo),[BinaryOp(-,Id(a),IntLiteral(1)),Id(b)]),Return(Id(c)))"
        self.assertTrue(TestChecker.test(input, expect, 422))
    
    def test23_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: For"""
        input = """
        void main(){
            float i, temp;
            for(i=1.0;i<10;i=i+1)
                {
                    if(temp<10)
                        temp=temp+1;
                }
            return;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),FloatLiteral(1.0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(<,Id(temp),IntLiteral(10)),BinaryOp(=,Id(temp),BinaryOp(+,Id(temp),IntLiteral(1))))]))"
        self.assertTrue(TestChecker.test(input, expect, 423))
        
    def test24_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: For"""
        input = """
        void main(){
            int i, temp;
            for(i=1;i=i+1;i=i+1)
                {
                    if(temp<10)
                        temp=temp+1;
                }
            return;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(<,Id(temp),IntLiteral(10)),BinaryOp(=,Id(temp),BinaryOp(+,Id(temp),IntLiteral(1))))]))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test25_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: For"""
        input = """
        void main(){
            int i, temp;
            for(i=1;i<10;1.1e-1)
                {
                    if(temp<10)
                        temp=temp+1;
                    i=i+1;
                }
            return;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(10));FloatLiteral(0.11);Block([If(BinaryOp(<,Id(temp),IntLiteral(10)),BinaryOp(=,Id(temp),BinaryOp(+,Id(temp),IntLiteral(1)))),BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)))]))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test26_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: Dowhile"""
        input = """
        int foo(int a[])
        {
            return a[0];
        }
        void main(){
            int arr[10];
            float f;
            f = 0;
            do 
                f=f+foo(arr); 
                f=f+1; 
            while (foo(arr)+f);
            return;
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([BinaryOp(=,Id(f),BinaryOp(+,Id(f),CallExpr(Id(foo),[Id(arr)]))),BinaryOp(=,Id(f),BinaryOp(+,Id(f),IntLiteral(1)))],BinaryOp(+,CallExpr(Id(foo),[Id(arr)]),Id(f)))"
        self.assertTrue(TestChecker.test(input, expect, 426))
    
    def test27_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: Dowhile"""
        input = """
        int foo(int a){
            if((a%2)==0)
                a=a+1;
            else
                do a=a-1;
                while a = 0;
            return a;
        }
        void main(){
            return;
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([BinaryOp(=,Id(a),BinaryOp(-,Id(a),IntLiteral(1)))],BinaryOp(=,Id(a),IntLiteral(0)))"
        self.assertTrue(TestChecker.test(input, expect, 427))
    
    def test28_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: Return"""
        input = """
        void main(){
            int a;
            {a =1;}
            if(a==1)
                return true;
            else                
                return;
        }
        """
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 428))
        
    def test29_TypeMismatchInStatement(self):
        """Type Mismatch In Statement: Return"""
        input = """
        int[] main(){
            float a[5];
            int b[5];
            if(true)
                return a;
            else
                return b;
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,429))

    # ---Test Type Mismatch In Expression
        
    def test30_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: ArrayCell"""
        input = """
        void main(){
            int a,b[10],i;
            a=10;
            for(i=1;i<=10;i=i+1)
                b[i-1.0];                
            return;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),BinaryOp(-,Id(i),FloatLiteral(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 430))
        
    def test31_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: ArrayCell"""
        input = """
        void main(){
            int a,b[1];
            a=1;
            b[1.0]=a;                
            return;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test32_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: ArrayCell"""
        input = """
        int foo(){
            return 1;
        }
        void main(){
                foo()[1]+1; 
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(foo),[]),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 432))
    
    def test33_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: ArrayCell"""
        input = """
        int[] foo(int a[]){
            return a;
        }
        void main(){
                int a[10];
                (foo(a)[1])[2]; 
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(ArrayCell(CallExpr(Id(foo),[Id(a)]),IntLiteral(1)),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input, expect, 433))
        
    def test34_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: BinaryOp"""
        input = """
        int main(){
            boolean boo; 
            boo=false;
            1-boo;
            return 1;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(-,IntLiteral(1),Id(boo))"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test35_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: UnaryOp(!,Id(boo))"""
        input = """
        int main(){
            int boo; 
            boo=1;
            (!boo)&&(true);
            return 1;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(boo))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test36_TypeMismatchInExpression(self):
        """Type Mismatch In Expression:  - boolean"""
        input = """
        int main(){
            boolean c;
            c=true;
            int i,a;
            i=a+3;
            if (i>0){
                int d;
                d=1;
                -c;
                putInt(d);
            }
            return i;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 436))
    
    def test37_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: int[] + 1"""
        input = """
        int[] foo(int a,float b[]) {
                int c[3];
                if(a>0) 
                {
                    foo(a-1,b);
                    return c;
                }
                else return c;
        }
        void main(){
            int a;
            float b[10];
            a= 69;
            foo(a,b)+1;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,CallExpr(Id(foo),[Id(a),Id(b)]),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 437))
    
    def test38_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: int = boolean"""
        input = """
        int main(){
            boolean c;
            int i;
            i=3;
            if (i>0){
                int d;
                d=true;
            }
            return i;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(d),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 438))
        
    def test39_TypeMismatchInExpression(self):
        """no error, test with expression"""
        input = """
        int main(){
            float a[6];
            int b[9];
            int c[69];
            a[1]=foo(2)[3]/(c[b[2]]+3.0);
            return b[0];
        }
        int[] foo(int a){
            int arr[10];
            return arr;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,439))
        
    def test40_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: int = float"""
        input = """
        int main(){
            int a;
            float b;
            b = 69;
            a = b;        
        {
            return 0;
        }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 440))
        
    def test41_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: type of LHS is ArrayType"""
        input = """
        void main(){
            int a[69];
            a = 69;        
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),IntLiteral(69))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test42_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: need two args in func f"""
        input = """
        int i;
        int f(int a, int b){
            return 200;
        }
        void main(){
            int test;
            test=f(test);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f),[Id(test)])"
        self.assertTrue(TestChecker.test(input, expect, 442))
    
    def test43_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: string hello -> boolean boo"""
        input = """
        int foo(boolean boo){
            return 69;
        }
        int main(){
            string hello;
            return foo(hello);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(hello)])"
        self.assertTrue(TestChecker.test(input, expect, 443))
        
    def test44_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: cann't pass int b[] to float b[]"""
        input = """
        int foo(int a[] , float b[]){
            return a[0]/a[1];
        }
        int main(){
            return foo(a,b);
        }
        int a[5], b[10];
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a),Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test45_TypeMismatchInExpression(self):
        """no error"""
        input = """
        int[] foo(int a[]){
            return a;
        }
        int main(){
            int arr[69];
            return foo(foo(foo(arr)))[1]/foo(foo(foo(arr)))[0];
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,445))

    def test46_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: func'name = value"""
        input = """
        int foo(int a){
            return a;
        }
        void main(){
            foo = 1;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(foo),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 446))
    
    def test47_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: int = void"""
        input = """
        int foo;
        void f(){
            return;
        }
        void main(){
            foo = f();
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(foo),CallExpr(Id(f),[]))"
        self.assertTrue(TestChecker.test(input, expect, 447))
    
    def test48_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: ArrayCell"""
        input = """
        int foo;
        void main(){
            foo[1];
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(foo),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 448))
        
    def test49_TypeMismatchInExpression(self):
        """Type Mismatch In Expression: float != float"""
        input = """
        void main(){
            int a,b;
            a=b=1;
            boolean boo;
            boo = foo(a,b);
            return;
        }
        boolean foo(float a, float b){
            if (a!=b)
                return true;
            else
                return false;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,449))

    #---Test Break/Continue not in loop
        
    def test50_BreakNotInLoop(self):
        """Break Not In Loop"""
        input = """
        void main(){
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 450))
    
    def test51_BreakNotInLoop(self):
        """Break Not In Loop"""
        input = """
        int foo(){
            if (true)
                break;
            else return 1;
            return 0;
        }
        void main(){}
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test52_BreakNotInLoop(self):
        """Break Not In Loop"""
        input = """
        string hello(string str){
            return str;
        }
        int main(){
            hello("Hi");
            {{break;}}
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 452))
    
    def test53_BreakNotInLoop(self):
        """Break Not In Loop"""
        input = """
        void main(){
            if (true)
                {
                    {
                        if (false)
                            break;
                    }
                }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 453))
        
    def test54_BreakNotInLoop(self):
        """Break Not In Loop"""
        input = """
        boolean foo(){
            return true;
        }
        int foo1(){
            return 1;
        }
        void main(){
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test55_ContinueNotInLoop(self):
        """Continue Not In Loop"""
        input = """
        void main(){
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test56_ContinueNotInLoop(self):
        """Continue Not In Loop"""
        input = """
        int foo(){
            if (true)
                continue;
            else return 1;
            return 0;
        }
        void main(){}
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 456))
    
    def test57_ContinueNotInLoop(self):
        """Continue Not In Loop"""
        input = """
        string hello(string str){
            return str;
        }
        int main(){
            hello("Hi");
            {{continue;}}
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 457))
    
    def test58_ContinueNotInLoop(self):
        """Continue Not In Loop"""
        input = """
        void main(){
            if (true)
                {
                    {
                        if (false)
                            continue;
                    }
                }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 458))
        
    def test59_ContinueNotInLoop(self):
        """Continue Not In Loop"""
        input = """
        boolean foo(){
            return true;
        }
        int foo1(){
            return 1;
        }
        void main(){
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,459))

    #---Test Function not return
        
    def test60_FunctionNotReturn(self):
        """Function main Not Return"""
        input = """
        int main(){
            int a,b;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 460))
        
    def test61_FunctionNotReturn(self):
        """Function foo Not Return"""
        input = """
        void main(){}
        int foo(){}
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test62_FunctionNotReturn(self):
        """Function main Not Return"""
        input = """
        int main(){
            if (true)
                return 1;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 462))
    
    def test63_FunctionNotReturn(self):
        """Function main Not Return"""
        input = """
        int main(){
            int i;
            for(i=1;i<69;i=i+1)
                return i;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 463))
        
    def test64_FunctionNotReturn(self):
        """no error"""
        input = """
        int main(){
            if(true)
                if(false)
                    return 1;
                else
                    return 0;
            else return 2;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,464))

    #---Test No Entry Point

    def test65_NoEntryPoint(self):
        """No Entry Point"""
        input = """
        int foo(){
            return 0;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test66_NoEntryPoint(self):
        """No Entry Point"""
        input = """
        int a,b;
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 466))
    
    def test67_NoEntryPoint(self):
        """No Entry Point"""
        input = """
        int a;
        float b;
        boolean main;
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 467))
    
    def test68_NoEntryPoint(self):
        """No Entry Point"""
        input = """
        void foo(){}
        int main;
        void f(){}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 468))
        
    def test69_NoEntryPoint(self):
        """Simple program: int main() {} """
        input = """
        int a;
        float main;
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,469))

    #---Test Unreachable function
        
    def test70_UnreachableFunction(self):
        """Unreachable Function: foo"""
        input = """
        int foo(){return 0;}
        void main()
        {
            return;
        }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 470))
        
    def test71_UnreachableFunction(self):
        """Unreachable Function: foo"""
        input = """
        int foo(int a){
            if (a>0)
                return foo(a-1);
            else
                return 0;
        }
        void main()
        {
            return;
        }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test72_UnreachableFunction(self):
        """no error"""
        input = """
        int foo1()
        {
            foo2();
            return 1;
        }
        int foo2()
        {
            foo1();
            return 1;
        }
        void main(){}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 472))
    
    def test73_UnreachableFunction(self):
        """no error"""
        input = """
        void foo1()
        {
            foo2();
        }
        void foo2()
        {
            foo3();
        }
        void foo3()
        {
            foo1();
        }
        void main(){}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 473))
        
    def test74_UnreachableFunction(self):
        """Unreachable Function: foo1"""
        input = """
        void foo1()
        {
            foo2();
            foo3();
        }
        void foo2(){}
        void foo3(){}
        void main(){}
        """
        expect = "Unreachable Function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 474))

    #---Test Not Left Value

    def test75_NotLeftValue(self):
        """Not Left Value"""
        input = """
        void main(){
            1+1=2; 
        }
        """
        expect = "Not Left Value: BinaryOp(+,IntLiteral(1),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test76_NotLeftValue(self):
        """Not Left Value"""
        input = """
        int foo(){ 
            return 0; 
        }
        void main(){
            foo()=1;
        }
        """
        expect = "Not Left Value: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input, expect, 476))
    
    def test77_NotLeftValue(self):
        """Not Left Value"""
        input = """
        int x;
        void main(){
            x+1=2;
        }
        """
        expect = "Not Left Value: BinaryOp(+,Id(x),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 477))
    
    def test78_NotLeftValue(self):
        """Not Left Value"""
        input = """
        void main(){
            float arr[10];
            arr[0]+arr[1]=arr[2]+3;
        }
        """
        expect = "Not Left Value: BinaryOp(+,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input, expect, 478))
        
    def test79_NotLeftValue(self):
        """Not Left Value"""
        input = """
        int foo(int a){
            return a;
        }
        void main(){
            a+foo(a)=foo(a)+a;
        }
        int a;
        """
        expect = "Not Left Value: BinaryOp(+,Id(a),CallExpr(Id(foo),[Id(a)]))"
        self.assertTrue(TestChecker.test(input,expect,479))

    #---Test More Complex Program
        
    def test80_True(self):
        """no error"""
        input = """
        int i;
        int f(){
            return 200;
        }
        void main(){
            int test;
            test=f();
            putIntLn(test);
            {
                int i, test, f;
                test=f=i=100;
                putIntLn(i);
                putIntLn(test);
                putIntLn(f);
            }
            putIntLn(test);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 480))
        
    def test81_UnreachableFunction(self):
        """Unreachable Function: rescursive"""
        input = """
        int x,y[8];
        int a,b,c;
        void main(){
            y[x+a+b*c];
        }
        void rescursive(int i,float z){
            boolean exp;
            int statement;
            exp =true;
            int x;
            int c;
            if(exp)
                statement;
            else
                return;
        }
        """
        expect = "Unreachable Function: rescursive"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test82_MoreDecls(self):
        """no error"""
        input = """
        int main(){
            int a;
            {
                int a;
                {
                    int a;
                    return b;
                }
            }
        }
        int b;
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 482))
    
    def test83(self):
        """int func return with float"""
        input = """
        int a,b,c;
        float d;
        int main(){
            if (a<b) 
                c=a; 
            else 
                if(c<b)
                    c=b;
                else
                    c=b;
            return d=a=b=c;
        }
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(=,Id(d),BinaryOp(=,Id(a),BinaryOp(=,Id(b),Id(c)))))"
        self.assertTrue(TestChecker.test(input, expect, 483))
        
    def test84_TypeMismatchInExpression(self):
        """use int in logic exp"""
        input = """
        int main(){
            boolean a,b,d,e,f;
            int c;
            a || b || c || d && e && f;
            return 1; 
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,BinaryOp(||,Id(a),Id(b)),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test85_MoreComplexReturn(self):
        """no error"""
        input = """
        int foo(){
            if(true)
            {
                int i;
                for(i=0;i<10;i=i+1)
                {
                    break;
                }
                return 1;
            }
            else
                do
                    if(true)
                        return 2;
                    else
                        return 3;
                while(true);
        }
        float main(){
            return foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,485))

    def test86_TestMoreComplexReturn(self):
        """No return in ThenStm"""
        input = """
        int foo(){
            if(true)
            {
                int i;
                for(i=0;i<10;i=i+1)
                {
                    break;
                }
                return 1;
            }
            else
                do
                    if(true)
                        foo();
                    else
                        return 3;
                while(true);
        }
        float main(){
            return foo();
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 486))
    
    def test87_NotLeftValue(self):
        """Not Left Value: b+c"""
        input = """
        int foo(){
            return 0;
        }
        int main(){
            int a,b,c;
            return a=b+c=foo();
        }
        """
        expect = "Not Left Value: BinaryOp(+,Id(b),Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 487))
    
    def test88_TypeMisMatchInExpressionUnaryOp(self):
        """ ! int """
        input = """
        int main()
        {
            int a,b,c;
            a = !b + -a;
            return a;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 488))
        
    def test89_CallMoreFunc(self):
        """no error"""
        input = """
        int main(){
            do
            {
                {
                    if (b>c)
                        return a+1;
                    else
                        return b-1;                    
                }
            }
            {
                a+b;
            }
            while (a<5);
            foo();
            foo();
            foo();
            foo();
            return 1;
        }
        int a,b,c;
        void foo(){}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,489))
        
    def test90_ComplexProgram(self):
        """No error"""
        input = """
        int main(){
            return foo(a,b);
        }
        int foo(int a[], float b){
            if (a[0] == 0) 
                return a[0];
            else
            {
                return foo(a,b);
            }
        }
        int a[10];
        float b;
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 490))
        
    def test91_complexprogram(self):
        """no error"""
        input = """
        void printf(string str){}
        void scanf(float a){}
        string int2str(int a){ return "Kael99" ;}
        int main()
        {
            int i, n, t1, t2, nextTerm;
            printf("Enter the number of terms: ");
            scanf(n);
            printf("Fibonacci Series: ");
            for (i = 1; i <= n; i=i+1)
            {
                printf(int2str(t1));
                nextTerm = t1 + t2;
                t1 = t2;
                t2 = nextTerm;
            }
            return 0;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test92_CompareWithFloat(self):
        """ number == float """
        input = """
        void printf(string str){}
        void scanf(float a){}
        int main()
        {
            float number;
            printf("Enter a number: ");
            scanf(number);
            if (number <= 0.0)
            {
                if (number == 0.0)
                    printf("You entered 0.");
                else
                    printf("You entered a negative number.");
            }
            else
                printf("You entered a positive number.");
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(number),FloatLiteral(0.0))"
        self.assertTrue(TestChecker.test(input, expect, 492))
    
    def test93_complexprogram(self):
        """no error"""
        input = """
        int main()
        {
            int low, high, i, flag;
            do
            {
                flag = 0;
                for(i = 2; i <= low/2.0; i=i+1)
                {
                    if(low % i == 0)
                        {
                            flag = 1;
                            break;
                        }
                }
                if (flag == 0)
                    return low;
                low=low+1;
            }
            while (low < high);
            return 0;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 493))
        
    def test94_complexprogram(self):
        """! float"""
        input = """
        int main()
        {   
            do
            {
                if(n1 > n2)
                    n1 = n1 - n2;
                else
                    n2 = n2 - n1;
            }
            while(n1!=n2);
            return foo(1);
        }
        int foo(float a){
            return !a;
        }
        int n1, n2; 
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test95_complexprogram(self):
        """float foo2 can not return in foo1"""
        input = """
        float main()
        {
            int n, i, sum;
            for(i=1; i <= n; i=i+1)
            {
                sum = sum+i;
            }
            return foo1();
        }
        int foo1(){
            return foo2();
        }
        float foo2(){
            return foo1();
        }
        """
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(foo2),[]))"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test96_complexprogram(self):
        """no error"""
        input = """
        void getFibonacii(int a,int b, int n)
        {   
            int sum;
            if(n>0)
            {
                sum=a+b;
                a=b;
                b=sum;
                getFibonacii(a,b,n-1);
            }
        }
        int main()
        {
            n = 10;     
            a=0;        //first term
            b=1;        //second term

            //call function with (n-2) terms
            getFibonacii(a,b,n-2);  
            return 0;
        }
        int a,b,sum,n;
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 496))
    
    def test97_complexprogram(self):
        """ int result = float getPower()"""
        input = """
        float getPower(int b,int p)
        {
            float result;
            if(p==0)
                return result;
            else 
            {
                result=b*(getPower(b,p-1));
                return result;
            }
        }
        int main()
        {
            int base,power;
            int result;     
            result=getPower(base,power);     
            return result;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(result),CallExpr(Id(getPower),[Id(base),Id(power)]))"
        self.assertTrue(TestChecker.test(input, expect, 497))
    
    def test98_AllBuiltinFunction(self):
        """Simple program: int main() {} """
        input = """
        void main () {
            float a;
            a=getInt();
            putInt(69);
            putIntLn(96);
            a=getFloat();
            putFloat(69);
            putFloatLn(69.96);
            putBool(true&&false);
            putBoolLn(true||false);
            putString("Hello hello, can u hear me?");
            putStringLn("Hello hello, can u hear me?");
            putLn();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 498))
        
    def test99(self):
        """Type Mismatch In Expression: use var as func"""
        input = """
        int foo;
        void main()
        {
            foo(1);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,499))