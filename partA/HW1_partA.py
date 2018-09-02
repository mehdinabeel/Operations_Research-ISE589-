"""
@author - smehdi@ncsu.edu

01/09/18
"""
import itertools

W=[9,5,20,11,17,25,13] # weight of 7 items mentioned in the proble
p =[9,5,20,11,17,25,13] #value of items
n = int(input("Enter value of vector n: ")) #ask user to input n for constructing 0-1 vectors
C = int(input("Enter knapsack capacity/weight c: ")) #ask capacity of the knapsack
f = open('solution.txt', 'w') #for saving all feasible and infeasible vectors and the objective solution values in file.
E = open('combine.txt', 'w')  #for saving all possible combinations of vector size 0 to n. Ex. 0 ==> X1, 6==>X2
feasible = []
fvalue =[]
for i in range(1,n+1): # construction af ll possible combinations of different items.
   temp = (list(itertools.combinations(range(n),i)))
   print(*temp,file=E)
   for combin in temp:
       value =0
       tempList =[]
       for val in combin:
           value=value+W[val]
           tempList.append(W[val])
           print(f"x{val+1}){W[val]}",end=' , ',file = f)

       if(value>C): #if objective function value is greater than capacity then infeasible solution else feasible.
           print(f"(infeasible) Zvalue:{value}",file = f)
       else:
           print(f" (feasible) Zvalue:{value}",file = f)
           feasible.append(tempList)
           fvalue.append(value)

print(f"Optimal Solution value is: {max(fvalue)}") #print maximum value of objective function feasible solutions
