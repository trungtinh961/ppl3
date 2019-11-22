import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
#{
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
#}


        
    def test_deep_block_declared_5th(self):
        """test break stmt outside loop deep block"""
        input = """
        int i;
        float f;
        string str;
        boolean boo;
        int main(){
            int LongLML;
            {
                int f; boolean i;
                {
                    {{{{{{{{string str;return f;}}}}}}}}
                }
                i = true&&false||(10<=5);
            }
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,481))
        
    def test_deep_block_do_1st(self):
        """test deep do-while if-else"""
        input = """
        int i;
        float f;
        string str;
        boolean boo;
        int main(){
            int str;
            do 
            do 
            do 
            if(true) return 0; else return 1; 
            while(true);
            while(true);
            while(true);
        }
        int foo(){
            return Long;
        }
        """
        expect = "Undeclared Identifier: Long"
        self.assertTrue(TestChecker.test(input,expect,482))
        
    def test_deep_block_do_2rd(self):
        """test function not return with float Epointer"""
        input = """
        int i;
        float f;
        string str;
        boolean boo;
        int main(){
            int str;
            do{
                if(false){
                    if(true){
                        if (1 <= 10){
                            return 10;
                        }
                        else {
                            continue;
                        }
                    }
                    else{
                        break;
                    }
                }
            }while(true);
            return 1e4;
        }
        void foo(){
            return ;
        }
        """
        expect = "Type Mismatch In Statement: Return(FloatLiteral(10000.0))"
        self.assertTrue(TestChecker.test(input,expect,483))
        
    def test_deep_block_do_3nd(self):
        """test continue stmt outside loop deep block"""
        input = """
        int i;
        float f;
        string str;
        boolean boo;
        int main(){
            int str;
            do{
                if(false){
                    if(true){
                        if (1 <= 10){
                            return 10;
                        }
                        else {
                            continue;
                        }
                    }
                    else{
                        break;
                    }
                }
            }while(true);
            return 1;
        }
        void foo(){
            continue;
            return ;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,484))
        
    def test_deep_block_do_4th(self):
        """test break stmt outside loop deep block"""
        input = """
        int i;
        float f;
        string str;
        boolean boo;
        int main(){
            int str;
            do{
                if(false){
                    if(true){
                        if (1 <= 10){
                            return 10;
                        }
                        else {
                            continue;
                        }
                    }
                    else{
                    }
                }
            }while(true);
            break;
            return 1;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,485))
        
    def test_deep_block_do_5th(self):
        """test stmt for expr"""
        input = """
        int i;
        float f;
        string str;
        boolean boo;
        int main(){
            for(10;true;1e1){
                "haha";
            }
        }
        """
        expect = "Type Mismatch In Statement: For(IntLiteral(10);BooleanLiteral(true);FloatLiteral(10.0);Block([StringLiteral(haha)]))"
        self.assertTrue(TestChecker.test(input,expect,486))
        
    def test_unrechable_func_1st(self):
        """test unrechable function recursive"""
        input = """
        void foo(){}
        void foo1(){foo();}
        void foo2(){foo1();}
        void foo3(){foo2(); foo3();}
        int main(){
            do
                return 1;
            while(true);
        }
        """
        expect = "Unreachable Function: foo3"
        self.assertTrue(TestChecker.test(input,expect,487))
        
    def test_unrechable_func_2nd(self):
        """test call exp  failed"""
        input = """
        void foo(){}
        void foo1(){foo();}
        void foo2(){foo2();}
        void foo3(){foo3();}
        int main(){
            foo1();
            foo3();
            float foo3;
            foo3();
            do
                return 1;
            while(true);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo3),[])"
        self.assertTrue(TestChecker.test(input,expect,488))
        
    def test_unrechable_func_3rd(self):
        """test call stmt failed"""
        input = """
        void foo(){}
        void foo1(){foo();}
        void foo2(boolean f){foo2(foo3());}
        boolean foo3(){return foo3();}
        int main(){
            foo1();
            float main;
            main = 1e10-10e1;
            string foo2;
            foo2(true);
            do
                return 1;
            while(true);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo2),[BooleanLiteral(true)])"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_all_check_1st(self):
        """test large code example expression failed 1st"""
        input = """
        void println(string str){}
        void save(int len){}
        void main(){
            int TimeRemaining,len,Per;
                    println("How many incorrect times do you want to get? ");
                    save(TimeRemaining);
                    println("what minimum word lengh do you want? ");
                    save(len);
                    //fstream f;
                    //f.open("input.txt",ios::in);
                    string data;
                    string List[255];
                    int NumOfWord,n;
                    List[-1] = "1005199"&&Per;
                    NumOfWord=0;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,StringLiteral(1005199),Id(Per))"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_all_check_2nd(self):
        """test large code example expression failed 2nd"""
        input = """
        void println(string str){}
        void save(int len){}
        void getline(int l, int data){}
        void main(){
            int data,f,NumOfWord;
            string List[255];
            do{
                        getline(f,data);
                        if (data!=1) List[NumOfWord]=data;

                    }while(data!=1);
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(List),Id(NumOfWord)),Id(data))"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_all_check_3rd(self):
        """test large code example stmt failed 3rd"""
        input = """
        //void println(string str){}
        //void save(int len){}
        void getline(int l, int data){}
        void main(){
            int data,f,NumOfWord;
            string List[255];
            do{
                getline(f,data);
            }while(data!=1);
            for(1;true;1){
                return 0;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_all_check_4th(self):
        """test large code example break failed 4th"""
        input = """
        //void println(string str){}
        //void save(int len){}
        void getline(int l, int data){}
        void main(){
            int data,f,NumOfWord;
            string List[255];
            do{
                getline(f,data);
            }while(data!=1);
            for(1;true;1){
                return;
            }
            if(true){
                break;
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_all_check_5th(self):
        """test large code example return failed 5th"""
        input = """
        //void println(string str){}
        //void save(int len){}
        void getline(int l, int data){}
        int main(){
            int data,f,NumOfWord;
            string List[255];
            do{
                getline(f,data);
            }while(data!=1);
            for(1;true;1){
                boolean b;
                b = !true&&false||(10.1>10);
            }
            if(true){
                return 0;
            }
            for(1;true;1)
                return 0;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_all_check_6th(self):
        """test large code example declared failed 6th"""
        input = """
        //void println(string str){}
        //void save(int len){}
        void getline(int l, int data){}
        int main(float flo){
            int data,f,NumOfWord;
            string List[255];
            do{
                getline(f,data);
            }while(data!=1);
            for(1;true;1){
                boolean b;
                b = !true&&false||(10.1>10);
            }
            if(true){
                return 0;
            }
            else{
                return 0;
            }
            int flo;
        }
        """
        expect = "Redeclared Variable: flo"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_all_check_7th(self):
        """test large code example left expression failed 7th"""
        input = """
        //void println(string str){}
        //void save(int len){}
        void getline(int l, int data){}
        int main(float flo){
            int data,f,NumOfWord;
            string List[255];
            do{
                getline(f,data);
            }while(data!=1);
            for(1;true;1){
                boolean b;
                b = !true&&false||(10.1>10);
            }
            if(true){
                return 0;
            }
            else{
                return 0;
            }
            10.1=-10;
        }
        """
        expect = "Not Left Value: FloatLiteral(10.1)"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_all_check_8th(self):
        """test large code example left undeclared indentifier failed 8th"""
        input = """
        //void println(string str){}
        //void save(int len){}
        void getline(int l, int data){}
        int main(float flo){
            int data,f,NumOfWord;
            string List[255];
            do{
                getline(f,data);
            }while(data!=1);
            for(1;true;1){
                boolean b;
                b = !true&&false||(10.1>10);
            }
            if(true){
                return 0;
            }
            else{
                return 0;
            }
            floas;

        }
        """
        expect = "Undeclared Identifier: floas"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_all_check_9th(self):
        """test large code example left expression failed 7th"""
        input = """
        //void println(string str){}
        //void save(int len){}
        void getline(int l, int data){}
        int main(float flo){
            int data,f,NumOfWord;
            string List[255];
            do{
                getline(f,data);
            }while(data!=1);
            for(1;true;1){
                boolean b;
                b = !true&&false||(10.1>10);
            }
            if(true){
                return 0;
            }
            else{
                return 0;
            }
            flo + data = 10;
        }
        """
        expect = "Not Left Value: BinaryOp(+,Id(flo),Id(data))"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_all_check_10th(self):
        """test large code example left stmt return failed 7th"""
        input = """
        //void println(string str){}
        //void save(int len){}
        // void reduce
        void getline(int l, int data){}
        int main(float flo){
            int data,f,NumOfWord;
            string List[255];
            do{
                getline(f,data);
            }while(data!=1);
            for(1;true;1){
                boolean b;
                b = !true&&false||(10.1>10);
            }
            if(true){
                return 0;
            }
            else{
                return 0;
            }
            return flo;
        }
        // This is the end of Assignment 3
        // Share to be better 
        """
        expect = "Type Mismatch In Statement: Return(Id(flo))"
        self.assertTrue(TestChecker.test(input,expect,499))