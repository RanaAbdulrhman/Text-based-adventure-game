import random
import time
animal = random.choice(["cougar" , "bear" , "giant lion" , "wolf"])


def print_pause(sentence):
    print(sentence)
    time.sleep(2)


def intro():
    print_pause("you and your friends were camping in the woods..")
    print_pause("in the afternoon, you and your friend 'John' "
    "are going for a walk to explore the place..")
    print_pause("after a couple of hours, you realized that you were far away from the"
    " camp and the sun started to set..")
    print_pause("on your way back, you started hearing movement sounds "
    "not far away from you..")
    print_pause(f"when you looked back, you saw a {animal} is coming toward you..")
    print_pause("you see an abandoned hut near you..\n")


def box():
    print_pause("you find a large knife in the box,"" you takeye the knife and your friend take the board")
    print_pause(f"you go outside, attack the {animal} and defeat him")
    print_pause("congratulations you win the game..you are so brave!!")


def board():
    print_pause("you take the wooden board with you")
    print_pause(f"you go outside the cottage and attack the {animal}")
    print_pause("you were so brave but the board is so weak")
    print_pause("unfortunatlly, he defeated you.")


def continue_running():
    print_pause("you are still running even though you are very tired ")
    print_pause("you reach the camp successfully")
    print_pause("you are so persistent, you won the game!!")


def rest():
    print_pause("you and you freind are setting on a tree trunk for a while")
    print_pause("the sky is getting darker and darker")
    print_pause(f"unexpectedly, the {animal} attacks and defeats you.")
    print_pause("Unfortunately, you lost, I wish you didn't stop!")


def entering_hut():
    print_pause("you and you friend are entering the hut quickly and closing the door.")
    print_pause("you see a closed wooden box in the left and a large wooden board on the floor\n")


def hut():
    entering_hut()
    print_pause("Enter 1 to open the box \n"
    "Enter 2 to just take the wooden board\n")
    box_or_board = input("what do you want to do?(1 or 2)\n")
    if box_or_board == "1":
        box()
    elif box_or_board == "2":
        board()
    else:
        print("sorry, I don't understand")
        hut()


def run():
    print_pause("you and your friend are running as fast as you can toward the camp.")
    print_pause("the animal is following you")
    print_pause("you kept running and running")
    print_pause("after a while, you don't see him anymore\n")
    running_or_rest = input("Enter (1) to continue running\n" "Enter (2) to rest for a while\n")
    if running_or_rest == "1":
        continue_running()
    elif running_or_rest == "2":
        rest()


def getting_away():
    print_pause("Enter (1) to enter the hut \n"
    "Enter (2) to run away to the camp\n")
    hut_or_run = input("what do you want to do? (1 or 2)\n")
    if hut_or_run == "1":
        hut()

    elif hut_or_run == "2":
        run()
            
    else: 
        print("sorry, I don't understand")
        getting_away()


def play_game():
    intro()
    getting_away()
    play_again()


def play_again():
    response =  input("would you like to play again? (no,yes)\n").lower()
    if "no" in response:
        print_pause("OK, goodbye!")
    elif "yes" in response:
        print_pause("lets play again")
        play_game()
    else:
        play_again()    


play_game()  

