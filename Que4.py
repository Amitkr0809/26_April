"""4.square
write a program that reads a number M and prints a square of M and M column using stars
sample input
4
output
* * * *
* * * *
* * * *
"""

m= int(input("Enter number "))
for i in range (1,m+1):
    print(m * "* ")