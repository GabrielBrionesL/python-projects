#Define function with string
def replace_word():
    #Pre-defined string
    str = "Howdy y'all, my name is Gabriel."
    #Ask user for word they would like to replace
    word_to_replace = input("Enter the word to replace: ")
    #Ask user for replacement
    word_replacement = input("Enter the word replacement: ")
    print(str.replace(word_to_replace, word_replacement))

replace_word()