#######################################
# NODES (Continuation)
#######################################

# Add these classes to your existing code:

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

#######################################
# PARSER (Continuation)
#######################################

# Update the existing Parser class:

class Parser:
    # ... (existing code)

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

#######################################
# Token Class Modifications
#######################################

# Update the existing Token class:

class Token:
    # ... (existing code)

    def matches(self, type_, value):
        return self.type == type_ and self.value == value

#######################################
# RUN (Continuation)
#######################################

# Update the existing run function:

def run(fn, text):
    # ... (existing code)

    # Generate AST
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error:
        return None, ast.error

    return ast.node, None

