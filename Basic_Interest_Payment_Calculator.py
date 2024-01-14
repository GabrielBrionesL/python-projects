def interest_payment():
    print("This is a monthly payment loan calculator")
    print("")

    # Collect the necessary inputs: principal, APR, years
    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Input the length of the loan in years: "))

    # Calculate the monthly payment
    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))

    # Show the result
    print("The monthly payment for this loan is: %.2f" % monthly_payment)

interest_payment()