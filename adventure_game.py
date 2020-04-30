import time
import random


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(2)


def intro(item, characters):
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + characters + " is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) dagger.")


def cave(item, characters):
    if "sward" in item:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all"
                    " the good stuff. It's just an empty cave"
                    " now.")
        print_pause("You walk back to the field.")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a "
                    "rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take "
                    "the sword with you.")
        print_pause("You walk back out to the field.")
        item.append("sward")
    field(item, characters)


def house(item, characters):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door "
                "opens and out steps a " + characters + ".")
    print_pause("Eep! This is the " + characters + "'s house!")
    print_pause("The " + characters + " attacks you!")
    if "sward" not in item:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
    while True:
        choice2 = input("Would you like to (1) fight or (2) "
                        "run away?")
        if choice2 == "1":
            if "sward" in item:
                print_pause("As the " + characters + " moves to attack, "
                            "you unsheath your new sword.")
                print_pause("The Sword of Ogoroth shines brightly in "
                            "your hand as you brace yourself for the "
                            "attack.")
                print_pause("But the " + characters + " takes one look at "
                            "your shiny new toy and runs away!")
                print_pause("You have rid the town of the " + characters +
                            ". You are victorious!")
            else:
                print_pause("You do your best...")
                print_pause("but your dagger is no match for the "
                            + characters + ".")
                print_pause("You have been defeated!")
            play_again()
            break
        if choice2 == "2":
            print_pause("You run back into the field. "
                        "Luckily, you don't seem to have been "
                        "followed.")
            field(item, characters)
            break


def field(item, characters):
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            house(item, characters)
            break
        elif choice1 == "2":
            cave(item, characters)
            break


def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("\nExcellent! Restarting the game ...")
        play_game()
    elif again == "n":
        print_pause("\nThanks for playing! See you next time.")
    else:
        play_again()


def play_game():
    item = []
    characters = random.choice(["wicked fairie", "pirate", "dragon", "troll","gorgon"])
    intro(item, characters)
    field(item, characters)

play_game()