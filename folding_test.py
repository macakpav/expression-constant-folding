from foldingLib.postfix2infix import post2in_constant_folding
from foldingLib.infix2postfix import in2post_with_parentheses
from foldingLib.subscriptMapping import map_arr_funct_calls, apply_map

# Example usage:
infixExpression = ".not. .not.a >  2.and..true. .and. ( arr(l2(1),2) .or. .false.)"

# mapping array and function calls makes life much easier down the road
mappedInfix, subExprMap=map_arr_funct_calls(infixExpression)
postfixWithParenth = in2post_with_parentheses(mappedInfix)
infixReconstructed = post2in_constant_folding(postfixWithParenth)
infixReMapped = apply_map(subExprMap,infixReconstructed)

print("Original Infix Expression:", infixExpression)
# print("Mapped Infix Expression:", mappedInfix)
# print("Postfix Expression with Parentheses:", postfixWithParenth)
# print("Reconstructed Infix Expression:", infixReconstructed)
print("Reconstructed Re-mapped Infix Expression:", infixReMapped)
