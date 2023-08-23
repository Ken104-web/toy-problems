#  Write intergers
# take three intergers as argunments
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

#  Assigning a function that cheks if the assigned values are greater than 0 and increment them
def integers(a, b, c):
    count = 0
    if a > 0:
        count += 1
    if b > 0:
        count += 1
    if c > 0:
        count +=1
    return count == 2
# Assign result
result = integers(a, b, c)
print(f"Only two numbers are positive: {result}")
   
