# Collect email from user
def email_slicer():
    print("Welcome to eMail Slicer")
    print("")

    email_input = input("Input your email address: ")

    # Split email with @ delimiter into user name and domain
    (username, domain) = email_input.split("@")

    # Split domain with . delimiter
    (domain, extension) = domain.split(".")

    #Print results
    print("Username: ", username)
    print("Domian: ", domain)
    print("Extension:L ", extension)

# Get multiple/continuous input from user
while True:
    email_slicer()