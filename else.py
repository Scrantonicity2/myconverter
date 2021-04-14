quest1 = input("Please enter a number: ")
quest2 = input("Please enter another one: ")
result = float(quest1) - float(quest2)

if result > 10: 
    print("the result is greater than 10")
elif result > 0:
    print("the result is greater than 0 but not than 10")
elif result == 0:
    print("0")
else:
    print("the result is negative")

print("you can try again")