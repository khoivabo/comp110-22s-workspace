

secret_word: str = ("python")
player_guess: str = (input(f"What is your {len(secret_word)}-letter guess? "))

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001f7E8"

index_guess: str = (player_guess[0])
correct_letter: str = GREEN_BOX 
player_counter: int = 0
secret_counter: int = 0
loop_counter: int = 0
color_boxes: str = ("")
secret_bool: bool = False 
secret_check: int = 0 

while secret_bool == (False) and secret_check < len(secret_word):
            if player_guess[player_counter] == secret_word[secret_check]:
                color_boxes = color_boxes + YELLOW_BOX
                secret_check = secret_check + len(secret_word)
                secret_bool = True
                player_counter = player_counter + 1
            else:
                while secret_check < len(secret_word):
                    secret_check = secret_check + 1
                secret_bool = True
                