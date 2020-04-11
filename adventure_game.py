import os
import time
import random
import termios
import sys


def print_pause(text, length):
    print(text)
    time.sleep(length)


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return response
        print_pause("That doesn't work, try again.", 1)


def intro():
    print_pause("The storm rages on around you. Waves throw your small"
                " ship", 2)
    print_pause("back and forth while you struggle to maintain course.", 3)
    print_pause("You've never attempted to sail through such a violent"
                " storm before,", 3)
    print_pause("but, at the time, Mother Nature seemed like a better bet"
                " than the", 3)
    print_pause("mercy of pirates.\n", 5)
    print_pause("Behind you, a loud, thunderous 'CRACK', and your"
                " stomach drops.\n", 4)
    print_pause("You look behind you just in time to see the mast"
                " of your ship", 3)
    print_pause("coming at you. There's no time to"
                " get out of the way...", 4)
    print_pause("\n\nEverything goes dark...", 5)
    print_pause("\n\nYou hear the dull roar of the ocean...", 3)
    print_pause("as you awaken to a seagull pecking at your face.", 3)
    print_pause("Suprised to still be alive, you shoo the bird away,", 3)
    print_pause("sit up, and take in your surroundings.\n", 3)


def choose_direction(directions, destinations, items):
    print_pause("\nInventory:", 0)
    print(items)
    time.sleep(.5)
    termios.tcflush(sys.stdin, termios.TCIOFLUSH)
    os.system("stty echo")
    response = valid_input("\nWhich way would you "
                           "like to go? N/S/E/W:  ", directions).lower()

    if response == "n":
        os.system("stty -echo")
        return destinations[0](items)
    elif response == "s":
        os.system("stty -echo")
        return destinations[1](items)
    elif response == "e":
        os.system("stty -echo")
        return destinations[2](items)
    elif response == "w":
        os.system("stty -echo")
        return destinations[3](items)


def ocean_1(items):
    # current_location = [0, 0]
    directions = ["n", "e"]
    destinations = [desert_1, 0, ocean_2, 0]
    print_pause("\nBeach\n", 2)
    print_pause("The ocean lies ahead. It seems like it goes on forever.\n", 2)
    random_event()
    choose_direction(directions, destinations, items)


def desert_1(items):
    # current_location = [0, 1]
    directions = ["n", "s", "e"]
    destinations = [desert_2, ocean_1, forest_1, 0]
    print_pause("\nSouthern Desert\n", 2)
    print_pause("An endless desert lies before you.\n", 2)
    random_event()
    choose_direction(directions, destinations, items)


def desert_2(items):
    # current_location = [0, 2]
    directions = ["n", "s", "e"]
    destinations = [desert_3, desert_1, road_1, 0]
    print_pause("\nDesert Road\n", 2)
    print_pause("You find yourself in a desert wasteland.\n", 2)
    print_pause("A road heads to the east.\n", 2)
    random_event()
    choose_direction(directions, destinations, items)


def desert_3(items):
    # current_location = [0, 3]
    directions = ["n", "s", "e"]
    destinations = [cliffs_1, desert_2, cliffs_2, 0]
    print_pause("\nNorthern Desert\n", 2)
    print_pause("You approach a rocky outcrop in the desert.\n", 2)
    random_event()
    if 'Bandana' not in items:
        print_pause("It seems like someone camped here recently.\nYou see a"
                    " bandana tied off to a stick in the ground\n", 2)
        print_pause("You acquired 'Bandana'\n", 2)
        items.append('Bandana')
    else:
        print_pause("There's and abandoned campsite here.\n", 2)
    choose_direction(directions, destinations, items)


def cliffs_1(items):
    # current_location = [0, 4]
    directions = ["s", "e"]
    destinations = [0, desert_3, cliffs_2, 0]
    print_pause("\nNorthern Cliffs\n", 2)
    print_pause("Tall cliffs loom above you. Their height is staggering\n", 2)
    random_event()
    choose_direction(directions, destinations, items)


def ocean_2(items):
    # current_location = [1, 0]
    directions = ["w", "n", "e"]
    destinations = [forest_1, 0, ocean_3, ocean_1]
    print_pause("\nBeach\n", 2)
    print_pause("The ocean lies before you."
                " Home is out there somewhere.\n", 2)
    random_event()
    choose_direction(directions, destinations, items)


def forest_1(items):
    # current_location = [1,1]
    directions = ["n", "s", "e", "w"]
    destinations = [road_1, ocean_2, road_4, desert_1]
    print_pause("\nSouthern Forest\n", 2)
    print_pause("You find yourself in a small forest.\n", 2)
    random_event()
    choose_direction(directions, destinations, items)


def road_1(items):
    # current_location = [1,2]swamp_2
    directions = ["n", "s", "e", "w"]
    destinations = [forest_2, forest_1, road_5, desert_2]
    print_pause("\nWestern Road\n", 2)
    print_pause("The road continues to the east and west.\n", 2)
    random_event()

    choose_direction(directions, destinations, items)


def forest_2(items):
    # current_location = [1,3]
    directions = ["n", "s", "e", "w"]
    destinations = [cliffs_2, road_1, road_2, desert_3]
    print_pause("\nNorthern Forest\n", 2)
    print_pause("You find yourself in the middle of a dark forest.\n", 2)
    random_event()
    choose_direction(directions, destinations, items)


def cliffs_2(items):
    # current_location = [1,4]
    directions = ["s", "e", "w"]
    destinations = [0, forest_2, hut_1, cliffs_1]
    print_pause("\nNorthern Cliffs\n", 2)
    print_pause("Tall cliffs loom above you. Just"
                " looking up at them makes you dizzy.\n", 2)
    random_event()
    choose_direction(directions, destinations, items)


def ocean_3(items):
    # current_location = [2,0]
    directions = ["n", "e", "w"]
    destinations = [road_4, 0, ocean_4, ocean_2]
    print_pause("\nBeach Road\n", 2)
    print_pause("There's the ocean. A flock of seagulls flies overhead,\n"
                "and a road leads northward", 2)
    random_event()
    choose_direction(directions, destinations, items)


def road_4(items):
    # current_location = [2,1]
    directions = ["n", "s", "e", "w"]
    destinations = [road_5, ocean_3, swamp_1, forest_1]
    print_pause("\nSouthern Road\n", 2)
    print_pause("You see a broken-down wagon."
                " The road continues to the north and south.\n", 2)
    if 'Torch' not in items:
        print_pause("You scour around the wreckage and"
                    " manage to find a torch.\n", 2)
        print_pause("You acquired 'Torch'\n", 2)
        items.append('Torch')
    else:
        print_pause("There's nothing else useful to find here\n", 2)
    random_event()
    choose_direction(directions, destinations, items)


def road_5(items):
    # current_location = [2, 2]
    directions = ["n", "s", "e", "w"]
    destinations = [road_2, road_4, road_3, road_1]
    print_pause("\nCrossroads\n", 2)
    print_pause("You are at a crossroads...\n", 2)
    random_event()
    choose_direction(directions, destinations, items)


def road_2(items):
    # current_location = [2,3]
    directions = ["n", "s", "e", "w"]
    destinations = [hut_1, road_5, swamp_2, forest_2]
    print_pause("\nNorthern Road\n", 2)
    print_pause("You are on the road."
                " It continues to the north and south.\n", 2)
    random_event()
    choose_direction(directions, destinations, items)


def hut_1(items):
    # current_location = [2,4]
    directions = ["n", "s", "e", "w"]
    destinations = [hut_2, road_2, cliffs_3, cliffs_2]
    print_pause("\nWitch's Hut\n", 1)
    print_pause("You see a small hut to the north."
                " A sign says 'Granny Weatherwax: Witch'\n", 2)
    print_pause("a road leads to the south\n", 2)
    random_event()
    choose_direction(directions, destinations, items)


def hut_2(items):
    # current_location = [2, 5]
    directions = ["s"]
    destinations = [0, hut_1, 0, 0]
    print_pause("\nWitch's Hut Interior\n", 1)
    print_pause("You are in the witch's hut\n", 2)
    if 'Stinky Mushroom' not in items:
        if 'Gloves' not in items:
            termios.tcflush(sys.stdin, termios.TCIOFLUSH)
            os.system("stty echo")
            print_pause("   'Well you're a new face! Do you think"
                        " you could help a little old lady?'", 2)
            choice = valid_input("\nY/N\n", ["y", "n"])
            if choice == "n":
                os.system("stty -echo")
                print_pause("'Well then get the hell out of my hut!'", 2)
                print_pause("She teleports you away,"
                            " leaving your items behind.", 3)
                items.clear()
                cave_2(items)
            elif choice == "y":
                os.system("stty -echo")
                print_pause("\n   'Oh Goody!'\n", 2)
                print_pause("   'There is a mushroom in a "
                            "cave past the swamp to\n"
                            "    the east that I need to "
                            "craft a special potion.'\n", 3)
                print_pause("   'I would go myself but"
                            " the place smells like hell,\n "
                            "   its pitch black in there,"
                            " and there's a nasty "
                            "troll\n    who has moved in!'\n", 3.5)
                print_pause("   'If you help me get it I "
                            "can magic you home!'\n\n", 4)
                print_pause("   'By the way, mushroom is "
                            "poisonus to the touch, \n"
                            "    take these gloves with you!'", 2)
                items.append('Gloves')
                print_pause("\n\nYou acquired 'Gloves'\n", 2)
                hut_2(items)
        elif 'Troll Tooth' not in items:
            print_pause("Granny Weatherwax says,\n\n   'By the way...'\n\n", 3)

            if 'Bandana' not in items:
                print_pause("   'You'll need something to help"
                            " you breathe in the swamp'\n", 2)
            else:
                print_pause("   'That Bandana should help you"
                            " get through the stench in the swamp'\n", 2)
            if 'Torch' not in items:
                print_pause("   'You'll need some way to see"
                            " in the cave, it is very dark'\n", 2)
            else:
                print_pause("   'That torch should help"
                            " you see in the cave.'\n", 2)
            if 'Sword' not in items:
                print_pause("   'You'll need some way to fight that troll. "
                            "They can be very dangerous'\n", 2)
                if 'Torch' not in items:
                    print_pause("   'I've also heard that"
                                " trolls don't like fire'\n", 2)
            else:
                print_pause("   'I hope you know how to use that sword,"
                            " you'll need it to defeat the troll!'\n", 2)
        else:
            print_pause("   'Oh goody, you got rid of that nasty troll'", 2)
        choose_direction(directions, destinations, items)
    else:
        print_pause("   'Oh goody! My mushroom!!'", 2)
        print_pause("   'Thank you so much!!'\n\n", 8)
        print_pause("\n\n   'Oh you're still here? Off you go!'", 3)
        print_pause("\nYou made it home! Congratulations!\n\n", 2)
        replay()

    choose_direction(directions, destinations, items)


def ocean_4(items):
    # current_location = [3,0]
    directions = ["n", "e", "w"]
    destinations = [swamp_1, 0, cliffs_4, ocean_3]
    print_pause("\nBeach\n", 2)
    print_pause("You find the wreckage of you ship."
                "  You were lucky to survive!\n", 2)
    random_event()
    choose_direction(directions, destinations, items)


def swamp_1(items):
    # current_location = [3,1]
    directions = ["n", "s", "e", "w"]
    destinations = [road_3, ocean_4, cliffs_5, road_4]
    print_pause("\nSouthern Swamp\n", 2)
    print_pause("A dense fog clings to the boggy ground in the swamp\n", 2)
    random_event()
    if 'Bandana' not in items:
        print_pause("It reeks here\n", 2)
    elif 'Troll Tooth' not in items:
        print_pause("\nYou feel like something is watching you.\n", 2)
    choose_direction(directions, destinations, items)


def road_3(items):
    # current_location = [3,2]
    directions = ["n", "s", "e", "w"]
    destinations = [swamp_2, swamp_1, cave_1, road_5]
    print_pause("\nEastern Road\n", 2)
    print_pause("You are on the road. It continues to the east and west.\n", 2)
    random_event()
    if 'Bandana' not in items:
        print_pause("Something stinks.\n", 2)
    if 'Troll Tooth' not in items:
        print_pause("\nYou feel like something is watching you.\n", 2)
    choose_direction(directions, destinations, items)


def swamp_2(items):
    # current_location = [3,3]
    directions = ["n", "s", "e", "w"]
    destinations = [cliffs_3, road_3, cliffs_6, road_2]
    print_pause("\nNorthern Swamp\n", 2)
    print_pause("A noxious swamp stands before you.\n", 2)
    random_event()
    if 'Sword' not in items:
        print_pause("\nYou see a faint glimmer of metal"
                    " in a shallow part of the water\n", 2)
        print_pause("You acquired 'Sword'\n", 2)
        items.append('Sword')
    if 'Bandana' not in items:
        print_pause("An unpleasent stench hangs the in air.\n", 2)
    if 'Troll Tooth' not in items:
        print_pause("\nYou feel like something is watching you.\n", 2)
    choose_direction(directions, destinations, items)


def cliffs_3(items):
    # current_location = [3,4]
    directions = ["s", "e", "w"]
    destinations = [0, swamp_2, cliffs_7, hut_1]
    print_pause("\nNorthern Cliffs\n", 2)
    print_pause("Tall cliffs loom above you.\n", 2)
    random_event()
    choose_direction(directions, destinations, items)


def cliffs_4(items):
    # current_location = [4, 0]
    directions = ["n", "w"]
    destinations = [cliffs_5, 0, 0, ocean_4]
    print_pause("\nSouthern Cliffs\n", 2)
    print_pause("Sheer cliffs meet the ocean in a"
                " breathtaking display of nature.\n", 2)
    random_event()
    choose_direction(directions, destinations, items)


def cliffs_5(items):
    # current_location = [4, 1]
    directions = ["n", "s", "w"]
    destinations = [cave_1, cliffs_4, 0, swamp_1]
    print_pause("\nEastern Cliffs", 2)
    print_pause("Tall cliffs loom above you.\n", 2)
    random_event()
    if 'Bandana' not in items:
        print_pause("A rancid stench wafts from the north\n", 2)
    elif 'Troll Tooth' not in items:
        print_pause("\nYou feel like something is watching you.\n", 2)
    choose_direction(directions, destinations, items)


def cave_1(items):
    # current_location = [4, 2]
    directions = ["n", "s", "e", "w"]
    destinations = [cliffs_6, cliffs_5, cave_2, road_3]
    print_pause("\nDark Cave\n", 1)
    print_pause("You see a dark misty cave ahead.\n", 2)
    if 'Bandana' not in items:
        print_pause("The smell here is overwhelming"
                    " and you have to turn back\n", 2)
        road_3(items)
    else:
        print_pause("Your Bandana manages to mitigate"
                    " the stench enough for you to continue\n", 2)
    if 'Troll Tooth' not in items:
        print_pause("\nYou feel like something is watching you.\n", 2)
        if 'Torch' not in items:
            print_pause("It looks dark in there. "
                        "Better find something to light the way.\n", 2)
        else:
            print_pause("It looks dark in there. "
                        "Good thing you found that torch!\n", 2)

    choose_direction(directions, destinations, items)


def cliffs_6(items):
    # current_location = [4, 3]
    directions = ["n", "s", "w"]
    destinations = [cliffs_7, cave_1, 0, swamp_2]
    print_pause("\nEastern Cliffs\n", 2)
    print_pause("Tall cliffs loom above you.\n", 2)
    random_event()
    if 'Bandana' not in items:
        print_pause("a rancid stench wafts from the south\n", 2)
    elif 'Troll Tooth' not in items:
        print_pause("\nYou feel like something is watching you.\n", 2)
    choose_direction(directions, destinations, items)


def cliffs_7(items):
    # current_location = [4, 4]
    directions = ["s", "w"]
    destinations = [0, cliffs_6, 0, cliffs_3]
    print_pause("\nEastern Cliffs\n", 1)
    print_pause("Tall cliffs loom above you.\n", 2)
    random_event()
    choose_direction(directions, destinations, items)


def cave_2(items):
    # current_location = [5, 2]
    directions = ["w"]
    destinations = [0, 0, 0, cave_1]
    print_pause("\nDark Cave Interior\n", 2)
    print_pause("A dank miasma fills the cave\n", 2)
    if 'Troll Tooth' not in items:
        print_pause("Out from nowhere a giant troll"
                    " appears and lunges at you!\n", 2.5)
        if 'Sword' not in items:
            print_pause("You are totally helpless"
                        " with no way to defend yourself", 2.5)
            print_pause("One big crunch and your lights go out...", 4)
            replay()
        else:
            print_pause("In an instant you draw "
                        "your sword to defend yourself!\n", 2.5)
            print_pause("The troll wasn't expecting armed prey! You manage to"
                        " stab\nhim as he lunges at you.\n", 2.5)
            print_pause("The troll howls in pain!\n", 2.5)
            print_pause("He seems to be regenerating! Oh no!\n", 4)
            if 'Torch' not in items:
                print_pause("After a long battle of "
                            "attrition the troll\ngets the better of you", 2.5)
                print_pause("\nOne big crunch and your lights go out...", 4)
                replay()
            else:
                print_pause("Thinking quickly, you shove "
                            "your torch into the trolls face\n", 2.5)
                print_pause("That did the trick! The troll bursts into flames"
                            " and falls \nlifelessly to the ground\n", 2.5)
                print_pause("You decide to take a tooth as a souveneir\n", 5)
                print_pause("You acquired 'Troll Tooth'\n", 2.5)
                items.append('Troll Tooth')
                cave_1(items)
    elif 'Stinky Mushroom' not in items:
        print_pause("Your Torch lights the way\n", 2)
        if 'Gloves' not in items:
            print_pause("You see giant, stinky mushroom\n", 2)
        else:
            print_pause("You see giant, stinky mushroom."
                        " This must be the one the witch wanted.\n", 2)
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)
        os.system("stty echo")
        choice = valid_input("Pick it? Y/N\n", ["y", "n"])
        if choice == "y" and 'Gloves' not in items:
            os.system("stty -echo")
            print_pause("You immediately regret your decision.\n You start to "
                        "feel sick and your vision starts to fade away...", 3)
            replay()
        elif choice == "y" and 'Gloves' in items:
            os.system("stty -echo")
            print_pause("You carefully harvest the "
                        "dangerous mushroom for the witch\n", 2)
            print_pause("You acquired 'Stinky Mushroom'\n", 2)
            items.append('Stinky Mushroom')
        elif choice == "n" and 'Gloves' not in items:
            print_pause("Good call, that thing looks dangerous\n", 2)
        elif choice == "n" and 'Gloves' in items:
            print_pause("Well, the witch is waiting...\n", 2)
            cave_1(items)
    choose_direction(directions, destinations, items)


def random_event():
    events = ["You trip and fall as you are walking. Ouch.", "A strong gust "
              "of wind from the south nearly knocks you down", "You gaze "
              "skyward and see a cloud that looks like a bunny rabbit. Neat.",
              "You stumble across the half-eaten body of a goblin.\nAnd you "
              "thought you were having a bad day!", "A family of deer scatter "
              "as you approach.", "It's raining.", "You gaze skyward and catch"
              " a glimpse of the most enormous bird you've ever seen.\nIt must"
              " have a nest in the cliffs", "You hear a loud 'THUD' from the "
              "north.  Watch out for falling rocks!", "The sun is shining",
              "It is overcast", "The air feels still", "You wonder how your "
              "friends are doing back home. Gotta make it back!", "You think"
              " back to the pirates who chased you into the storm.\nBastards!"
              " This is all their fault!", "Ethereal laughter echos all around"
              " you.  Was that real? Or just in your head?", "You hear a small"
              " critter scamper away, but you didn't catch a glimpse of it.",
              "A hot, dry wind breeze blows from the west.", "You could really"
              " go for a drink right about now.", "Just where the hell is this"
              " place anyway?", "It is eerily quiet", "The air feels heavy",
              "It seems like someone has been here recently", "The songs of"
              " the birds make music to your ears.", "You sneeze. 'ACHOO'.",
              "You hear footsteps behind you, but when you turn"
              " around\nno one seems to be there. Gotta get out of here!",
              "You whistle a melody to pass the time. After a few minutes\nyou"
              " notice something is harmonizing with you. Creepy.", "You"
              " feel a draft across your bum. \nMust've ripped a hole in your "
              "pants during the wreck. Great.", ""]
    random.shuffle(events)
    print_pause(random.choice(events), 2.5)


def play_game():
    os.system('clear')
    os.system("stty -echo")
    items = []
    start_loc_list = [ocean_1, ocean_2, ocean_3, ocean_4]
    intro()
    # hut_1(items)
    random.choice(start_loc_list)(items)


def replay():
    os.system("stty echo")
    choice = valid_input("\nWould you like to play again? y/n\n", ["y", "n"])
    yes_list = ["Yeehaw!", "Oh no not again!", "Lets do this!",
                "One more turn!", "Why does this keep happening to me?"]
    if choice == "y":
        print_pause(random.choice(yes_list), 3)
        play_game()
    elif choice == "n":
        print_pause("Get me out of here!", 1)
        print_pause("Thanks for playing!", 1)
        sys.exit()

if __name__ == '__main__':
    play_game()
