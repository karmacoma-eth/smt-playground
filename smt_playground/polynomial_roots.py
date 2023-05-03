'''
Use z3 to find a polynomial root for x**3 + 3*x**2 + 4*x + 2
'''

from pysmt.shortcuts import *
from pysmt.oracles import get_logic

x = Symbol('x', REAL)
p = Pow(x, Real(3)) + Real(3) * Pow(x, Real(2)) + Real(4) * x + Real(2)
formula = Equals(p, Real(0))

print("Serialization of the formula:")
print(formula.serialize())

target_logic = get_logic(formula)
print("Target Logic: %s" % target_logic)
# -> Target Logic: QF_NRA

model = get_model(formula)
print(model or "No solution found")
# -> x := -1.0

formula = And(formula, Not(Equals(x, model[x])))
model = get_model(formula)
print(model or "No other roots found")
