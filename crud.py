from create import create
from delete import delete
from read import read
from update import update

def inquiry():
    selection = input("Welcome to Broadway. Choose C/R/U/D/E")
    selection = selection.lower()

    def continue_or_not(c):
        inquiry() if c else print("Thank you. See you again")

    if selection == "c":
        cont = create()
        return continue_or_not(cont)
        # if cont == True:
        #     inquiry()
        # else:
        #     print("Thank you. See you again")

    elif selection == "r":
        cont = read()
        return continue_or_not(cont)

    elif selection == "u":
        cont = update()
        return continue_or_not(cont)

    elif selection == "d":
        cont = delete()
        return continue_or_not(cont)
    else:
        print("Thank you. See you again")

inquiry()

