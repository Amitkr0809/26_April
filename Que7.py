"""7.Right angled triangle
write a program that reads a number N and prints a right angled triangle of N rows using stars (*) and pluses(+)
input
4
output
*
* *
* * *
+ + + + """

n = int(input("enter number : "))
for i in range (1,n+1):
    if i <= n-1:
        print(i * "* ")
    else:
        print(i * "+ ")