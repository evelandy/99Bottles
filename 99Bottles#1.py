import sys


def main():
    try:
        drink = input("what type of drink do you want?\n[b]-Beer\n[s]-Soda\n[w]-Water\n"
                      "Choose by pressing a corresponding letter and press enter.\n: ")
        drink = logic(drink)

        quantity = int(input("\nHow many bottles of {} do you want to start with?\n"
                             "Pick a number between 1 and 99\n: ".format(drink)))
        song(drink, quantity)
    except ValueError:
        print('\n\n\nPlease make sure you choose a digit for the quantity.\n'
              'Restart the program and try again.\n')
        sys.exit()


def song(drink, quantity):
    print()
    for quant in range(quantity, 1 - 1, -1):
        if quant == 1:
            print("{quant} bottle of {drink} on the wall, {quant} bottle of {drink}. Take one down, pass it around no "
                  "more bottles of {drink} on the wall".format(drink=drink, quant=quant))
        else:
            print("{quant} bottles of {drink} on the wall, {quant} bottles of {drink}. Take one down, pass it around "
                  "{new_quant} bottles of {drink} on the wall".format(drink=drink, quant=quant, new_quant=(quant-1)))


def logic(drink):
    if drink.lower() == 'b':
        drink = 'beer'
    elif drink.lower() == 's':
        drink = 'soda'
    elif drink.lower() == 'w':
        drink = 'water'
    else:
        print('\n\n\nPlease make sure you choose from the choices provided.\n'
              'Restart the program and try again.\n')
        sys.exit()
    return drink


main()
