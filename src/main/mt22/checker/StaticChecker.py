from AST import *
from Visitor import Visitor
from Utils import Utils
from StaticError import *
from functools import *

class MType:
    def __init__(self, partype, rtype):
        self.partype = partype
        self.rtype = rtype
    
class Symbol:
    def __init__(self, name, typ):
        self.name = name
        self.mtype = typ

class TypeUtils:
    @ staticmethod
    def infer(id, type, o, kind=Variable):
        for env in o:
            if (id.name in env) and (env[id.name]["kind"] is kind):
                env[id.name]["type"] = type
                return {"type": type}
        return {"type": None}
class Search:
    @ staticmethod
    def search(name, env, func, kind=Variable):
        for x in env:
            if (name in x) and (x[name]["kind"] is kind):
                return x[name]
        return func()
    
class Check:
    @ staticmethod
    def check(name, env, func) -> None:
        if name in env:
            func()    

class StaticChecker(Visitor, Utils):
    globalenv = [
        Symbol("readInteger", MType([], IntegerType())),
        Symbol("printInteger", MType([IntegerType()], VoidType())),
        Symbol("readFloat", MType([], FloatType())),
        Symbol("writeFloat", MType([FloatType()], VoidType())),
        Symbol("readBoolean", MType([], BooleanType())),
        Symbol("printBoolean", MType([BooleanType()], VoidType())),
        Symbol("readString", MType([], StringType())),
        Symbol("printString", MType([StringType()], VoidType())),
        Symbol("super", MType([[Expr()]], VoidType())),
        Symbol("preventDefault", MType([], VoidType())),
    ]
    def raisee(self, x):
        raise x

    def __init__(self, ast):
        self.ast = ast
        self.env = [{}]
        self.init = None
        self.inloop = []
        self.forloop= {"t": False, "ast": None}
        self.funcdecl = {"t": False, "rtype": None, "name": None, "inher": {"funcname": None, "s_pD": None}}
        
 
    def check(self):
        return self.visit(self.ast, StaticChecker.globalenv)

    def visitIntegerType(self, ast, param): return {"type": IntegerType()}
    def visitFloatType(self, ast, param): return {"type": FloatType()}
    def visitBooleanType(self, ast, param): return {"type": BooleanType()}
    def visitStringType(self, ast, param): return {"type": StringType()}
    def visitArrayType(self, ast, param): return ast
    def visitAutoType(self, ast, param): return {"type": AutoType()}
    def visitVoidType(self, ast, param): return {"type": VoidType()}

    def visitBinExpr(self, ast: BinExpr, param):
        o, typ= param
        op = ast.op
        righttyp = None
        lefttyp = None
        if (ast.right is FuncCall) and (ast.left is FuncCall):
            rightn = ast.right.name
            leftn = ast.left.name
            rightsym = self.lookup(rightn, StaticChecker.globalenv, lambda sym: sym.name)
            leftsym = self.lookup(leftn, StaticChecker.globalenv, lambda sym: sym.name)
            righttyp = Search.search(rightn, o, lambda: self.raisee(Undeclared(Function(), rightn)), Function)["type"] if rightsym is None else rightsym.mtype.rtype
            lefttyp = Search.search(leftn, o, lambda: self.raisee(Undeclared(Function(), leftn)), Function)["type"] if leftsym is None else leftsym.mtype.rtype
            if righttyp is AutoType and lefttyp is AutoType:
                righttyp = self.visit(ast.right, param)["type"]
                lefttyp = self.visit(ast.left, param)["type"]
            elif righttyp is AutoType:
                righttyp = self.visit(ast.right, (o, lefttyp))["type"]
            elif lefttyp is AutoType:
                lefttyp = self.visit(ast.right, (o, righttyp))["type"]
                
        elif ast.right is FuncCall:
            rightn = ast.right.name
            rightsym = self.lookup(rightn, StaticChecker.globalenv, lambda sym: sym.name)
            righttyp = Search.search(rightn, o, lambda: self.raisee(Undeclared(Function(), rightn)), Function)["type"] if rightsym is None else rightsym.mtype.rtype
            lefttyp = self.visit(ast.left, param)["type"]
            righttyp = self.visit(ast.right, (o, lefttyp if righttyp is AutoType else typ))["type"]
            
        elif ast.left is FuncCall:
            leftn = ast.left.name
            leftsym = self.lookup(rightn, StaticChecker.globalenv, lambda sym: sym.name)
            lefttyp = Search.search(rightn, o, lambda: self.raisee(Undeclared(Function(), leftn)), Function)["type"] if leftsym is None else leftsym.mtype.rtype
            righttyp = self.visit(ast.right, param)["type"]
            lefttyp = self.visit(ast.left, (o, righttyp if lefttyp is AutoType else typ))["type"]
            
        else:
            righttyp = self.visit(ast.right, param)["type"]
            lefttyp = self.visit(ast.left, param)["type"]
            
        if op in ["+", "-", "*", "/"]:
            if (righttyp is FloatType or righttyp is IntegerType) and (lefttyp is FloatType or lefttyp is IntegerType):
                if lefttyp is FloatType or righttyp is FloatType:
                    return {"type": FloatType()}
                return {"type": IntegerType()}
            raise TypeMismatchInExpression(ast)

        if op in ["%"]:
            if righttyp is IntegerType and lefttyp is IntegerType:
                return {"type": IntegerType()}
            raise TypeMismatchInExpression(ast)

        if op in ["==", "!="]:
            if (righttyp is IntegerType and lefttyp is IntegerType) or (righttyp is BooleanType and lefttyp is BooleanType):
                return {"type": BooleanType()}
            raise TypeMismatchInExpression(ast)

        if op in ["<", ">", "<=", ">="]:
            if (righttyp is IntegerType and lefttyp is IntegerType) or (righttyp is FloatType and lefttyp is FloatType):
                return {"type": BooleanType()}
            raise TypeMismatchInExpression(ast)

        if op in ["&&", "||"]:
            if righttyp is BooleanType and lefttyp is BooleanType:
                return {"type": BooleanType()}
            raise TypeMismatchInExpression(ast)
        
        if op in ["::"]:
            if righttyp is StringType and lefttyp is StringType:
                return {"type": StringType()}
            raise TypeMismatchInExpression(ast)

        
    def visitUnExpr(self, ast: UnExpr, param):
        e = self.visit(ast.val, param)
        op = ast.op
        if op in ["!"]:
            if e["type"] is BooleanType:
                return {"type": BooleanType()}
            raise TypeMismatchInExpression(ast)
        if op == "-":
            if e["type"] is IntegerType or e["type"] is FloatType:
                return {"type": e["type"]}
            raise TypeMismatchInExpression(ast)

    def visitId(self, ast: Id, param):
        (o, _) = param
        return Search.search(ast.name, o, lambda: self.raisee(
            Undeclared(Identifier(), ast.name)), Variable)
    def visitArrayCell(self, ast, param): pass
    def visitIntegerLit(self, ast, param): return {"type": IntegerType()}
    def visitFloatLit(self, ast, param): return {"type": FloatType()}
    def visitStringLit(self, ast, param): return {"type": BooleanType()}
    def visitBooleanLit(self, ast, param): return {"type": StringType()}
    def visitArrayLit(self, ast, param): pass
    def visitFuncCall(self, ast, param): pass

    def visitAssignStmt(self, ast, param): pass
    def visitBlockStmt(self, ast: BlockStmt, param):
        (o, t) = param
        reduce(lambda _, e: self.visit(e, (o if self.forloop["t"] or self.funcdecl["t"] else [{}] + o, t)), ast.body, [])
    def visitIfStmt(self, ast: IfStmt, param):
        cond = self.visit(ast.cond, param)
        if cond["type"] is BooleanType:
            if ast.fstmt is None:
                self.visit(ast.tstmt, param)
            else:
                self.visit(ast.tstmt, param)
                self.visit(ast.fstmt, param)
        else: raise TypeMismatchInStatement(ast)
            
    def visitForStmt(self, ast, param): pass
    def visitWhileStmt(self, ast, param): pass
    def visitDoWhileStmt(self, ast, param): pass
    def visitBreakStmt(self, ast, param): pass
    def visitContinueStmt(self, ast, param): pass
    def visitReturnStmt(self, ast, param): pass
    def visitCallStmt(self, ast, param): pass

    def visitVarDecl(self, ast, param): pass
    def visitParamDecl(self, ast, param): pass
    def visitFuncDecl(self, ast, param): pass

    def visitProgram(self, ast, param): pass
