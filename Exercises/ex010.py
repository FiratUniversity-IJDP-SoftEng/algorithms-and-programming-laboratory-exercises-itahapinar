# Your Student ID:230543019
# Your Name and Surname:IBRAHIM TAHA PINAR
while True:
    firstNumber = int(input("Please enter a number:"))
    secondNumber = int(input("Please enter a number:"))
    operation = input("Select the operation (+, -, *, /):")
    if operation == "+":
        print(f"The result is {firstNumber + secondNumber}")
    elif operation == "-":
        print(f"The result is {firstNumber - secondNumber}") 
    elif operation == "*":
        print(f"The result is {firstNumber * secondNumber}")
    elif operation == "/":
        if secondNumber == 0:
            print("Error! Division by Zero")
        else:
            print(f"The result is {float(firstNumber / secondNumber)}")
    else:
        print("Invalid option!")  

    option =input("Do you want another calculation?(y/n):")
    if  option.lower() == "n":
        break


