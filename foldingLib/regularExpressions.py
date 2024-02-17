import re

class Regex:
    operationPrecedence = {'.not.': 3, '.and.': 2, '.or.': 1, '(': 0}
    RE_operatorOrParenth=re.compile(r'(\(|\)|\.or\.|\.and\.|\.not\.)',re.I)

# categorization functions
    is_operand=lambda token: Regex.RE_operatorOrParenth.fullmatch(token) is None
    is_operator=re.compile(r'\.or\.|\.and\.|\.not\.',re.I).fullmatch
    is_unary=re.compile(r"\.not\.",re.I).fullmatch
    is_true_or_false=re.compile(r"\s*(\.true\.|\.false\.)\s*",re.I).fullmatch
    is_inside_parentheses=re.compile(r"\s*\(.*\)\s*").fullmatch

    contains_true_or_false=re.compile(r"\.true\.|\.false\.",re.I).search

    __and_or=re.compile(r"\.and\.|\.or\.",re.I)
    hasnt_and_or=lambda token: Regex.__and_or.search(token) is None

# constant folding subs
    __sub_and_true=re.compile( r"\s*\.true\.\s*\.and\.\s*|\s*\.and\.\s*\.true\.\s*",re.I).sub
    __sub_and_false=re.compile(r"\.false\.\s*\.and\..*|.*\.and\.\s*\.false\.",re.I).sub
    __sub_or_true=re.compile(  r"\.true\.\s*\.or\..*|.*\.or\.\s*\.true\.",re.I).sub
    __sub_or_false=re.compile( r"\s*\.false\.\s*\.or\.\s*|\s*\.or\.\s*\.false\.\s*",re.I).sub

    __sub_two_nots=re.compile(r"\.not\.\s*\.not\.\s*",re.I).sub
    __sub_not_false=re.compile(r"\.not\.\s*\.false\.",re.I).sub
    __sub_not_true=re.compile(r"\.not\.\s*\.true\.",re.I).sub

# convenience lambdas for constant folding
    sub_and_true=lambda expr: Regex.__sub_and_true("",expr)
    sub_and_false=lambda expr: Regex.__sub_and_false(".false.",expr)
    sub_or_true=lambda expr: Regex.__sub_or_true(".true.",expr)
    sub_or_false=lambda expr: Regex.__sub_or_false("",expr)

    sub_two_nots=lambda expr: Regex.__sub_two_nots("",expr)
    sub_not_false=lambda expr: Regex.__sub_not_false(".true.",expr)
    sub_not_true=lambda expr: Regex.__sub_not_true(".false.",expr)

# is subscripted or is function call (does not cover calls within calls), TODO exclude potential operators from first \w+
    RE_subscripted=re.compile(r'[a-z]\w*\s*\(\s*\w+\s*(,\s*\w+\s*)*\)',re.I)
