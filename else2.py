a = input("entre un numéro: ")
b = input("entre un autre numéro: ")
result = float(a) + float(b)
print(result)

if result > 30: 
    print("le résultat de cette opération est supérieur à 30")

elif result < 30: 
    print("le reésultat est inférieur à 30 mais supérieur à 0 quand même!!")

elif result == 0:
    print("le résultat est 0")

print("je sais faire des additions c'est fou non?")