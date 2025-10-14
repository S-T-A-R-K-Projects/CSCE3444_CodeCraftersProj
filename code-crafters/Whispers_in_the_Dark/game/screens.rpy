################################################################################
## Initialization
################################################################################

init offset = -1

################################################################################
## Whispers In The Dark Custom Screens - Tanner  & kaushik
################################################################################
screen character_selection():
    add "images/character/character selection.webp"
    tag menu
    modal True
    frame:
        xpos 0.5
        ypos 0.3
        xanchor 0.5
        yanchor 0.3
        padding (50,30)
        background "#080808aa"  # background to  better show the options
        xsize 700
        ysize 600

    vbox:
        spacing 20
        align (0.5, 0.3)

        text "Choose Your Character" size 45 bold True color "#FFD700"

        # Michael Redwood
        
        textbutton "Michael Redwood"  action  [
            SetVariable("selected_character", mc_m),  
            Show("character_confirm")
        ]
        
        textbutton "Evelyn \"Evie\" Carter" action [
            SetVariable("selected_character", mc_e), 
            Show("character_confirm")
        ]

        textbutton "Jeremy Hardin" action [
            SetVariable("selected_character", mc_j), 
            Show("character_confirm")
        ]

        textbutton "Sam Winchester" action [ 
            SetVariable("selected_character", mc_s), 
            Show("character_confirm")
        ]

        textbutton "Dean Winchester" action [
            SetVariable("selected_character", mc_d), 
            Show("character_confirm")
        ]
        

        # Back Button
        textbutton "Back" action Return() text_size 30

screen character_confirm():
    tag menu
    modal True

    # Update to use dictionary format
    if selected_character["name"] == "Michael Redwood":
        add "images/character/MichaelRedwood.png" xpos 1 ypos 1
    elif selected_character["name"] == "Evelyn Carter":
        add "images/character/EvelynCarter.png" xpos 1 ypos 1
    elif selected_character["name"] == "Jeremy Hardin":
        add "images/character/JeremyHardin.png" xpos 1 ypos 1
    elif selected_character["name"] == "Sam Winchester":
        add "images/character/samwinchester.png" xpos 1 ypos 1
    elif selected_character["name"] == "Dean Winchester":
        add "images/character/deancharacter.png" xpos 1 ypos 1

    frame:
        xpos 0.75
        ypos 0.25
        xanchor 0.5
        yanchor 0.5
        padding (50, 30)
        background "#222222AA"  # background to better show the options
        xsize 700

        vbox:
            spacing 20
            align (0.5, 0.5)

            text "You selected [selected_character['name']]" size 40 bold True color "#FFD700"  # Gold color for the name
            text "[selected_character['bio']]" size 28 italic True color "#FFFFFF"
            
            # Display character stats using dictionary keys
            text "Strength: [selected_character['strength']]" size 28 color "#FF6347"  # Red color
            text "Intelligence: [selected_character['intelligence']]" size 28 color "#87CEEB"  # Light blue color
            text "Fortitude: [selected_character['fortitude']]" size 28 color "#32CD32"  # Green color

            hbox:
                spacing 40
                align (0.5, 0.5)

                textbutton "🔄 Go Back" action [
                    Hide("character_confirm"), 
                    Show("character_selection")
                ] text_size 30

                textbutton "✅ Confirm" action [
                    SetVariable("final_character", selected_character), 
                    Hide("character_confirm"), 
                    Jump("start_game")
                ] text_size 30


#Character stat HUD, displays health bar and relavent character info - Tanner
screen character_stats_hud():
    zorder 100  # Ensure it's always on top
    modal False  # Allows interaction with other UI elements

    frame:
        xpos 0.00
        ypos 0.00
        xanchor 0
        yanchor 0
        padding (20, 20)
        background "#000000AA"  # Semi-transparent background
        xsize 300  # Set width
        ysize 250  # Set height (adjust as needed)

    vbox:
        spacing 5
        xalign 0.0
        xoffset 20
        yoffset 10

        text "[char['name']]" size 25 bold True color "#FFD700"  # Gold color for name
        text "Strength: [char['strength']]" size 18 color "#FF6347"  # Red color
        text "Intelligence: [char['intelligence']]" size 18 color "#87CEEB"  # Light blue color
    
        text "Fortitude: [char['fortitude']]" size 18 color "#32CD32"
        bar value VariableValue("current_fortitude", current_fortitude) range current_fortitude xsize 200 style "fortitude_bar"

        text "Health: [current_health]" size 18 color "#ec0abb" 
        bar value VariableValue("current_health", current_health) range current_health xsize 200 style "health_bar"

screen minimap(current_room):
    zorder 100
    modal False

    if "BS" in current_room:
        frame:
            xalign 1.0
            yalign 1.05
            padding (10, 10)
            background "#00000088"
            xsize 350
            ysize 350

            if current_room in minimap_images:
                add minimap_images[current_room] fit "contain"
            else:
                text "No Map" size 20 color "#FFFFFF" xalign 0.5 yalign 0.5

    elif "FF" in current_room:
        frame:
            xalign 0.95
            yalign 1.05
            padding (10, 10)
            background "#00000088"
            xsize 350
            ysize 350

            if current_room in minimap_images:
                add minimap_images[current_room] zoom 1.5 fit "contain"
            else:
                text "No Map" size 20 color "#FFFFFF" xalign 0.5 yalign 0.5








##############################################################################
# TRANSFORMS Tanner + kaushik
##############################################################################
#---Office-Mini-Game-and-skill-check------------------------------------------------------------------------------
screen bookshelf_screen():
    imagebutton:
        idle "images/First_Floor/MiniGame/Book_Item.png"
        hover "images/First_Floor/MiniGame/Book_Item_Exam.png"  # Changes cursor to a magnifying glass when hovering
        xpos 1000  # Adjust to where the book is on the bookshelf
        ypos 850
        xsize 75  # Size of the hover area
        ysize 61
        action Show("examine_menu")  # Opens the examine menu

screen examine_menu():
    modal True
    frame:
        xpos 0.5
        ypos 0.5
        xanchor 0.5
        yanchor 0.5
        padding (20, 20)
        background "#222222AA"
        xsize 500
        ysize 300

        vbox:
            spacing 20
            align (0.5, 0.5)

            text "This looks like a special book..." size 28 color "#FFFFFF"

            textbutton "Examine Book (Intelligence Check Lvl.4)" action [Function(exam_book)] text_size 30
            textbutton "Close" action Hide("examine_menu") text_size 30


init python:
    import random  # Import random for generating numbers

    def exam_book():
        global book_exam_check, difficulty
        difficulty = random.randint(3, 9) # Generate a difficulty between 1 and 10

        if char['intelligence'] >= difficulty:  # Pass check if intelligence is high enough
            renpy.notify("A hidden door exists behind the book shelf!")
            book_exam_check = True
        else:
            renpy.notify("Your dumb brain couldn't read the text!")   
    

            


#-----------------------------------------------------------------------------------------------------------------
transform fadeout: #used to fade out images
    alpha 1.0
    xcenter 0.5  # Centers the image horizontally
    yoffset 0  # Keeps vertical position unchanged
    easein 1.0 alpha 0.0  # Fades out smoothly over 1 second

transform menu_popup:
    alpha 0.0
    zoom 0.8
    linear 0.2 alpha 1.0 zoom 1.0

screen navigation_button():
    tag navigation_button
    zorder 100

    # orginally box was on bottom right, which was blocking the text, moved it to top right
    vbox:
        xpos 1.0        # orginally 0.95
        ypos 0.0        # orginally 0.95
        xanchor 1.0     
        yanchor 0.0     # orginally 1.0

        textbutton "Navigate" action [ Hide("navigation_button"), Show("navigation_menu") ] style "nav_button_style"



screen navigation_menu():
    tag navigation_menu
    modal False          # will allow progressing without using the nav menu
    zorder 110

    # Removed the overlay so background is not fully darkened

    frame:
        style_group "navigation_menu"
        at menu_popup

        # Bottom-right position instead of center
        align (1.0, 0.0)            # orginally 0.95, 0.95
        #xanchor 1.0
        #yanchor 1.0

        vbox:
            style "navigation_menu_vbox"

            text "Where do you want to go?" style "navigation_menu_title"

            ###---First Floor---###

            if current_room == "FF_Stage_1":
                textbutton "Enter the Office" action [SetVariable("current_room", "FF_Office"), Jump("FF_Office")] style "navigation_menu_textbutton"
                textbutton "Move Further into the Home" action [SetVariable("current_room", "FF_Stage_2"), Jump("FF_Stage_2")] style "navigation_menu_textbutton"
                textbutton "Go up the Stairs" action [SetVariable("current_room", "SF_Hallway"), Jump("SF_Hallway")] style "navigation_menu_textbutton"
                textbutton "Go downstairs" action [SetVariable("current_room", "Basement"), Jump("Basement")] style "navigation_menu_textbutton" # downstairs entrance command 
                textbutton "Exit Through front door" action [ 
                    SetVariable("try_door", try_door + 1), #Increment the door attempt count
                    Play("sound", "audio/lockeddoor.wav", selected=None),
                    Jump("FF_Stage_1")
                ] style "navigation_menu_textbutton"

            elif current_room == "FF_Stage_2":
                textbutton "Enter Living Room" action [SetVariable("current_room", "FF_Living_Room"), Jump("FF_Living_Room")] style "navigation_menu_textbutton"
                textbutton "Enter Hallway" action [SetVariable("current_room", "FF_Stage_3"), Jump("FF_Stage_3")] style "navigation_menu_textbutton"
                textbutton "Enter Kitchen" action [SetVariable("current_room", "FF_Kitchen"), Jump("FF_Kitchen")] style "navigation_menu_textbutton"
                textbutton "Go back to Front Door" action [SetVariable("current_room", "FF_Stage_1"), Jump("FF_Stage_1")] style "navigation_menu_textbutton"

            elif current_room == "FF_Stage_3":
                textbutton "Move down hall" action [SetVariable("current_room", "FF_Stage_4"), Jump("FF_Stage_4")] style "navigation_menu_textbutton"
                textbutton "Enter Front Room" action [SetVariable("current_room", "FF_Front_Room"), Jump("FF_Front_Room")] style "navigation_menu_textbutton"
                textbutton "Enter Bedroom" action [SetVariable("current_room", "FF_Room_1"), Jump("FF_Room_1")] style "navigation_menu_textbutton"
                textbutton "Move to Living Room" action [SetVariable("current_room", "FF_Stage_2"), Jump("FF_Stage_2")] style "navigation_menu_textbutton"

            elif current_room == "FF_Stage_4":
                textbutton "Enter Kitchen" action [SetVariable("current_room", "FF_Kitchen"), Jump("FF_Kitchen")] style "navigation_menu_textbutton"
                textbutton "Enter Room 2" action [SetVariable("current_room", "FF_Room_2"), Jump("FF_Room_2")] style "navigation_menu_textbutton"
                textbutton "Move Down the Hall" action [SetVariable("current_room", "FF_Stage_3"), Jump("FF_Stage_3")] style "navigation_menu_textbutton"

            elif current_room == "FF_Office":
                if book_exam_check:
                    textbutton "Enter Hidden Room" action [SetVariable("current_room", "FF_Hidden_1"), Jump("FF_Hidden_1")] style "navigation_menu_textbutton"

                textbutton "Exit to Front Door" action [SetVariable("current_room", "FF_Stage_1"), Jump("FF_Stage_1")] style "navigation_menu_textbutton"


            elif current_room == "FF_Hidden_1":
                textbutton "Leave Hidden Room" action [SetVariable("current_room", "FF_Office"), Jump("FF_Office")] style "navigation_menu_textbutton"

            elif current_room == "FF_Stairs_Up":
                textbutton "Turn Back" action [SetVariable("current_room", "FF_Stage_1"), Jump("FF_Stage_1")] style "navigation_menu_textbutton"

            elif current_room == "FF_Living_Room":
                textbutton "Exit to Hallway" action [SetVariable("current_room", "FF_Stage_2"), Jump("FF_Stage_2")] style "navigation_menu_textbutton"

            elif current_room == "FF_Kitchen":
                textbutton "Enter Dining Room" action [SetVariable("current_room", "FF_Dinning"), Jump("FF_Dinning")] style "navigation_menu_textbutton"
                textbutton "Enter Hallway" action [SetVariable("current_room", "FF_Stage_4"), Jump("FF_Stage_4")] style "navigation_menu_textbutton"
                textbutton "Exit Kitchen" action [SetVariable("current_room", "FF_Stage_2"), Jump("FF_Stage_2")] style "navigation_menu_textbutton"

            elif current_room == "FF_Dinning":
                textbutton "Enter Garden" action [SetVariable("current_room", "FF_Garden"), Jump("FF_Garden")] style "navigation_menu_textbutton"
                textbutton "Enter Kitchen" action [SetVariable("current_room", "FF_Kitchen"), Jump("FF_Kitchen")] style "navigation_menu_textbutton"

            elif current_room == "FF_Garden":
                textbutton "Enter Suspicious Room" action [SetVariable("current_room", "FF_Sus_Room"), Jump("FF_Sus_Room")] style "navigation_menu_textbutton"
                textbutton "Return to Dining Room" action [SetVariable("current_room", "FF_Dinning"), Jump("FF_Dinning")] style "navigation_menu_textbutton"

            elif current_room == "FF_Sus_Room":
                textbutton "Leave Suspicious Room" action [SetVariable("current_room", "FF_Garden"), Jump("FF_Garden")] style "navigation_menu_textbutton"

            elif current_room == "FF_Front_Room":
                textbutton "Enter Hidden Door" action [SetVariable("current_room", "FF_Hidden_2"), Jump("FF_Hidden_2")] style "navigation_menu_textbutton"
                textbutton "Exit to Hallway" action [SetVariable("current_room", "FF_Stage_3"), Jump("FF_Stage_3")] style "navigation_menu_textbutton"

            elif current_room == "FF_Room_1":
                textbutton "Exit to Hallway" action [SetVariable("current_room", "FF_Stage_3"), Jump("FF_Stage_3")] style "navigation_menu_textbutton"

            elif current_room == "FF_Room_2":
                textbutton "Enter Hidden Room" action [SetVariable("current_room", "FF_Hidden_2"), Jump("FF_Hidden_2")] style "navigation_menu_textbutton"
                textbutton "Exit to Hallway" action [SetVariable("current_room", "FF_Stage_4"), Jump("FF_Stage_4")] style "navigation_menu_textbutton"

            elif current_room == "FF_Hidden_2":
                textbutton "Exit to Front Room" action [SetVariable("current_room", "FF_Front_Room"), Jump("FF_Front_Room")] style "navigation_menu_textbutton"
                textbutton "Exit to Bedroom" action [SetVariable("current_room", "FF_Room_2"), Jump("FF_Room_2")] style "navigation_menu_textbutton"

            # BASEMENT NAVIGATION REMAINS UNCHANGED
            elif current_room == "BS_Stage_1":
                textbutton "Go Forward" action [SetVariable("current_room","BS_GoForward_1" ), Jump("BS_GoForward_1")] style "navigation_menu_textbutton"   
                textbutton "Go upstairs" action [SetVariable("current_room","FF_Stage_1" ), Jump("FF_Stage_1")] style "navigation_menu_textbutton"
                textbutton "Go under the Basement Stairway" action [SetVariable("current_room", "BS_Under_Stairway"), Jump("BS_Under_Stairway")] style "navigation_menu_textbutton"
            
            elif current_room == "Basement":
                textbutton "Go back" action [SetVariable("current_room","FF_Stage_1" ), Jump("FF_Stage_1")] style "navigation_menu_textbutton"

            elif current_room == "BS_Under_Stairway":
                # If the wall is already broken, offer a direct entrance.
                if bswall_broken:
                    textbutton "Enter Torture Chamber" action [
                        SetVariable("current_room", "BS_Torture_Chamber"),
                        Jump("BS_Torture_Chamber")
                    ] style "navigation_menu_textbutton"

                # If the player has the hammer and the wall is not yet broken, allow breaking the wall.
                elif bsfound_hammer:
                    textbutton "Break the Wall" action [
                        SetVariable("bswall_broken", True),
                        SetVariable("current_room", "BS_Under_Stairway"),
                        Jump("BS_Under_Stairway")
                    ] style "navigation_menu_textbutton"

                # If the player does NOT have the hammer, there's nothing to do.
                else:
                    textbutton "Nothing to do here" style "navigation_menu_textbutton"
                
                textbutton "Go back" action [
                    SetVariable("current_room", "BS_Stage_1"),
                    Jump("BS_Stage_1")
                ] style "navigation_menu_textbutton"


            elif current_room == "BS_Torture_Chamber":
                textbutton "Enter Chamber Storage on the left" action [SetVariable("current_room", "BS_Chamber_Storage"), Jump ("BS_Chamber_Storage")] style "navigation_menu_textbutton"
                textbutton "Go Deeper" action [SetVariable("current_room", "BS_Cell_Entrances"), Jump ("BS_Cell_Entrances")] style "navigation_menu_textbutton"
                textbutton "Go back under the stairway" action [SetVariable("current_room", "BS_Under_Stairway"),Jump ("BS_Under_Stairway")] style "navigation_menu_textbutton"

            elif current_room == "BS_Chamber_Storage":
                textbutton "Enter Electric Room" action [SetVariable("current_room", "BS_Electric_Room"), Jump ("BS_Electric_Room")] style "navigation_menu_textbutton"
                textbutton "Enter Drainway" action [SetVariable("current_room", "BS_Drainway"), Jump ("BS_Drainway")] style "navigation_menu_textbutton"
                textbutton "Go back to Torture Chamber" action [SetVariable("current_room", "BS_Torture_Chamber") ,Jump ("BS_Torture_Chamber")] style "navigation_menu_textbutton"

            elif current_room == "BS_Electric_Room":
                textbutton "Go back to Chamber Storage" action [SetVariable("current_room", "BS_Chamber_Storage") ,Jump ("BS_Chamber_Storage")] style "navigation_menu_textbutton"

            elif current_room == "BS_Drainway":
                textbutton "Go back to Chamber Storage" action [SetVariable("current_room", "BS_Chamber_Storage") ,Jump ("BS_Chamber_Storage")] style "navigation_menu_textbutton"

            elif current_room == "BS_Cell_Entrances":
                textbutton "{b} Enter Cell 1 {b}" action [SetVariable("current_room", "BS_Cell_1") ,Jump ("BS_Cell_1")] style "navigation_menu_textbutton"
                textbutton "{b} Enter Cell 2 {b}" action [SetVariable("current_room", "BS_Cell_2") ,Jump ("BS_Cell_2")] style "navigation_menu_textbutton"
                textbutton "{b} Enter Cell 3 {b}" action [SetVariable("current_room", "BS_Cell_3") ,Jump ("BS_Cell_3")] style "navigation_menu_textbutton"
                textbutton "Go near the wall on the right side" action [SetVariable("current_room", "BS_Bodies_Wall") ,Jump ("BS_Bodies_Wall")] style "navigation_menu_textbutton"
                textbutton "Go back to Torture Chamber" action [SetVariable("current_room", "BS_Torture_Chamber") ,Jump ("BS_Torture_Chamber")] style "navigation_menu_textbutton"

            elif current_room == "BS_Cell_1":
                textbutton "Go back to Cell Entrances" action [SetVariable("current_room", "BS_Cell_Entrances") ,Jump ("BS_Cell_Entrances")] style "navigation_menu_textbutton"

            elif current_room == "BS_Cell_2":
                textbutton "Go back to Cell Entrances" action [SetVariable("current_room", "BS_Cell_Entrances") ,Jump ("BS_Cell_Entrances")] style "navigation_menu_textbutton"

            elif current_room == "BS_Cell_3":
                textbutton "Go back to Cell Entrances" action [SetVariable("current_room", "BS_Cell_Entrances") ,Jump ("BS_Cell_Entrances")] style "navigation_menu_textbutton"

            elif current_room == "BS_Bodies_Wall":
                textbutton "Go back to Cell Entrances" action [SetVariable("current_room", "BS_Cell_Entrances") ,Jump ("BS_Cell_Entrances")] style "navigation_menu_textbutton"

            elif current_room == "BS_GoForward_1":
                textbutton "Enter the Guest Bathroom on the left" action [SetVariable("current_room", "BS_Guest_Bathroom"), SetVariable("bsbloodstorage_blast", True)  ,Jump ("BS_Guest_Bathroom")] style "navigation_menu_textbutton"
                textbutton "Go Further in the Basement" action [SetVariable("current_room", "BS_GoForward_2") ,Jump ("BS_GoForward_2")] style "navigation_menu_textbutton"
                textbutton "Go back to the Stairway" action [SetVariable("current_room", "BS_Stage_1") ,Jump ("BS_Stage_1")] style "navigation_menu_textbutton"

            elif current_room == "BS_Guest_Bathroom":
                # if player found explosives and the blood storage wall is not blasted
                if bsexplosives_found and not bsbloodstorage_broken:
                    textbutton "Blow up door" action [SetVariable("bsbloodstorage_broken", True),  SetVariable("current_room", "BS_Guest_Bathroom") ,Jump ("BS_Guest_Bathroom")] style "navigation_menu_textbutton"
                
                #textbutton "Blow up door and enter the Blood Storage" action [SetVariable("bsbloodstorage_broken", True), SetVariable("current_room", "BS_Blood_Storage") ,Jump ("BS_Blood_Storage")] style "navigation_menu_textbutton"

                # if blood storage wall is already blasted
                elif bsbloodstorage_broken:
                    textbutton "Enter the Blood Storage" action [SetVariable("current_room", "BS_Blood_Storage") ,Jump ("BS_Blood_Storage")] style "navigation_menu_textbutton"
  
                textbutton "Exit the Guest Bathroom" action [SetVariable("current_room", "BS_GoForward_1") ,Jump ("BS_GoForward_1")] style "navigation_menu_textbutton"

            elif current_room == "BS_Blood_Storage":
                if bsfoundelectricgloves and bsmotoron:
                    textbutton "Enter the path" action [SetVariable("current_room", "BS_Destroyed_Path") ,Jump ("BS_Destroyed_Path")] style "navigation_menu_textbutton"

                textbutton "Return Back to the Guest Bathroom" action [SetVariable("current_room", "BS_Guest_Bathroom") ,Jump ("BS_Guest_Bathroom")] style "navigation_menu_textbutton"

            elif current_room == "BS_Destroyed_Path":
                textbutton "Go deeper" action [SetVariable("current_room", "BS_Bodies_Room") ,Jump ("BS_Bodies_Room")] style "navigation_menu_textbutton"
                textbutton "Return back to the Blood Storage Room" action [SetVariable("current_room", "BS_Blood_Storage") ,Jump ("BS_Blood_Storage")] style "navigation_menu_textbutton"

            elif current_room == "BS_Bodies_Room":
                textbutton "Go back into the tunnel" action [SetVariable("current_room", "BS_Destroyed_Path") ,Jump ("BS_Destroyed_Path")] style "navigation_menu_textbutton"
 

            elif current_room == "BS_GoForward_2":
                textbutton "Enter the Storage Closet on the left" action [SetVariable("current_room", "BS_Left_Closet") ,Jump ("BS_Left_Closet")] style "navigation_menu_textbutton"
                textbutton "Enter the Private Bathroom in front" action [SetVariable("current_room", "BS_Private_Bathroom") ,Jump ("BS_Private_Bathroom")] style "navigation_menu_textbutton"
                textbutton "Enter the Private Bedroom in front" action [SetVariable("current_room", "BS_Private_Bedroom") ,Jump ("BS_Private_Bedroom")] style "navigation_menu_textbutton"
                textbutton "Go to the right" action [SetVariable("current_room", "BS_TV_Corridor") ,Jump ("BS_TV_Corridor")] style "navigation_menu_textbutton"
                textbutton "Go back" action [SetVariable("current_room", "BS_GoForward_1") ,Jump ("BS_GoForward_1")] style "navigation_menu_textbutton"

            elif current_room == "BS_Left_Closet":
                textbutton "Exit the Storage Closet" action [SetVariable("current_room", "BS_GoForward_2") ,Jump ("BS_GoForward_2")] style "navigation_menu_textbutton"

            elif current_room == "BS_Private_Bathroom":
                textbutton "Exit the Private Bathroom" action [SetVariable("current_room", "BS_GoForward_2") ,Jump ("BS_GoForward_2")] style "navigation_menu_textbutton"

            elif current_room == "BS_Private_Bedroom":
                # if player gained superstrength but the door is not blasted
                if bsfoundsuperstrength and not bsmovedbookshelf:
                    textbutton "Use your power to move the book shelf" action [SetVariable("bsmovedbookshelf", True), SetVariable("current_room", "BS_Private_Bedroom") ,Jump ("BS_Private_Bedroom")] style "navigation_menu_textbutton"

                # if book shelf is already moved and player just has to enter
                elif bsmovedbookshelf:
                    textbutton "Enter the Secret Room" action [SetVariable("current_room", "BS_SecretRoom_PBedroom") ,Jump ("BS_SecretRoom_PBedroom")] style "navigation_menu_textbutton"
                
                textbutton "Exit the Private Bedroom" action [SetVariable("current_room", "BS_GoForward_2") ,Jump ("BS_GoForward_2")] style "navigation_menu_textbutton"

            elif current_room == "BS_SecretRoom_PBedroom":
                textbutton "Exit the Secret Room" action [SetVariable("current_room", "BS_Private_Bedroom") ,Jump ("BS_Private_Bedroom")] style "navigation_menu_textbutton"

            elif current_room == "BS_TV_Corridor":
                textbutton "Go near the TV" action [SetVariable("current_room", "BS_InFront_TV") ,Jump ("BS_InFront_TV")] style "navigation_menu_textbutton"
                textbutton "Enter the Library" action [SetVariable("current_room", "BS_Library") ,Jump ("BS_Library")] style "navigation_menu_textbutton"
                textbutton "Return Back" action [SetVariable("current_room", "BS_GoForward_2") ,Jump ("BS_GoForward_2")] style "navigation_menu_textbutton"

            elif current_room == "BS_InFront_TV":
                textbutton "Return Back" action [SetVariable("current_room", "BS_TV_Corridor") ,Jump ("BS_TV_Corridor")] style "navigation_menu_textbutton"

            elif current_room == "BS_Library":
                # If the player has found the library clue but hasn't moved the wall yet
                if bsfoundlibraryclue and bslibrarydoorclosed:
                    textbutton "Pull the book out" action [
                        SetVariable("bslibrarydoorclosed", False),
                        SetVariable("current_room", "BS_Library"),
                        Jump("BS_Library")
                    ] style "navigation_menu_textbutton"

                # If the wall is already moved
                elif not bslibrarydoorclosed:
                    textbutton "Enter the Hidden Ladder Room" action [
                        SetVariable("current_room", "BS_Ladder_Room"),
                        Jump("BS_Ladder_Room")
                    ] style "navigation_menu_textbutton"
                elif bslibrarydoorclosed:
                    textbutton "Clue not found" style "navigation_menu_textbutton"

                textbutton "Exit the Library" action [
                    SetVariable("current_room", "BS_TV_Corridor"),
                    Jump("BS_TV_Corridor")
                ] style "navigation_menu_textbutton"


            elif current_room == "BS_Ladder_Room":
                textbutton "Use the Ladder" action [SetVariable("current_room", "SF_Library") ,Jump ("SF_Library")] style "navigation_menu_textbutton"
                textbutton "Exit the Secret Ladder Room" action [SetVariable("current_room", "BS_Library") ,Jump ("BS_Library")] style "navigation_menu_textbutton"
   

            
            # SECOND FLOOR NAVIGATION

            elif current_room == "SF_Hallway":
                textbutton "Enter Master Bedroom" action [SetVariable("current_room", "SF_Master_Bedroom"), Jump("SF_Master_Bedroom")] style "navigation_menu_textbutton"
                textbutton "Enter Dusty Library" action [SetVariable("current_room", "SF_Library"), Jump("SF_Library")] style "navigation_menu_textbutton"
                textbutton "Go Down Hallway" action [SetVariable("current_room", "SF_Stage_2"), Jump("SF_Stage_2")] style "navigation_menu_textbutton"
                textbutton "Go Downstairs" action [SetVariable("current_room", "FF_Stage_1"), Jump("FF_Stage_1")] style "navigation_menu_textbutton"

            elif current_room == "SF_Stage_2":
                textbutton "Enter Abandoned Nursery" action [SetVariable("current_room", "SF_Nursery"), Jump("SF_Nursery")] style "navigation_menu_textbutton"
                textbutton "Enter Locked Study" action [SetVariable("current_room", "SF_Study"), Jump("SF_Study")] style "navigation_menu_textbutton"
                textbutton "Enter Grand Balcony" action [SetVariable("current_room", "SF_Balcony"), Jump("SF_Balcony")] style "navigation_menu_textbutton"
                textbutton "Return to Hallway" action [SetVariable("current_room", "SF_Hallway"), Jump("SF_Hallway")] style "navigation_menu_textbutton"

            elif current_room == "SF_Master_Bedroom":
                textbutton "Return to Hallway" action [SetVariable("current_room", "SF_Hallway"), Jump("SF_Hallway")] style "navigation_menu_textbutton"

            elif current_room == "SF_Library":
                textbutton "Search the Bookshelves" action [SetVariable("current_room", "SF_Hidden_Library"), Jump("SF_Hidden_Library")] style "navigation_menu_textbutton"
                if bsfoundlibraryclue:
                    textbutton "Use Ladder to Basement" action [SetVariable("current_room", "BS_Ladder_Room"), Jump("BS_Ladder_Room")] style "navigation_menu_textbutton"
                elif not bsfoundlibraryclue:
                    textbutton "Ladder Blocked" style "navigation_menu_textbutton"
                textbutton "Return to Hallway" action [SetVariable("current_room", "SF_Hallway"), Jump("SF_Hallway")] style "navigation_menu_textbutton"

            elif current_room == "SF_Hidden_Library":
                textbutton "Enter Ritual Chamber" action [SetVariable("current_room", "SF_Ritual_Chamber"), Jump("SF_Ritual_Chamber")] style "navigation_menu_textbutton"
                textbutton "Return to Library" action [SetVariable("current_room", "SF_Library"), Jump("SF_Library")] style "navigation_menu_textbutton"

            elif current_room == "SF_Study":
                if study_unlocked:
                    textbutton "Enter Hidden Study" action [SetVariable("current_room", "SF_Hidden_Study"), Jump("SF_Hidden_Study")] style "navigation_menu_textbutton"
                textbutton "Return to Hallway" action [SetVariable("current_room", "SF_Stage_2"), Jump("SF_Stage_2")] style "navigation_menu_textbutton"
                
            elif current_room == "SF_Hidden_Study":
                textbutton "Enter Ritual Chamber" action [SetVariable("current_room", "SF_Ritual_Chamber"), Jump("SF_Ritual_Chamber")] style "navigation_menu_textbutton"
                textbutton "Return to Study" action [SetVariable("current_room", "SF_Study"), Jump("SF_Study")] style "navigation_menu_textbutton"

            elif current_room == "SF_Ritual_Chamber":
                if ritual_entry_point == "library":
                    textbutton "Return to Hidden Library" action [SetVariable("current_room", "SF_Hidden_Library"), Jump("SF_Hidden_Library")] style "navigation_menu_textbutton"
                elif ritual_entry_point == "study":
                    textbutton "Return to Hidden Study" action [SetVariable("current_room", "SF_Hidden_Study"), Jump("SF_Hidden_Study")] style "navigation_menu_textbutton"
                else:
                    text "You feel lost. There's no clear way back..." style "navigation_menu_textbutton"

            elif current_room == "SF_Nursery":
                textbutton "Return to Hallway" action [SetVariable("current_room", "SF_Stage_2"), Jump("SF_Stage_2")] style "navigation_menu_textbutton"

            elif current_room == "SF_Balcony":
                textbutton "Look Down" action [Hide("navigation_menu"), Jump("look_down_event")] style "navigation_menu_textbutton"
                textbutton "Jump Off" action [Hide("navigation_menu"), Jump("death_scene")] style "navigation_menu_textbutton"
                textbutton "Return to Hallway" action [SetVariable("current_room", "SF_Stage_2"), Jump("SF_Stage_2")] style "navigation_menu_textbutton"
               
            textbutton "Close" action [ Hide("navigation_menu"), Show("navigation_button") ] style "navigation_menu_textbutton"
################################################################################
## Custom Styles for Whispers In The Dark -Tanner + kaushik + Priscilla
################################################################################

# "Navigate" button in the corner
style nav_button_style is default:
    size 24
    color "#ffffff"
    idle_background "#444"
    hover_background "#666"
    selected_background "#666"
    insensitive_background "#222"
    padding (10, 5)

# Frame style for the navigation menu
style navigation_menu_frame is default:
    background Frame("#2B2B2Bcc", 20, 20)  # Rounded corners
    xpadding 40
    ypadding 40


# VBox style inside the navigation menu
style navigation_menu_vbox is vbox:
    spacing 15

# Title text style
style navigation_menu_title is default:
    size 40
    color "#ffffff"
    outlines [(2, "#000000")]
    xalign 0.5

# Textbutton style for navigation options
style navigation_menu_textbutton is default:
    size 26
    color "#ffffff"
    # Explicitly set backgrounds for each button state
    idle_background "#555"
    hover_background "#43ac36"
    selected_background "#3823af"
    insensitive_background "#c02626" #originaly #333, changed for testing
    xpadding 15
    ypadding 10
    xalign 0.5          # orginally 0.5



################################################################################
## Interative Hover areas & Styles - Whispers In The Dark -kaushik
################################################################################


screen hotspot_overlay(hotspots):
    # Draw all hotspot buttons
    for hotspot in hotspots:
        $ x, y, w, h = hotspot["area"]
        $ label = hotspot["label"]
        $ tooltip = hotspot.get("tooltip", "")
        $ image = hotspot["image"]
        $ win_txt = hotspot.get("win_txt", "")
        $ win_lose_exit_label = hotspot["win_lose_exit_label"]
        $ state_var = hotspot["state_var"]

        button:
            xpos x
            ypos y
            xsize w
            ysize h
            action [
                    Hide("hotspot_overlay"),
                    SetVariable("current_hotspot", hotspot),
                    Jump(label)
                    ]
            tooltip tooltip
            focus_mask True
            background Solid("#ffffff40")
            at glow_on_hover

    # Tooltip text in the center of the screen
    if GetTooltip():
        fixed:
            xalign 0.5
            yalign 0.5
            text GetTooltip():
                style "tooltip_text"


style tooltip_text is default:
    color "#ffffff"
    size 30
    xalign 0.5
    text_align 0.5
    outlines [(2, "#ff0000")]


transform fade_tooltip:
    alpha 0.0
    on show:
        linear 0.2 alpha 1.0


transform glow_on_hover:
    on hover:
        linear 0.15 alpha 0.8
    on idle:
        linear 0.15 alpha 0.0



#####################################################################################
## BASEMENT LEFT CLOSET MINI GAME SCREEN & TRANSFORM - Whispers In The Dark -kaushik
#####################################################################################

## The warning for LiveCorip is fine

screen fifteen_scr:

    ##### Timer.
    if timer_on:
        timer 1.0 action If(
            fifteen_timer > 0,
            [SetVariable("fifteen_timer", fifteen_timer - 1), Return("smth")],
            Return("time_is_up")
        ) repeat True
        text str(fifteen_timer) xalign 0.3 yalign 0.1

    ##### Game field.
    frame:
        xalign 0.5 yalign 0.5
        background Solid("#ccc")

        grid grid_width grid_height spacing 0:
            for every_tile in tiles_list:
                if every_tile["tile_value"] == empty_tile_value and not fifteen_is_solved:
                    null
                else:
                    button:


                        # Image mode
                        left_padding 0 right_padding 0 top_padding 0 bottom_padding 0
                        left_margin 0 right_margin 0 top_margin 0 bottom_margin 0
                        add LiveCrop(
                            (
                                (every_tile["tile_value"] - 1) % grid_width * tile_width,
                                (every_tile["tile_value"] - 1) // grid_width * tile_height,
                                tile_width,
                                tile_height
                            ),
                            chosen_img
                        )

                        action [
                            If(
                                every_tile["tile_number"] not in top_row,
                                true=If(
                                    tiles_list[every_tile["tile_number"] - grid_width]["tile_value"] == empty_tile_value,
                                    true=[
                                        SetDict(tiles_list[every_tile["tile_number"] - grid_width], "tile_value", every_tile["tile_value"]),
                                        SetDict(tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value)
                                    ],
                                    false=None
                                ),
                                false=None
                            ),
                            If(
                                every_tile["tile_number"] not in bottom_row,
                                true=If(
                                    tiles_list[min(len(tiles_list) - 1, every_tile["tile_number"] + grid_width)]["tile_value"] == empty_tile_value,
                                    true=[
                                        SetDict(tiles_list[min(len(tiles_list) - 1, (every_tile["tile_number"] + grid_width))], "tile_value", every_tile["tile_value"]),
                                        SetDict(tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value)
                                    ],
                                    false=None
                                ),
                                false=None
                            ),
                            If(
                                every_tile["tile_number"] not in left_column,
                                true=If(
                                    tiles_list[every_tile["tile_number"] - 1]["tile_value"] == empty_tile_value,
                                    true=[
                                        SetDict(tiles_list[every_tile["tile_number"] - 1], "tile_value", every_tile["tile_value"]),
                                        SetDict(tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value)
                                    ],
                                    false=None
                                ),
                                false=None
                            ),
                            If(
                                every_tile["tile_number"] not in right_column,
                                true=If(
                                    tiles_list[min(len(tiles_list) - 1, (every_tile["tile_number"] + 1))]["tile_value"] == empty_tile_value,
                                    true=[
                                        SetDict(tiles_list[min(len(tiles_list) - 1, (every_tile["tile_number"] + 1))], "tile_value", every_tile["tile_value"]),
                                        SetDict(tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value)
                                    ],
                                    false=None
                                ),
                                false=None
                            ),
                            Return("smth")
                        ]

    ##### Control buttons.
    textbutton "Quit" action Jump("quit_fifteen_game") xalign 0.9 yalign 0.1
    textbutton "Show/hide image" action If(
        renpy.get_screen("full_image"),
        Hide("full_image"),
        Show("full_image")
    ) xalign 0.5 yalign 0.1

##### Full image screen.
screen full_image:
    add chosen_img xalign 0.5 yalign 0.5 at pic_trans

transform pic_trans:
    alpha 0.0 zoom 0.7
    on show:
        parallel:
            linear 1.0 alpha 1.0
        parallel:
            linear 0.6 zoom 1.2
            linear 0.4 zoom 1.0
    on hide:
        linear 0.5 alpha 0.0


################################################################################
# On screen image -- Kaushik Naik Guguloth
################################################################################

transform bsmgpull_overlay:
    xpos 1067
    ypos 695
    xsize 145
    ysize 99




################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            #textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)     # removing skip button on sreen
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    #background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with team effort")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
