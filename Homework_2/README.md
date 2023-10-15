## Homework Assignment 2: Network Models---Project Management
### Submission for Group Two - Connor Cassedy, Heidi Huckabay, Susan Alrifai, and Charles Lamb

code finds a critical path using linear programming.
solves via both a lp using time variables and dictionary based approach 

### Problem Inputs

The exhibit below describes the project management problem.  A project is divided into tasks.  Each task and a estimated, best, and worse case time estimate is described for each task.  Certain tasks have dependecies which must be completed before the task can be started.  The goal is to estimate the minimum time to complete the project.  We solve using linear programming.

![image.png](attachment:image.png)

### Findings: Critical Path

we find the critical path to be:  describe product, requirement analysis, software design, coding, unit test, system test, package deliverables, develop pricing plan, write client proposal.

### Findings: Completion Time

Under expected time for each task: project completion time is 1170 hours
Under worse case time for each task: project completion time is 1432 hours
Under best case time for each task:  project completion time is 1072 hours

### Code:


```python
# lp using time variables
```


```python
#import libraries
import pandas as pd
import pulp
from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize, lpSum
```


```python
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
```


```python
#setting up problem.  minimizing 3 seperate functions: a expected scenario, best case, and worse case scenario
prob_exp = LpProblem("problem",LpMinimize)
prob_exp += z
prob_worse = LpProblem("problem",LpMinimize)
prob_worse += z
prob_best = LpProblem("problem",LpMinimize)
prob_best += z
```


```python
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
```


```python
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
```


```python
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
```


```python
#solving expected scenario
prob_exp.solve()
print('Expected Scenario:')
for variable in prob_exp.variables():
    print(f'{variable}: {value(variable.varValue)}')
```

    Expected Scenario:
    t0: 0.0
    tA: 5.0
    tB: 10.0
    tC: 10.0
    tD1: 21.0
    tD2: 261.0
    tD3: 221.0
    tD4: 481.0
    tD5: 489.0
    tD6: 641.0
    tD7: 801.0
    tD8: 805.0
    tE: 20.0
    tF: 1125.0
    tG: 850.0
    z: 1170.0
    


```python
#critical pathway: describe product, requirement analysis, sofware design, coding, unit test, system test, package deliverables, develop pricing plan, write client proposal
```


```python
status_worse = prob_worse.solve()
print('Worse Scenario:')
for variable in prob_worse.variables():
    print(f'{variable}: {value(variable.varValue)}')
```

    Worse Scenario:
    t0: 0.0
    tA: 6.0
    tB: 12.0
    tC: 11.0
    tD1: 23.0
    tD2: 306.0
    tD3: 263.0
    tD4: 574.0
    tD5: 584.0
    tD6: 764.0
    tD7: 974.0
    tD8: 978.0
    tE: 23.0
    tF: 1378.0
    tG: 1039.0
    z: 1432.0
    


```python
status_best = prob_best.solve()
print('Best Scenario:')
for variable in prob_best.variables():
    print(f'{variable}: {value(variable.varValue)}')
```

    Best Scenario:
    t0: 0.0
    tA: 5.0
    tB: 10.0
    tC: 10.0
    tD1: 20.0
    tD2: 229.0
    tD3: 208.0
    tD4: 431.0
    tD5: 439.0
    tD6: 589.0
    tD7: 728.0
    tD8: 732.0
    tE: 20.0
    tF: 1030.0
    tG: 772.0
    z: 1072.0
    


```python
#alternative approach using dictionary
#based on code from Thomas W. Miller

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
```


```python
# create a list of tasks
expected_tasks_list = list(expected_tasks.keys())
worse_tasks_list = list(worst_tasks.keys())
best_tasks_list = list(best_tasks.keys())
```


```python
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
```


```python
# create the LP problem
prob_exp2 = LpProblem("Critical_Path", LpMinimize)
prob_worse2 = LpProblem("Critical_Path", LpMinimize)
prob_best2 = LpProblem("Critical_Path", LpMinimize)
```


```python
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
```


```python
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
```


```python
# Set the objective function
prob_exp2 += lpSum([end_times_expected[task] for task in expected_tasks_list])
prob_worse2 += lpSum([end_times_worse[task] for task in worse_tasks_list])
prob_best2 += lpSum([end_times_best[task] for task in best_tasks_list])
```


```python
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
```

    Critical Path time for Expected Time Estimates:
    A starts at time 0
    B starts at time 0
    H ends at 1170.0 days in duration
    
    Solution variable values:
    end_A = 5.0
    end_B = 10.0
    end_C = 10.0
    end_D1 = 21.0
    end_D2 = 261.0
    end_D3 = 221.0
    end_D4 = 481.0
    end_D5 = 489.0
    end_D6 = 641.0
    end_D7 = 801.0
    end_D8 = 805.0
    end_E = 20.0
    end_F = 1125.0
    end_G = 850.0
    end_H = 1170.0
    start_A = 0.0
    start_B = 0.0
    start_C = 5.0
    start_D1 = 5.0
    start_D2 = 21.0
    start_D3 = 21.0
    start_D4 = 261.0
    start_D5 = 481.0
    start_D6 = 481.0
    start_D7 = 641.0
    start_D8 = 801.0
    start_E = 10.0
    start_F = 805.0
    start_G = 805.0
    start_H = 1125.0
    


```python
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
```

    Critical Path time for Worse Case Time Estimates:
    A starts at time 0
    B starts at time 0
    H ends at 1432.0 days in duration
    
    Solution variable values:
    end_A = 6.0
    end_B = 12.0
    end_C = 11.0
    end_D1 = 23.0
    end_D2 = 306.0
    end_D3 = 263.0
    end_D4 = 574.0
    end_D5 = 584.0
    end_D6 = 764.0
    end_D7 = 974.0
    end_D8 = 978.0
    end_E = 23.0
    end_F = 1378.0
    end_G = 1039.0
    end_H = 1432.0
    start_A = 0.0
    start_B = 0.0
    start_C = 6.0
    start_D1 = 6.0
    start_D2 = 23.0
    start_D3 = 23.0
    start_D4 = 306.0
    start_D5 = 574.0
    start_D6 = 574.0
    start_D7 = 764.0
    start_D8 = 974.0
    start_E = 12.0
    start_F = 978.0
    start_G = 978.0
    start_H = 1378.0
    


```python
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
```

    Critical Path time for Best Case Time Estimates:
    A starts at time 0
    B starts at time 0
    H ends at 1072.0 days in duration
    
    Solution variable values:
    end_A = 5.0
    end_B = 10.0
    end_C = 10.0
    end_D1 = 20.0
    end_D2 = 229.0
    end_D3 = 208.0
    end_D4 = 431.0
    end_D5 = 439.0
    end_D6 = 589.0
    end_D7 = 728.0
    end_D8 = 732.0
    end_E = 20.0
    end_F = 1030.0
    end_G = 772.0
    end_H = 1072.0
    start_A = 0.0
    start_B = 0.0
    start_C = 5.0
    start_D1 = 5.0
    start_D2 = 20.0
    start_D3 = 20.0
    start_D4 = 229.0
    start_D5 = 431.0
    start_D6 = 431.0
    start_D7 = 589.0
    start_D8 = 728.0
    start_E = 10.0
    start_F = 732.0
    start_G = 732.0
    start_H = 1030.0
    
