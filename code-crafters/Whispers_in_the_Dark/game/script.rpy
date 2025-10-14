# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

################################################################################
## Whispers In The Dark Custom Characters - Tanner 
################################################################################

#---Default Character stuff---
#This is too keep things stable incase a character is not selected
default GameCharacter = None
default current_health = 1  # This will be updated once the character is selected
default current_fortitude = 1  # This will be updated once the character is selected
#-----------------------------

default current_hotspot = None


#---First Floor Dialouge checks---
default DiaCheck_Stage_1 = False
default DiaCheck_Stage_2 = False
default DiaCheck_Stage_3 = False
default DiaCheck_Stage_4 = False
default DiaCheck_Office = False
default DiaCheck_Hidden_1 = False
default DiaCheck_Living_Room = False
default DiaCheck_Kitchen = False
default DiaCheck_Dinning = False
default DiaCheck_Garden = False
default DiaCheck_Sus_Room = False
default DiaCheck_Front_Room = False
default DiaCheck_Room_1 = False
default DiaCheck_Room_2 = False
default DiaCheck_Hidden_2 = False
#----------------------------------
#---Default First Floor Vairables--
default try_door = 0
#----------------------------------



# The game starts here.

label start:
    
    #jump First_Floor #quick jump to First Floor for testing
    #jump BS_InFront_TV
    #jump Basement #quick jump to Basement for
     
    #Show haunted house image
    scene haunted_house with fade


    # Show the character selection screen

    "Welcome to our {b}Haunted Story{b}, where you will experience {b}thrill{b}, {b}mystery{b}, and {b}terror{b} like never before."
    "Hello, player! Before starting our game, please choose the character you wish to play as."
    scene black with fade

    #into the story of how the huntaed house was created 
    scene black with fade
    pause 0.5
    scene house_scene with dissolve

    "lets get in a bit of the back story about the family "
    "Year: 1849."
    "The house at 1677 Round Top Road was constructed by Edward and Margaret Sinclair, a reclusive couple. Edward, a wealthy merchant, commissioned the estate as a grand gift for his wife."
    "Locals whispered rumors about Margaret’s family lineage—dark rituals, witchcraft—but these tales were dismissed as mere superstition. For a time, the Sinclairs lived quietly, unaware of the darkness that would soon emerge."
    scene black with fade
    pause 0.3

    scene family portrait with dissolve

    "Edward and Margaret had three children: Emily, Thomas, and the youngest, Abigail—frail from birth."
    "As you explore old corridors, you spot a dusty portrait of the family. Emily stands tall with a gentle smile, Thomas looks mischievous, and little Abigail appears delicate, almost translucent in her mother’s arms."
    "Tragedy soon befell the Sinclairs. At age seven, Abigail died under mysterious circumstances. Her passing left Margaret inconsolable, fueling the first whispers of rituals performed by candlelight."
    pause 2
    scene black with fade

    scene ritual candlelight with dissolve
    "Grief consumed Margaret. Determined to communicate with Abigail’s spirit, she delved into forbidden practices."
    "A malevolent presence answered—a spirit wearing Abigail’s face, beckoning Margaret deeper into darkness, promising a reunion if she performed certain… sacrifices."
    "Ill fortune soon claimed the rest of the family:"
    pause 1
    scene ghost_pressence with flash

    "Edward tumbled down the main staircase, Thomas drowned mysteriously, and Emily vanished without a trace."
    "Night by night, Margaret’s rituals became more desperate, her sanity unraveling."
    pause 1.2
    scene black with fade

    scene ritual candlelight with dissolve
    "Margaret ultimately sealed herself inside the house, consumed by guilt and terror. Even after her death, her anguished spirit lingered, earning the house its ominous moniker—the 'Conjuring House.'"
    "Despite the horrors, Edward, Thomas, and Emily’s spirits feel no resentment toward Margaret; they recognize her torment and the cruel manipulations of the entity masquerading as Abigail."
    "They remain trapped, yearning to free their mother—and themselves."
    scene black with fade

    scene new_family with dissolve
    "In the modern day, a new family—the Fletchers—moved into 1677 Round Top Road, unaware of its bloodstained past."
    "Within weeks, they reported vivid nightmares and surreal apparitions. The father, George Fletcher, died mysteriously soon after."
    "Terrified, the rest of the family fled, leaving the house abandoned, reinforcing its grim reputation."

    "Now it’s your turn to enter the Conjuring House. "

    scene black with fade

    call screen character_selection
    return


label start_game:
    
    #---Character initialization area---
    #set relavent character variables here
    $ char = final_character  # Use the final confirmed character, See character.rpy for class definiton
    $ current_health = char['strength'] * 10 #set health bar, dependent on character stat
    $ current_fortitude = char['fortitude'] #set fortitude bar, dependent on character stat
    show screen character_stats_hud # Show the persistent character stats HUD
    #------------------------------------
    scene bg outsidehousefog with fade

    "{b}Hello, [char['name']] !{b}" #see character.rpy for class information

    "Step into the darkness of {b}Blackwood Mansion{b}, a place where whispers call your name, shadows move on their own, and every choice could be your last."

    "Will you uncover the truth behind its sinister past, or will you become just another lost soul trapped within its walls?"

    play sound "audio/dooropen.wav" volume 0.4 fadein 0.5
    "{b}The door creaks open...{b}"
    pause 2.5

    "{b}Are you ready to begin?{b}"
    menu:
        "Yes":
            jump gameStart # this actually starts and goes into the main
        "No":
            "You are not brave enough!!" # this quits to main menu
            return


label gameStart:
    scene bg outsidehouse with fade
    play music "audio/spookymusic1.wav" volume 0.3 fadein 1.5 loop #Background music--Tanner

    if final_character == "Evelyn Carter":
        scene evelyn_entrance with fade

        "Evelyn Carter steps out of her van, clutching her grandmother’s old spirit light — a brass contraption that hums faintly in the dark."
        "The house looms before her, windows like blind eyes."
        "Her grandmother had tried to cleanse this place once. It had driven her mad."
        "Now, Evelyn has returned — not just to face the darkness, but to finish what her family started."
        
    elif final_character == "Jeremy Hardin":
        scene jeremy_entrance with fade

        "Jeremy Hardin adjusts the infrared camera on his shoulder. The red record light clicks on."
        "He’s been chasing ghost stories for years... ever since his sister disappeared inside this house."
        "Tonight, he’s not just filming. He’s hunting."
        "Not for fame — but for truth."
        

    elif final_character == "Sam Winchester":
        scene sam_entrance with fade


        "Sam Winchester lifts the trunk of the Impala. Salt rounds, EMF detector, iron rods... check."
        "He and Dean have dealt with worse, but something about this place feels wrong in his gut."
        "Visions have led him here. Something wants him inside this house — and that never ends well."
        
    elif final_character == "Dean Winchester":
        scene dean_entrance with fade


        "Dean Winchester shuts the Impala door and checks his machete. The kind that works on ghosts."
        "He’s here because an old friend — Margaret’s descendant — disappeared inside."
        "Dean’s hunted spirits before... but this house? It’s personal."
        
    elif final_character == "Michael Redwood":
        scene michael_entrance with fade
        "Michael Redwood turns on his phone flashlight, muttering curses as he steps onto the rotting porch."
        "A stupid dare. That’s all this was supposed to be."
        "Now the front door creaks open — on its own."
        "He wants to believe it’s the wind."
        
    scene bg outsidehouseexplosion with fade
    play sound "audio/scaryexplosion.mp3" volume 0.4 # FUN-EXPLOSION04.wav by newagesoup -- https://freesound.org/s/347317/ -- License: Attribution 4.0
    "{b} Wow what is that "
    play sound "outsidehousefog.wav" volume 0.4 # Woosh_Low_05.wav by moogy73 -- https://freesound.org/s/425697/ -- License: Creative Commons 0
    scene bg outsidehousefog with fade
    "You went to check for the loud bang "
    scene bg black with fade

    jump First_Floor

    return
