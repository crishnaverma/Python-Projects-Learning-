def add(n1,n2):
    return n1 + n2


def substract(n1,n2):
    return n1 - n2


def multiply(n1,n2):
    return n1 * n2


def divide(n1,n2):
    return n1 / n2

disc ={
    "+": add,
    "-" : substract,
    "*" : multiply,
    "/" : divide,
}
def calculator():
    
    logo='''             _____________________
            |  _________________  |
            | | JO           0. | |
            | |_________________| |
            |  ___ ___ ___   ___  |
            | | 7 | 8 | 9 | | + | |
            | |___|___|___| |___| |
            | | 4 | 5 | 6 | | - | |
            | |___|___|___| |___| |
            | | 1 | 2 | 3 | | x | |
            | |___|___|___| |___| |
            | | . | 0 | = | | / | |
            | |___|___|___| |___| |
            |_____________________|

            (Regular Calculator)
'''

    print(logo)
    number_1 = float(input("Enter the First Number"))

    should_conti = True

    while should_conti:


        for symbol in disc:
            print(symbol)
        operation = input("Choose the Operation\n")
        number_2 = float(input("Enter the second Second\n"))


        value=disc[operation](number_1,number_2)

        print(f"{number_1}{operation}{number_2} = {value}")

        conti = input(f"Type 'y'  if you like to continue with previous number({value}) else press 'n' to stop or to restart")

        if conti == "y":
            number_1 = value

        else:
            should_conti = False
            print("\n"*20)
            

calculator()