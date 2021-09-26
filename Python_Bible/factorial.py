num = int(input("Input the number for calculating the factorial:").strip())
fact = 1
i=1
print(type(num))
while i <=num:
    fact = fact*i
    i = i + 1

print (fact)
