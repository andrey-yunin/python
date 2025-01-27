# excetion = events detected during execution that interrupt the flow of program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator

#except Exception:
# print("Somthing went wrong:( ")
    
except ZeroDivisionError as e: 
    print(e)
    print("You can't divide by zero")

except ValueError as e:
    print(e)
    print("Enter only number please")

else:
    print(result)

finally:
    print("this will always execute")












































