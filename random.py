import random

x = random.randint(1, 6)
y = random.random()
print(x, y)

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)
print(z)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]

for j in cards:
    print(j)

random.shuffle(cards)
for i in cards:
    print(i)




































