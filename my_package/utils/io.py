def get_numbers():
    numbers = []

    numbers.append(float(input("please enter first number: ")))
    numbers.append(float(input("please enter second number: ")))

    return numbers

def display_menu():
    print("1 = add")
    print("2 = substract")
    print("3 = multiply")
    print("4 = divide")
    print("5 = power")