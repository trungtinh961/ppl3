import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """int main () {
            getIntLn();
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("getIntLn"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
   
   def test_all(self):        
        input = """
        void main()
        {
            int n;
            float a, b, c ;
            float R;
            float P;
            float S;
            do
            {
                printf("Nhap ban kinh duong tron:");
                scanf("%f", R);
            }
            while(R <= 0);
            P = 2 * PI * R;
            S = PI * R * R;
            printf("Chu vi hinh tron : %f dvdd", P);
            printf("Dien tich hinh tron : %f dvdt", S);
            break;               
            getch();
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("n",IntType()),VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("R",FloatType()),VarDecl("P",FloatType()),VarDecl("S",FloatType()),Dowhile([Block([CallExpr(Id("printf"),[StringLiteral("Nhap ban kinh duong tron:")]),CallExpr(Id("scanf"),[StringLiteral("%f"),Id("R")])])],BinaryOp("<=",Id("R"),IntLiteral(0))),BinaryOp("=",Id("P"),BinaryOp("*",BinaryOp("*",IntLiteral(2),Id("PI")),Id("R"))),BinaryOp("=",Id("S"),BinaryOp("*",BinaryOp("*",Id("PI"),Id("R")),Id("R"))),CallExpr(Id("printf"),[StringLiteral("Chu vi hinh tron : %f dvdd"),Id("P")]),CallExpr(Id("printf"),[StringLiteral("Dien tich hinh tron : %f dvdt"),Id("S")]),Break(),CallExpr(Id("getch"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))