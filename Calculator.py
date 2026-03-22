print("CALCULATOR")
def add(num1, num2):
    sum = num1 + num2
    print("The answer is : " + str(sum))

def sub(num1, num2):
    diff = num1 - num2
    print("The answer is : " + str(diff))

def mult(num1, num2):
    product = num1 * num2
    print("The answer is : " + str(product))

def div(num1, num2):
    quotient = num1/num2
    print("The answer is : " + str(quotient))

while True:

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
        operation = input("Choose operation [+, -, *, /] : ")


        if(operation == "+"):
            add(first_number, second_number)
        elif(operation == "-"):
            sub(first_number, second_number)
        elif(operation == "*"):
            mult(first_number, second_number)
        elif(operation == "/"):
            if(second_number == 0):
                print("Divisor cannot be zero!")
            else:
                div(first_number, second_number)
        else:
            print("Operation not valid!")
    except ValueError:
        print("Invalid input, Please enter numbers only!")
    choice = input("Do you wish to do another operation? (y/n) : ")
    if (choice != "y"):
        print("Bye!")
        break

