label Basement:
    if not bsfoundentrykey:
        show screen navigation_button
        play sound "audio/bsdmaindoorlocked.wav" volume 0.4             # Door_Locked_01.wav by skyumori -- https://freesound.org/s/104530/ -- License: Creative Commons 0
        "Look around the first floor to find the basement key"
        $ renpy.pause(2.5, hard=True)
        jump FF_Stage_1
        

    elif bsfoundentrykey:
        show screen navigation_button
        jump BS_Stage_1

    
# ALL Basement Stages  BS == BASEMENT
# Labels start with this format ---->                          BS_Xyz_Abc
# Please use this format here for consistency, use the same format where ever you call this

# call this label to clear all mini games and other screen elements expect navigaiton sys
label bsmgscreens:
    hide screen fifteen_scr
    hide screen hotspot_overlay
    hide screen full_image
    hide screen pong
    hide screen clicker
    hide screen click_chest
    hide screen pick_choose
    hide screen lockpicking
    hide screen temp_screen
    hide screen main_game
    hide screen gamez_over

    return 


# Default main stage of basement
label BS_Stage_1:
    $ current_room = "BS_Stage_1"
    show screen minimap(current_room=current_room)
    scene bg bsstairway with fade
    if Bs_Diachk_Stage_1:       # Dialouge for after viewing this place == FIRST TIME
        "Here in the basement floor"
        "Basement Stairway"

    elif not Bs_Diachk_Stage_1:       # Dialouge for viewing this place => SECOND TIME
        "What is this place? It feels like I've stepped into another world..."
        "{i}The stench is overpowering—dank, musty, and filled with decay...{/i}"
        "This must be the basement. Every step echoes like a forgotten memory."
        "{i}It seems no soul has set foot here for ages...{/i}"
        "I need to search every dark corner for something—anything—that can lead me out of this cursed maze."
        $ Bs_Diachk_Stage_1 = True
        jump BS_Stage_1

    "Basement Stairway"
    $ renpy.pause(hard=True)

# ALl stff is bottom right of the map
label BS_Under_Stairway:
    $ current_room = "BS_Under_Stairway"
    show screen minimap(current_room=current_room)
    if not bswall_broken and not bs_Diadchlwalltalked:
        scene bg bsunderstairway with fade
        if not bs_Diachk_bswall_broken and not bsfound_hammer:     # Dialouge for after viewing this place == FIRST TIME and hammer not found and wall not broken
            "So this is the underside of the stairs... It's cramped, dark, and reeks of mold."
            "{i}I can barely stand up straight. Everything about this place feels wrong...{/i}"
            "There's a slight stench of {b}BODIES{/b} here. Strange... Where is it coming from?"
            "The bricks in the center look repaired, like it's been patched up hastily."
            "{b}Could it be hollow?{/b}"
            "{i}If there's something behind it, it might lead me out of this nightmare—or deeper into it.{/i}"
            "I need to see if I can break through... but I'll have to be careful. No telling what's on the other side."
            "I'd have to find a hammer or something that will let me break this brick wall"
            $ bs_Diadchlwalltalked = True
            $ bs_Diachkseen_bswall_broken = True
            jump BS_Under_Stairway
    elif bs_Diachkseen_bswall_broken and not bsfound_hammer:        # Dialouge for viewing this place => SECOND TIME but player has not found hammer basically left the room and came back
        scene bg bsunderstairway with fade
        "Ah, still can't do anything here, I will have to find something to break this wall"
        "Under the Basement Stairway"
    elif bsfound_hammer:
        if bswall_broken:
            scene bg bsbrokenwall with fade
        elif not bswall_broken:
            scene bg bsunderstairway with fade
    elif not bsfound_hammer:
            if bswall_broken:
                scene bg bsbrokenwall with fade
            elif not bswall_broken:
                scene bg bsunderstairway with fade
    if not bs_Diachk_bswall_broken and bsfound_hammer and not bswall_broken:     # Dialouge for viewing this place => SECOND TIME player has found hammer but not broken wall yet
        "Ah ha! Finally, I have found the hammer. Now I can get through this brick wall."
        $ bs_Diachk_bswall_broken = True

    elif bswall_broken and bs_Diachk_bswall_broken and not bs_Diachkseen_bswall_broken_talked:  # Dialouge for viewing this place => SECOND TIME player has found hammer and broke the wall
        "With the hammer clutched in my hand, I take a deep breath and swing with all my might..."
        "Each strike reverberates through the silence, sending clouds of dust and debris into the air."
        "{i}I'm almost through...{/i}"
        "At last, the wall shudders and crumbles, revealing a gaping hole."
        scene bg bsbrokenwall with fade
        "A faint red glow seeps through the gap, growing steadily more intense."
        "{b}What on earth...?{/b}"
        "I edge closer, my heart pounding in my ears. Beyond the rubble lies a narrow, mysterious passage pulsing with an eerie light."
        "{i}I can't say what's waiting for me... but I've come too far to turn back now.{/i}"
        play sound "audio/bsbrokenwallwhisper.wav" volume 0.5
        "I hear something very faintly"
        "{b} WHAT THE HELL WAS THAT"
        $ bs_Diachkseen_bswall_broken_talked = True
        jump BS_Under_Stairway

    elif bswall_broken and bs_Diachkseen_bswall_broken_talked:  # hammer found and wall broken just a text that says where the player is
        "Under the basement Stairway"
    
    $ renpy.pause(hard=True)


label BS_Torture_Chamber:
    call bsmgscreens
    $ current_room = "BS_Torture_Chamber"
    show screen minimap(current_room=current_room)
    scene bg bstorturechamber with fade

    if bs_Diachk_Torture_Chamber:       # Dialouge for viewing this place => SECOND TIME 
        "Ah, not this place again"
        "The Torture Chamber"

    if not bs_Diachk_Torture_Chamber:       # Dialouge for after viewing this place == FIRST TIME
        "I step through the rubble and into a chamber of nightmares..."  
        "{i}The air is heavy with the stench of rusted metal and old blood...{/i}"  
        "Shackles, cages, and instruments of torture line the walls. This place is a monument to cruelty."  
        "{b}What in the world happened here?{/b}"  
        "I can almost feel the agony lingering in the shadows, like ghosts that refuse to leave."  
        "{i}I need to get out of here... but maybe there's something—some clue—hidden among this horror.{/i}"
        "{i}There is a door to the left. I could approach the cages, and something is on the wall near them.{/i}"
        $ bs_Diachk_Torture_Chamber = True

    "The Torture Chamber"
    $ renpy.pause(hard=True)

label BS_Chamber_Storage:
    $ current_room = "BS_Chamber_Storage"
    show screen minimap(current_room=current_room)
    stop sound fadeout 0.5
    scene bg bschamberstorage with fade

    if bs_Diachk_Chamber_Storage:     # Dialouge for viewing this place => SECOND TIME
        "The horrors in this place, Ah!"
        "Torture Chamber Storage"

    if not bs_Diachk_Chamber_Storage:   # Dialouge for after viewing this place == FIRST TIME
        "I enter the room and find myself in a narrow corridor filled with nightmarish instruments—rusted saws, chains, and scalpels lie scattered on workbenches."
        "{i}The smell is the worst part—blood and rust and something else I can't quite name...{/i}"
        "Tools of torture line the walls, and my stomach churns at the thought of what might have happened here."
        "{b}I have to keep it together... There's got to be a clue or a way out in this place.{/b}"
        "The fluorescent lights overhead flicker and buzz, casting shifting shadows on the blood-smeared concrete floor."
        "I see a drainway on the ground, leading to its entrance at the far end."
        "{i}I see an electrical room on the right-maybe there's a way to turn on all the lights, or open some locked door...{/i}"
        "I just need to hold my nerve. {b}Whatever's lurking here, I can’t let it stop me from escaping this hellhole.{/b}"
        $ bs_Diachk_Chamber_Storage = True

    "Torture Chamber Storage"
    $ renpy.pause(hard=True)

label BS_Cell_Entrances:
    $ current_room = "BS_Cell_Entrances"
    show screen minimap(current_room=current_room)
    scene bg bscellentrances with fade
    stop sound fadeout 0.5

    if bsCell01paper and bsCell02paper and bsCell03paper and not bs_Diachk_Cell_Entrances:
        "Combining the 3 three pieces of text says {b}PULL THE BOOK{/b}"
        $ bsfoundlibraryclue = True
        "This could be useful"
        "I should look around the basement and maybe find a bookshelf"
        $ bs_Diachk_Cell_Entrances = True

    "Cell Corridor"
    $ renpy.pause(hard=True)

label BS_Electric_Room:
    $ current_room = "BS_Electric_Room"
    show screen minimap(current_room=current_room)
    

    if not bs_Diachk_Electric_Room and not bsfoundelectricgloves:       # Dialouge for after viewing this place == FIRST TIME and not found electric gloves
        scene bg bselectricroom with fade
        "I step into the electric room and instantly feel my nerves on edge—wires dangle like a twisted spider’s web, sparking and humming with untamed energy."
        "{i}One wrong move in here and I'd fry myself in an instant...{/i}"
        "The panels on the walls are rusted and ancient, the dials barely legible beneath layers of grime."
        "{b}I definitely need some protection before I start messing around with these cables...{/b}"
        "I scan the floor for anything that might help, but there's nothing but sand and tangled cords."
        "{i}I’m not taking any chances. I need to find a pair of rubber gloves—or something like them—before I even think about touching this mess.{/i}"
        $ bs_Diachk_Electric_Room = True

    elif bs_Diachk_Electric_Room and not bsfoundelectricgloves:     # Dialouge for viewing this place => SECOND TIME and not found electric gloves
        scene bg bselectricroom with fade
        "I've returned, but without any rubber gloves. That electric room is still as dangerous as ever."
        "{i}I can't risk a shock—no way I'm messing with those sparking wires naked.{/i}"
        "I need to find something to protect me before I dare step back in there."
        "{b}For now, I'll hold off and search elsewhere...{/b}"

    elif bsfoundelectricgloves and not bsfoundfuse:     # found electric gloves
        scene bg bselectricroom with fade
        "I return to the electric room, gloves in hand—finally, some protection against this electrified chaos."
        "{i}These gloves might just be my lifeline, but I still need to tread carefully...{/i}"
        "I study the sparking wires and tangled cables, my pulse quickening at the thought of a single misstep."
        "{b}Now, I'm ready to figure out what these panels are hiding, but not a moment sooner.{/b}"
        "I take a deep breath, pausing to let the silence of the room settle as I plan my next move."
        "Wait what do I do though?"

    elif bsfoundelectricgloves and bsfoundfuse:
        if not bsmotoron:
            scene bg bselectricroom
            "I can do something now"
            "Let me put the fuse inside there"
            $ bsmotoron = True
            play sound "audio/bsglassbreaking.flac" volume 5.0              # glass10-proc.flac by Craxic -- https://freesound.org/s/204133/ -- License: Attribution 3.0
            "That sound came from the Blood Storage room"
            "I must investigate"
            "That sound scared me out"
            "Let me put in the fuse first"
            jump BS_Electric_Room

        elif bsmotoron:
            scene bg bselectricroomfuse with fade
            play sound "audio/bsmgmotor.mp3" volume 0.6 fadein 0.5 loop                 #2 by AUDACITIER -- https://freesound.org/s/632325/ -- License: Attribution 4.0
            "The Drainway motor is turned on"


    "Electric Room"
    $ renpy.pause(hard=True)

label BS_Drainway:
    call bsmgscreens
    scene bg bsdrainout with fade

    if not bs_Diachk_Drainway and not bsfoundwatergear:     # Dialouge for after viewing this place == FIRST TIME and not found water gear
        scene bg bsdrainout with fade
        "I edge closer to the drainway, my eyes straining to make sense of the murky depths."
        "{i}All I see is water, choked with a repulsive, slimy liquid. I can barely breathe just from the stench.{/i}"
        "Every inch of that passage is submerged, and there's no telling what lurks beneath."
        "{b}There's no way I'm stepping in without proper gear.{/b}"
        "I need to track down some water equipment—maybe a mask or something else—to brave this liquid."
        $ bs_Diachk_Drainway = True
        jump BS_Drainway

    elif bs_Diachk_Drainway and not bsfoundwatergear:     # Dialouge for viewing this place => SECOND TIME and not found water gear
        scene bg bsdrainout with fade
        "I come back to the drainway, my heart pounding as I see the murky water still lurking below."
        "{i}It hasn't changed—thick, repulsive, and filled with that disgusting, slimy liquid...{/i}"
        "I don't have the water gear I need, and the thought of diving in like this is terrifying."
        "{b}I can't risk it—I'll have to find proper equipment before I try again.{/b}"
        "The drainway remains a forbidden abyss, silently daring me to come back when I'm ready."   

    elif not bs_Diachk_Drainway and bsfoundwatergear:     # Dialouge for viewing this place => SECOND TIME and found water gear
        stop audio
        scene bg bsdrainout with fade
        "Equipped with my waterproof mask and gear, I return to the drainway, feeling a mix of trepidation and resolve."
        "{i}This time, I have the protection I need. No more blind risk—I'm prepared to face whatever lies beneath.{/i}"
        "I take a deep breath, steady my nerves, and edge closer to the murky passage."
        "Every step forward is a step into the unknown, but I won't let fear hold me back."
        "{i}This is the point of no return, once you enter you cannot leave"
        "{i}Make your choice wisely"
        "{i}click to enter"
        
        window hide
        scene bs mgtunnel with fade
        hide screen minimap
        jump bsmgrunnerstart
        pause

    elif bs_Diachk_Drainway and bsfoundwatergear:     # Dialouge for viewing this place => SECOND TIME and found water gear
        stop audio
        scene bg bsdrainout with fade
        "Equipped with my waterproof mask and gear, I return to the drainway, feeling a mix of trepidation and resolve."
        "{i}This time, I have the protection I need. No more blind risk—I'm prepared to face whatever lies beneath.{/i}"
        "I take a deep breath, steady my nerves, and edge closer to the murky passage."
        "Every step forward is a step into the unknown, but I won't let fear hold me back."
        "{i}This is the point of no return, once you enter you cannot leave"
        "{i}Make your choice wisely"
        "{i}click to enter"
        
        window hide
        scene bs mgtunnel with fade
        hide screen minimap
        jump bsmgrunnerstart
        pause
            
    
    $ current_room = "BS_Drainway"
    show screen minimap(current_room=current_room)
    "Sewer Drainway"
    
    $ renpy.pause(hard=True)

label BS_Cell_1:
    $ current_room = "BS_Cell_1"
    show screen minimap(current_room=current_room)
    

    if bs_Diachk_Cell_1:
        scene bg bscell01 with fade
        "This is Cell 01..."

    if not bs_Diachk_Cell_1 and not bsCell01paper:
        scene bg bscellpull01 with fade
        "This is Cell 01... {b}The air is heavy with secrets.{/b}"
        "{i}Every step echoes, as if the past is whispering its regrets to me...{/i}"
        "I feel the weight of unseen eyes tracking my every move in this musty gloom."
        "{b}I can't shake off the chill—it's as if the very walls are mourning.{/b}"
        "IS THAT BLOOD ON THE BED AND THE FLOOR"
        "{i} I should investigate {/i}"
        $ bs_Diachk_Cell_1 = True
        
        $ current_hotspot = None    ## MUST CALL THIS BEFORE THE START OF THE MINI GAME
        # Define interactive hotspots in this scene
        $ bsclosetstorage_hotspots = [
            {
                "area": (1078, 684, 104, 116),
                "label": "BS_Cell_1_PULL",
                "tooltip": "What is that piece of paper on the Floor",
                "image": "Basement/minigames/bsmgornament.png",
                "win_txt": "The paper says \"PULL\" ",
                "win_lose_exit_label": "BS_Cell_1",
                "state_var": "bsCell01paper"
            },
            # add more here
        ]

        show screen hotspot_overlay(bsclosetstorage_hotspots)

    if bsCell01paper and bsCell02paper and bsCell03paper and not bs_Diachk_Cell_Entrances:
        "Combining the 3 three pieces of text says {b}PULL THE BOOK{/b}"
        $ bsfoundlibraryclue = True
        "This could be useful"
        "I should look around the basement and maybe find a bookshelf"
        $ bs_Diachk_Cell_Entrances = True
        

    "Cell #1"
    $ renpy.pause(hard=True)

label BS_Cell_2:
    $ current_room = "BS_Cell_2"
    show screen minimap(current_room=current_room)

    if bs_Diachk_Cell_2:
        scene bg bscell02 with fade
        "This is Cell 02..."

    if not bs_Diachk_Cell_2 and not bsCell02paper:
        scene bg bscellthe02 with fade
        "This is Cell 02... {b}The air is heavy with secrets.{/b}"
        "{i}Every step echoes, as if the past is whispering its regrets to me...{/i}"
        "I feel the weight of unseen eyes tracking my every move in this musty gloom."
        "{b}I can't shake off the chill—it's as if the very walls are mourning.{/b}"
        "IS THAT BLOOD ON THE BED AND THE FLOOR"
        "{i} I should investigate {/i}"
        $ bs_Diachk_Cell_2 = True
        
        $ current_hotspot = None    ## MUST CALL THIS BEFORE THE START OF THE MINI GAME
        # Define interactive hotspots in this scene
        $ bsclosetstorage_hotspots = [
            {
                "area": (1090, 682, 85, 133),
                "label": "BS_Cell_2_PULL",
                "tooltip": "What is that piece of paper on the Floor",
                "image": "Basement/minigames/bsmgornament.png",
                "win_txt": "The paper says \"THE\" ",
                "win_lose_exit_label": "BS_Cell_2",
                "state_var": "bsCell02paper"
            },
            # add more here
        ]

        show screen hotspot_overlay(bsclosetstorage_hotspots)

    if bsCell01paper and bsCell02paper and bsCell03paper and not bs_Diachk_Cell_Entrances:
        "Combining the 3 three pieces of text says {b}PULL THE BOOK{/b}"
        $ bs_Diachk_Cell_Entrances = True
        "This could be useful"
        "I should look around the basement and maybe find a bookshelf"
        
        $ bsfoundlibraryclue = True

    "Cell #2"
    $ renpy.pause(hard=True)

label BS_Cell_3:
    $ current_room = "BS_Cell_3"
    show screen minimap(current_room=current_room)

    if bs_Diachk_Cell_3:
        scene bg bscell03 with fade
        "This is Cell 03..."

    if not bs_Diachk_Cell_3 and not bsCell03paper:
        scene bg bscellbook03 with fade
        "This is Cell 03... {b}The air is heavy with secrets.{/b}"
        "{i}Every step echoes, as if the past is whispering its regrets to me...{/i}"
        "I feel the weight of unseen eyes tracking my every move in this musty gloom."
        "{b}I can't shake off the chill—it's as if the very walls are mourning.{/b}"
        "IS THAT BLOOD ON THE BED AND THE FLOOR"
        "{i} I should investigate {/i}"
        $ bs_Diachk_Cell_3 = True
        
        $ current_hotspot = None    ## MUST CALL THIS BEFORE THE START OF THE MINI GAME
        # Define interactive hotspots in this scene
        $ bsclosetstorage_hotspots = [
            {
                "area": (1095, 701, 69, 103),
                "label": "BS_Cell_3_PULL",
                "tooltip": "What is that piece of paper on the Floor",
                "image": "Basement/minigames/bsmgornament.png",
                "win_txt": "The paper says \"BOOK\" ",
                "win_lose_exit_label": "BS_Cell_3",
                "state_var": "bsCell03paper"
            },
            # add more here
        ]

        show screen hotspot_overlay(bsclosetstorage_hotspots)

    if bsCell01paper and bsCell02paper and bsCell03paper and not bs_Diachk_Cell_Entrances:
        "Combining the 3 three pieces of text says {b}PULL THE BOOK{/b}"
        $ bs_Diachk_Cell_Entrances = True
        "This could be useful"
        "I should look around the basement and maybe find a bookshelf"
        
        $ bsfoundlibraryclue = True

    "Cell #3"
    $ renpy.pause(hard=True)

label BS_Bodies_Wall:
    $ current_room = "BS_Bodies_Wall"
    show screen minimap(current_room=current_room)
    scene bg bgbodieswall with fade
    play sound "audio/bsbodieswallcrying.mp3" volume 0.6 fadein 0.5 loop # Group_Cry_Lementations.mp3 by thepaganpanda -- https://freesound.org/s/627002/ -- License: Attribution 4.0
    $ bslistenedtobodiescrying = True
    if bs_Diachk_Bodies_Wall:
        "Ah! I can't stand near this wall"
        "My head hurts from their wailing"
    "Suspicious Wall"

    if not bs_Diachk_Bodies_Wall:
        "This wall... {i}it's soaked with something dark and slick{/i}. I can almost taste the iron in the air."
        "{b}The cries are growing louder{/b}. They hiss in and out, clawing at my mind."
        "I can feel the sticky warmth on the bricks... as if it's still {i}fresh{/i}."
        "Each drop that falls makes their wailing heavier, like a dying heartbeat echoing through these halls."
        "{i}I have to keep my eyes forward... but these voices, they never let go{/i}."
        "There is definitely something behind this wall"
        $ bs_Diachk_Bodies_Wall = True


    $ renpy.pause(hard=True)


# All stuff in left and top left of the map
label BS_GoForward_1:
    $ current_room = "BS_GoForward_1"
    show screen minimap(current_room=current_room)
    scene bg bsforward1 with fade



    if bs_Diachk_GoForward_1:
        "Can either enter the door on the left or go straight into the darkness"

    if not bs_Diachk_GoForward_1:
        "This hallway... it feels like it's closing in around me, {i}whispers trailing every step{/i}."
        "The door on my left beckons, scratched and worn, its handle stained with old secrets."
        "{b}If I dare open it{/b}, who knows what lurks inside—yet the darkness ahead seems no safer."
        "Every breath tastes of dust and dread, urging me forward... but in which direction?"
        $ bs_Diachk_GoForward_1 = True


    "Beside Stairway"
    $ renpy.pause(hard=True)

label BS_Guest_Bathroom:
    call bsmgscreens        # clear mini game screen
    $ current_room = "BS_Guest_Bathroom"
    show screen minimap(current_room=current_room)

    if not bsbloodstorage_broken and bsbloodstorage_blast and bsexplosives_found:   # >=2 time enter, found explosives, door can be broken now
        if not bsbloodstorage_broken:
            scene bg bsguestbathroomnotbroken with fade
            "Now I will blow up the door"
            jump BS_Guest_Bathroom

    if bsbloodstorage_broken:                                                            # >=2 time enter, found explosives, door blast here
        scene bg bsguestbathroombroken with fade
        if not bsbodeiesexplosion:
            play sound "audio/bsbloodstorageblast.mp3" volume 0.7
            $ bsbodeiesexplosion = True

        "Now I can enter this room"

    if not bsbloodstorage_broken and bs_DiackGuest_Bathroom and not bsexplosives_found:     # >=2 time enter, not found explosives, not door broken
        scene bg bsguestbathroomnotbroken with fade
        "The door is still sealed shut"
        play sound "audio/bsdmaindoorlocked.wav" volume 0.4             # Door_Locked_01.wav by skyumori -- https://freesound.org/s/104530/ -- License: Creative Commons 0
        "No matter how hard I shove, it won't budge. {b}I might have to blow it apart{/b} if I ever want to leave this place."

    if not bsbloodstorage_broken and bs_DiackGuest_Bathroom and bsexplosives_found:     # >=2 time enter, found explosives, not door broken
        scene bg bsguestbathroomnotbroken with fade
        "This guest bathroom feels more like a tomb now, silent but for the whispers of dread."
        "I've found the explosives—my only key to unlocking the secrets behind that sealed door."
        "With trembling hands, I set the fuse, the scent of sulfur mixing with the iron tang of blood."
        "In just moments, a roaring blast will shatter the silence and free whatever horror lies beyond."
        "This is it: no turning back now, as I face the consequences of breaking barriers meant to remain forever shut."

    if not bsbloodstorage_broken and not bs_DiackGuest_Bathroom and not bsexplosives_found:     # first time enter, not found explosives, not door broken
        scene bg bsguestbathroomnotbroken with fade
        $ bs_DiackGuest_Bathroom = True
        "This guest bathroom is a {i}rotting nightmare{/i}—blood streaks every tile, drips off the rim of the tub, and pools beneath the toilet."
        "There's another door across the room, but it's sealed shut, {i}oozing crimson{/i} from its edges like a wounded beast."
        play sound "audio/bsdmaindoorlocked.wav" volume 0.4             # Door_Locked_01.wav by skyumori -- https://freesound.org/s/104530/ -- License: Creative Commons 0
        "No matter how hard I shove, it won't budge. {b}I might have to blow it apart{/b} if I ever want to leave this place."


    "Basement Guest Bathroom"
    $ renpy.pause(hard=True)

label BS_Blood_Storage:
    call bsmgscreens        # clear mini game screen
    $ current_room = "BS_Blood_Storage"
    show screen minimap(current_room=current_room)

    if bs_Diachk_Blood_Storage:
        jump BS_BloodStorageFuse

    if not bs_Diachk_Blood_Storage:
        scene bg bsbloodstoragefuse with fade
        "The doorway is blown apart, revealing a room lined with metal shelves—each brimming with vials and IV bags of {i}thick, crimson liquid{/i}."
        "The air is thick and metallic, and every shelf seems to pulse with a twisted life of its own."
        "{b}Rows and rows of blood{/b}, meticulously categorized, as though someone—or something—has been collecting it for a dreadful purpose."
        "I can feel my heart hammering with each echoing drop, a steady reminder that {i}I shouldn't be here{/i}."
        $ bs_Diachk_Blood_Storage = True
        jump BS_BloodStorageFuse

    "Blood Storage Room"
    $ renpy.pause(hard=True)

label BS_BloodStorageFuse:

    if not bsfoundfuse:
        scene bg bsbloodstoragefuse with fade
        #"What's that on the floor"
        show expression Text("What's that glowing thing on the floor") at truecenter as txt
        with dissolve
        pause
        hide txt
        window hide
        $ current_hotspot = None    ## MUST CALL THIS BEFORE THE START OF THE MINI GAME
        # Define interactive hotspots in this scene
        $ bsclosetstorage_hotspots = [
            {
                "area": (880, 929, 190, 79),
                "label": "fifteen_game",
                "tooltip": "Let me pick that up",
                "image": "Basement/minigames/bsmgfuse.png",
                "win_txt": "You pick up the glowing thing \nIt is a fuse\nThis could be useful in an {b}Electric room{/b} or something",
                "win_lose_exit_label": "BS_BloodStorageFuse",
                "state_var": "bsfoundfuse"
            },
            # add more here
        ]

        show screen hotspot_overlay(bsclosetstorage_hotspots)
    elif bsfoundfuse and bsmotoron:
        scene bg bsbloodstoragebroken with fade
        "What happened here?"
        "Everything was fine before"
        "Looks like a path has opened up"
        "I must investigate"

    elif bsfoundfuse:
        scene bg bsbloodstorage with fade
        $ current_hotspot = None    ## MUST CALL THIS AFTER THE END OF THE MINI GAME
        "I have found everything that can be found in this room."

    $ renpy.pause(hard=True)

label BS_Destroyed_Path:
    call bsmgscreens
    stop sound fadeout 0.5
    $ current_room = "BS_Destroyed_Path"
    show screen minimap(current_room=current_room)
    scene bg bsdestroyedpath with fade
    "How long does this go on for"
    "I can see barely see the end"
    $ renpy.pause(hard=True)

label BS_Bodies_Room:
    call bsmgscreens
    play sound "audio/bsbodieswallcrying.mp3" volume 0.6 fadein 0.5 loop # Group_Cry_Lementations.mp3 by thepaganpanda -- https://freesound.org/s/627002/ -- License: Attribution 4.0

    $ current_room = "BS_Bodies_Room"
    show screen minimap(current_room=current_room)

    if not bskeletonmoved:
        scene bg bsbodiesroomlocked with fade
        if bslistenedtobodiescrying:
            "Wait a minute, I have heard these wailings before"
            "Ah! Yes, I have heard these sounds when I was near that bloody brick wall near those cells"
        "It looks like whoever tried to open that chest was locked in here and perished"
        "Let me move it aside"
        $ bskeletonmoved = True
        jump BS_Bodies_Room
    
    elif bskeletonmoved:
        if not bsmglockedchest:
            scene bg bsbodiesroomlockedmoved
            "Ah! that was disgusting"
            "Now that it's done"
            "I do have a lockpick with me"
            show expression Text("I can give it a crack") at truecenter as txt
            with dissolve
            pause
            hide txt
            show screen click_chest("lock_chest1")
            

        elif bsmglockedchest:
            hide screen click_chest
            scene bg bsbodiesroomopened
            "You have found scuba gear inside"
            "I could use this in the drainway to swim and get out "
            

    


    $ renpy.pause(hard=True)

label BS_GoForward_2:
    call bsmgscreens        # clear mini game screen

    $ current_room = "BS_GoForward_2"
    show screen minimap(current_room=current_room)
    scene bg bsgoforward2 with fade

    "Basement Hallway"
    $ renpy.pause(hard=True)

label BS_Left_Closet:
    $ current_room = "BS_Left_Closet"
    show screen minimap(current_room=current_room)

    scene bg bsstoragecloset with fade
    "Basement Closet"
    if not bsfoundsuperstrength:
        "Something is weird here, I can feel the power"
        window hide
        $ current_hotspot = None    ## MUST CALL THIS BEFORE THE START OF THE MINI GAME
        # Define interactive hotspots in this scene
        $ bsclosetstorage_hotspots = [
            {
                "area": (949, 325, 233, 460),                                                                            # custom area of the highlited part on the image
                "label": "fifteen_game",                                                                                 # default label of the mini game 
                "tooltip": "Open the door to gain power",                                                                # custom tool tip on the image
                "image": "Basement/minigames/bsmgbicep.png",                                                             # custom image for the mini game
                "win_txt": "You gained power to move something heavy\n Look around in the basement to use this power",   # custom win txt
                "win_lose_exit_label": "BS_Left_Closet",                                                                 # custom win, exit or leave label, label when user finishes the mini game
                "state_var": "bsfoundsuperstrength"                                                                      # your custom variable you want to flip when user wins the mini game     # 
            },
            # add more here
        ]
    

        show screen hotspot_overlay(bsclosetstorage_hotspots)
    
    elif bsfoundsuperstrength:
        "I have found everything that can be found in this room."
        $ current_hotspot = None    ## MUST CALL THIS AFTER THE END OF THE MINI GAME
    
    $ renpy.pause(hard=True)


label BS_Private_Bathroom:
    $ current_room = "BS_Private_Bathroom"
    show screen minimap(current_room=current_room)

    if not bsfound_hammer:
        scene bg bsprivatebathroomhammer with fade
        "There is a hammer on the toilet seat"
        "I should pick that up, it could prove to be useful"
        $ current_hotspot = None    ## MUST CALL THIS BEFORE THE START OF THE MINI GAME
        # Define interactive hotspots in this scene
        $ bsclosetstorage_hotspots = [
            {
                "area": (1208, 570, 391, 263),
                "label": "BS_Private_Bathroom_Hammer",
                "tooltip": "Let me pick that hammer up",
                "image": "Basement/minigames/bsmgfuse.png",
                "win_txt": "Pick up the hammer",
                "win_lose_exit_label": "BS_Private_Bathroom",
                "state_var": "bsfound_hammer"
            },
            # add more here
        ]

        show screen hotspot_overlay(bsclosetstorage_hotspots)
    elif bsfound_hammer:
        scene bg bsprivatebathroom with fade
        "OMG!!! I can't stay in here for another second"
        "This {b}STINKS SO BAD{/b}"
        "I'm gonna Puke"
        "Basement Private Bathroom"
    $ renpy.pause(hard=True)

label BS_Private_Bedroom:
    $ current_room = "BS_Private_Bedroom"
    show screen minimap(current_room=current_room)
    if bsmovedbookshelf:
        scene bg bsprvtsecroomopen with fade
    elif not bsmovedbookshelf and not bs_Diachk_Private_Bedroom:
        scene bg bsprvtsecroomnotopen with fade
        "That bookshelf over there looks like it can be moved"
        "Ahhh! Damn, thats heavy"
        "Even that is too much for me"
        $ bs_Diachk_Private_Bedroom = True

    elif not bsmovedbookshelf and bs_Diachk_Private_Bedroom:
        scene bg bsprvtsecroomnotopen with fade
        "Still can't move the bookshelf"
        "I will have to hit the gym"

    "Basement Private Bedrrom"
    $ renpy.pause(hard=True)

label BS_SecretRoom_PBedroom:
    $ current_room = "BS_SecretRoom_PBedroom"
    show screen minimap(current_room=current_room)
    #scene bg bsprvtsecroomgloves with fade
    if not bsfoundelectricgloves:
        scene bg bsprvtsecroomgloves with fade
        $ current_hotspot = None    ## MUST CALL THIS BEFORE THE START OF THE MINI GAME
        show expression Text("Are those gloves on the floor?") at truecenter as txt
        with dissolve
        pause
        hide txt
        $ bsclosetstorage_hotspots = [
            {
                "area": (662, 815, 381, 224),                                                                            # custom area of the highlited part on the image
                "label": "play_pong",                                                                                 # default label of the mini game 
                "tooltip": "pick up Electric Gloves",                                                                # custom tool tip on the image
                "image": "Basement/minigames/bsmgbicep.png",                                                             # custom image for the mini game
                "win_txt": "I should be able to use these gloves somewhere in the electric room",   # custom win txt
                "win_lose_exit_label": "BS_SecretRoom_PBedroom",                                                                 # custom win, exit or leave label, label when user finishes the mini game
                "state_var": "bsfoundelectricgloves"                                                                      # your custom variable you want to flip when user wins the mini game     # 
            },
            # add more here
        ]
        show screen hotspot_overlay(bsclosetstorage_hotspots)

    elif bsfoundelectricgloves:
        scene bg bsprvtsecroom with fade
    
        #jump play_pong
        #scene bg bsprvtsecroom with fade
    $ renpy.pause(hard=True)

label BS_TV_Corridor:
    $ current_room = "BS_TV_Corridor"
    show screen minimap(current_room=current_room)
    call bsmgscreens
    scene bg bstvcorridor with fade
    "TV Hallway"
    $ renpy.pause(hard=True)

label BS_InFront_TV:
    $ current_room = "BS_InFront_TV"
    show screen minimap(current_room=current_room)
    
    if not bstvjumpscarepassed:
        play sound "bstvjumpscare.wav" volume 0.5
        scene bg bstvjumpscare
        $ current_hotspot = None    ## MUST CALL THIS BEFORE THE START OF THE MINI GAME
        $ bsclosetstorage_hotspots = [
            {
                "area": ((0, 0, 1920, 1080)),                                                                            # custom area of the highlited part on the image
                "label": "bsclickermg",                                                                                 # default label of the mini game 
                "tooltip": "Click any where to get started",                                                                # custom tool tip on the image
                "image": "Basement/minigames/bsmgbicep.png",                                                             # custom image for the mini game
                "win_txt": "OMG!!\nI thought I would have died\nI will look around in the basement to use these explosives",   # custom win txt
                "win_lose_exit_label": "BS_InFront_TV",                                                                 # custom win, exit or leave label, label when user finishes the mini game
                "state_var": "bstvjumpscarepassed"                                                                      # your custom variable you want to flip when user wins the mini game     # 
            },
            # add more here
        ]
        show screen hotspot_overlay(bsclosetstorage_hotspots)

    elif bstvjumpscarepassed:
        scene bg bstvnojumpscare with fade
        if not bs_Diachk_InFront_TV:
            $ bs_Diachk_InFront_TV = True
            "[ current_hotspot['win_txt'] ]"
        if bs_Diachk_InFront_TV:
            "I don't want to meet her again"
    
    $ renpy.pause(hard=True)

label BS_Library:
    $ current_room = "BS_Library"
    show screen minimap(current_room=current_room)
    if bslibrarydoorclosed and not bsfoundlibraryclue:
        scene bg bslibrarydoorclosed with fade
        "That big door is locked"
        "I could look around in the library"
        "Does not seem very useful"
        "I have to find something useful elsewhere and return here"
    elif not bslibrarydoorclosed:
        scene bg bslibrarydooropen with fade
        "I can go in there now"

    elif bslibrarydoorclosed and bsfoundlibraryclue:
        scene bg bslibrarydoorclosed with fade
        "Okay, piecing together the clue I found in those cells"
        "I must look around and pull a book out"

    "Basement Library"
    hide screen fifteen_scr
    $ renpy.pause(hard=True)

label BS_Ladder_Room:
    $ current_room = "BS_Ladder_Room"
    show screen minimap(current_room=current_room)
    scene bg bsladderroom with fade
    "Secret Ladder Room"
    jump fifteen_game
    $ renpy.pause(hard=True)


