#!/usr/bin/env python
# coding: utf-8

# Homework Assignment 2: Network Models---Project Management
# Submission for Group Two - Connor Cassedy, Heidi Huckabay, Susan Alrifai, and Charles Lamb

# code finds a critical path using linear programming.
# solves via both a lp using time variables and dictionary based approach 

# lp using time variables

#import libraries
import pandas as pd
import pulp
from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize, lpSum

#establishing variables.  
#ti represents time of completion of task for i in (A,B,C,D1,D2,D3,D4,D5,D6,D8,D8,E,F,G,H)
#t0 represents time of starting any tasl
#z represents completion time of project
t0 = LpVariable("t0",0,None)
tA = LpVariable("tA",0,None)
tB = LpVariable("tB",0,None)
tC = LpVariable("tC",0,None)
tD1 = LpVariable("tD1",0,None)
tD2 = LpVariable("tD2",0,None)
tD3 = LpVariable("tD3",0,None)
tD4 = LpVariable("tD4",0,None)
tD5 = LpVariable("tD5",0,None)
tD6 = LpVariable("tD6",0,None)
tD7 = LpVariable("tD7",0,None)
tD8 = LpVariable("tD8",0,None)
tE = LpVariable("tE",0,None)
tF = LpVariable("tF",0,None)
tG = LpVariable("tG",0,None)
tH = LpVariable("tH",0,None)
z = LpVariable("z",0,None)

#setting up problem.  minimizing 3 seperate functions: a expected scenario, best case, and worse case scenario
prob_exp = LpProblem("problem",LpMinimize)
prob_exp += z
prob_worse = LpProblem("problem",LpMinimize)
prob_worse += z
prob_best = LpProblem("problem",LpMinimize)
prob_best += z

#constraints for expected scenario
prob_exp += tA - t0 >= 5
prob_exp += tB - t0 >= 10
prob_exp += tC - tA >= 5
prob_exp += tE - tB >= 10
prob_exp += tE - tC >= 0 #dummy pathway
prob_exp += tD1 - tA >= 16
prob_exp += tD2 - tD1 >= 240
prob_exp += tD3 - tD1 >= 200
prob_exp += tD4 - tD2 >= 220
prob_exp += tD4 - tD3 >= 0
prob_exp += tD6 - tD4 >= 160
prob_exp += tD7 - tD6 >= 160
prob_exp += tD5 - tD4 >= 8
prob_exp += tD8 - tD7 >= 4
prob_exp += tD8 - tD5 >= 0 #dummy pathway
prob_exp += tF - tD8 >= 320
prob_exp += tF - tE >= 0
prob_exp += tG - tD8 >= 45
prob_exp += tG - tA >= 0  #dummay pathway
prob_exp += z - tF >= 45
prob_exp += z - tG >= 0

#constraints for worse case scenario
prob_worse += tA - t0 >= 6
prob_worse += tB - t0 >= 12
prob_worse += tC - tA >= 5
prob_worse += tE - tB >= 11
prob_worse += tE - tC >= 0 #dummy pathway
prob_worse += tD1 - tA >= 17
prob_worse += tD2 - tD1 >= 283
prob_worse += tD3 - tD1 >= 240
prob_worse += tD4 - tD2 >= 268
prob_worse += tD4 - tD3 >= 0
prob_worse += tD6 - tD4 >= 190
prob_worse += tD7 - tD6 >= 210
prob_worse += tD5 - tD4 >= 10
prob_worse += tD8 - tD7 >= 4
prob_worse += tD8 - tD5 >= 0 #dummy pathway
prob_worse += tF - tD8 >= 400
prob_worse += tF - tE >= 0
prob_worse += tG - tD8 >= 61
prob_worse += tG - tA >= 0  #dummay pathway
prob_worse += z - tF >= 54
prob_worse += z - tG >= 0

#constraints for best case scenario
prob_best += tA - t0 >= 5
prob_best += tB - t0 >= 10
prob_best += tC - tA >= 5
prob_best += tE - tB >= 10
prob_best += tE - tC >= 0 #dummy pathway
prob_best += tD1 - tA >= 15
prob_best += tD2 - tD1 >= 209
prob_best += tD3 - tD1 >= 188
prob_best += tD4 - tD2 >= 202
prob_best += tD4 - tD3 >= 0
prob_best += tD6 - tD4 >= 158
prob_best += tD7 - tD6 >= 139
prob_best += tD5 - tD4 >= 8
prob_best += tD8 - tD7 >= 4
prob_best += tD8 - tD5 >= 0 #dummy pathway
prob_best += tF - tD8 >= 298
prob_best += tF - tE >= 0
prob_best += tG - tD8 >= 40
prob_best += tG - tA >= 0  #dummay pathway
prob_best += z - tF >= 42
prob_best += z - tG >= 0

#solving expected scenario
prob_exp.solve()
print('Expected Scenario:')
for variable in prob_exp.variables():
    print(f'{variable}: {value(variable.varValue)}')

#critical pathway: describe product, requirement analysis, sofware design, coding, unit test, system test, package deliverables, develop pricing plan, write client proposal

status_worse = prob_worse.solve()
print('Worse Scenario:')
for variable in prob_worse.variables():
    print(f'{variable}: {value(variable.varValue)}')


status_best = prob_best.solve()
print('Best Scenario:')
for variable in prob_best.variables():
    print(f'{variable}: {value(variable.varValue)}')


#alternative approach using dictionary
#based on code from Thomas W. Miller
print('alternative approach using dictionary.  gets same answers as above:')

#expected hours and cost
expected_tasks = {
    'A': {'duration': 5, 'cost': 500},
    'B': {'duration': 10, 'cost': 1000},
    'C': {'duration': 5, 'cost': 500},
    'D1': {'duration': 16, 'cost': 1600},
    'D2': {'duration': 240, 'cost': 24000},
    'D3': {'duration': 200, 'cost': 20000},
    'D4': {'duration': 220, 'cost': 22000},
    'D5': {'duration': 8, 'cost': 800},
    'D6': {'duration': 160, 'cost': 16000},
    'D7': {'duration': 160, 'cost': 16000},
    'D8': {'duration': 4, 'cost': 400},
    'E': {'duration': 10, 'cost': 1000},
    'F': {'duration': 320, 'cost': 32000},
    'G': {'duration': 45, 'cost': 45000},
    'H': {'duration': 45, 'cost': 45000}
}

#worse case hours and cost
worst_tasks  = {
    'A': {'duration': 6, 'cost': 600},
    'B': {'duration': 12, 'cost': 1200},
    'C': {'duration': 5, 'cost': 500},
    'D1': {'duration': 17, 'cost': 1700},
    'D2': {'duration': 283, 'cost': 28300},
    'D3': {'duration': 240, 'cost': 24000},
    'D4': {'duration': 268, 'cost': 26800},
    'D5': {'duration': 10, 'cost': 1000},
    'D6': {'duration': 190, 'cost': 19000},
    'D7': {'duration': 210, 'cost': 21000},
    'D8': {'duration': 4, 'cost': 400},
    'E': {'duration': 11, 'cost': 1100},
    'F': {'duration': 400, 'cost': 40000},
    'G': {'duration': 61, 'cost': 61000},
    'H': {'duration': 54, 'cost': 54000}
}

#best case hours and cost
best_tasks  = {
    'A': {'duration': 5, 'cost': 500},
    'B': {'duration': 10, 'cost': 1000},
    'C': {'duration': 5, 'cost': 500},
    'D1': {'duration': 15, 'cost': 1500},
    'D2': {'duration': 209, 'cost': 20900},
    'D3': {'duration': 188, 'cost': 18800},
    'D4': {'duration': 202, 'cost': 20200},
    'D5': {'duration': 8, 'cost': 800},
    'D6': {'duration': 158, 'cost': 15800},
    'D7': {'duration': 139, 'cost': 13900},
    'D8': {'duration': 4, 'cost': 400},
    'E': {'duration': 10, 'cost': 1000},
    'F': {'duration': 298, 'cost': 29800},
    'G': {'duration': 40, 'cost': 4000},
    'H': {'duration': 42, 'cost': 4200}
}


# create a list of tasks
expected_tasks_list = list(expected_tasks.keys())
worse_tasks_list = list(worst_tasks.keys())
best_tasks_list = list(best_tasks.keys())


# create a dictionary of precedences 
precedences = {'A':[],
               'B': [],
               'C': ['A'],
               'D1':['A'],
               'D2': ['D1'],
               'D3': ['D1'],
               'D4': ['D2','D3'],
               'D5': ['D4'],
               'D6':['D4'],
               'D7': ['D6'],
               'D8': ['D5', 'D7'],
               'E': ['B', 'C'],
               'F': ['D8','E'],
               'G': ['A', 'D8'],
               'H': ['F','G']
               }


# create the LP problem
prob_exp2 = LpProblem("Critical_Path", LpMinimize)
prob_worse2 = LpProblem("Critical_Path", LpMinimize)
prob_best2 = LpProblem("Critical_Path", LpMinimize)

# Create the LP variables
#for expected
start_times_expected = {task: LpVariable(f"start_{task}", 0, None) for task in expected_tasks_list}
end_times_expected = {task: LpVariable(f"end_{task}", 0, None) for task in expected_tasks_list}
#for worse
start_times_worse = {task: LpVariable(f"start_{task}", 0, None) for task in worse_tasks_list}
end_times_worse = {task: LpVariable(f"end_{task}", 0, None) for task in worse_tasks_list}
#for best
start_times_best = {task: LpVariable(f"start_{task}", 0, None) for task in best_tasks_list}
end_times_best = {task: LpVariable(f"end_{task}", 0, None) for task in best_tasks_list}

# Add the constraints
#for expected
for task in expected_tasks_list:
    prob_exp2 += end_times_expected[task] == start_times_expected[task] + expected_tasks[task]['duration'], f"{task}_duration"
    for predecessor in precedences[task]:
        prob_exp2 += start_times_expected[task] >= end_times_expected[predecessor],f"{task}_predecessor_{predecessor}"
#for worst case
for task in worse_tasks_list:
    prob_worse2 += end_times_worse[task] == start_times_worse[task] + worst_tasks[task]['duration'], f"{task}_duration"
    for predecessor in precedences[task]:
        prob_worse2 += start_times_worse[task] >= end_times_worse[predecessor],f"{task}_predecessor_{predecessor}"
#for best
for task in best_tasks_list:
    prob_best2 += end_times_best[task] == start_times_best[task] + best_tasks[task]['duration'], f"{task}_duration"
    for predecessor in precedences[task]:
        prob_best2 += start_times_best[task] >= end_times_best[predecessor],f"{task}_predecessor_{predecessor}"


# Set the objective function
prob_exp2 += lpSum([end_times_expected[task] for task in expected_tasks_list])
prob_worse2 += lpSum([end_times_worse[task] for task in worse_tasks_list])
prob_best2 += lpSum([end_times_best[task] for task in best_tasks_list])

# Solve the LP problem for the expected times estimates
status = prob_exp2.solve()
# Print the results
print("Critical Path time for Expected Time Estimates:")
for task in expected_tasks_list:
    if value(start_times_expected[task]) == 0:
        print(f"{task} starts at time 0")
    if value(end_times_expected[task]) == max([value(end_times_expected[task]) for task
in expected_tasks_list]):
        print(f"{task} ends at {value(end_times_expected[task])} days in duration")
        # Print solution
print("\nSolution variable values:")
for var in prob_exp2.variables():
    if var.name != "_dummy":
        print(var.name, "=", var.varValue)

# Solve the LP problem for the worse cast time estimates
status = prob_worse2.solve()
# Print the results
print("Critical Path time for Worse Case Time Estimates:")
for task in worse_tasks_list:
    if value(start_times_worse[task]) == 0:
        print(f"{task} starts at time 0")
    if value(end_times_worse[task]) == max([value(end_times_worse[task]) for task
in worse_tasks_list]):
        print(f"{task} ends at {value(end_times_worse[task])} days in duration")
        # Print solution
print("\nSolution variable values:")
for var in prob_worse2.variables():
    if var.name != "_dummy":
        print(var.name, "=", var.varValue)

# Solve the LP problem for the best times estimates
status = prob_best2.solve()
# Print the results
print("Critical Path time for Best Case Time Estimates:")
for task in best_tasks_list:
    if value(start_times_best[task]) == 0:
        print(f"{task} starts at time 0")
    if value(end_times_best[task]) == max([value(end_times_best[task]) for task
in best_tasks_list]):
        print(f"{task} ends at {value(end_times_best[task])} days in duration")
        # Print solution
print("\nSolution variable values:")
for var in prob_best2.variables():
    if var.name != "_dummy":
        print(var.name, "=", var.varValue)

