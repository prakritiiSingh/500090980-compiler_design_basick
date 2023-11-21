# NODES (Continuation)

class VarAccessNode:
    def __init__(self, var_name_tok):
        self.var_name_tok = var_name_tok

    def __repr__(self):
        return f'{self.var_name_tok}'

class VarAssignNode:
    def __init__(self, var_name_tok, value_node):
        self.var_name_tok = var_name_tok
        self.value_node = value_node

    def __repr__(self):
        return f'({self.var_name_tok}, {self.value_node})'

# PARSER (Continuation)

class Parser:
    # ... (existing code)

    def visit(self, node, context):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node, context)

    def no_visit_method(self, node, context):
        raise Exception(f'No visit_{type(node).__name__} method defined')

    def var_access(self):
        res = ParseResult()
        var_name_tok = self.current_tok
        res.register(self.advance())
        return res.success(VarAccessNode(var_name_tok))

    def var_assign(self):
        res = ParseResult()
        var_name_tok = self.current_tok
        res.register(self.advance())
        if self.current_tok.type != TT_EQ:
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                "Expected '='"
            ))
        res.register(self.advance())
        value = res.register(self.expr())
        if res.error: return res
        return res.success(VarAssignNode(var_name_tok, value))

    def statement(self):
        res = ParseResult()
        if self.current_tok.matches(TT_KEYWORD, 'var'):
            res.register(self.advance())
            if self.current_tok.type != TT_IDENTIFIER:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected identifier"
                ))
            var_name = self.current_tok
            res.register(self.advance())
            if self.current_tok.type != TT_EQ:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected '='"
                ))
            res.register(self.advance())
            expr = res.register(self.expr())
            if res.error: return res

            # Semantic Analysis for Variable Declaration
            if context.symbol_table.get(var_name.value):
                return res.failure(InvalidSyntaxError(
                    var_name.pos_start, var_name.pos_end,
                    f"Variable '{var_name.value}' has already been declared"
                ))
            context.symbol_table[var_name.value] = True

            return res.success(VarAssignNode(var_name, expr))
        else:
            expr = res.register(self.expr())
            if res.error: return res
            return res.success(expr)

    def statements(self):
        res = ParseResult()
        statements = []
        while self.current_tok.type == TT_NEWLINE:
            res.register(self.advance())
        statement = res.register(self.statement())
        if res.error: return res
        statements.append(statement)

        while self.current_tok.type == TT_NEWLINE:
            res.register(self.advance())
        while self.current_tok.type == TT_KEYWORD and self.current_tok.value == 'var':
            statement = res.register(self.statement())
            if res.error: return res
            statements.append(statement)

        return res.success(statements)

    def parse(self):
        res = ParseResult()
        statements = res.register(self.statements())
        if res.error: return res
        return res.success(statements)

    # ... (existing code)

# Semantic Analysis Context

class Context:
    def __init__(self):
        self.symbol_table = {}

# RUN (Continuation)

def run(fn, text):
    # ... (existing code)

    # Generate AST
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error:
        return None, ast.error

    # Semantic Analysis
    context = Context()
    semantic_result = parser.visit(ast.node, context)

    if semantic_result.error:
        return None, semantic_result.error

    return ast.node, None
