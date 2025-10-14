    # ALL First Floor Stages  FF == FIRST FLOOR
    # Labels start with this format ---->  FLOOR_ROOM_NAME
    # Please use this format here for consistency, use the same format where ever you call this

label First_Floor:
    play sound "audio/lockeddoor.wav"
    "{i}The front door locks behind you"
    show screen navigation_button #Display persisten navigation menu    
    jump FF_Stage_1
    ###---STAGES---###

    label FF_Stage_1:
        $ current_room = "FF_Stage_1"
        show screen minimap(current_room=current_room)
        #Dialogue Check: Declare default DiaCheck_Stage_1 = False at the top of script.rpy

        scene bg ff_stage_1
        if try_door != 0:
            play sound "audio/lockeddoor.wav" volume 0.4 fadein 0.5
            if try_door == 1:
                "The Front Door is locked...And the handle is cold..."
            elif try_door == 2:
                "The Front Door is still locked!"
            elif try_door == 3:
                "Yep...still locked"
            elif try_door == 4:
                "I either need a key or a hammer to get the door open..."
            else:
                $ exclamation = "!" * (try_door - 4)  # Adds an exclamation mark for each attempt after the 4th
                "The door remains locked[exclamation]" # String formatting for concatenation

        if DiaCheck_Stage_1: #This dialogue will appear evertime the player enters EXCEPT for the first time
            "Back at the front door..."
            "Nothing new here"
        elif not DiaCheck_Stage_1: #This dialoge will appear ONLY THE FIRST TIME the player enters it
            "WHAT ON EARTH WAS THAT!?"
            "WAS THAT MAGIC?"
            "Does an angry wizard live here?"
            "Whoever or Whatever is running this place seems to have some unnatural abilities"
            "{i}You examine the room around you"
            "{i}The home is cold and dirty..."
            "{i}You observe a welded bead of metal around the perimeter of the door"
            "{i}The door shows no signs of opening...not by your hands at least"
            "Teleported inside just to have the door locked behind me"
            "This angry wizard is playing a strange game with me"
            "I will have to find another way out."
            "Where should I begin?"
            $ DiaCheck_Stage_1 = True #Set DiaCheck to True once all the dialogue has been read!




        $ renpy.pause(hard=True) #prevents player from clicking to advance room with out using navigation menu
        #this will likely cause some problems and will need to be reworked

        
    label FF_Stage_2:
        scene bg ff_stage_2 with fade
        $ current_room = "FF_Stage_2"
        show screen minimap(current_room=current_room)

        if DiaCheck_Stage_2:
            "Nothing new here"
        elif not DiaCheck_Stage_2:
            "Living room on the right..."
            "Kitchen dead ahead..."
            "Hallway on the right..."
            "Where to go?"
            $ DiaCheck_Stage_2 = True
        
        $ renpy.pause(hard=True) #prevents player from clicking to advance room with out using navigation menu
        #this will likely cause some problems and will need to be reworked
  
    
    label FF_Stage_3:
        scene bg ff_stage_3 with fade
        $ current_room = "FF_Stage_3"
        show screen minimap(current_room=current_room)

        if DiaCheck_Stage_3:
            "Nothing new here"
        elif not DiaCheck_Stage_3:
            "A long dark hallway"
            "Maybe one of these rooms has somthing usefull"
            $ DiaCheck_Stage_3 = True

        $ renpy.pause(hard=True) #prevents player from clicking to advance room with out using navigation menu
        #this will likely cause some problems and will need to be reworked

    label FF_Stage_4:
        scene bg ff_stage_4 with fade
        $ current_room = "FF_Stage_4"
        show screen minimap(current_room=current_room)

        if DiaCheck_Stage_4:
            "Nothing new here"
        elif not DiaCheck_Stage_4:
            "I guess this hallway does end..."
            "Kitchen on the right..."
            "And a large room on the left"
            $ DiaCheck_Stage_4 = True

        $ renpy.pause(hard=True) #prevents player from clicking to advance room with out using navigation menu
        #this will likely cause some problems and will need to be reworked

    
    ###---ROOM LABELS---###
    label FF_Office:
        $ current_room = "FF_Office"
        show screen minimap(current_room=current_room)
        if bsfoundentrykey:
            scene bg ff_office with fade
        else:
            scene bg ffofficekey with fade          # <a href="https://www.vecteezy.com/free-png/virtual">Virtual PNGs by Vecteezy</a>
        
        if DiaCheck_Office:
            "Nothing new here"
        elif not DiaCheck_Office:
            "Looks like a study room"
            "Maybe i can find somthing helpful"
            $ DiaCheck_Office = True

        if not bsfoundentrykey:
            #scene bg FF_Office1_key
            $ current_hotspot = None    ## MUST CALL THIS BEFORE THE START OF THE MINI GAME
            # Define interactive hotspots in this scene
            $ bsclosetstorage_hotspots = [
                {
                    "area": (1127, 884, 93, 103),                                                                            # custom area of the highlited part on the image
                    "label": "FF_Hidden_1_Key_Get",                                                                                 # default label of the mini game 
                    "tooltip": "Pick up the key",                                                                # custom tool tip on the image
                    "image": "Basement/minigames/bsmgbicep.png",                                                             # custom image for the mini game
                    "win_txt": "This looks like a key that could unlock the basement",   # custom win txt
                    "win_lose_exit_label": "FF_Office",                                                                 # custom win, exit or leave label, label when user finishes the mini game
                    "state_var": "bsfoundentrykey"                                                                      # your custom variable you want to flip when user wins the mini game     # 
                },
                # add more here
            ]

            show screen hotspot_overlay(bsclosetstorage_hotspots)
        
        call screen bookshelf_screen
            
        $ renpy.pause(hard=True) #prevents player from clicking to advance room with out using navigation menu
        #this will likely cause some problems and will need to be reworked
    
    label FF_Hidden_1:
        #scene bg ff_hidden_1 with fade
        $ current_room = "FF_Hidden_1"
        show screen minimap(current_room=current_room)

        if DiaCheck_Hidden_1:
            scene bg ff_hidden_1 with fade
            "Nothing new here"
        elif not DiaCheck_Hidden_1:
            scene bg ff_hidden_1 with fade
            "A Hidden room!!"
            "A Hidden room must have secrets..."
            "Just have to find them"
            $ DiaCheck_Hidden_1 = True




        $ renpy.pause(hard=True) #prevents player from clicking to advance room with out using navigation menu
        #this will likely cause some problems and will need to be reworked


    label FF_Stairs_Up:
        $ current_room = "FF_Stairs_Up"

        #ADD JUMP TO UP STAIRS
        $ renpy.pause(hard=True) #prevents player from clicking to advance room with out using navigation menu
        #this will likely cause some problems and will need to be reworked

    label FF_Living_Room:
        scene bg ff_living with fade
        $ current_room = "FF_Living_Room"
        show screen minimap(current_room=current_room)
        
        if DiaCheck_Living_Room:
            "Nothing new here"
        elif not DiaCheck_Living_Room:
            "Not a lot of living in the {i}living room"
            "I like my living rooms to have large TV's"
            "This place is all buisness..."
            $ DiaCheck_Living_Room = True
            call screen locket_image
            
        $ renpy.pause(hard=True) #prevents player from clicking to advance room with out using navigation menu
        #this will likely cause some problems and will need to be reworked
    
    label FF_Kitchen:
        scene bg ff_kitchen with fade
        $ current_room = "FF_Kitchen"
        show screen minimap(current_room=current_room)

        if DiaCheck_Kitchen:
            "Nothing new here"
        elif not DiaCheck_Kitchen:
            "Wonder whats cooking in the kitchen.."
            "Time to raid the pantry"
            $ DiaCheck_Kitchen = True

        $ renpy.pause(hard=True) #prevents player from clicking to advance room with out using navigation menu
        #this will likely cause some problems and will need to be reworked


    label FF_Dinning:
        scene bg ff_dinning with fade
        $ current_room = "FF_Dinning"
        show screen minimap(current_room=current_room)

        if DiaCheck_Dinning:
            "Nothing new here"
        elif not DiaCheck_Dinning:
            "Dang! Nice dinning room."
            "Why is it so neat?"
            "Why is the table set?"
            "This place looks oddly untouched"
            $ DiaCheck_Dinning = True

        $ renpy.pause(hard=True) #prevents player from clicking to advance room with out using navigation menu
        #this will likely cause some problems and will need to be reworked

    label FF_Garden:
        scene bg ff_garden with fade
        $ current_room = "FF_Garden"
        show screen minimap(current_room=current_room)

        if DiaCheck_Garden:
            "Nothing new here"
        elif not DiaCheck_Garden:
            "Nothing good can be growing here"
            "I cant help but feel like im being watched"
            "That probably means im heading in the right direction"
            $ DiaCheck_Garden = True

        $ renpy.pause(hard=True) #prevents player from clicking to advance room with out using navigation menu
        #this will likely cause some problems and will need to be reworked


    label FF_Sus_Room: ##Suspicious room
        scene bg ff_sus with fade
        $ current_room = "FF_Sus_Room"
        show screen minimap(current_room=current_room)

        if DiaCheck_Sus_Room:
            "Nothing new here"
        elif not DiaCheck_Sus_Room:
            "This is a suspicous room..."
            "The candles are lit!"
            "Someone was here...recently"
            $ DiaCheck_Sus_Room = True


        $ renpy.pause(hard=True) #prevents player from clicking to advance room with out using navigation menu
        #this will likely cause some problems and will need to be reworked


    label FF_Front_Room:
        scene bg ff_front_room with fade
        $ current_room = "FF_Front_Room"
        show screen minimap(current_room=current_room)

        if DiaCheck_Front_Room:
            "Nothing new here"
        elif not DiaCheck_Front_Room:
            "Plenty of stuff to look at here..."
            $ DiaCheck_Front_Room = True

        $ renpy.pause(hard=True) #prevents player from clicking to advance room with out using navigation menu
        #this will likely cause some problems and will need to be reworked


    label FF_Room_1:
        scene bg ff_room_1 with fade
        $ jumpscare("HauntingGhost","audio/bstvjumpscare.wav") #popup, will add fortitude/health reduction
        $ current_room = "FF_Room_1"
        show screen minimap(current_room=current_room)

        if DiaCheck_Room_1:
            "Nothing new here"
        elif not DiaCheck_Room_1:
            "WHAT WAS THAT!?"
            "That definetly was not a wizard..."
            "What is going on in this place?"
            "Guess I would be grumpy too if this was my bedroom..."
            $ DiaCheck_Room_1 = True
            call screen bookshelf_thomasscreen


        $ renpy.pause(hard=True) #prevents player from clicking to advance room with out using navigation menu
        #this will likely cause some problems and will need to be reworked


    label FF_Room_2:
        scene bg ff_room_2 with fade
        $ current_room = "FF_Room_2"
        show screen minimap(current_room=current_room)

        if DiaCheck_Room_2:
            "Nothing new here"
        elif not DiaCheck_Room_2:
            "Wow...Cozy"
            $ DiaCheck_Room_2= True

        $ renpy.pause(hard=True) #prevents player from clicking to advance room with out using navigation menu
        #this will likely cause some problems and will need to be reworked

    
    label FF_Hidden_2:
        scene bg ff_hidden_2 with fade
        $ current_room = "FF_Hidden_2"
        show screen minimap(current_room=current_room)

        $ renpy.pause(hard=True) #prevents player from clicking to advance room with out using navigation menu
        #this will likely cause some problems and will need to be reworked

