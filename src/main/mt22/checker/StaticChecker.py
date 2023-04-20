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
    @staticmethod
    def infer(name, type, o, kind=Variable):
        for env in o:
            if (name in env) and (env[name]["kind"] is kind):
                env[name]["type"] = type
                return {"type": type}
        return {"type": None}
class Search:
    @staticmethod
    def search(name, env, func, kind=Variable):
        for x in env:
            if (name in x) and (x[name]["kind"] is kind):
                return x[name]
        return func()
    
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

    def __init__(self, ast):
        self.ast = ast
        self.env = [{}]
        self.init = None
        self.inloop = []
        self.forloop= {"t": False, "ast": None}
        self.funcdecl = {"t": False, "rtype": None, "name": None, "inher": {"func": None, "s_pD": None}}
        
 
    def check(self):
        return self.visit(self.ast, StaticChecker.globalenv)
    
    def raisee(self, x):
        raise x
    
    def checkParam(self, name, o):
        if self.funcdecl["inher"]["func"] is not None and self.funcdecl["inher"]["s_pD"] == "super":
            func = Search.search(self.funcdecl["inher"]["func"]["name"], o, None, Function)
            param = self.lookup(name, func["params_inher"], lambda x: x["name"])
            if param is not None and param["inher"]:
                raise Invalid(Parameter(), name)

    def visitIntegerType(self, ast: IntegerType, param): return {"type": IntegerType()}
    def visitFloatType(self, ast:FloatType, param): return {"type": FloatType()}
    def visitBooleanType(self, ast:BooleanType, param): return {"type": BooleanType()}
    def visitStringType(self, ast:StringType, param): return {"type": StringType()}
    def visitArrayType(self, ast:ArrayType, param): return ast
    def visitAutoType(self, ast:AutoType, param): return {"type": AutoType()}
    def visitVoidType(self, ast:VoidType, param): return {"type": VoidType()}

    def visitBinExpr(self, ast: BinExpr, param):
        o, typ= param
        op = ast.op
        righttyp = None
        lefttyp = None
        if (ast.right is FuncCall) and (ast.left is FuncCall):
            rightn = ast.right.name
            leftn = ast.left.name
            rightsym = self.lookup(rightn, StaticChecker.globalenv, lambda x: x.name)
            leftsym = self.lookup(leftn, StaticChecker.globalenv, lambda x: x.name)
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
            rightsym = self.lookup(rightn, StaticChecker.globalenv, lambda x: x.name)
            righttyp = Search.search(rightn, o, lambda: self.raisee(Undeclared(Function(), rightn)), Function)["type"] if rightsym is None else rightsym.mtype.rtype
            lefttyp = self.visit(ast.left, param)["type"]
            righttyp = self.visit(ast.right, (o, lefttyp if righttyp is AutoType else typ))["type"]
            
        elif ast.left is FuncCall:
            leftn = ast.left.name
            leftsym = self.lookup(rightn, StaticChecker.globalenv, lambda x: x.name)
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
        o, _ = param
        return Search.search(ast.name, o, lambda: self.raisee(Undeclared(Identifier(), ast.name)), Variable)
    def visitArrayCell(self, ast: ArrayCell, param): pass
    def visitIntegerLit(self, ast: IntegerLit, param): return {"type": IntegerType()}
    def visitFloatLit(self, ast:FloatLit, param): return {"type": FloatType()}
    def visitStringLit(self, ast:StringLit, param): return {"type": BooleanType()}
    def visitBooleanLit(self, ast:BooleanLit, param): return {"type": StringType()}
    
    def visitArrayLit(self, ast:ArrayLit, param): pass
    def visitFuncCall(self, ast:FuncCall, param): pass
    def visitAssignStmt(self, ast:AssignStmt, param): pass
    
    def visitBlockStmt(self, ast: BlockStmt, param):
        o, t = param
        reduce(lambda _, line: self.visit(line, (o if self.forloop["t"] or self.funcdecl["t"] else [{}] + o, t)), ast.body, [])
    def visitIfStmt(self, ast: IfStmt, param):
        cond = self.visit(ast.cond, param)
        if cond["type"] is BooleanType:
            if ast.fstmt is None:
                self.visit(ast.tstmt, param)
            else:
                self.visit(ast.tstmt, param)
                self.visit(ast.fstmt, param)
        else: raise TypeMismatchInStatement(ast)
            
    def visitForStmt(self, ast: ForStmt, param): 
        o, t = param
        self.forloop["t"] = True
        self.forloop["ast"] = ast
        e = "layer"
        self.inloop.append(e)
        env = [{}] + o
        self.visit(ast.init, (env, t))
        self.forloop["t"] = False
        self.forloop["ast"] = None
        cond= self.visit(ast.cond, (env, t))["type"]
        upd = self.visit(ast.upd, (env, t))["type"]
        if cond is BooleanType and upd is BooleanType:
            self.visit(ast.stmt, (env, t))
            self.inloop.pop()
        else: raise TypeMismatchInStatement(ast)
    def visitWhileStmt(self, ast: WhileStmt, param):
        e = "layer"
        self.inloop.append(e)
        cond = self.visit(ast.cond, param)["type"]
        if cond is BooleanType:
            self.visit(ast.stmt, param)
            self.inloop.pop()
        else: raise TypeMismatchInStatement(ast)
    def visitDoWhileStmt(self, ast: DoWhileStmt, param):
        e = "layer"
        self.inloop.append(e)
        self.visit(ast.stmt, param)
        cond = self.visit(ast.cond, param)["type"]
        if cond is BooleanType:
            self.inloop.pop()
        else: raise TypeMismatchInStatement(ast)
    def visitBreakStmt(self, ast:BreakStmt, param):
        if len(self.inloop) == 0:
            MustInLoop(ast)
    def visitContinueStmt(self, ast:ContinueStmt, param):
        if len(self.inloop) == 0:
            MustInLoop(ast)
    def visitReturnStmt(self, ast:ReturnStmt, param):
        o, _ = param
        exprtyp = VoidType() if ast.expr is None else self.visit(ast.expr, param)["type"]

        if self.funcdecl["t"]:
            functype = self.funcdecl["rtype"]["type"]
            if functype is AutoType:
                self.funcdecl["rtype"] = TypeUtils.infer(self.funcdecl["name"], exprtyp, o, Function)
            else:
                if functype is not FloatType and exprtyp is not IntegerType:
                    if functype is not exprtyp:
                        raise TypeMismatchInStatement(ast)
                    
    def visitCallStmt(self, ast:CallStmt, param): pass
    def visitVarDecl(self, ast:VarDecl, param): pass
    def visitParamDecl(self, ast:ParamDecl, param):
        o, _ = param
        name = ast.name
        self.checkParam(name, o, Parameter())
        par = {"name": name, "type": ast.typ, "kind": Variable(),
               "inher": ast.inherit, "out": ast.out}
        o[0][name] = par
        return par
    def visitFuncDecl(self, ast:FuncDecl, param): 
        o, _ = param
        name = ast.name
        check = self.lookup(name, StaticChecker.globalenv, lambda x: x.name)
        if check is not None:
            raise Redeclared(Function(), name)
        o1 = [{}] + o
        inherit = ast.inherit
        body = ast.body
        self.funcdecl["t"] = True
        self.funcdecl["rtype"] = ast.return_type
        self.funcdecl["name"] = ast.name

        if inherit is not None:
            inherfunc = Search.search(inherit, o1, lambda: self.raisee(
                Undeclared(Function(), inherit)), Function)
            if len(inherfunc["params"]) != 0:
                if len(body.body) == 0:
                    raise InvalidStatementInFunction(name)
                fstmt = body.body[0]
                if fstmt is not CallStmt:
                    raise InvalidStatementInFunction(name)
                fstmt_name = fstmt.name
                if fstmt_name != "super" and fstmt_name != "preventDefault":
                    raise InvalidStatementInFunction(name)
                self.funcdecl["inher"]["s_pD"] = "preventDefault" if fstmt_name == "preventDefault" else "super"
            else:
                if len(body.body) != 0:
                    fstmt = body.body[0]
                    if fstmt is CallStmt:
                        fstmt_name = fstmt.name
                        if fstmt_name == "preventDefault":
                            self.funcdecl["inher"]["s_pD"] = "preventDefault"
                        else:
                            raise InvalidStatementInFunction(name)
                    else:
                        raise InvalidStatementInFunction(name)
            self.funcdecl["inher"]["func"] = {
                **inherfunc, **{"name": inherit}}
        params = []
        params_inher = [*self.funcdecl["inher"]["func"]["params_inher"]] if self.funcdecl["inher"]["func"] is not None else []
        if self.funcdecl["inher"]["super_or_preventDefault"] == "super":
            for par in params_inher:
                o1[0][par["name"]] = par
        for e in ast.params:
            par = self.visit(e, (o1, None))
            if par["inher"]:
                params_inher.append(par)
            params.append(par)
        o[0][name]["params_inher"] = params_inher
        o[0][name]["params"] = params
        self.visit(body, (o1, None))
        self.funcdecl["t"] = False
        self.funcdecl["rtype"] = None
        self.funcdecl["name"] = None
        self.funcdecl["inher"] = {
            "func": None, "s_pD": None}
    def visitProgram(self, ast:Program, param): pass
