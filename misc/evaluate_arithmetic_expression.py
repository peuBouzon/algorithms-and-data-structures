
expression = "( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )"

operands = []
operators = []

for c in expression.replace(' ', ''):
    if c in ['+', '-', '*', '/']:
        operators.append(c)
    elif c != '(' and c != ')':
        operands.append(c)
    elif c == ')':
        op = operators.pop()
        x2 = operands.pop()
        x1 = operands.pop()
        operands.append(eval(f'{x1} {op} {x2}'))

print(operands.pop())
