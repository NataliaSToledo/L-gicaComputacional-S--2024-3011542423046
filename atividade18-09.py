def logical_expression(p, q, r, s):
       left_side = (not p or q) and (not r or s) and (p or r)
       right_side = q or s
       return not left_side or right_side 
p = True
q = False
r = True
s = False
 
result = logical_expression(p, q, r, s)
print("Resultado:", result)