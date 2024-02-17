from foldingLib.regularExpressions import Regex

# variant of shunting yard algorithm, without handling array or function calls, and with parentheses saving
def in2post_with_parentheses(infix_expression:str)->list[str]:

    output = []
    operator_stack = []
    tokens = split_tokens(infix_expression)

    for token in tokens:
        if Regex.is_operand(token):
            output.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()  # Discard the '('
            output.append(token)  # Add ')' at the end
        elif Regex.is_operator(token):
            while operator_stack and Regex.operationPrecedence[operator_stack[-1]] > Regex.operationPrecedence[token]:
                output.append(operator_stack.pop())
            operator_stack.append(token)

    while operator_stack:
        output.append(operator_stack.pop())

    return output

def split_tokens(expression):
    return [x for x in Regex.RE_operatorOrParenth.split(expression) if x.strip()!='']
