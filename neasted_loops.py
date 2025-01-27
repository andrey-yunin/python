# neasted loop = "the inner loop"  will finish all of it's iteration befor
# finishing one iteration of "outer loop"

import time

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
simbol = (input("Enter simpol to use: "))
""" minute = 0
for i in range (rows):
    second = 0        
    for j in range (columns):       
       print(str(minute) + ": " + str(second))
       time.sleep(1)
       second = second + 1
    minute = minute + 1 """

for i in range(rows):
    for j in range(columns):
        print(simbol, end = " ")
        time.sleep(1)
    print()





























