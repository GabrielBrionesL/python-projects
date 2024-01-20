from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input("Enter the word you would like to define: ")
    if word == "":  # Break out of the program if left blank
        break
    print(dictionary.meaning(word))  # Print the definition of the word