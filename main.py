gameList = "delta force, call of duty, angry birds, clash of clans,NFS"
#in the video game store

price = 10
#price is assign to 10

name = input(str("Shop-owner: Hey! What is your name?\n"))
#takes the input as the name variable

print("Shop-owner: Nice to meet ya " + name + " How can I help you?\n")
#print the name variable

print("You: I want to buy some video games\n")

print("Shop-owner: Okay, here's our video games " + gameList)

theGame = input(str("Shop-owner: Which one do you need?\n"))
#asking which game & storing the value

print("Shop-owner: Sure " + name + " Give me a second, I'll get you " + theGame)

print("-------------------------------------------")

quantity = input("Shop-owner: Hey " + name + " i have got your " + theGame + " How many copies do you need bro?\n")
#asking the quantity and storing the value

total = (price*int(quantity))
#total is price*quantity

print("Shop-owner: Okay buddy! your total is " + str(total) + " and here is your " + str(quantity) + " of your " + theGame + " copies")

print("You: oh great!")