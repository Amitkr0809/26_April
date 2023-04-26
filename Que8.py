"""8.two right angled triangles
write a program that reads a number N and print two right angled triangles of N rows using numbers strating from 1
input
4
sample
1
22
333
4444
1
22
333
4444"""

n = int(input("enter number : "))
count = 1
while count < 3:
    for i in range (1,n+1):
        print(i * str(i))
    count = count+1