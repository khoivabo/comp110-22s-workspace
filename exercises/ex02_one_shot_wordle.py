"""Ex02_One_shot_Wordle."""

__author__ = "730277137"


from readline import write_history_file


secret_word: str = ("condom")
player_guess: str = (input(f"What is your {len(secret_word)}-letter guess? "))
played: bool = False

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001f7E8"

word_index: int = 0
emoji: str = ""


while (not played):
    while (len(player_guess) != len(secret_word)):
        player_guess = (input(f"That was not {len(secret_word)} letters! Try again: "))
    while(word_index < len(secret_word)):
        foobar: bool = False
        foobar_tracker: int = 0
        if(player_guess[word_index] != secret_word[word_index]):
            while not foobar and foobar_tracker < len(secret_word):
                if player_guess[word_index] == secret_word[foobar_tracker]:
                    foobar = True
                else:
                    foobar_tracker += 1
            if foobar:
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
        else: 
            emoji += GREEN_BOX
        word_index += 1
    print(emoji)
    if (player_guess != secret_word):
        print("Not quite. Play again soon!")
        played = True
    else: 
        print("Woo! You got it!")
        played = True