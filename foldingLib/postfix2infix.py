from foldingLib.regularExpressions import Regex

# cannot handle subscript or function calls

def post2in_constant_folding(postfix_expression:list[str]):
    stack = []

    for token in postfix_expression:
        if Regex.is_operand(token):
            stack.append(token)
        elif Regex.is_operator(token):
            if Regex.is_unary(token):
                operand = stack.pop()
                stack.append(resolve_unary_operation(token,operand))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(resolve_operation(operand1, token, operand2))
        elif token == ')':
            paren=resolve_paren(stack.pop())
            stack.append(paren)

    return stack[0] if stack else ""

def resolve_operation(arg1:str, op:str, arg2:str):
    expression= f"{arg1} {op} {arg2}"
    if Regex.contains_true_or_false(expression):
        expression = Regex.sub_and_true(expression)
        expression = Regex.sub_and_false(expression)
        expression = Regex.sub_or_true(expression)
        expression = Regex.sub_or_false(expression)
    return expression

def resolve_unary_operation(op:str, arg:str):
    expression= f"{op} {arg}"
    expression = Regex.sub_two_nots(expression)
    expression = Regex.sub_not_false(expression)
    expression = Regex.sub_not_true(expression)
    return expression

def resolve_paren(inside:str):
    if Regex.is_true_or_false(inside) or \
        Regex.is_inside_parentheses(inside) or \
        Regex.hasnt_and_or(inside):
        return inside.strip()
    return f"({inside})"

