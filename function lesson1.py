number = input("enter 3 single-digit numbers:")
mynumbers = number.split()
a,b,c = int(mynumbers[0]),int(mynumbers[1]), int(mynumbers[2])
print(a,b,c)

def adder (a,b,c):
    return a*b*c
result = adder (a,b,c)
print (result)



def calculate_tax(salary):
    if salary>1_000_000:
        tax  = salary*0.5
    else:
        tax = salary*0.1
    return tax

result1 = calculate_tax(1_500_000)
result2 = calculate_tax(2_000_000)
print(result1,result2)