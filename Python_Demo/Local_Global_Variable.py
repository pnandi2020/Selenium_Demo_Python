#Local and Global Variable
#
# Declare a variable and initialize it
f = 101
print(f)
# Global vs. local variables in functions
def someFunction():
    #global f
    f = 'I am learning Python'
    print(f)

someFunction()
print(f)
