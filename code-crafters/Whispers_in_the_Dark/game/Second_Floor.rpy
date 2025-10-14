###--- script.rpy ---###

label Second_Floor:
    "You step onto the creaky wooden floor, shadows flickering from unseen candlelight."
    show screen navigation_button
    jump SF_Hallway

label SF_Hallway:
    $ current_room = "SF_Hallway"
    hide screen minimap
    scene bg hallway with fade

    if not sf_Hallway_seen:
        "You are in the hallway of the second floor.\nFaint whispers and the sound of creaking fills the air."
        $ sf_Hallway_seen = True
    else:
        "You're back in the second floor hallway. The whispers still echo faintly."

    $ renpy.pause(hard=True)
    show screen navigation_button
    return

label SF_Stage_2:
    $ current_room = "SF_Stage_2"
    scene bg hallway2 with fade
    "You walk further down the hallway.\nThe floorboards groan underfoot, and the walls seem to close in slightly."
    $ renpy.pause(hard=True)
    show screen navigation_button
    return

label SF_Master_Bedroom:
    $ current_room = "SF_Master_Bedroom"
    scene bg master_bedroom
    "You enter the master bedroom. The air is thick and cold, and something feels terribly off."
    $ renpy.pause(hard=True)
    show screen navigation_button
    return

label SF_Nursery:
    $ current_room = "SF_Nursery"
    scene bg nursery
    "You enter the abandoned nursery. The air smells musty, and the dolls' eyes seem to follow you."
    $ renpy.pause(hard=True)
    show screen navigation_button
    return

label SF_Library:
    $ current_room = "SF_Library"
    $ ritual_entry_point = "library"
    scene bg dusty_library
    "You step inside the dusty library. Cobwebs hang from the shelves, and ancient books line the walls."
    $ renpy.pause(hard=True)
    show screen navigation_button
    return

label SF_Hidden_Library:
    $ current_room = "SF_Hidden_Library"
    $ ritual_entry_point = "library"
    scene bg hidden_library
    "As you touch the bookshelves, it suddenly jolts. Revealing a hidden passage that leads somewhere."
    $ renpy.pause(hard=True)
    show screen navigation_button
    return

label SF_Study:
    $ current_room = "SF_Study"
    scene bg locked_study

    if not study_unlocked:
        "It's called a locked study for a reason!!"
        menu:
            "Use key":
                if has_study_key:
                    "You insert the old key and hear a satisfying click."
                    $ study_unlocked = True
                    jump SF_Study
                else:
                    "You don’t have the key."
                    jump SF_Stage_2
            "Leave":
                jump SF_Stage_2
    else:
        "The door creaks open as you enter the study."
        $ renpy.pause(hard=True)
        show screen navigation_button
        return

label SF_Hidden_Study:
    $ current_room = "SF_Hidden_Study"
    $ ritual_entry_point = "study"
    scene bg hidden_study
    "You find a secret compartment behind the bookshelf. It reveals a dusty journal and old trinkets."
    $ renpy.pause(hard=True)
    show screen navigation_button
    return

label SF_Ritual_Chamber:
    $ current_room = "SF_Ritual_Chamber"
    scene bg ritual_chamber
    "You enter a ritual chamber...\nWhispers grow louder as you step further in.
    Strange symbols cover the floor, and the air is thick with incense."
    $ renpy.pause(hard=True)
    show screen navigation_button
    return

label SF_Balcony:
    $ current_room = "SF_Balcony"
    scene bg balcony with fade
    "You step out onto the grand balcony.\nIt's a beautiful sight... but something's off."
    $ renpy.pause(hard=True)
    show screen navigation_button
    return

label look_down_event:
    "You look over the balcony, it's almost a beautiful sight..."
    "Suddenly... You feel a hard shove."
    jump death_scene

label death_scene:
    scene bg falling
    "As you leap from the balcony, a chilling scream fills the air."
    "Your vision goes black as you hit the cold, hard floor below."
    scene bg dead
    "{b}You Died.{/b}"
    jump return_game_over

label return_game_over:
    "Would you like to try again?"
    menu:
        "Yes, restart the game.":
            jump start_game
        "No, quit to the main menu.":
            return
