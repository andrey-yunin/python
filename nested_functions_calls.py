# nested functions calls = function calls inside other function calls 
#                          innermost function calls are resolved first
#                          returned value is used as argument for the next outer function 


""" num = input("input whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num) """

result = round(abs(float(input("input whole positive number: "))))

print(result)

































