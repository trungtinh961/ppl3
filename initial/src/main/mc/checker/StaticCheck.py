
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

    def checkRedeclared(self,decl,env,param):
        name = ""
        if isinstance(decl,VarDecl) and param == False:
            name = decl.variable
            if self.lookup(name, env, lambda x: x.name):
                raise Redeclared(Variable(), name)
            else:
                return Symbol(name, decl.varType)
        elif isinstance(decl,FuncDecl) and param == False:
            name = decl.name.name
            if self.lookup(name, env, lambda x: x.name):
                raise Redeclared(Function(), name)
            else:
                return Symbol(name, MType([x.varType for x in decl.param], decl.returnType))
        else:
            name = decl.variable
            if self.lookup(name, env, lambda x: x.name):
                raise Redeclared(Parameter(), name)
            else:
                return Symbol(name, decl.varType)


    def __init__(self,ast):
        self.ast = ast
        self.lstFunc = []
        self.lstCall = []

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast,c):
        lstDecl = c.copy()
        for decl in ast.decl:
            temp = self.checkRedeclared(decl,lstDecl,False)
            lstDecl.append(temp)
            if type(decl) is FuncDecl:
                self.lstFunc.append(temp)
        
        entryPoint = self.lookup("main", self.lstFunc, lambda x: x.name)

        if entryPoint is None:
            raise NoEntryPoint()
        else:
            self.lstCall.append(entryPoint)

        at = [self.visit(x, (lstDecl, self.lstFunc)) for x in ast.decl]

        return ''

    def visitVarDecl(self,ast,c):
        return False
        

    def visitFuncDecl(self,ast, c):
        env = c[0].copy()
        lstLocal = []
        for param in ast.param:
            res = self.checkRedeclared(param,lstLocal,True)
            lstLocal.append(res)
            env.append(res)

        at = self.visit(ast.body, (env, lstLocal, False, ast.returnType))

        return at

   
    def visitBlock(self,ast,c):
        lstLocal = c[1].copy()
        env = c[0].copy()
        isReturn = False
        lstVarDecl = filter(lambda x: isinstance(x,VarDecl),ast.member)
        for i in ast.member:
            if i in lstVarDecl:
                res = self.checkRedeclared(i,lstLocal,False)
                lstLocal.append(res)
                env.append(res)            
            else:
                at = self.visit(i,(env,[],c[2],c[3])) # c = (global,[],isLoop,rettype)

        return isReturn

    def visitCallExpr(self, ast, c): 
        at = [self.visit(x,(c[0],False)) for x in ast.param]        
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(),ast.method.name)
        elif len(res.mtype.partype) != len(at):
            raise TypeMismatchInExpression(ast)
        else:
            self.lstCall.append(res)
            for left,right in zip(res.mtype.partype, at):
                if type(left) is ArrayPointerType and type(right) in [ArrayPointerType,ArrayType]:
                    if type(left.eleType) != type(right.eleType):
                        raise TypeMismatchInExpression(ast)
                elif type(left) != type(right):
                    if not (type(left), type(right)) == (FloatType, IntType):
                        raise TypeMismatchInExpression(ast)
                else:
                    raise TypeMismatchInExpression(ast)
        return res.mtype.rettype
    
    def visitId(self,ast,c):
        at = self.lookup(ast.name,c[0],lambda x: x.name)
        if at is None or type(at.mtype) is MType:
            raise Undeclared(Identifier(),ast.name)
        else:
            return at.mtype 

    def visitArrayCell(self,ast,c):
        arr = self.visit(ast.arr,c)
        idx = self.visit(ast.idx,c)
        if not isinstance(idx,IntType) or (not type(arr) in [ArrayType, ArrayPointerType]):        
            raise TypeMismatchInExpression(ast)
        else:
            return arr.eleType

    def visitBinaryOp(self,ast,c):
        left = self.visit(ast.left,c)
        right = self.visit(ast.right,c)
        if ast.op is '=':
            if type(left) != type(right):
                if type(left) is FloatType and type(right) is IntType:
                    return FloatType()
                else:
                    raise TypeMismatchInStatement(ast) 
            elif type(left) is ArrayPointerType and type(right) in [ArrayPointerType,ArrayType]:
                if type(left.eleType) == type(right.eleType):
                    return left
                else:
                    return TypeMismatchInStatement(ast)
            elif not type(left) in [Id, ArrayCell]:
                raise NotLeftValue(ast)
            else:
                return left

        elif ast.op in ['+', '-', '*', '/']:
            if type(left) is IntType and type(right) is IntType:
                return IntType()
            elif (type(left),type(right)) in [(IntType,FloatType),(FloatType,IntType),(FloatType,FloatType)]:
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

        elif ast.op in ['&&','||']:
            if type(left) is Boolean and type(right) is Boolean:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        else:
            raise TypeMismatchInExpression(ast)


    def visitUnaryOp(self, ast, c):
        expr = self.visit(ast.body, c)
        if ast.op == '-':
            if type(expr) in [IntType, FloatType]:
                return expr
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == '!':
            if type(expr) is BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        else: raise TypeMismatchInExpression(ast)


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
        rettype = c[2]
        res = ast.expr
        if res is not None:
            expr = self.visit(res, c)
        if isinstance(rettype,VoidType):
            if res is not None:
                raise TypeMismatchInStatement(ast)
            else:
                return True  
        else:
            if res is None:
                raise TypeMismatchInStatement(ast) 
            elif type(rettype) != type(expr):
                if isinstance(rettype,FloatType) and isinstance(expr,IntType):
                    return True
                else:
                    return False
            elif isinstance(rettype,ArrayPointerType):
                    if isinstance(expr,ArrayPointerType) or isinstance(expr,ArrayType):
                        if type(rettype.eleType) == type(expr.eleType):
                            return True
                        else:
                            return False
                    else:
                        return False
            else:
                return True
   
    

    def visitIntLiteral(self,ast, c): 
        return IntType()

    def visitFloatLiteral(self,ast,c):
        return FloatType()

    def visitBooleanLiteral(self,ast,c):
        return BoolType()

    def visitStringLiteral(self,ast,c):
        return StringType()