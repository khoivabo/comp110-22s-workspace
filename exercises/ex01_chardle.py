"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = 730277137

instances_found: int = 0 
choosen_word: str = input("Enter a 5-character word: ") 
if len(choosen_word) == 5:
    searched_character: str = input("Enter a single character: ")
    if len(searched_character) == 1:
        print("Searching for " + searched_character + " in " + choosen_word)
        if choosen_word[0] == searched_character:
            print(searched_character + " found at index 0")
            instances_found = instances_found + 1 
        if choosen_word[1] == searched_character:
            print(searched_character + " found at index 1")
            instances_found = instances_found + 1 
        if choosen_word[2] == searched_character:
            print(searched_character + " found at index 2")
            instances_found = instances_found + 1 
        if choosen_word[3] == searched_character:
            print(searched_character + " found at index 3")
            instances_found = instances_found + 1 
        if choosen_word[4] == searched_character:
            print(searched_character + " found at index 4")
            instances_found = instances_found + 1
        if instances_found == 0:
            print("No instances of " + searched_character + " found in " + choosen_word)
        else:
            print(str(instances_found) + " instances of " + searched_character + " found in " + choosen_word)
    else:
        print("Error: Character must be a single character.")
else:
    print("Error: Word must contain 5 characters")
