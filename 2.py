def getBMI():
    # Accept user input for weight and height
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = weight / (height ** 2)

    # Print the BMI value
    print(f"Your BMI is: {bmi:.2f}")

    # Determine the message based on the BMI value
    if bmi < 17:
        print("You are underweight.")
    elif 17 <= bmi <= 24:
        print("Your BMI is fine.")
    else:
        print("You are overweight.")

# Call the function
getBMI()
