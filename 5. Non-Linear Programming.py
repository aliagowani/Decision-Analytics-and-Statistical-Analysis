############ Import Libraries #################

import numpy as np
from scipy.optimize import minimize
from math import pi, sqrt

################## Part 1 ###################
#############################################
# define objectives and constraints
def objective(x, sign=1.0):
    return sign*(4*x[0] + 2*x[1] - 0.5*x[0]**2 - 0.25*x[1]**2)

def constraint(x):
    return - (8000*x[0] + 5000*x[1]) + 40000

# initial guess(es)
n = 2
x0 = np.zeros(n)
x0[0] = 0
x0[1] = 0

# define bounds
b1 = (0, None)
b2 = (0, None)
bounds = (b1, b2)

# optimize model
cons = [{'type': 'ineq', 'fun': constraint}]
solution = minimize(objective,x0, args=(-1.0,), method='SLSQP', bounds=bounds, constraints=cons)
x = solution.x

# print optimized solution
print('Optimized Solution: ')
print('')
print('Raw Material x1:', round(x[0],4), ' Cost: $', round(x[0] * 8000, 2))
print('Raw Material x2:', round(x[1],4), ' Cost: $', round(x[1] * 5000, 2))
print('')

# print total raw materials objective
print('Total Raw Materials: ', round(objective(x),4))
print('Total Cost: $', round(8000*x[0] + 5000*x[1],2))
#############################################

################## Part 2 ###################
#############################################
# define objectives and constraints
def objective(x, sign=1.0):
    s = np.sum(x) * .5
    return sign*(sqrt(s * (s - x[0]) * (s - x[1]) * (s - x[2])))

def constraint_1(x):
    return (x[0] + x[1]) - x[2]

def constraint_2(x):
    return (x[0] + x[2]) - x[1] 

def constraint_3(x):
    return (x[1] + x[2]) - x[0]

def constraint_4(x):
    return 60 - np.sum(x)

# initial guess(es)
n = 3
x0 = np.zeros(n)
x0[0] = 0
x0[1] = 0
x0[2] = 0

# define bounds
b1 = (1, 60)
b2 = (1, 60)
b3 = (1, 60)
bounds = (b1, b2, b3)

# optimize model
cons = [{'type': 'ineq', 'fun': constraint_1},
        {'type': 'ineq', 'fun': constraint_2},
        {'type': 'ineq', 'fun': constraint_3},
       {'type': 'ineq', 'fun': constraint_4}]
solution = minimize(objective,x0, args=(-1.0,), method='SLSQP', bounds=bounds, constraints=cons)
x = solution.x

# print optimized solution
print('Optimized Solution: ')
print('')
print('Side A:', round(x[0],4))
print('Side B:', round(x[1],4))
print('Side C:', round(x[2],4))
print('')

# print perimeter and area objective
print('Perimeter: ', round(x[0] + x[1] + x[2],4))
print('Area: ', round(objective(x),4))
#############################################

