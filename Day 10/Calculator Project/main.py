import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

continue_no = True
while continue_no:
    number_1 = int(input("What is your first number?: "))
    continue_yes = True
    while continue_yes:
        print("+ \n- \n* \n/")
        operation_1 = input("Pick an operation: ")
        number_2 = int(input("What is the next number?: "))
        result =operations[operation_1](number_1, number_2)
        print(f"{number_1} {operation_1} {number_2} = {operations[operation_1](number_1, number_2)}")
        selection = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if selection == "y":
            number_1 = result
            continue_no = False
        elif selection == "n":
            continue_yes = False
            continue_no = True
