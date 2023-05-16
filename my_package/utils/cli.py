from my_package.math.basic import add
from my_package.math.basic import subtract
from my_package.math.basic import multiply
from my_package.math.advanced import divide
from my_package.math.advanced import power
#from .io import get_numbers
from my_package.utils.io import get_numbers
from .io import display_menu

def main():
    display_menu()


    choise = int(input("Please enter your choise: "))

    numbers = get_numbers()

    x = numbers[0]
    y = numbers[1]

    result = 0
    if choise == 1:
        result = add(x, y)
    elif choise == 2:
        result = subtract(x, y)
    elif choise == 3:
        result = multiply(x, y)
    elif choise == 4:
        result = divide(x, y)
    elif choise == 5:
        result = power(x, y)
    else:
        print("there is no such choise. program ended")

    print(f"result = {result}")