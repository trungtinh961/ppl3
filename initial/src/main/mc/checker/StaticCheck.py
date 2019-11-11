
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor,Utils):

    global_envi = [    
        Symbol("getInt",MType([],IntType())),
        Symbol("putInt",MType([IntType()],VoidType())),
        Symbol("putIntLn",MType([IntType()],VoidType())),
        Symbol("getFloat",MType([],FloatType())),
        Symbol("putFloat",MType([FloatType()],VoidType())),
        Symbol("putFloatLn",MType([FloatType()],VoidType())),
        Symbol("putBool",MType([BoolType()],VoidType())),
        Symbol("putBoolLn",MType([BoolType()],VoidType())),
        Symbol("putString",MType([StringType()],VoidType())),
        Symbol("putStringLn",MType([StringType()],VoidType())),
        Symbol("putLn",MType([],VoidType()))
    ]
            
    def __init__(self,ast):
        #print(ast)
        #print(ast)
        #print()
        self.ast = ast 

    def flatten(self,lst):
        return [item for sublist in lst for item in sublist]

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def checkRedeclared(self,symbol,kind,env):
        if self.lookup(symbol.name, env, lambda x:x.name):
            raise Redeclared(kind,symbol.name)
        else:
            return [symbol]

    def getName(self, decl):
        if isinstance(decl, VarDecl):
            return decl.variable
        else:
            return decl.name.name
    
    def getType(self, decl):
        if isinstance(decl, VarDecl):
            return decl.varType
        else:
            return MType([z.varType for z in decl.param], decl.returnType)

    def visitProgram(self,ast,c):
        lstDecl = []
        for x in ast.decl:
            lstDecl.append(Symbol(self.getName(x),self.getType(x)))
        lstFunc = []
        lstFunc = filter(lambda x: isinstance(x.mtype,MType),lstDecl)
        
        if self.lookup("main", lstFunc, lambda x: x.name) is None:
            raise NoEntryPoint()

        return reduce(lambda x,y: x + self.visit(y,[x+c,lstDecl+c]),ast.decl,[])

    def visitVarDecl(self,ast,c):
        return self.checkRedeclared(Symbol(self.getName(ast), self.getType(ast)),Variable(),c[0])
        

    def visitFuncDecl(self,ast, c): 
         return self.checkRedeclared(Symbol(ast.name.name,MType([x.varType for x in ast.param],ast.returnType)),Function(),c[0])

   
    # def visitCallExpr(self, ast, c): 
    #     at = [self.visit(x,(c[0],False)) for x in ast.param]
        
    #     res = self.lookup(ast.method.name,c[0],lambda x: x.name)
    #     if res is None or not type(res.mtype) is MType:
    #         raise Undeclared(Function(),ast.method.name)
    #     elif len(res.mtype.partype) != len(at):
    #         if c[1]:
    #             raise TypeMismatchInStatement(ast)
    #         else:
    #             raise TypeMismatchInExpression(ast)
    #     else:
    #         return res.mtype.rettype

    # def visitIntLiteral(self,ast, c): 
    #     return IntType()
    

