from AST import *
from Visitor import Visitor
from Utils import Utils
from StaticError import *
from functools import *

class MType:
    def __init__(self, ptype, rtype):
        self.ptype = ptype
        self.rtype = rtype
    
class Symbol:
    def __init__(self, name, typ):
        self.name = name
        self.mtype = typ

class TypeUtils:
    @staticmethod
    def infer(name, type, o, kind=Variable):
        for env in o:
            if (name in env) and (env[name]['kind'] is kind):
                env[name]['type'] = type
                return {'type': type}
        return {'type': None}
class Search:
    @staticmethod
    def search(name, env, func, kind=Variable):
        for x in env:
            if (name in x) and (x[name]['kind'] is kind):
                return x[name]
        return func()
class Check:
    @staticmethod
    def check(name, dic, func) -> None:
        if name in dic:
            func()
class Array(Type):
    def __init__(self, v: int, t: Type) -> None:
        self.v = v
        self.t = t
    @staticmethod
    def getDi(a):
        if a is not Array:
            return []
        return [a.v, *Array.getDi(a.t)]
    @staticmethod
    def equal(dimen1, dimen2, func):
        if (len(dimen1) != len(dimen2)):
            func()
        return True
        
class StaticChecker(Visitor, Utils):
    globalenv = [
        Symbol('readInteger', MType([], IntegerType())),
        Symbol('printInteger', MType([IntegerType()], VoidType())),
        Symbol('readFloat', MType([], FloatType())),
        Symbol('writeFloat', MType([FloatType()], VoidType())),
        Symbol('readBoolean', MType([], BooleanType())),
        Symbol('printBoolean', MType([BooleanType()], VoidType())),
        Symbol('readString', MType([], StringType())),
        Symbol('printString', MType([StringType()], VoidType())),
        Symbol('super', MType([[Expr()]], VoidType())),
        Symbol('preventDefault', MType([], VoidType())),
    ]

    def __init__(self, ast):
        self.ast = ast
        self.env = [{}]
        self.init = None
        self.inloop = []
        self.ill = None
        self.forloop= {'t': False, 'ast': None}
        self.funcdecl = {'t': False, 'rtype': None, 'name': None, 'inher': {'func': None, 's_pD': None}}
        
 
    def check(self):
        return self.visit(self.ast, StaticChecker.globalenv)
    
    def raisee(self, x):
        raise x
    
    def checkParam(self, name, o):
        if self.funcdecl['inher']['func'] is not None and self.funcdecl['inher']['s_pD'] == 'super':
            func = Search.search(self.funcdecl['inher']['func']['name'], o, None, Function)
            param = self.lookup(name, func['params_inher'], lambda x: x['name'])
            if param is not None and param['inher']:
                raise Invalid(Parameter(), name)

    def visitIntegerType(self, ast: IntegerType, param): return {'type': IntegerType()}
    def visitFloatType(self, ast:FloatType, param): return {'type': FloatType()}
    def visitBooleanType(self, ast:BooleanType, param): return {'type': BooleanType()}
    def visitStringType(self, ast:StringType, param): return {'type': StringType()}
    def visitArrayType(self, ast:ArrayType, param): return ast
    def visitAutoType(self, ast:AutoType, param): return {'type': AutoType()}
    def visitVoidType(self, ast:VoidType, param): return {'type': VoidType()}

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
            righttyp = Search.search(rightn, o, lambda: self.raisee(Undeclared(Function(), rightn)), Function)['type'] if rightsym is None else rightsym.mtype.rtype
            lefttyp = Search.search(leftn, o, lambda: self.raisee(Undeclared(Function(), leftn)), Function)['type'] if leftsym is None else leftsym.mtype.rtype
            if righttyp is AutoType and lefttyp is AutoType:
                righttyp = self.visit(ast.right, param)['type']
                lefttyp = self.visit(ast.left, param)['type']
            elif righttyp is AutoType:
                righttyp = self.visit(ast.right, (o, lefttyp))['type']
            elif lefttyp is AutoType:
                lefttyp = self.visit(ast.right, (o, righttyp))['type']
                
        elif ast.right is FuncCall:
            rightn = ast.right.name
            rightsym = self.lookup(rightn, StaticChecker.globalenv, lambda x: x.name)
            righttyp = Search.search(rightn, o, lambda: self.raisee(Undeclared(Function(), rightn)), Function)['type'] if rightsym is None else rightsym.mtype.rtype
            lefttyp = self.visit(ast.left, param)['type']
            righttyp = self.visit(ast.right, (o, lefttyp if righttyp is AutoType else typ))['type']
            
        elif ast.left is FuncCall:
            leftn = ast.left.name
            leftsym = self.lookup(rightn, StaticChecker.globalenv, lambda x: x.name)
            lefttyp = Search.search(rightn, o, lambda: self.raisee(Undeclared(Function(), leftn)), Function)['type'] if leftsym is None else leftsym.mtype.rtype
            righttyp = self.visit(ast.right, param)['type']
            lefttyp = self.visit(ast.left, (o, righttyp if lefttyp is AutoType else typ))['type']
            
        else:
            righttyp = self.visit(ast.right, param)['type']
            lefttyp = self.visit(ast.left, param)['type']
            
        if op in ['+', '-', '*', '/']:
            if (righttyp is FloatType or righttyp is IntegerType) and (lefttyp is FloatType or lefttyp is IntegerType):
                if lefttyp is FloatType or righttyp is FloatType:
                    return {'type': FloatType()}
                return {'type': IntegerType()}
            raise TypeMismatchInExpression(ast)

        if op in ['%']:
            if righttyp is IntegerType and lefttyp is IntegerType:
                return {'type': IntegerType()}
            raise TypeMismatchInExpression(ast)

        if op in ['==', '!=']:
            if (righttyp is IntegerType and lefttyp is IntegerType) or (righttyp is BooleanType and lefttyp is BooleanType):
                return {'type': BooleanType()}
            raise TypeMismatchInExpression(ast)

        if op in ['<', '>', '<=', '>=']:
            if (righttyp is IntegerType and lefttyp is IntegerType) or (righttyp is FloatType and lefttyp is FloatType):
                return {'type': BooleanType()}
            raise TypeMismatchInExpression(ast)

        if op in ['&&', '||']:
            if righttyp is BooleanType and lefttyp is BooleanType:
                return {'type': BooleanType()}
            raise TypeMismatchInExpression(ast)
        
        if op in ['::']:
            if righttyp is StringType and lefttyp is StringType:
                return {'type': StringType()}
            raise TypeMismatchInExpression(ast)

        
    def visitUnExpr(self, ast: UnExpr, param):
        e = self.visit(ast.val, param)
        op = ast.op
        if op in ['!']:
            if e['type'] is BooleanType:
                return {'type': BooleanType()}
            raise TypeMismatchInExpression(ast)
        if op == '-':
            if e['type'] is IntegerType or e['type'] is FloatType:
                return {'type': e['type']}
            raise TypeMismatchInExpression(ast)

    def visitId(self, ast: Id, param):
        o, _ = param
        return Search.search(ast.name, o, lambda: self.raisee(Undeclared(Identifier(), ast.name)), Variable)
    def visitArrayCell(self, ast: ArrayCell, param):
        id = self.visit(Id(ast.name), param)
        if id['type'] is not ArrayType:
            raise TypeMismatchInExpression(ast)
        reduce(lambda _, e: self.raisee(TypeMismatchInExpression(ast)) if self.visit(e, param)['type'] is not IntegerType else None, ast.cell, [])
        dimensions = id['type'].dimensions[len(ast.cell):][::-1]
        if (len(dimensions) != 0):
            res = reduce(lambda x, y: Array(y, x),dimensions[1:], Array(dimensions[0], id['type']))
            return {'type': res}
        return {'type': id['type'].typ}
    def visitIntegerLit(self, ast: IntegerLit, param): return {'type': IntegerType()}
    def visitFloatLit(self, ast:FloatLit, param): return {'type': FloatType()}
    def visitStringLit(self, ast:StringLit, param): return {'type': BooleanType()}
    def visitBooleanLit(self, ast:BooleanLit, param): return {'type': StringType()}
    
    def visitArrayLit(self, ast:ArrayLit, param):
        o, typ = param
        exprlist = ast.explist
        list = list(map(lambda expr: self.visit(expr, param), exprlist))
        if len(list) != 0:
            firsttyp = list[0]['type']
            if firsttyp is Array:
                maxv = firsttyp
                for e in list:
                    if e['type'].v >= maxv.v:
                        maxv = e['type']
                return {'type': Array(len(exprlist), maxv)}
            list(map(lambda r: self.raisee(IllegalArrayLiteral(ast)) if ((r['type'] if r['type'] is not ArrayType else r['type'].typ) is not firsttyp) else None, list))
            for e in list:
                etyp = e['type'] if e['type'] is not ArrayType else e['type'].typ
                if self.ill['type'] is not etyp and (not(self.ill['type'] is FloatType and etyp is IntegerType)) and etyp is not Array:
                    raise TypeMismatchInStatement(self.ill['ast'])
            return {'type': Array(len(exprlist), typ)}
        return {'type': Array(0, typ)}
    def visitFuncCall(self, ast:FuncCall, param):
        o, t = param
        func = dict()
        params = None
        functyp = None
        name = ast.name
        sym= self.lookup(name, StaticChecker.globalenv, lambda x: x.name)
        if sym is None:
            func = Search.search(name, o, lambda: self.raisee(Undeclared(Function(), name)), Function)
            functyp = func['type']
            params = func['params']
        else:
            if name == 'super' or name == 'preventDefault':
                params = self.funcdecl['inher']['func']['params'] if name == 'super' else sym.mtype.ptype
            else:
                params = list(map(lambda par: self.visit(
                    par, param), sym.mtype.ptype))
            functyp = sym.mtype.rtype
        if len(ast.args) != len(params) or functyp is VoidType:
            raise TypeMismatchInExpression(ast)
        for pa in zip(params, ast.args):
            patyp = self.visit(pa[1], (o, pa[0]['type']))['type']
            if not (pa[0]['type'] is FloatType and patyp is IntegerType):
                if pa[0]['type'] is not patyp:
                    raise TypeMismatchInExpression(ast)
        if functyp is AutoType and sym is None:
            functyp = TypeUtils.infer(
                name, t, o, Function)['type']
            func['type'] = functyp
        return {'type': functyp}
    def visitAssignStmt(self, ast:AssignStmt, param):
        o, _ = param
        lhstyp = None
        if self.forloop['t']:
            name = ast.lhs.name
            id = Search.search(name, o, lambda: None, Variable)
            if id is None:
                o[0][name] = {'type': IntegerType(), 'kind': Variable()}
                lhstyp = IntegerType()
            else:
                if id['type'] is not IntegerType:
                    raise TypeMismatchInStatement(self.forloop['ast'])
                lhstyp = id['type']
        else:
            lhstyp = self.visit(ast.lhs, param)['type']
            if lhstyp is ArrayType or lhstyp is VoidType:
                raise TypeMismatchInStatement(ast)

        rhstyp = self.visit(ast.rhs, (o, lhstyp))['type']
        if not (lhstyp is FloatType and rhstyp is IntegerType):
            if lhstyp is not rhstyp:
                raise (TypeMismatchInStatement(ast if not self.forloop['t'] else self.forloop['ast']))

    
    def visitBlockStmt(self, ast: BlockStmt, param):
        o, t = param
        reduce(lambda _, line: self.visit(line, (o if self.forloop['t'] or self.funcdecl['t'] else [{}] + o, t)), ast.body, [])
    def visitIfStmt(self, ast: IfStmt, param):
        cond = self.visit(ast.cond, param)
        if cond['type'] is BooleanType:
            if ast.fstmt is None:
                self.visit(ast.tstmt, param)
            else:
                self.visit(ast.tstmt, param)
                self.visit(ast.fstmt, param)
        else: raise TypeMismatchInStatement(ast)
            
    def visitForStmt(self, ast: ForStmt, param): 
        o, t = param
        self.forloop['t'] = True
        self.forloop['ast'] = ast
        e = 'layer'
        self.inloop.append(e)
        env = [{}] + o
        self.visit(ast.init, (env, t))
        self.forloop['t'] = False
        self.forloop['ast'] = None
        cond= self.visit(ast.cond, (env, t))['type']
        upd = self.visit(ast.upd, (env, t))['type']
        if cond is BooleanType and upd is BooleanType:
            self.visit(ast.stmt, (env, t))
            self.inloop.pop()
        else: raise TypeMismatchInStatement(ast)
    def visitWhileStmt(self, ast: WhileStmt, param):
        e = 'layer'
        self.inloop.append(e)
        cond = self.visit(ast.cond, param)['type']
        if cond is BooleanType:
            self.visit(ast.stmt, param)
            self.inloop.pop()
        else: raise TypeMismatchInStatement(ast)
    def visitDoWhileStmt(self, ast: DoWhileStmt, param):
        e = 'layer'
        self.inloop.append(e)
        self.visit(ast.stmt, param)
        cond = self.visit(ast.cond, param)['type']
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
        exprtyp = VoidType() if ast.expr is None else self.visit(ast.expr, param)['type']

        if self.funcdecl['t']:
            functype = self.funcdecl['rtype']['type']
            if functype is AutoType:
                self.funcdecl['rtype'] = TypeUtils.infer(self.funcdecl['name'], exprtyp, o, Function)
            else:
                if not (functype is FloatType and exprtyp is IntegerType):
                    if functype is not exprtyp:
                        raise TypeMismatchInStatement(ast)
                    
    def visitCallStmt(self, ast:CallStmt, param):
        o, _ = param
        name = ast.name
        sym = self.lookup(name, StaticChecker.globalenv, lambda sym: sym.name)
        params = None
        functyp = None
        func = dict()
        if sym is None:
            func = Search.search(name, o, lambda: self.raisee(Undeclared(Function(), name)), Function)
            functyp = func['type']
            params = func['params']
            if functyp is AutoType:
                func['type'] = functyp = VoidType()
        else:
            if name == 'super' or name == 'preventDefault':
                params = self.funcdecl['inher']['func']['params'] if name == 'super' else sym.mtype.ptype
            else:
                params = list(map(lambda par: self.visit(par, param), sym.mtype.ptype))
            functyp = sym.mtype.rtype

        if len(ast.args) != len(params) or functyp is not VoidType:
            raise (TypeMismatchInStatement(ast))
        
        for pa in zip(params, ast.args):
            patyp = self.visit(pa[1], (o, pa[0]['type']))['type']
            if not (pa[0]['type'] is FloatType and patyp is IntegerType):
                if pa[0]['type'] is not patyp:
                    raise TypeMismatchInStatement(ast)
        return {'type': functyp}
    def visitVarDecl(self, ast:VarDecl, param):
        o, _ = param
        name = ast.name
        Check.check(name, o[0], lambda: self.raisee(Redeclared(Variable(), name)))
        typ = ast.typ
        init = ast.init
        self.checkParam(name, o)
        if init is not None:
            if typ is ArrayType:
                adis = typ.dimensions
                atype = typ.typ
                self.ill = {'type': atype, 'dimensions': adis, 'ast': ast}

                if init is not ArrayLit and init is not ArrayCell:
                    raise TypeMismatchInVarDecl(ast)
                init = self.visit(init, (o, atype))
                dilist = Array.getDi(init['type'])
                if Array.equal(adis, dilist, lambda: self.raisee(TypeMismatchInVarDecl(ast))):
                    o[0][name] = {
                        'type': typ, 'kind': Variable(), 'dimensions': dilist}
                self.ill = None
            else:
                init = self.visit(init, (o, typ))
                inittyp = init['type']
                if inittyp is IntegerType and typ is FloatType:
                    o[0][name] = {'type': FloatType(), 'kind': Variable()}
                    return
                if type(typ) is not type(inittyp) and type(typ) is not AutoType:
                    raise TypeMismatchInExpression(ast)

                o[0][name] = {'type': inittyp if typ is AutoType else typ, 'kind': Variable()}
        else:
            if typ is AutoType:
                raise Invalid(Variable(), name)
            o[0][name] = {'type': typ, 'kind': Variable()}
    def visitParamDecl(self, ast:ParamDecl, param):
        o, _ = param
        name = ast.name
        self.checkParam(name, o, Parameter())
        par = {'name': name, 'type': ast.typ, 'kind': Variable(),
               'inher': ast.inherit, 'out': ast.out}
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
        self.funcdecl['t'] = True
        self.funcdecl['rtype'] = ast.return_type
        self.funcdecl['name'] = ast.name

        if inherit is not None:
            inherfunc = Search.search(inherit, o1, lambda: self.raisee(
                Undeclared(Function(), inherit)), Function)
            if len(inherfunc['params']) != 0:
                if len(body.body) == 0:
                    raise InvalidStatementInFunction(name)
                fstmt = body.body[0]
                if fstmt is not CallStmt:
                    raise InvalidStatementInFunction(name)
                fstmt_name = fstmt.name
                if fstmt_name != 'super' and fstmt_name != 'preventDefault':
                    raise InvalidStatementInFunction(name)
                self.funcdecl['inher']['s_pD'] = 'preventDefault' if fstmt_name == 'preventDefault' else 'super'
            else:
                if len(body.body) != 0:
                    fstmt = body.body[0]
                    if fstmt is CallStmt:
                        fstmt_name = fstmt.name
                        if fstmt_name == 'preventDefault':
                            self.funcdecl['inher']['s_pD'] = 'preventDefault'
                        else:
                            raise InvalidStatementInFunction(name)
                    else:
                        raise InvalidStatementInFunction(name)
            self.funcdecl['inher']['func'] = {
                **inherfunc, **{'name': inherit}}
        params = []
        params_inher = [*self.funcdecl['inher']['func']['params_inher']] if self.funcdecl['inher']['func'] is not None else []
        if self.funcdecl['inher']['s_pD'] == 'super':
            for par in params_inher:
                o1[0][par['name']] = par
        for e in ast.params:
            par = self.visit(e, (o1, None))
            if par['inher']:
                params_inher.append(par)
            params.append(par)
        o[0][name]['params_inher'] = params_inher
        o[0][name]['params'] = params
        self.visit(body, (o1, None))
        self.funcdecl['t'] = False
        self.funcdecl['rtype'] = None
        self.funcdecl['name'] = None
        self.funcdecl['inher'] = {
            'func': None, 's_pD': None}
    def visitProgram(self, ast:Program, param):
        for decl in ast.decls:
            if decl is FuncDecl:
                rtype = decl.return_type
                params = []
                Check.check(decl.name, self.env[0], lambda: self.raisee(Redeclared(Function(), decl.name)))
                for e in decl.params:
                    for p in params:
                        if p["name"] == e.name:
                            raise Redeclared(Parameter(), e.name)
                    par = {"type": e.typ, "kind": Variable(), "inherit": e.inherit, "out": e.out, "name": e.name}
                    params.append(par)
                self.env[0][decl.name] = {"type": rtype, "kind": Function(), "params": params, "params_inherit": []}
        entry = False
        for decl in ast.decls:
            if decl is FuncDecl:
                rtype = decl.return_type
                params = decl.params
                if decl is FuncDecl and decl.name == "main" and rtype is VoidType and len(params) == 0:
                    entry = True
            self.visit(decl, (self.env, None))
        if not entry:
            raise NoEntryPoint()
