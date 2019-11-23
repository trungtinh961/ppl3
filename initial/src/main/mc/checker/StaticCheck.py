
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
            lstDecl.insert(0,temp)
            if type(decl) is FuncDecl:
                self.lstFunc.append(temp)        
        entryPoint = self.lookup("main", self.lstFunc, lambda x: x.name)
        if entryPoint is None:
            raise NoEntryPoint()
        else:
            self.lstCall.append(entryPoint)
        at = [self.visit(x, (lstDecl, self.lstFunc)) for x in ast.decl]
        for x in self.lstFunc:
            if not x in self.lstCall:
                raise UnreachableFunction(x.name)
        return at

    def visitVarDecl(self,ast,c):
        return False
        
    def visitFuncDecl(self,ast, c):
        env = c[0].copy()
        lstLocal = []
        for param in ast.param:
            res = self.checkRedeclared(param,lstLocal,True)
            lstLocal.append(res)
            env.insert(0,res)
        hasReturn = self.visit(ast.body, (env, lstLocal, False, ast.returnType, ast.name.name))
        if not hasReturn and not (type(ast.returnType) is VoidType):
            raise FunctionNotReturn(ast.name.name)
        return hasReturn

    def visitBlock(self,ast,c):
        lstLocal = c[1].copy()
        env = c[0].copy()
        hasReturn = False
        for i in ast.member:
            if type(i) is VarDecl:
                res = self.checkRedeclared(i,lstLocal,False)
                lstLocal.append(res)
                env.insert(0,res)
            else:
                at = self.visit(i,(env,[],c[2],c[3],c[4])) # c = (global,[],isLoop,rettype,name)
                if type(at) is bool and at == True:
                    hasReturn = True
        return hasReturn

    def visitCallExpr(self, ast, c): 
        at = [self.visit(x,c) for x in ast.param]        
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None:
            raise Undeclared(Function(),ast.method.name)
        elif not type(res.mtype) is MType:
            raise TypeMismatchInExpression(ast)
        elif len(res.mtype.partype) != len(at):
            raise TypeMismatchInExpression(ast)
        else:
            if ast.method.name != c[4]:
                self.lstCall.append(res)
            for a,b in zip(res.mtype.partype, at):
                if type(a) is ArrayPointerType and type(b) in [ArrayPointerType,ArrayType]:
                    if type(a.eleType) != type(b.eleType):
                        raise TypeMismatchInExpression(ast)
                elif type(a) != type(b):
                    if not (type(a), type(b)) == (FloatType, IntType):
                        raise TypeMismatchInExpression(ast)
        return res.mtype.rettype
    
    def visitId(self,ast,c):
        at = self.lookup(ast.name,c[0],lambda x: x.name)
        if at is None: 
            raise Undeclared(Identifier(),ast.name)
        else:
            return at.mtype 

    def visitArrayCell(self,ast,c):
        arr = self.visit(ast.arr,c)
        idx = self.visit(ast.idx,c)
        if not type(idx) is IntType or (not type(arr) in [ArrayType, ArrayPointerType]):        
            raise TypeMismatchInExpression(ast)
        else:
            return arr.eleType

    def visitBinaryOp(self,ast,c):
        left = self.visit(ast.left,c)
        right = self.visit(ast.right,c)
        if ast.op is '=':
            if not type(ast.left) in [Id, ArrayCell]:
                raise NotLeftValue(ast.left)
            elif type(left) in [VoidType, ArrayType, ArrayPointerType, MType]:
                raise TypeMismatchInExpression(ast)
            elif type(left) != type(right):
                if type(left) is FloatType and type(right) is IntType:
                    return FloatType()
                else:
                    raise TypeMismatchInExpression(ast)
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
            if type(left) is BoolType and type(right) is BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)

        elif ast.op in ['<', '>', '<=', '>=']:
            if type(left) in [IntType,FloatType] and type(right) in [IntType,FloatType]:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)

        elif ast.op in ['&&','||']:
            if type(left) is BoolType and type(right) is BoolType:
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
        else: 
            raise TypeMismatchInExpression(ast)

    def visitIf(self,ast,c):
        exp = ast.expr
        thenStmt = ast.thenStmt
        elseStmt = ast.elseStmt
        if not type(self.visit(exp, c)) is BoolType:
            raise TypeMismatchInStatement(ast)
        thenReturn = self.visit(thenStmt,c)
        if elseStmt is None:
            return False
        else:
            elseReturn = self.visit(elseStmt,c)
            return (thenReturn is True) and (elseReturn is True)
            
    def visitFor(self,ast,c):
        expr1 = self.visit(ast.expr1,c)
        expr2 = self.visit(ast.expr2,c)
        expr3 = self.visit(ast.expr3,c)        
        if (type(expr1), type(expr2), type(expr3)) != (IntType, BoolType, IntType):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.loop, (c[0], c[1], True, c[3], c[4]))

    def visitDowhile(self,ast,c):
        exp = self.visit(ast.exp, c)
        if type(exp) != BoolType:
            raise TypeMismatchInStatement(ast)
        hasReturn = False
        for x in ast.sl:
            at = self.visit(x, (c[0], c[1], True, c[3], c[4]))
            if type(at) is bool and at is True:
                hasReturn = True
        return hasReturn

    def visitBreak(self,ast,c):
        if c[2] == False:
            raise BreakNotInLoop()
        else:
            return False

    def visitContinue(self, ast, c):
        if c[2] == False:
            raise ContinueNotInLoop()
        else:
            return False 

    def visitReturn(self, ast, c):
        rettype = c[3]
        if ast.expr is not None:
            expr = self.visit(ast.expr, c)
        if isinstance(rettype,VoidType):
            if ast.expr is not None:
                raise TypeMismatchInStatement(ast)
            else:
                return True  
        else:
            if ast.expr is None:
                raise TypeMismatchInStatement(ast) 
            else:
                if type(rettype) is ArrayPointerType and type(expr) in [ArrayPointerType,ArrayType]:
                    if type(rettype.eleType) == type(expr.eleType):
                        return True
                    else: 
                        raise TypeMismatchInStatement(ast)
                elif type(rettype) != type(expr):
                    if (type(rettype), type(expr)) == (FloatType, IntType):
                        return True
                    else: 
                        raise TypeMismatchInStatement(ast)
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