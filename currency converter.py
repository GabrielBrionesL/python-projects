# We are using a static exchange rate of Euros to Japanese Yen
convert_to_JPY = lambda euros: euros * 158.85

# Create the function to convert
def curr_convert():
    print("This program converts Euros (EUR) to Japanese Yen (JPY)")
    print("")

    EUR = eval(input("Enter the amount in euros: "))

    JPY = convert_to_JPY(EUR)

    print(f"{EUR} Euros is {JPY} Japanese Yen.")

curr_convert()