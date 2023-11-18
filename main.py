import random


gameList = ["delta force" , "call of duty" , "angry birds" , "clash of clans" , "NFS"]
#in the video game store
price = 0
budget = 15
chocolate = (random.randint(1,3))

name = input(str("Shop-owner: Hey! What is your name?\n"))
#takes the input as the name variable

isStupid = input(str("are you stupid?\n"))

isGolden = str(input("Hey! " + name + " are you a our golden member?\n"))

if name == "no" or isStupid == "yes":
    print("LOL. Get out yo!!")
    exit()
#if the user enter "No" as a value and isStupid value as a Yes, the program will be ended if not program will be continue
elif isStupid == "no" and isGolden == "yes":
    print("Shop-owner: Please request any video game you like, we'll find it from anywhere today " + name)

print("Shop-owner: " + name + " How can I help you?\n")
#print the name variable

print("You: I want to buy some video games\n")

print("Shop-owner: Okay, here's our video games " + str(gameList))

theGame = input(str("Shop-owner: Which one do you need?\n"))
#asking which game & storing the value

if theGame == "delta force":
    price = 3
    print("It is 3$ for one")
elif theGame == "call of duty":
    price = 3.50
    print("Shop-owner: It is 3.50$ for one")
elif theGame == "angry birds":
    price = 4
    print("Shop-owner: It is 4$ for one")
elif theGame == "clash of clans":
    price = 1.99
    print("Shop-owner: It is 1.99$ for one")
elif theGame == "NFS":
    price = 4.55
    print("Shop-owner: It is 4.55$ for one")
else:
    if isGolden == "no":
        print("Shop-owner: Sorry, we don't have it here " + name)
        print("okay then bye bye")
        exit()
    elif isGolden == "yes":
        #adding the requesting video game to the game list because of the user is a golden member
        gameList.append(theGame)
        print("Shop-owner: here it's our new list!!" + str(gameList))
        price = (random.randint(1,5))
        print("Shop-owner: It is " + str(price) + " for one")

#user must select one of these choices & the prices will be changed according to the user's choice

print("Shop-owner: Sure " + name + " Give me a second, I'll get you " + theGame)

print("-------------------------------------------")
print("-------------------------------------------")
print("meanwhile in the back of the video game-store")

print("Shop-owner: Yo, nick. there is a customer. you should get my new video games as soon as possible")
print("Nick: I am working on it.")

for x in range(2):
    if isGolden == "no":
        out_of_stock = (random.choice(gameList))
        #generating random value from the list
        print("Nick: Hey! " + out_of_stock + " gonna be out of stock ASAP!")
        print("Shop-owner: damn, ")

        gameList.remove(out_of_stock)
        #remove the random generated value from the list

        if theGame == out_of_stock:

            print("Shop-owner: Unlucky! he is not gonna have " + theGame + " today!")
        else:
            print("Shop-owner: Thanks god. it is not " + theGame + " I should go to the POS now")

    if theGame == out_of_stock:
        print("Shop-owner: i am so sorry " + name + "!" + theGame + "has just sold out")
        print("Shop-owner: This is our new item list: " + str(gameList))

        theGame = input(str("Shop-owner: Which one do you need?\n"))
#asking which game & storing the value

    if theGame == "Shop-owner: delta force":
        price = 3
        print("It is 3$ for one")
    elif theGame == "call of duty":
        price = 3.50
        print("Shop-owner: It is 3.50$ for one")
    elif theGame == "angry birds":
        price = 4
        print("Shop-owner: It is 4$ for one")
    elif theGame == "clash of clans":
        price = 1.99
        print("Shop-owner: It is 1.99$ for one")
    elif theGame == "NFS":
        price = 4.55
        print("Shop-owner: It is 4.55$ for one")
    else:
        if isGolden == "no":
            print("Shop-owner: Sorry, we don't have it here " + name)
            print("okay then bye bye")
            exit()
        elif isGolden == "yes":
            #adding the requesting video game to the game list because of the user is a golden member
            gameList.append(theGame)
            print("Shop-owner: here it's our new list!!" + str(gameList))
            price = (random.randint(1,5))
            print("Shop-owner: It is " + str(price) + " for one")

    #user must select one of these choices & the prices will be changed according to the user's choice



quantity = input("Shop-owner: Hey " + name + " i have got your " + theGame + " How many copies do you need bro?\n")
#asking the quantity and storing the value

total = (price*int(quantity))
#total is price*quantity
newTotal = float(total) + float(chocolate)
#new total with a chocolate

print("Shop-owner: Okay buddy! your total is " + str(total) + " and here is your " + str(quantity) + " of your " + theGame + " copies")

print("You: oh great!")

print("You: here's the money")

if budget > total:
    print("You: can i have 1 chocolate as well")
    print("Shop-owner: Sure, that'll be " + str(chocolate) + "$. your total is " + str(newTotal) + "$")
    #budget variable must be less than total
    if budget >= newTotal:
        print("You: Yes! great. Thank you")
    else:
        print("Shop-owner: oops. sorry your money is not enough for a chocolate")
        print("You: okay. give me the " + theGame + " Please")
    #budget variable is less than total but not enough for the chocolate variable value
else:
    print("Shop-owner: Sorry " + name + " your money is not enough for the " + theGame )
    #budget variable value is not enough for the total
    isGambling = str(input("Shop-owner: Hey! i have an idea, do you want to earn money by gambling?\n" ))
    if isGambling == "yes":
        print("Shop-owner: great!! follow me")
        print("----------------------------------------------")
        print("----------------------------------------------")
        print("Shop-owner: let's gamble! we should do the guessing game. would you like it?")
        print("You: i don't mind it")

        rounds = int(input("Shop-owner: How many rounds do you want to play?"))

        for i in range(rounds):
            
            print("Shop-owner: This is the guessing game!!! you have to guess the number i have")
            print("You: great, i'll guess now.....\n")

            guess = (random.randint(0,9))
            #randomly generating a number within 0-100
            answer = int(input())
            #the answer will be storing in a answer variable
            if answer == guess:
                print("Shop-owner: alright you guessed it")
            else:
                print("Shop-owner: Bad luck yo.")

            print("Shop-owner: want to quit?\n")
            quit = str(input())
            if quit == "yes":
                exit()