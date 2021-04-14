

def money(currency):
    if currency < 300:
        print("le mec a pas de thune wesh")
    mess = " Euros are "
    mess2 = " Dollars"
    result = (currency * 1.4389)
    payday = str(currency) + mess + str(int(result)) + mess2
    return payday

print(money(800))
print(money(100))



