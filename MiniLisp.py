import operator as op
import copy

def printNum(num):
    global PRINT
    PRINT = True
    return num

def printBool(bool):
    global PRINT
    PRINT = True
    if bool:
        return '#t'
    else:
        return '#f'

def ADD(*args):
    global PRINT
    if len(args) < 2:
        PRINT = True
        return 'syntax error'
    ans = 0
    for num in args:
        ans += num
    return ans

def MUL(*args):
    global PRINT
    if len(args) < 2:
        PRINT = True
        return 'syntax error'
    ans = 1
    for num in args:
        ans *= num
    return ans

def DIV(a, b):
    return a//b

def EQ(*args):
    global PRINT
    if len(args) < 2:
        PRINT = True
        return 'syntax error'
    for n in args[1:]:
        if args[0] != n:
            return False
    return True

def AND(*args):
    global PRINT
    if len(args) < 2:
        PRINT = True
        return 'syntax error'
    return all(args)

def OR(*args):
    global PRINT
    if len(args) < 2:
        PRINT = True
        return 'syntax error'
    return any(args)

symbol = str
PRINT = False
dic = {'+': ADD, '-': op.sub, '*': MUL, '/': DIV,
       '>': op.gt, '<': op.lt, '=': EQ, 'mod': op.mod, 'and': AND,
       'or': OR, 'not': op.not_, '#t': True, '#f': False,
       'print-num': printNum, 'print-bool': printBool}

def str_2_token(Input):
    "Convert a string into a list of tokens."
    tokens = Input.replace('(', ' ( ').replace(')', ' ) ').split()
    return tokens

def read_token(tokens):
    "Read a sequence of tokens"
    now_token = tokens.pop(0)
    if now_token == '(':
        Lt = []
        while tokens[0] != ')':
            Lt.append(read_token(tokens))
        tokens.pop(0)
        return Lt
    elif now_token == ')':
        raise SyntaxError('syntax error')
    else:
        return get_type(now_token)

def get_type(token):
    "give the token type"
    try:
        return int(token)
    except ValueError:
        return symbol(token)

class Function(object):
    def __init__(self, ids, body, d):
        self.ids, self.body, self.d = ids, body, d
    def __call__(self, *args):
        temp_d = copy.deepcopy(self.d)
        for i in range(len(self.ids)):      # update temp_d
            temp_d[self.ids[i]] = args[i]
        return execuate(self.body, temp_d)

def execuate(i, d=dic):
    "deal with tokens"
    global PRINT
    if isinstance(i, symbol):   # the symbol token
        return d[i]
    elif not isinstance(i, list):   # number
        return i
    elif i[0] == 'if':
        (_, test, THEN, ELSE) = i
        e = (THEN if execuate(test, d) else ELSE)
        return execuate(e, d)
    elif i[0] == 'define':
        (_, id, exp) = i
        d[id] = execuate(exp, d)
    elif i[0] == 'fun':
        if len(i) > 3:      # Nested function
            (ids, body) = (i[1], i[-1])
            for f in i[2:-1]:
                execuate(f, d)
            return Function(ids, body, d)
        else:               # normal function
            (_, ids, body) = i
            return Function(ids, body, d)
    else:                       # list type
        p = execuate(i[0], d)   # procedure
        a = [execuate(t, d) for t in i[1:]]     # args
        try:
            ans = p(*a)
        except:
            ans = 'syntax error'
            PRINT = True
        return ans

import sys, os, readline

if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):   # read file
    tokens = str_2_token(open(sys.argv[1]).read())
    while len(tokens) != 0:
        answer = execuate(read_token(tokens))
        if answer != None and PRINT:
            print(answer)
            PRINT = False
else:                   # manual enter
    while True:
        try:
            v = execuate(read_token(str_2_token(input('>'))))
            if v != None and PRINT:
                print(v)
                PRINT = False
        except:
            break