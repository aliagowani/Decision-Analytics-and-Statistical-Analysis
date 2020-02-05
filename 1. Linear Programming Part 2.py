from pulp import *

#################################
prob = LpProblem("Assignment2_Q2_Max_Students", LpMaximize)

# Variables
TA = LpVariable("Texas_AS", 0, None)
TC = LpVariable("Texas_College", 0, None)
CA = LpVariable("California_AS", 0, None)
CC = LpVariable("California_College", 0, None)
DA = LpVariable("DC_AS", 0, None)
DC = LpVariable("DC_College", 0, None)
NA = LpVariable("NewYork_AS", 0, None)
NC = LpVariable("NewYork_College", 0, None)

# Objective
prob += TA + TC + CA + CC + DA + DC + NA + NC, "obj"

# Constraints
prob += TA + CA + DA + NA >= 1000, "AS_Supply"
prob += TC + CC + DC + NC >= 1400, "College_Supply"
prob += TA + TC <= 750, "Texas_Demand"
prob += CA + CC <= 650, "California_Demand"
prob += DA + DC <= 300, "DC_Demand"
prob += NA + NC <= 800, "NewYork_Demand"

# Solve the problem using the default solver
prob.solve()

# Print the status and output of the solved LP
print("Assignment2_Q2_Max_Students:")

print("\nObjective function:", (prob.objective))

print ("\nConstraints:")
for constraint in prob.constraints:
        print("\t", prob.constraints[constraint])
print("\nStatus:", LpStatus[prob.status])

print("\nObjective value:", format(value(prob.objective), ',.0f'))

print ("\nThe values of the variables:")
for v in prob.variables():
    print("\t", v.name, "=", format(value(v.varValue), ',.0f'))
#################################


#################################
prob = LpProblem("Assignment2_Q2_Min_Cost", LpMinimize)

# Variables
TA = LpVariable("Texas_AS", 0, None)
TC = LpVariable("Texas_College", 0, None)
CA = LpVariable("California_AS", 0, None)
CC = LpVariable("California_College", 0, None)
DA = LpVariable("DC_AS", 0, None)
DC = LpVariable("DC_College", 0, None)
NA = LpVariable("NewYork_AS", 0, None)
NC = LpVariable("NewYork_College", 0, None)

# Objective
prob += 3000*TA + 4500*TC + 2500*CA + 4000*CC + 5000*DA + 1500*DC + 4000*NA + 2000*NC, "obj"

# Constraints
prob += TA + CA + DA + NA >= 1000, "AS_Supply"
prob += TC + CC + DC + NC >= 1400, "College_Supply"
prob += TA + TC <= 750, "Texas_Demand"
prob += CA + CC <= 650, "California_Demand"
prob += DA + DC <= 300, "DC_Demand"
prob += NA + NC <= 800, "NewYork_Demand"

# Solve the problem using the default solver
prob.solve()

# Print the status and output of the solved LP
print("Assignment2_Q2_Min_Cost:")

print("\nObjective function:", (prob.objective))

print ("\nConstraints:")
for constraint in prob.constraints:
        print("\t", prob.constraints[constraint])
print("\nStatus:", LpStatus[prob.status])

print("\nObjective value:", '$' + format(value(prob.objective), ',.0f'))


print ("\nThe values of the variables:")
for v in prob.variables():
    print("\t", v.name, "=", format(value(v.varValue), ',.0f')),

add_var = 0
for v in prob.variables():
	add_var = value(v.varValue) + add_var
print("\t", "Variable Total", "=", add_var)

#################################


print("Assignment2_Q2_Min_Cost:")...
Assignment2_Q2_Min_Cost:

Objective function: 2500*California_AS + 4000*California_College + 5000*DC_AS + 1500*DC_College + 4000*NewYork_AS + 2000*NewYork_College + 3000*Texas_AS + 4500*Texas_College

Constraints:
	 California_AS + DC_AS + NewYork_AS + Texas_AS >= 1000
	 California_College + DC_College + NewYork_College + Texas_College >= 1400
	 Texas_AS + Texas_College <= 750
	 California_AS + California_College <= 650
	 DC_AS + DC_College <= 300
	 NewYork_AS + NewYork_College <= 800

Status: Optimal

Objective value: $6,075,000

The values of the variables:
	 California_AS = 350
	 California_College = 300
	 DC_AS = 0
	 DC_College = 300
	 NewYork_AS = 0
	 NewYork_College = 800
	 Texas_AS = 650
	 Texas_College = 0
