user = {
    "name" : "John",
    "money" : 48,
    "bag": {}
}

store = {
    "snikers" : 23,
    "pepsi" : 13 ,
    "car" : 10 ,
    "fish" : 11
}

def buy(user, store, item):
    if item in store and store[item] > 0 and user["money"] >= store[item]:
        user["money"] -= store[item]
        store[item] = 0
        if item in user["bag"]:
            user["bag"][item] += 1
        else:
            user["bag"][item] = 1
        print("Bought:", "'", item, "'")
    else:
        print("Cannot buy:", item)
        print("(Your balance:", user["money"])
        print("Price of", item, "is", store[item])
        print("You need", store[item] - user["money"], "more to buy", item,"!)")
    if store[item] == 0:
        del store[item]

def show_bag(user):
    if user["bag"]:
        print("Bag contents:")
        for item, count in user["bag"].items():
            print(item)
    else:
        print("There is nothing here yet!")

print("Hello, " + user["name"] + "! Welcome to the store!")
print("Our products and prices:")
for item, price in store.items():
    print(item, ":", price)
print("Your balance:", user["money"])

while True:
    choice = input("Enter command (B - buy, S - show bag, Q - quit): ")
    if choice == "Q":
        break
    elif choice == "B":
        item = input("Enter item to buy: ")
        buy(user, store, item)
        print("Store contents:")
        for item, count in store.items():
            print(item, ":", count)
        print("Your balance:", user["money"])
    elif choice == "S":
        show_bag(user)
    else:
        print("Invalid command")