from pulp import *

prob = LpProblem("test1", LpMaximize)

# Variables
# 0 <= x
x = LpVariable("tables", 0, None)
# 0 <= y
y = LpVariable("chairs", 0, None)
# 0 <= z
# z = LpVariable("z", 0)
# Use None for +/- Infinity, i.e. z <= 0 -> LpVariable("z", None, 0)


# Objective
prob += x*7 + y*5, "obj"
# (the name at the end is facultative)

# Constraints
# (the names at the end are facultative)
prob += x*3 + y*4 <= 2400, "c1"
prob += x*2 + y*1 <= 1000, "c2"
prob += y <= 450, "c3"
prob += x >= 100, "c4"


# Write the problem as an LP file
# prob.writeLP("test1.lp")

# Solve the problem using the default solver
prob.solve()
# Use prob.solve(GLPK()) instead to choose GLPK as the solver
# Use GLPK(msg = 0) to suppress GLPK messages
# If GLPK is not in your path and you lack the pulpGLPK module,
# replace GLPK() with GLPK("/path/")
# Where /path/ is the path to glpsol (excluding glpsol itself).
# If you want to use CPLEX, use CPLEX() instead of GLPK().
# If you want to use XPRESS, use XPRESS() instead of GLPK().
# If you want to use COIN, use COIN() instead of GLPK(). In this last case,
# two paths may be provided (one to clp, one to cbc).

# Print the status of the solved LP
print("Status:", LpStatus[prob.status])

# Print the value of the variables at the optimum
for v in prob.variables():
	print(v.name, "=", v.varValue)

# Print the value of the objective
print("objective=", value(prob.objective))


from pulp import *

prob = LpProblem("Bonus", LpMaximize)

# Variables
# 0 <= x
x = LpVariable("tables", 0, None)
# 0 <= y
y = LpVariable("chairs", 0, None)


# Objective
prob += x*7 + y*5, "obj"


# Constraints
prob += x*3 + y*4 <= 2400, "c1"
prob += x*2 + y*1 <= 1000, "c2"
prob += y <= 450, "c3"
prob += x >= 100, "c4"


# Solve the problem using the default solver
prob.solve()


# Print the status of the solved LP
print("Status:", LpStatus[prob.status])

# Print the value of the variables at the optimum
for v in prob.variables():
	print(v.name, "=", v.varValue)

# Print the value of the objective
print("Total Profit: ", value(prob.objective))