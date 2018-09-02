"""
@author - smehdi@ncsu.edu

01/09/18
"""
import itertools
import random
import time

start = time.time()

n = int(input("Enter value of vector n: ")) #ask user to input n for constructing 0-1 vectors
#C = int(input("Enter knapsack capacity/weight c: ")) #ask capacity of the knapsack
wj=[random.randint(5, 20) for i in range(n)] # weight of n items mentioned in the proble
pj =[random.randint(20, 50) for i in range(n)] #value of n items

W = sum(wj)/4
#f = open('solution.txt', 'w') #for saving all feasible and infeasible vectors and the objective solution values in file.
#E = open('combine.txt', 'w')  #for saving all possible combinations of vector size 0 to n. Ex. 0 ==> X1, 6==>X2
feasible = []
fvalue =[]
for i in range(1,n+1): # construction af ll possible combinations of different items.
   temp = 0
   temp = (list(itertools.combinations(range(n),i)))
   #print(*temp,file=E)
   for combin in temp:
       weight =0
       value =0
       tempList =[]
       for val in combin:
           weight=weight+wj[val]
           value = value + pj[val]
           tempList.append(wj[val])
           #print(f"x{val+1}){wj[val]}",end=' , ',file = f)
           #test line- print(tempList,value)
       if(weight>W): #if objective function value is greater than capacity then infeasible solution else feasible.
           #print(f"(infeasible) Zvalue:{value}",file = f)
           pass
       else:
           #print(f" (feasible) Zvalue:{value}",file = f)
           feasible.append(tempList)
           fvalue.append(value)
print(f"wj is {wj}")
print(f"pj is {pj}")
print(f"knapsack capacity : {W}")
#print(f"feasible solutions : {(feasible)}")
#print(f"feasible values : {(fvalue)}")
print(f"optimal solution : {feasible[fvalue.index(max(fvalue))]}")
print(f"optimal Z value : {max(*fvalue)}")
end = time.time()
print(f"Execution time : {round(end - start,5)} secs",)
