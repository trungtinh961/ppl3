
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

        return reduce(lambda x,y: x + self.visit(y,(x+c,lstDecl+c)),ast.decl,[])

    def visitVarDecl(self,ast,c):
        return self.checkRedeclared(Symbol(self.getName(ast), self.getType(ast)),Variable(),c[0])
        

    def visitFuncDecl(self,ast, c): 
        __lstLocal = []
        for i in ast.param:
            if self.lookup(self.getName(i), __lstLocal, lambda x: x.name):
                raise Redeclared(Parameter(), self.getName(i))
            else:
                __lstLocal.insert(0, Symbol(self.getName(i),self.getType(i)))
        res = self.visit(ast.body,(__lstLocal,c[1],ast.returnType))

        return self.checkRedeclared(Symbol(ast.name.name,MType([x.varType for x in ast.param],ast.returnType)),Function(),c[0])

   
    def visitBlock(self,ast,c):
        __lstLocal = c[0]
        lstVarDecl = filter(lambda x: isinstance(x, VarDecl),ast.member)
        
        for i in ast.member:
            if i in lstVarDecl:
                if self.lookup(i.variable, __lstLocal, lambda x: x.name):
                    raise Redeclared(Variable(), i.variable)
                else:
                    __lstLocal.insert(0, Symbol(self.getName(i),self.getType(i)))
        
            else:
                res = self.visit(i,([],__lstLocal+c[1],c[2],True))

        return  __lstLocal + c[1] #all decl use to check undecl

    def visitCallExpr(self, ast, c): 
        at = [self.visit(x,(c[1],False)) for x in ast.param]
        
        res = self.lookup(ast.method.name,c[1],lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(),ast.method.name)
        elif len(res.mtype.partype) != len(at) or True in [type(a) != type(b) for a,b in zip(at,res.mtype.partype)]:
            if c[3]:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        else:
            return res.mtype.rettype

    
    def visitId(self,ast,c):
        at = self.lookup(ast.name,c[0],lambda x: x.name)
        if at is not None:
            return at.mtype
        else:
            raise Undeclared(Identifier(),ast.name)

    def visitArrayCell(self,ast,c):
        arr = self.visit(ast.arr,c)
        idx = self.visit(ast.idx,c)
        if not isinstance(idx,IntType) or not isinstance(arr,ArrayType) or not isinstance(arr,ArrayPointerType):        
            raise TypeMismatchInExpression(ast)
        else:
            return arr.eleType

    def visitBinaryOp(self,ast,c):
        left = self.visit(ast.left,(c[1],False))
        right = self.visit(ast.right,(c[1],False))
        if ast.op is '=':
            if type(left) != type(right):
                if type(left) is FloatType and type(right) is IntType:
                    return FloatType()
                else:
                    raise TypeMismatchInStatement(ast) 
            elif type(left) is StringType or type(left) is ArrayType or type(left) is ArrayPointerType:
                raise TypeMismatchInStatement(ast)
            else:
                return left

        elif ast.op in ['+', '-', '*', '/']:
            if type(left) is IntType and type(right) is IntType:
                return IntType()
            elif type(left) is IntType and type(right) is FloatType:
                return FloatType()
            elif type(left) is FloatType and type(right) is IntType:
                return FloatType()
            elif type(left) is FloatType and type(right) is FloatType:
                return FloatType()   
            else:
                raise TypeMismatchInExpression(ast)

        elif ast.op is '%':
            if type(left) is IntType and type(right) is IntType:
                return IntType()
            else:
                raise TypeMismatchInExpression(ast)

        elif ast.op in ['==','!=']:
            if type(left) is IntType and type(right) is IntType:
                return BoolType()
            if type(left) is Boolean and type(right) is Boolean:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)

        elif ast.op in ['<', '>', '<=', '>=']:
            if type(left) in [IntType,FloatType] and type(right) in [IntType,FloatType]:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)

        elif ast.op in ['!','&&','||']:
            if type(left) is Boolean and type(right) is Boolean:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)

        else:
            raise TypeMismatchInExpression(ast)




    # def visitUnaryOp(self,ast,c):
    #     return

    # def visitIf(self,ast,c):
    #     return 

    # def visitFor(self,ast,c):
    #     return

    # def visitBreak(self,ast,c):
    #     return

    # def visitContinue(self,ast,c):
    #     return

    # def visitFor(self,ast,c):
    #     return
    
    # def visitDowhile(self,ast,c):
    #     return

    def visitReturn(self, ast, c):
        checkType = c[2]
        res = ast.expr
        if type(checkType) is VoidType and (res is not None):
            raise TypeMismatchInStatement(ast)      
        if type(checkType) is not  VoidType:
            if res is None:
                raise TypeMismatchInStatement(ast) 
            elif type(checkType) is FloatType and any(type(self.visit(res, c)) is x for x in [IntType, FloatType]):
                pass
            elif type(checkType) != type(self.visit(res, c)):
                raise TypeMismatchInStatement(ast) 
            elif (type(checkType) is ArrayType) and checkType != self.visit(res, c):
                raise TypeMismatchInStatement(ast) 

   
    

    def visitIntLiteral(self,ast, c): 
        return IntType()

    def visitFloatLiteral(self,ast,c):
        return FloatType()

    def visitBooleanLiteral(self,ast,c):
        return BoolType()

    def visitStringLiteral(self,ast,c):
        return StringType()    
    
    def visitArrayType(self, ast, c):
        return ArrayType(ast.dimen,ast.eleType)

    def visitArrayPointerType(self,ast,c):
        return ArrayPointerType(eleType)


    
        

