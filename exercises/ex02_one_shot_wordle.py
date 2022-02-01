"""Ex02_One_shot_Wordle."""

__author__ = "730277137"


secret_word: str = ("python")
player_guess: str = (input(f"What is your {len(secret_word)}-letter guess? "))

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001f7E8"

while len(player_guess) != len(secret_word):
    player_guess: str = (input(f"That was not {len(secret_word)} letters! Try again: "))
index_guess: str = (player_guess[0])
correct_letter: str = GREEN_BOX 
player_counter: int = 0
secret_counter: int = 0
color_boxes: str = ("")
secret_bool: bool = False 
secret_check: int = 0 
while player_counter < len(secret_word):
    if player_guess[player_counter] == secret_word[player_counter]:
        color_boxes = color_boxes + GREEN_BOX
    elif player_guess[player_counter] != secret_word[player_counter]:
        secret_bool: bool = False 
        secret_check: int = 0 
        while secret_bool == (False) and secret_check < len(secret_word):
            if player_guess[player_counter] == secret_word[secret_check]:
                secret_check = secret_check + len(secret_word) 
                secret_bool = True
            elif player_guess[player_counter] != secret_word[secret_check]:
                secret_check = secret_check + 1
        if secret_bool:
            color_boxes = color_boxes + YELLOW_BOX
        else: 
            color_boxes = color_boxes + WHITE_BOX
    player_counter = player_counter + 1
print(color_boxes)
if player_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
    exit()