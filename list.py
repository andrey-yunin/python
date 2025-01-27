# list =  used to store multiple items in a single variable

food = ["pizza", "hamburger", "hotdag", "spaghetti"]

print (food)
print (food[0])
for i in range(0,4):
    print (food[i])

food[0] = "sushi"
print (food)

food.append("ice scream")

food.remove(food[3])
food.remove("sushi")
food.pop()
food.insert(0, "meat")
food.sort()
food.clear()

for j in food:
    print(j)




























