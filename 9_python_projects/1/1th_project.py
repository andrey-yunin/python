
print ("Welcome to my computer quiz!")

playing = input("Do you whant to play: ")
if playing != "yes":
    quit()
    
print("Ok! Let's play!")

answer = input("what does CPU stand for?: ").lower()

if answer == "central processing unit":
    print("It is correct!")
else:
    print("it is not correct")

answer = input("what does GPU stand for?: ").lower()

if answer == "grafics processing unit":
    print("It is correct!")
else:
    print("it is not correct")

answer = input("what does RAM stand for?: ").lower()

if answer == "random access memory":
    print("It is correct!")
else:
    print("it is not correct")

answer = input("what does PSU stand for?: ").lower()

if answer == "power supply unit":
    print("It is correct!")
else:
    print("it is not correct")


