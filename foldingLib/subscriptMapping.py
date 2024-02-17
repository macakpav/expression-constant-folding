from foldingLib.regularExpressions import Regex

def map_arr_funct_calls(expression:str):
    tagDict={}
    for i in range(100): # to avoid potential infinite loop with while
        tag=f"__mapped_sub_{i}"
        replaced=Regex.RE_subscripted.search(expression)
        if replaced is None: return expression, tagDict
        expression=expression.replace(replaced.group(),tag)
        tagDict[tag]=replaced.group()
    raise Exception("Did maximum number of substitutions during mapping. The parsed expression is either invalid or has VERY many array/function calls.")

    

def apply_map(map:dict[str], string:str):
    while any(x in string for x in map.keys()):
        for key, value in map.items():
            string=string.replace(key,value)
    return string