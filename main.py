gameList = "delta force 3$\ncall of duty 3.50$\nangry birds 4$\nclash of clans 1.99$\nNFS 4.55$"
#in the video game store
price = 0
budget = 15
chocolate = .10

name = input(str("Shop-owner: Hey! What is your name?\n"))
#takes the input as the name variable
isStupid = input(str("are you stupid?\n"))

if name == "No" and isStupid == "Yes":
    print("LOL. Get out yo!!")
    exit()
#if the user enter "No" as a value and isStupid value as a Yes, the program will be ended if not program will be continue

print("Shop-owner: Nice to meet ya " + name + " How can I help you?\n")
#print the name variable

print("You: I want to buy some video games\n")

print("Shop-owner: Okay, here's our video games " + gameList)

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
    print("Shop-owner: Sorry, we don't have it here " + name)
    print("okay then bye bye")
    exit()
#user must select one of these choices & the prices will be changed according to the user's choice


print("Shop-owner: Sure " + name + " Give me a second, I'll get you " + theGame)

print("-------------------------------------------")
print("-------------------------------------------")

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
    print("Shop-owner: Sure, that'll be .10$. your total is " + str(newTotal))
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
