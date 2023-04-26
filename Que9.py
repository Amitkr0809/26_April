"""9.rectangle -3
write a program that reads tow numbers M and N and prints a rectangle m rows and N columns using number
input:
2
3
output:
1 1 1
2 2 2 """

m = int(input("enter Number of row "))
n = int(input("enter Number of Column "))

for i in range(1,m+1):
    for j in range(1,n+1):
        print(i,end="")
    print()