"""Ex02_One_shot_Worlde."""


__author__ = "730277137"

secret_word: str = ("python")
player_guess: str = (input("What is your 6-letter guess? "))

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001f7E8"

while len(player_guess) != len(secret_word):
    player_guess: str = (input(f"That was not {len(secret_word)} letters! Try again: "))
index_guess: str = (player_guess[0])
correct_letter: str = GREEN_BOX 
player_counter: int = 0
secret_counter_one: int = 0
loop_counter: int = 0
color_boxes: str = ("")
word_check : bool = False
secret_counter: int = 0
loop_secret_counter : int = 0
while player_counter < len(player_guess):
    if player_guess[player_counter] == secret_word[secret_counter_one]:
        color_boxes = color_boxes + GREEN_BOX
        player_counter = player_counter + 1
        secret_counter_one = secret_counter_one + 1
        loop_counter = loop_counter + 1
    else: 
        while word_check == False and loop_secret_counter < len(secret_word):
            if player_guess[player_counter] == secret_word[secret_counter]:
                color_boxes = color_boxes + YELLOW_BOX
                word_check = True
            elif player_guess[player_counter] != secret_word[secret_counter]: 
                secret_counter = secret_counter + 1
                loop_secret_counter = loop_secret_counter + 1
            else:
                color_boxes = color_boxes + WHITE_BOX 
                player_counter = player_counter + 1
                secret_counter = secret_counter + 1 
                loop_counter = loop_counter + 1
print(color_boxes)
if player_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
    exit()