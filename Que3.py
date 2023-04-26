"""3.sum of Numbers from M to N using for loop
given two integers M and N write a program to print thr sum of the numbers from M to N
sample input
2
6
output
20"""

m = int(input("Enter number "))
n = int(input("Enter number "))
sum = 0
for i in range (m,n+1):
    sum = sum+i
print(sum)
