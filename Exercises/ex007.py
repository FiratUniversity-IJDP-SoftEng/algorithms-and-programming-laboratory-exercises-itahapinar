# Your Student ID:230543019
# Your Name and Surname:IBRAHIM TAHA PINAR
word = input("Please enter a string: ")
listofWord = set(word)
print("Character frequencies:")
for letter in sorted(listofWord):
    print(f"{letter} : {word.count(letter)}")
