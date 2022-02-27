"""EX03-Wordle.""" 

__author__ = "730277137"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001f7E8"           


def contains_char(word_to_search: str, character_to_find: str) -> bool:
    """Check if a character is in a word."""
    assert len(character_to_find) == 1
    word_check: int = 0 
    while word_check < len(word_to_search):
        if word_to_search[word_check] == character_to_find:
            return True
        else:
            word_check += 1 
    return False


def input_guess(expected_length: int) -> str:  
    """Make sure guess is correct length."""
    entered_guess = input(f"Enter a {expected_length} character word: ")
    while len(entered_guess) != expected_length:
        entered_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return entered_guess


def emojified(your_guess: str, secret: str) -> str:
    """Concatenate the emojis."""
    assert len(your_guess) == len(secret)
    emojified_bool: bool = False
    emoji: str = ""
    while not emojified_bool: 
        emojified_tracker: int = 0 
        while emojified_tracker < len(secret):
            if contains_char(secret, your_guess[emojified_tracker]) is True: 
                if your_guess[emojified_tracker] == secret[emojified_tracker]:
                    emoji += GREEN_BOX
                else:
                    emoji += YELLOW_BOX
            else: 
                emoji += WHITE_BOX
            emojified_tracker += 1 
        emojified_bool = True
    return emoji
           

def main() -> None:  
    """The main game."""
    played: bool = True
    secret_word: str = "codes"
    current_turn: int = 1
    while played and current_turn <= 6:
        print(f"=== Turn {current_turn}/6 ===")
        player_guess = input_guess(len(secret_word))
        match = emojified(player_guess, secret_word)
        print(match)
        if player_guess == secret_word: 
            played = False
        else:
            current_turn += 1 
    if current_turn == 7:
        print("X/6 - Sorry, try again tomorrow!")

    else:
        print(f"You won in {current_turn}/6 turns!")


if __name__ == "__main__":
    main()