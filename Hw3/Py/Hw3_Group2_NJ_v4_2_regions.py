#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/cglamb/Collab/blob/main/Hw3_Group2_NJ_LowerNJ.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# ### Redistricting New Jersey

# Group 2: Charles Lamb, Connor Cassedy, Heidi Huckabay, and Susan Alrifai

# ### Library Import

# In[1]:


#pip install pulp


# In[2]:


#import libraries
import pulp, numpy as np, pandas as pd, math
from pulp import *


# ### Log Start

# In[3]:


#drops a local file that records the start time
#just using this to track computation time
#d=[]
#df_dummy = pd.DataFrame(d)
#df_dummy.to_csv('start_time.txt')


# ### New Jersey State Data

# Data source is US Census data containing 2020 population size by county for the state of New Jersey: https://www.census.gov/data/tables/time-series/demo/popest/2020s-counties-total.html

# In[4]:


#bringing in county and population as list
#pre-processing was done in excel
county_pop = [['Atlantic',274536],['Bergen',955746],['Burlington',461863],['Camden',523486],['Cape',95266],['Cumberland',154148],['Essex',862782],['Gloucester',302285],['Hudson',724857],['Hunterdon',128962],['Mercer',387340],['Middlesex',863183],['Monmouth',643608],['Morris',509277],['Ocean',637229],['Passaic',525052],['Salem',64834],['Somerset',345356],['Sussex',144231],['Union',575352],['Warren',109638]]


# In[5]:


#setting up a dataframe
df0 = pd.DataFrame(county_pop,columns=['county','pop'])


# In[6]:


#checking we have the appropriate number of counties in the dataframe
#per the assignment we expect to see 21
county_cnt = len(df0['county'].unique())
print(county_cnt)


# ### Adjacent Pair Setup

# Based on data from the following: https://www2.census.gov/geo/docs/reference/county_adjacency.txt

# Some pre-proceesing was performed.  Pairs were found only for the state of New Jersey.  And some many adjustment to county name conventions was made to be consistent with the rest of data used in this file

# In[7]:


county_pair_list= [['Atlantic','Burlington'],['Atlantic','Camden'],['Atlantic','Cape'],['Atlantic','Cumberland'],['Atlantic','Gloucester'],['Atlantic','Ocean'],['Bergen','Essex'],['Bergen','Hudson'],['Bergen','Passaic'],['Burlington','Atlantic'],['Burlington','Camden'],['Burlington','Mercer'],['Burlington','Monmouth'],['Burlington','Ocean'],['Camden','Atlantic'],['Camden','Burlington'],['Camden','Gloucester'],['Cape','Atlantic'],['Cape','Cumberland'],['Cumberland','Atlantic'],['Cumberland','Cape'],['Cumberland','Gloucester'],['Cumberland','Salem'],['Essex','Bergen'],['Essex','Hudson'],['Essex','Morris'],['Essex','Passaic'],['Essex','Union'],['Gloucester','Atlantic'],['Gloucester','Camden'],['Gloucester','Cumberland'],['Gloucester','Salem'],['Hudson','Bergen'],['Hudson','Essex'],['Hudson','Union'],['Hunterdon','Mercer'],['Hunterdon','Morris'],['Hunterdon','Somerset'],['Hunterdon','Warren'],['Mercer','Burlington'],['Mercer','Hunterdon'],['Mercer','Middlesex'],['Mercer','Monmouth'],['Mercer','Somerset'],['Middlesex','Mercer'],['Middlesex','Monmouth'],['Middlesex','Somerset'],['Middlesex','Union'],['Monmouth','Burlington'],['Monmouth','Mercer'],['Monmouth','Middlesex'],['Monmouth','Ocean'],['Morris','Essex'],['Morris','Hunterdon'],['Morris','Passaic'],['Morris','Somerset'],['Morris','Sussex'],['Morris','Union'],['Morris','Warren'],['Ocean','Atlantic'],['Ocean','Burlington'],['Ocean','Monmouth'],['Passaic','Bergen'],['Passaic','Essex'],['Passaic','Morris'],['Passaic','Sussex'],['Salem','Cumberland'],['Salem','Gloucester'],['Somerset','Hunterdon'],['Somerset','Mercer'],['Somerset','Middlesex'],['Somerset','Morris'],['Somerset','Union'],['Sussex','Morris'],['Sussex','Passaic'],['Sussex','Warren'],['Union','Essex'],['Union','Hudson'],['Union','Middlesex'],['Union','Morris'],['Union','Somerset'],['Warren','Hunterdon'],['Warren','Morris'],['Warren','Sussex']]


# In[8]:


df_pair = pd.DataFrame(county_pair_list, columns=['county','adj_county'])


# ### Total Pop Count

# In[9]:


state_pop = df0['pop'].sum()


# ### Global Variables

# In[10]:


num_counties = county_cnt #number of counties
num_leg_districits = 2 #number of legistlative districts
pop_per_rep = state_pop / num_leg_districits #gives us population per representative
pop_sen = 1.10 #variance we will allow in district pop from average
pop_max = pop_per_rep * pop_sen #max pop allowed in each legislative district
pop_min = pop_per_rep / pop_sen #min pop allowed in each legislative district


# ### Looking for Counties with Populations within the Pop Range

# In[11]:


df0[df0['pop'] >= pop_min]['county']


# In[12]:


isolate_list = df0[df0['pop'] >= pop_min]['county']


# ### Setup

# In[13]:


#creating a variable for each county.
counties = df0['county'].unique()


# In[14]:


#creating a variable for each district
district = list(range(0,num_leg_districits))


# In[15]:


#creating a population dictionary
pop_list = df0['pop']
pop = dict(zip(counties, pop_list))


# In[16]:


#adjacency dictionary
adj_dict = df_pair.groupby('county')['adj_county'].apply(list).to_dict()


# ### Creating All Possible Adjacent Pairs

# In[17]:


#just some list magic to generate objects i will use to generate pair variables in PulP
pair_temp = []
sorted_pair_temp = []
start_county = []
end_county = []
for i in counties:
    for p in adj_dict[i]:
       pair_temp.append(i+p)
       sorted_pair_temp.append(sorted(i+p))
       start_county.append(i)
       end_county.append(p)
d = {'pair_list':pair_temp,'sorted':sorted_pair_temp,"start":start_county,"end":end_county}
df = pd.DataFrame(d)
key_list = df.sorted.drop_duplicates().keys()
pair_list = df.pair_list[key_list]
start_list = df.start[key_list]
end_list = df.end[key_list]


# ### Creating a dataframe of each pair within each district layer

# In[18]:


#this will help built the constraint a little quicker, so doing this here and now
pair_list2  = [(p,d) for p in pair_list for d in district]
start_list2  = [(s,d) for s in start_list for d in district]
end_list2  = [(e,d) for e in end_list for d in district]
d2 = {'pair_list':pair_list2,'start':start_list2,"end":end_list2}
df2 = pd.DataFrame(d2)


# ### Establishing Variables

# In[19]:


#establish county/district variables
county_district = LpVariable.dicts("xij",[(c,d) for c in counties for d in district],0,1,cat="Integer")
adj_pair = LpVariable.dicts("xprime",[p for p in pair_list],0,1,cat="Integer")


# ### Objective Function

# In[20]:


#setting up problem
prob = LpProblem("problem",LpMinimize)
prob += lpSum([adj_pair[i] for i in adj_pair])


# In[21]:


#just a reminder we expect these counties to be their own districts as they exceed the population min threshold. 
#that being said, it is possible a very small adjacent county good get lumped in with these
#for NJ, I doubt this will happen though as the most populated counties are concentrated near the NY boarder
isolate_list


# ### Establishing constraints

# In[22]:


#making sure each county is assigned to one and only one district
for c in counties:
    prob += lpSum([county_district[(c,d)] for d in district]) == 1

#setting up constraints on max population in each district
for d in district:
    prob += lpSum([county_district[(i,d)] * pop[i] for i in counties]) <= pop_max

#setting up constraints on min population in each district
for d in district:
    prob += lpSum([county_district[(i,d)] * pop[i] for i in counties]) >= pop_min

#cut edge variables
for i in range(len(pair_list2)):
    prob += adj_pair[list(adj_pair)[math.ceil(i/num_leg_districits)-1]] >= county_district[start_list2[i]] - county_district[end_list2[i]]

for i in range(len(pair_list2)):
    prob += adj_pair[list(adj_pair)[math.ceil(i/num_leg_districits)-1]] >= county_district[end_list2[i]] - county_district[start_list2[i]]
    
#mandating adjacency
#the counties in the isolation list to do not have adjacency requirements
#this is because we expect these counties to be their own districts
#having an adjacency rule would force them to merge with a neighbor
#as we enforce adjacency every else this shouldnt create a problem for us
for d in district:
    prob += county_district["Atlantic",d] <= county_district["Burlington",d] + county_district["Camden",d] + county_district["Cape",d]  + county_district["Cumberland",d] + county_district["Gloucester",d] + county_district["Ocean",d]
    prob += county_district["Burlington",d] <= county_district["Atlantic",d] + county_district["Camden",d] + county_district["Mercer",d]  + county_district["Monmouth",d] + county_district["Ocean",d] 
    prob += county_district["Camden",d] <= county_district["Burlington",d] + county_district["Atlantic",d] + county_district["Gloucester",d]
    prob += county_district["Cape",d] <= county_district["Cumberland",d] + county_district["Atlantic",d]
    prob += county_district["Cumberland",d] <= county_district["Salem",d] + county_district["Gloucester",d] + county_district["Atlantic",d] + county_district["Cape",d] 
    prob += county_district["Gloucester",d] <= county_district["Salem",d] + county_district["Cumberland",d] + county_district["Atlantic",d] + county_district["Camden",d]
    prob += county_district["Hunterdon",d] <= county_district["Mercer",d] + county_district["Morris",d] + county_district["Somerset",d] + county_district["Warren",d] 
    prob += county_district["Mercer",d] <= county_district["Burlington",d] + county_district["Hunterdon",d] + county_district["Middlesex",d] + county_district["Monmouth",d] + county_district["Somerset",d] 
    prob += county_district["Monmouth",d] <= county_district["Burlington",d] + county_district["Mercer",d] + county_district["Middlesex",d] + county_district["Ocean",d] 
    prob += county_district["Morris",d] <= county_district["Essex",d] + county_district["Hunterdon",d] + county_district["Passaic",d] + county_district["Somerset",d] + county_district["Sussex",d] + county_district["Union",d] + county_district["Warren",d] 
    prob += county_district["Ocean",d] <= county_district["Atlantic",d] + county_district["Burlington",d] + county_district["Monmouth",d]
    prob += county_district["Passaic",d] <= county_district["Bergen",d] + county_district["Essex",d] + county_district["Morris",d] + county_district["Sussex",d]
    prob += county_district["Salem",d] <= county_district["Gloucester",d] + county_district["Cumberland",d]  
    prob += county_district["Somerset",d] <= county_district["Hunterdon",d] + county_district["Mercer",d] + county_district["Middlesex",d] + county_district["Morris",d] + county_district["Union",d]
    prob += county_district["Sussex",d] <= county_district["Morris",d] + county_district["Passaic",d] + county_district["Warren",d]                 
    prob += county_district["Union",d] <= county_district["Essex",d] + county_district["Hudson",d] + county_district["Middlesex",d] + county_district["Morris",d] + county_district["Somerset",d]    


# ### Solve

# In[23]:


prob.solve(GLPK_CMD(options=["--mipgap", "0.05", "--gomory"]))


# ### Show the Assignment of County to Legislative District

# In[24]:


assignment_list = []
assignment_county = []
assignment_district = []
assignment_pop = []
for i in county_district:
    assignment_list.append(county_district[i].varValue)
for c in counties:
    for j in district:
        assignment_county.append(c)
        assignment_district.append(j)
        assignment_pop.append(pop[c])
d3 = {"County":assignment_county, "Legislative_District": assignment_district, "assignment_list": assignment_list, "pop": assignment_pop}
df3 = pd.DataFrame(d3)
df3 = df3[df3['assignment_list'] == 1]


# In[25]:


print(df3.groupby('Legislative_District')['County'].apply(' '.join).reset_index())


# In[26]:


#df3.groupby('Legislative_District')['pop'].sum().reset_index()


# In[28]:


#exports a assignment table to the local directory for reference
#df3.to_excel('output_NJ.xlsx')


# ### Check

# In[ ]:


for variable in prob.variables():
    print(f'{variable}: {value(variable.varValue)}')


# In[ ]:


#print(prob)

