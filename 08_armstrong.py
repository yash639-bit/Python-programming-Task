n=int(input("Enter number: "))
power=len(str(n))
total=sum(int(d)**power for d in str(n))
print(total==n)
