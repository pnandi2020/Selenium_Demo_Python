def SwitchExample(userargument):
    switcher = {
        0: " This is Case Zero ",
       	1: " This is Case One ",
       	2: " This is Case Two ",
    }
    return switcher.get(userargument, "nothing")
if __name__ == "__main__":
    argument = 1
    print (SwitchExample(argument))
