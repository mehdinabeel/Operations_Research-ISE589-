"""
@author - smehdi@ncsu.edu

01/09/18
"""
import itertools
import random

W=[]
p=[]
#ask user to input n for constructing 0-1 vectors
n = int(input("Enter size of vector n: "))
Q = int(input("For random values enter 1 for manual entry type 0: "))
if Q==1:
    W=[random.randint(5, 20) for i in range(n)] # weight of n items mentioned in the proble
    p =[random.randint(20, 50) for i in range(n)] #value of n items

    C = sum(W)/4
else:
    #weight of items
    for i in range(n):
        a = 0
        a=int(input(f"Enter weight of item {i+1}:"))
        W.append(a)
    #value of items
    for i in range(n):
        b=0
        b=int(input(f"Enter value of item {i+1}:"))
        p.append(b)
    #ask capacity of the knapsack
    C = int(input("Enter knapsack capacity/weight c: "))
 #for saving all feasible and infeasible vectors and the objective solution values in file.
f = open('solution.txt', 'w')
#for saving all possible combinations of vector size 0 to n. Ex. 0 ==> X1, 6==>X2
E = open('combine.txt', 'w')
feasible = []
fvalue =[]
# construction af ll possible combinations of different items.
for i in range(1,n+1):
   temp = (list(itertools.combinations(range(n),i)))
   print(*temp,file=E)
   for combin in temp:
       value =0
       tempList =[]
       for val in combin:
           value=value+W[val]
           tempList.append(W[val])
           print(f"x{val+1}){W[val]}",end=' , ',file = f)
#if objective function value is greater than capacity then infeasible solution else feasible.
       if(value>C):
           print(f"(infeasible) Zvalue:{value}",file = f)
       else:
           print(f" (feasible) Zvalue:{value}",file = f)
           feasible.append(tempList)
           fvalue.append(value)
#print maximum value of objective function feasible solutions
ma = max(fvalue)
print(f"wi : {W}")
print(f"pi : {p}")
print(f"W : {C}")
#print multiple solutions
print(f"Optimal Solution value is: {max(fvalue)}")
Done = []
for i in range(len(fvalue)):
    if (fvalue[i]==ma) and (feasible[i] not in Done):
        print(f"Optimal Solution {feasible[i]}")
        Done.append(feasible[i])
