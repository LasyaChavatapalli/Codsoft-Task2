print("---Calculator---")
print("Choose any Arithmetic Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
while True:
    choice = int(input("Enter any choice from 1-4 : "))
    if choice < 1 or choice > 4:
        print("Invalid Choice...Please enter choice from 1-4 again")
    else:
        num1 = int(input("Enter First number : "))
        num2 = int(input("Enter Second number : "))
        if choice ==1:
            print("Addition of",num1,"and",num2,"is:",num1+num2)
            break
        elif choice == 2:
            print("Subtraction of",num1,"and",num2,"is:",num1 - num2)
            break
        elif choice == 3:
            print("Multiplication of",num1,"and",num2,"is:",num1*num2)
            break
        elif choice == 4:
            if num2 == 0:
                print("Cannot divide by zero")
            else:
                print("Division of",num1,"and",num2,"is:",num1/num2)
            break
 