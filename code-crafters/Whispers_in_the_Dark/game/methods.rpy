#Folder for custom methods and functions

init python:
    def jumpscare(image, sound=None, duration=0.5, shake=True, fade_out=True):
        """
        Creates a jumpscare effect in the game.
        
        Arguments:
        - image (str): Path to the jumpscare image.
        - sound (str, optional): Path to the jumpscare sound effect.
        - duration (float, optional): How long the jumpscare lasts (default 0.5 seconds).
        - shake (bool, optional): Whether to shake the screen (default True).
        - fade_out (bool, optional): Whether to fade out after (default True).
        """
        
        renpy.show(image, at_list=[Position(xalign=0.5, yalign=0.5)], zorder=100)  # Center image

        if sound:
            renpy.play(sound)  # Play jumpscare sound if provided
        
        if shake:
            renpy.with_statement(hpunch)  # Simulated shake

        #renpy.pause(duration)  # Hold for the set duration

        if fade_out:
            renpy.show(image, at_list=[fadeout])  # Apply fading transform
            renpy.pause(1.0)  # Wait for fade-out to complete
            renpy.hide(image)  # Remove the image after fading

        renpy.pause(0.2)  # Small pause before resuming gameplay
   
   
    minimap_images = {
        "FF_Stage_1": "ff_map_Stage1",
        "FF_Stage_2": "ff_map_Stage2",
        "FF_Stage_3": "ff_map_Stage3",
        "FF_Stage_4": "ff_map_Stage4",

        "FF_Hidden_1": "ff_map_Hidden1",
        "FF_Hidden_2": "ff_map_Hidden2",

        "FF_Room_1": "ff_map_Room1",
        "FF_Room_2": "ff_map_Room2",

        "FF_Office": "ff_map_Office",
        "FF_Living_Room": "ff_map_Living",
        "FF_Kitchen": "ff_map_Kitchen",
        "FF_Dinning": "ff_map_Dinning",
        "FF_Garden": "ff_map_Garden",

        "FF_Sus_Room": "ff_map_Sus",
        "FF_Front_Room": "ff_map_FrontRoom",
        # Basement
        "BS_Stage_1": "BS_Map_Stage_1",
        "BS_Under_Stairway": "BS_Map_Under_Stairway",
        "BS_Torture_Chamber": "BS_Map_Torture_Chamber",
        "BS_Chamber_Storage": "BS_Map_Chamber_Storage",
        "BS_Cell_Entrances": "BS_Map_Cell_Entrances",
        "BS_Electric_Room": "BS_Map_Electric_Room",
        "BS_Drainway": "BS_Map_Drainway",
        "BS_Cell_1": "BS_Map_Cell_1",
        "BS_Cell_2": "BS_Map_Cell_2",
        "BS_Cell_3": "BS_Map_Cell_3",
        "BS_Bodies_Wall": "BS_Map_Bodies_Room", #"BS_Map_Bodies_Wall",
        "BS_GoForward_1": "BS_Map_GoForward_1",
        "BS_Guest_Bathroom": "BS_Map_Guest_Bathroom",
        "BS_Blood_Storage": "BS_Map_Blood_Storage",
        "BS_Destroyed_Path": "BS_default", #"BS_Map_Destroyed_Path",
        "BS_Bodies_Room": "BS_Map_Bodies_Room",
        "BS_GoForward_2": "BS_Map_GoForward_2",
        "BS_Left_Closet": "BS_Map_Left_Closet",
        "BS_Private_Bathroom": "BS_Map_Private_Bathroom",
        "BS_Private_Bedroom": "BS_Map_Private_Bedroom",
        "BS_SecretRoom_PBedroom": "BS_Map_SecretRoom_PBedroom",
        "BS_TV_Corridor": "BS_Map_TV_Corridor",
        "BS_InFront_TV": "BS_Map_InFront_TV",
        "BS_Library": "BS_Map_Library",
        "BS_Ladder_Room": "BS_Map_Ladder_Room",
        "BS_default" : "BS_Map_Default",
    }



    