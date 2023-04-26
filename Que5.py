"""5.square-2
write a program that reads a number M and print square of M rows and M columns using number
sample input
4
output
1111
2222
3333
4444"""

m= int(input("Enter number "))
for i in range (1,m+1):
    print(m * str(i))