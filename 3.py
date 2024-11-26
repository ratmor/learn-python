def find_largest():
    # Accept user input for three integers
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    num3 = int(input("Enter the third integer: "))

    # Determine and print the relevant message based on the input values
    if num1 == num2 == num3:
        print("All three numbers are equal.")
    elif num1 == num2 or num1 == num3 or num2 == num3:
        if num1 == num2:
            largest = num3
        elif num1 == num3:
            largest = num2
        else:
            largest = num1
        print(f"Two numbers are equal, and the largest of the three is {largest}.")
    else:
        if num1 > num2 and num1 > num3:
            largest = num1
        elif num2 > num1 and num2 > num3:
            largest = num2
        else:
            largest = num3
        print(f"The largest of the three numbers is {largest}.")

# Call the function
find_largest()
