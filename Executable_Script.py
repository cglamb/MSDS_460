#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
import pandas as pd
import pulp
from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize


# In[2]:


#building a pandas dataframe with nutrition information 
Labels = ['Sodium','Calories','Protein','VitD','Calcium','Iron','K','VitA','VitC','VitE','VitK','Zinc','VitB6','VitB12','Servings_per_Container','Price_Per_Container','Price_Per_Serving']
Daily_Req = [5000,2000,50,20,1300,18,4700,900,90,15,120,11,1.7,2.4,0,0,0]
Whole_Milk = [125,150,8,2,325,0,376,90,0,0,0,0,0,0,16,2.99,0.19]
Mixed_Nuts = [90,170,6,0,40,1.2,200,0,0,3.4,0,1,0,0,56,15.18,0.27]
Kidney_Beans = [270,130,8,0,80,2.4,480,0,0,0,0,0,0,0,3.5,1.67,0.48]
Canned_Tuna = [360,90,20,2,0,1.44,188,0,0,0,0,0,0.17,2.88,4,4.99,1.25]
Orange_Juice = [0,110,2,5,455,0,450,0,90,0,0,0,0.068,0,7,4.79,0.68]

df = pd.DataFrame(
    {
        "Labels": Labels,
        "Daily_Req": Daily_Req,
        "Whole_Milk": Whole_Milk,
        "Mixed_Nuts": Mixed_Nuts,
        "Kindey_Beans": Kidney_Beans,
        "Canned_Tuna": Canned_Tuna,
        "Orange_Juice": Orange_Juice
    })

df = df.set_index("Labels")


# In[3]:


#explanation
print("Script Note: This script optimizes two linear programs.  Both programs determine a minium cost diet, based on consumption of five possible foods: whole milk(m), mixed nuts(n), kidney beans(b), canned tuna(t), and orange juice(o).  The first linear program is subject to nutritional constraints based on the FDA's suggested intake of sodium, energy, protein, vitamin D, calcium, iron, and potasum.  The second problem considers these seven constraints plus additional constraints for Vitamin C and E.")


# In[4]:


#establishing variables.  these represent the number of servings of each of our 5 different foods.
m = LpVariable("m",0,None)
n = LpVariable('n',0,None)
b = LpVariable('b',0,None)
t = LpVariable('t',0,None)
o = LpVariable('o',0,None)


# In[5]:


#setting up problem
prob = LpProblem("problem",LpMinimize)
prob += df["Whole_Milk"].Price_Per_Serving * m + df["Mixed_Nuts"].Price_Per_Serving * n + df["Kindey_Beans"].Price_Per_Serving * b + df["Canned_Tuna"].Price_Per_Serving * t + df["Orange_Juice"].Price_Per_Serving * o


# In[6]:


#esablishing constrains
#sodium constraint
prob += df["Whole_Milk"].Sodium * m + df["Mixed_Nuts"].Sodium * n + df["Kindey_Beans"].Sodium * b + df["Canned_Tuna"].Sodium * t + df["Orange_Juice"].Sodium * o <= df["Daily_Req"].Sodium
#caloric constraint
prob += df["Whole_Milk"].Calories * m + df["Mixed_Nuts"].Calories * n + df["Kindey_Beans"].Calories * b + df["Canned_Tuna"].Calories * t + df["Orange_Juice"].Calories * o >= df["Daily_Req"].Calories
#protein constrant
prob += df["Whole_Milk"].Protein * m + df["Mixed_Nuts"].Protein * n + df["Kindey_Beans"].Protein * b + df["Canned_Tuna"].Protein * t + df["Orange_Juice"].Protein * o >= df["Daily_Req"].Protein
#vitamin d constraint
prob += df["Whole_Milk"].VitD * m + df["Mixed_Nuts"].VitD * n + df["Kindey_Beans"].VitD * b + df["Canned_Tuna"].VitD * t + df["Orange_Juice"].VitD * o >= df["Daily_Req"].VitD
#adding calcium constraint
prob += df["Whole_Milk"].Calcium * m + df["Mixed_Nuts"].Calcium * n + df["Kindey_Beans"].Calcium * b + df["Canned_Tuna"].Calcium * t + df["Orange_Juice"].Calcium * o >= df["Daily_Req"].Calcium
#Iron contraint
prob += df["Whole_Milk"].Iron * m + df["Mixed_Nuts"].Iron * n + df["Kindey_Beans"].Iron * b + df["Canned_Tuna"].Iron * t + df["Orange_Juice"].Iron * o >= df["Daily_Req"].Iron
#K constraint
prob += df["Whole_Milk"].K * m + df["Mixed_Nuts"].K * n + df["Kindey_Beans"].K * b + df["Canned_Tuna"].K * t + df["Orange_Juice"].K * o >= df["Daily_Req"].K


# In[7]:


#checking to make sure the problem is setup correctly
print('Linear Programming Problem is:')
print(prob)


# In[8]:


#solving
#print('optimzation status is:')
status = prob.solve()
#print(pulp.LpStatus[status])


# In[9]:


#printing the solution
print('The min cost diet results from the following servings per food item:')
for variable in prob.variables():
    print(f'{variable}: {value(variable.varValue)}')


# In[10]:


#print cost of diet
print(f'daily cost of the diet is: {value(prob.objective)}')


# In[11]:


#adding two additional nutritional constraints 
#VitC constraint
prob += df["Whole_Milk"].VitC * m + df["Mixed_Nuts"].VitC * n + df["Kindey_Beans"].VitC * b + df["Canned_Tuna"].VitC * t + df["Orange_Juice"].VitC * o >= df["Daily_Req"].VitC
#VitE constraint
prob += df["Whole_Milk"].VitE * m + df["Mixed_Nuts"].VitE * n + df["Kindey_Beans"].VitE * b + df["Canned_Tuna"].VitE * t + df["Orange_Juice"].VitE * o >= df["Daily_Req"].VitE


# In[12]:


#checking to make sure the problem is setup correctly
print("Model 2: adding additional constraints for Vitamin C and E.  The new linear programming problem becomes:")
print(prob)


# In[13]:


#solving
#print('optimzation status of problem 2 is:')
status = prob.solve()
#print(pulp.LpStatus[status])


# In[14]:


#printing the solution
print('The min cost diet results from the following servings per food item:')
for variable in prob.variables():
    print(f'{variable}: {value(variable.varValue)}')


# In[15]:


#print cost of diet
print(f'daily cost of the diet is: {value(prob.objective)}')

