#Define the functions for addition, subtraction, multiplication and division
def add(a, b):
    answer = a + b
    #Give user visualization
    print(str(a) + " + " + str(b) + " = " + str(answer))

def sub(a, b):
    answer = a - b
    #Give user visualization
    print(str(a) + " - " + str(b) + " = " + str(answer))

def multi(a, b):
    answer = a * b
    #Give user visualization
    print(str(a) + " * " + str(b) + " = " + str(answer))

def div(a, b):
    answer = a / b
    #Give user visualization
    print(str(a) + " / " + str(b) + " = " + str(answer))


#Add while to continue the program until the user wants to exit
while True:
#Print options available to user
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    #Ask for calculations
    choice = input("Please select calculation")

    if choice == "a" or choice == "A":
        print("Addition")
        #Ask for values
        a = int(input("Input first number"))
        b = int(input("Input second number"))
        #Call the functions
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        #Ask for values
        a = int(input("Input first number"))
        b = int(input("Input second number"))
        #Call the functions
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        #Ask for values
        a = int(input("Input first number"))
        b = int(input("Input second number"))
        #Call the functions
        multi(a, b)
    elif choice == "d" or choice == "D":
        print("Division")
        #Ask for values
        a = int(input("Input first number"))
        b = int(input("Input second number"))
        #Call the functions
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Program ended")
        quit()