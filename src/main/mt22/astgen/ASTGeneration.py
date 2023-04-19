from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
from functools import *
class Unknown(Type): pass

class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext): 
        decls = reduce(lambda x, y: x + y, [self.visit(x) for x in ctx.decl()])
        return Program(decls)
    
   
    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#vardecls.
    def visitVardecls(self, ctx:MT22Parser.VardeclsContext):
        if ctx.paradecl():
            return [self.visit(ctx.paradecl())]
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        idlist = self.visit(ctx.idlist())
        type = self.visit(ctx.datatype())
        return [VarDecl(x, type, None) for x in idlist]


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [ctx.ID().getText()]
        return [ctx.ID().getText()] + self.visit(ctx.idlist())


    # Visit a parse tree produced by MT22Parser#vardecl_init.
    def visitVardecl_init(self, ctx:MT22Parser.Vardecl_initContext):
        x,y,datatype = self.visit(ctx.init())
        return list(map(lambda i: VarDecl(x[i],datatype,y[i]),range(len(x))))


    # Visit a parse tree produced by MT22Parser#init.
    def visitInit(self, ctx:MT22Parser.InitContext):
        if ctx.EQ():
            return [ctx.ID().getText()], [self.visit(ctx.expr())], self.visit(ctx.datatype())
        x,y,datatype = self.visit(ctx.init())
        x = [ctx.ID().getText()] + x
        y = y + [self.visit(ctx.expr())]
        return x,y,datatype


    # Visit a parse tree produced by MT22Parser#paradecl.
    def visitParadecl(self, ctx:MT22Parser.ParadeclContext):
        if ctx.INHER():
            if ctx.OUT():
                return ParamDecl(ctx.ID().getText(), self.visit(ctx.datatype()), True, True)
            else:
                return ParamDecl(ctx.ID().getText(), self.visit(ctx.datatype()), False, True)
        if ctx.OUT():
            return ParamDecl(ctx.ID().getText(), self.visit(ctx.datatype()), True, False)
        return ParamDecl(ctx.ID().getText(), self.visit(ctx.datatype()), False, False)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        if ctx.getChildCount() == 10:
            return [FuncDecl(ctx.ID(0).getText(), self.visit(ctx.datatype()), self.visit(ctx.paralist()), ctx.ID(1).getText(), self.visit(ctx.block_statement()))]
        return [FuncDecl(ctx.getChild(0).getText(), self.visit(ctx.datatype()), self.visit(ctx.paralist()), None, self.visit(ctx.block_statement()))]

    # Visit a parse tree produced by MT22Parser#paralist.
    def visitParalist(self, ctx:MT22Parser.ParalistContext):
        if ctx.paralistt():
            return self.visit(ctx.paralistt())
        return []


    # Visit a parse tree produced by MT22Parser#paralistt.
    def visitParalistt(self, ctx:MT22Parser.ParalisttContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.paradecl())]
        return [self.visit(ctx.paradecl())] + self.visit(ctx.paralistt())
    
    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#other.
    def visitOther(self, ctx:MT22Parser.OtherContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#block_statement.
    def visitBlock_statement(self, ctx:MT22Parser.Block_statementContext):
        return BlockStmt(self.visit(ctx.inner_block()))


    # Visit a parse tree produced by MT22Parser#inner_block.
    def visitInner_block(self, ctx:MT22Parser.Inner_blockContext):
        if ctx.vardecls():
            return self.visit(ctx.vardecls()) + self.visit(ctx.inner_block())
        if ctx.statement():
            return [self.visit(ctx.statement())] + self.visit(ctx.inner_block())
        return []


    # Visit a parse tree produced by MT22Parser#assign_statement.
    def visitAssign_statement(self, ctx:MT22Parser.Assign_statementContext):
        return self.visit(ctx.initial())

    # Visit a parse tree produced by MT22Parser#if_statement.
    def visitIf_statement(self, ctx:MT22Parser.If_statementContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#ifmatch.
    def visitIfmatch(self, ctx:MT22Parser.IfmatchContext):
        if ctx.getChildCount() == 7:
            return IfStmt(self.visit(ctx.expr()), self.visit(ctx.ifmatch(0)), self.visit(ctx.ifmatch(1)))
        return self.visit(ctx.other())


    # Visit a parse tree produced by MT22Parser#ifunmatch.
    def visitIfunmatch(self, ctx:MT22Parser.IfunmatchContext):
        if ctx.getChildCount() == 5:
            return IfStmt(self.visit(ctx.expr()), self.visit(ctx.if_statement()))
        return IfStmt(self.visit(ctx.expr()), self.visit(ctx.ifmatch()), self.visit(ctx.ifunmatch()))


    # Visit a parse tree produced by MT22Parser#for_statement.
    def visitFor_statement(self, ctx:MT22Parser.For_statementContext):
        return ForStmt(self.visit(ctx.initial()),self.visit(ctx.expr(0)),self.visit(ctx.expr(1)),self.visit(ctx.statement()))

    # Visit a parse tree produced by MT22Parser#initial.
    def visitInitial(self, ctx:MT22Parser.InitialContext):
        if ctx.getChildCount() == 6:
            return AssignStmt(ArrayCell(self.visit(ctx.ID()), self.visit(ctx.list_expr())), self.visit(ctx.expr()))
        return AssignStmt(Id(ctx.ID().getText()), self.visit(ctx.expr()))
    
    # Visit a parse tree produced by MT22Parser#while_statement.
    def visitWhile_statement(self, ctx:MT22Parser.While_statementContext):
        return WhileStmt(self.visit(ctx.expr()), self.visit(ctx.statement()))


    # Visit a parse tree produced by MT22Parser#dowhile_statement.
    def visitDowhile_statement(self, ctx:MT22Parser.Dowhile_statementContext):
        return DoWhileStmt(self.visit(ctx.expr()), self.visit(ctx.block_statement()))


    # Visit a parse tree produced by MT22Parser#break_statement.
    def visitBreak_statement(self, ctx:MT22Parser.Break_statementContext):
        return BreakStmt()


    # Visit a parse tree produced by MT22Parser#continue_statement.
    def visitContinue_statement(self, ctx:MT22Parser.Continue_statementContext):
        return ContinueStmt()


    # Visit a parse tree produced by MT22Parser#return_statement.
    def visitReturn_statement(self, ctx:MT22Parser.Return_statementContext):
        return ReturnStmt()


    # Visit a parse tree produced by MT22Parser#call_statement.
    def visitCall_statement(self, ctx:MT22Parser.Call_statementContext):
        return CallStmt(ctx.ID().getText(), self.visit(ctx.list_expr()))
    
    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        return self.visit(ctx.expr3())

    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        return self.visit(ctx.expr4())

    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        return self.visit(ctx.expr5())

    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        if ctx.getChildCount() == 2:
            return UnExpr(ctx.NOT().getText(), self.visit(ctx.expr5()))
        return self.visit(ctx.expr6())


    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        if ctx.getChildCount() == 2:
            return UnExpr(ctx.MINUS().getText(), self.visit(ctx.expr6()))
        return self.visit(ctx.expr7())


    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        if ctx.getChildCount() == 4:
            return ArrayCell(ctx.ID().getText(), self.visit(ctx.list_expr()))
        return self.visit(ctx.expr8())


    # Visit a parse tree produced by MT22Parser#expr8.
    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        if ctx.getChildCount() == 4:
            return FuncCall(ctx.ID().getText(), self.visit(ctx.list_expr()))
        return self.visit(ctx.expr9())


    # Visit a parse tree produced by MT22Parser#expr9.
    def visitExpr9(self, ctx:MT22Parser.Expr9Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr())
        if ctx.literal():
            return self.visit(ctx.literal())
        return Id(ctx.ID().getText())


    # Visit a parse tree produced by MT22Parser#list_expr.
    def visitList_expr(self, ctx:MT22Parser.List_exprContext):
        if ctx.expr_list():
            return self.visit(ctx.expr_list()) 
        return []


    # Visit a parse tree produced by MT22Parser#expr_list.
    def visitExpr_list(self, ctx:MT22Parser.Expr_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.expr_list())
    
    # Visit a parse tree produced by MT22Parser#literal.
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        if ctx.INTLIT(): return IntegerLit(int(ctx.INTLIT().getText()))
        if ctx.FLOATLIT(): return FloatLit(float(ctx.FLOATLIT().getText()))
        if ctx.BOOLIT():
            if ctx.BOOLIT().getText() == "true": return BooleanLit(True)
            return BooleanLit(False)
        if ctx.STRINGLIT(): return StringLit(str(ctx.STRINGLIT().getText()))
        return self.visit(ctx.arrlit())


    # Visit a parse tree produced by MT22Parser#arrlit.
    def visitArrlit(self, ctx:MT22Parser.ArrlitContext):
        if ctx.arraylist():
            return ArrayLit(self.visit(ctx.arraylist()))


    # Visit a parse tree produced by MT22Parser#arraylist.
    def visitArraylist(self, ctx:MT22Parser.ArraylistContext):
        if ctx.array():
            return self.visit(ctx.array()) 
        return []

    def visitArray(self, ctx:MT22Parser.ArrayContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.array())

    # Visit a parse tree produced by MT22Parser#datatype.
    def visitDatatype(self, ctx:MT22Parser.DatatypeContext):
        if ctx.AUTO(): return AutoType()
        if ctx.VOID(): return VoidType()
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#atomic.
    def visitAtomic(self, ctx:MT22Parser.AtomicContext):
        if ctx.INT(): return IntegerType()
        if ctx.FLOAT(): return FloatType()
        if ctx.BOOL(): return BooleanType()
        return StringType()


    # Visit a parse tree produced by MT22Parser#arrdecl.
    def visitArrdecl(self, ctx:MT22Parser.ArrdeclContext):
        return ArrayType(self.visit(ctx.dimension()),self.visit(ctx.atomic()))


    # Visit a parse tree produced by MT22Parser#dimension.
    def visitDimension(self, ctx:MT22Parser.DimensionContext):
        if ctx.di_list():
            return self.visit(ctx.di_list()) 
        return []
    # Visit a parse tree produced by MT22Parser#di_list.
    def visitDi_list(self, ctx:MT22Parser.Di_listContext):
        if ctx.getChildCount() == 1:
            return [IntegerLit(int(ctx.INTLIT().getText()))]
        return [IntegerLit(int(ctx.INTLIT().getText()))] + self.visit(ctx.di_list())