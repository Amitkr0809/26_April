"""6.Right angles triangle using for loop
write a program that reads a number N and prints a right angled triangle of N rows using stars
input
4
output
*
* *
* * *
* * * *"""

n = int(input("enter number "))
for i in range (1,n+1):
    print(i * "* ")