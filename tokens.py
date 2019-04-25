keywords = {
    'if' : 'token_IF',
    'then' : 'token_THEN',
    'else' : 'token_ELSE',
    'while' : 'token_WHILE'
}

tokens = [
    'token_DOT',
    'token_SEMICOL',
    'token_COMMA',
    'token_LPAREN',
    'token_RPAREN',
    'token_COLON',
    'token_LBRACKET',
    'token_LBRACKET',
    'token_ASSIGN',
    'token_DOTDOT',
] 
token = token + list(keywords.values())
op_types = {
    
    '.' : 'op_DOT',
    '<' : 'op_LT',
    '<=' : 'op_LE',
    '>' : 'op_GT',







}

