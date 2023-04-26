"""1. write a program that reads a number N and prints 10 numbers after N
sample input
5
output:
5
6
7
8
9
10 .... upto numbers"""

n = int(input("enter number "))
for i in range(n,(n+11)):
    print(i)