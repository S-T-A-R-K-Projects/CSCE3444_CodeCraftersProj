##### modularied basement corss moving puizzle minigame
##### 

label fifteen_game:

    ##### Game setup
    $ grid_width = 3
    $ grid_height = 3
    $ chosen_img = current_hotspot["image"]
    $ chosen_img_width, chosen_img_height = renpy.image_size(chosen_img)
    $ tile_width = int(chosen_img_width / grid_width)
    $ tile_height = int(chosen_img_height / grid_height)

    $ top_row = [i for i in range(grid_width)]
    $ bottom_row = [grid_width * (grid_height - 1) + i for i in range(grid_width)]
    $ left_column = [grid_width * i for i in range(grid_height)]
    $ right_column = [grid_width * (i + 1) - 1 for i in range(grid_height)]

    $ tiles_list = []
    python:
        for i in range(grid_height):
            for j in range(grid_width):
                tiles_list.append({"tile_number": (i * grid_width + j), "tile_value": (i * grid_width + (j + 1))})

    $ empty_tile_value = renpy.random.randint(1, grid_width * grid_height)

    $ fifteen_is_solved = False
    $ fifteen_timer = 300
    $ timer_on = False

    show screen fifteen_scr

    $ shuffle_moves = 21
    label tiles_shuffle:
        if shuffle_moves > 0:
            python:
                possible_moves_list = []
                for j in tiles_list:
                    if j["tile_value"] == empty_tile_value:
                        if j["tile_number"] not in top_row:
                            possible_moves_list.append("top")
                        if j["tile_number"] not in bottom_row:
                            possible_moves_list.append("bottom")
                        if j["tile_number"] not in left_column:
                            possible_moves_list.append("left")
                        if j["tile_number"] not in right_column:
                            possible_moves_list.append("right")
                        move_tile = renpy.random.choice(possible_moves_list)
                        if move_tile == "top":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"] - grid_width]["tile_value"]
                            tiles_list[j["tile_number"] - grid_width]["tile_value"] = empty_tile_value
                        elif move_tile == "bottom":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"] + grid_width]["tile_value"]
                            tiles_list[j["tile_number"] + grid_width]["tile_value"] = empty_tile_value
                        elif move_tile == "left":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"] - 1]["tile_value"]
                            tiles_list[j["tile_number"] - 1]["tile_value"] = empty_tile_value
                        elif move_tile == "right":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"] + 1]["tile_value"]
                            tiles_list[j["tile_number"] + 1]["tile_value"] = empty_tile_value
                        shuffle_moves -= 1
                        renpy.jump("tiles_shuffle")

    $ timer_on = True

    label fifteen_game_loop:
        $ result = ui.interact()
        $ fifteen_timer = fifteen_timer
        if result == "time_is_up":
            jump fifteen_lose
        python:
            for j in tiles_list:
                if j["tile_value"] - 1 != j["tile_number"]:
                    renpy.jump("fifteen_game_loop")
        jump fifteen_win

label fifteen_win:
    $ timer_on = False
    $ renpy.pause(0.1, hard=True)
    $ renpy.pause(1, hard=True)
    $ fifteen_is_solved = True
    "You win!"
    "[ current_hotspot['win_txt'] ]"
    hide screen fifteen_scr
    $ setattr(renpy.store, current_hotspot["state_var"], True)
    jump expression current_hotspot["win_lose_exit_label"]

label fifteen_lose:
    $ timer_on = False
    $ renpy.pause(0.1, hard=True)
    $ renpy.pause(0.1, hard=True)
    "Too slow... Try again."
    hide screen fifteen_scr
    jump expression current_hotspot["win_lose_exit_label"]

label quit_fifteen_game:
    hide screen fifteen_scr
    "Enough for now..."
    jump expression current_hotspot["win_lose_exit_label"]



label BS_Cell_1_PULL:
    $ setattr(renpy.store, current_hotspot["state_var"], True)
    "[ current_hotspot['win_txt'] ]"
    jump expression current_hotspot["win_lose_exit_label"]

label BS_Cell_2_PULL:
    $ setattr(renpy.store, current_hotspot["state_var"], True)
    "[ current_hotspot['win_txt'] ]"
    jump expression current_hotspot["win_lose_exit_label"]

label BS_Cell_3_PULL:
    $ setattr(renpy.store, current_hotspot["state_var"], True)
    "[ current_hotspot['win_txt'] ]"
    jump expression current_hotspot["win_lose_exit_label"]


label BS_Private_Bathroom_Hammer:
    $ setattr(renpy.store, current_hotspot["state_var"], True)
    "[ current_hotspot['win_txt'] ]"
    jump expression current_hotspot["win_lose_exit_label"]
    

label FF_Hidden_1_Key_Get:
    $ setattr(renpy.store, current_hotspot["state_var"], True)
    "[ current_hotspot['win_txt'] ]"
    jump expression current_hotspot["win_lose_exit_label"]