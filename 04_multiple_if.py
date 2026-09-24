a = int(input("Enter the age: "))

# If statement no: 1
if(a%2 == 0) :
    print("a is even")
# End of if statement no: 1

# If statement no: 2
if(a>=18) :
    print("You are above the age")

elif(a<0) :
    print("You are entering a negative age which is invalid")

elif(a==0) :
    print("You are entering an invalid age")

else :
    print("You are below the age")
# End of if statement no: 2

print("End of the program")