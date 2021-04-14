
ask = input("enter a number: ")
ask2 = input("enter a second one: ")

if int(ask) > 10 and int(ask2) > 10:
    print("both are greater than 10")
elif int(ask) < 10 and int(ask2) > 10:
    print("the first number is smaller than 10 but not the second one")
elif int(ask) < 10 and int(ask2) < 10:
    print("both are smaller than 10")
elif int(ask) > 10 and int(ask2) < 10:
    print("first number is greater than 10 but second is not")

print("this is a fun game right?.....RIGHT??....")