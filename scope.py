# scope = the region that a variable is recognazed
#         a variable is only available from inside the region that is created 
#         a global and locally scoped versions of a variable can be created 
#         L - local
#         E - enclosing
#         G - global
#         B - built-in         

name = "Yunin" # globale scope (available inside and otside of function)

def display_name():
    # name = "Andrey" # local scope (available only inside this function)
    print(name)

display_name()
print(name)



































