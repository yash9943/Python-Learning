n = int(input("Enter Any Number : "))
if n%2 == 0 :
    print("Number Is Even.")
else:
    print("Number Is Odd.")


# Using of ternory operator   
msg = "Number is even" if n%2==0 else "Number is odd"
print(msg)
