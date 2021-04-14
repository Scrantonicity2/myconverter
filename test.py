question = input("Qui est ton fils? ")


if question == "James" or question == "james":
    print("oui James le petit renard d'amour!!")

question2 = input("Quel âge as-tu? ")

if int(question2) != 37:
    print("nan mais quelle menteuse celle-là...")
    question2b = input("donne ton vrai âge: ")
    if int(question2b) == 37:
        print("ah je préfère ça..")

question3 = input("comment s'appelle ton mari (juste le prénom ça ira): ")

if question3 != "Stéphane":
    print("t'es sérieuse là?????")
elif question3 == "Stéphane" or question3 == "stéphane":
    print("ahhhh Stéphane le plus beau...je le connais ce mec...un dieu vivant")


