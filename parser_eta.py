import ply.yacc as yacc
from lexer import tokens

# Define the grammar rules
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

def p_statement_expression(p):
    'statement : expression'
    p[0] = p[1]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]

def p_expression_printin(p):
    'expression : PRINTIN LPAREN expression RPAREN'
    if isinstance(p[3], str):
        print(p[3])
    else:
        print(p[3])
    p[0] = None

def p_comment(p):
    'expression : COMMENT'
    pass  # Skip comments

def p_error(p):
    print("Syntax error")

# Build the parser
parser = yacc.yacc(write_tables=False)
