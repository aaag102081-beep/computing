#print(" anaya"*200)
age=25
if age<18:
    print("you are a child")
elif age>100:
    print("you are lying!")
else:
    print ("you are an adult")

if age>=18 and hasPassport:
    print("fly to other contry")
elif age>=18 and not hasPassport:
    print("Fly within the country")
else:
    print("Stay in the nation")
    
    
if age>=18:
    if hasPassport:
        print("fly to other contry")
    else:
        print("Fly within the country")
else:
    print("Stay in the nation")



