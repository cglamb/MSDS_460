### Integer Program for Redistricting New Jersey

Program defines a integer program that draws lines for congressional districts in the state of New Jersey.  Program optimizes compactness (by minimizing the number of cut edges between districts).

Program constraints include:

(1) No subdivision of counties

(2) Counties may only be joined into a congressional district with geographically adjacent counties (defined by sharing a county border)

(3) Population in each district must be roughly equivalend

### Version Explanation

Hw3_Group2_NJ_v3.ipynb: Is an integer program for the entire state of New Jersey.  Computational constraints prevented us from getting a solution from this version

Hw3_Group2_NJ_v4_2_regions.ipynb:  Version of the code above but sub-divides the state into a region A and B, each with approximately half of the state population.

Hw3_Group2_NJ_North_Jersey_v3.ipynb: Takes region A above and draws congressional districts within that regions.  

Hw3_Group2_NJ_South_Jersey_v3.ipynb: Takes region B above and draws congressional districts withn the regions

Hw3_Group2_NJ_South_Jersey_v4.ipynb: Variant of Hw3_Group2_NJ_South_Jersey_v3.ipynb.  This reduces the number of districts but allows the largest regions to be allocated two representitves

### Solution

Map of the regions below.  10 unique districts.  2 of the districs receive two representives

![image.png](attachment:image.png)

Per each district, population per representitive:

![image.png](attachment:image.png)
