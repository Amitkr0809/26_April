"""10.Inverted right angled triangle
write a program that reads a number N and prints an interved right angled triangle of N rows using start
input
5
put
* * * * *
* * * *
* * *
* *
*              """

n = int(input("enter number "))
for i in range(n,0,-1):
    print(i * "* ")