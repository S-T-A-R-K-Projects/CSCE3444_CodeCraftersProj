
init -1:

    image bg_tonnel = Movie(
        size=(1920, 1080),
        channel="movie",
        fps=60,
        play="images/Basement/minigames/bsmgtunnelvideo.mp4",
        loop=True
    )
    image bg_tonnel_v3 = Movie(
        size=(1920, 1080),
        channel="movie",
        fps=60,
        play="images/Basement/minigames/bsmgtunnelvideo.ogv",
        loop=True
    )
    image bg_tonnel_v2 = Movie(
        fps=60,
        play="images/Basement/minigames/bsmgtunnelvideo.mov"
    )

    image run_guy = Animation(
        'images/Basement/minigames/player_run/1.png',   0.1,
        'images/Basement/minigames/player_run/2.png',   0.1,
        'images/Basement/minigames/player_run/3.png',   0.1,
        'images/Basement/minigames/player_run/4.png',   0.1,
        'images/Basement/minigames/player_run/5.png',   0.1,
        'images/Basement/minigames/player_run/6.png',   0.1,
        'images/Basement/minigames/player_run/7.png',   0.1,
        'images/Basement/minigames/player_run/8.png',   0.1,
        'images/Basement/minigames/player_run/9.png',   0.1,
        'images/Basement/minigames/player_run/10.png',  0.1,
        'images/Basement/minigames/player_run/11.png',  0.1,
        'images/Basement/minigames/player_run/12.png',  0.1,
        'images/Basement/minigames/player_run/13.png',   0.1
    )

    image conus = 'images/Basement/minigames/conus.png'


transform conus_move_mid:
    xalign 0.5
    zoom 0.2
    ypos 560
    linear 2.0 zoom 1.4 ypos 1080

transform conus_move_right:
    xalign 0.53
    zoom 0.2
    ypos 560
    linear 2.0 zoom 1.4 ypos 1080 xalign 0.9

transform conus_move_left:
    xalign 0.47
    zoom 0.2
    ypos 560
    linear 2.0 zoom 1.4 ypos 1080 xalign 0.1

transform alpha_but_left:
    alpha 0.6

transform alpha_but_right:
    alpha 0.6
    zoom -1


init -1:
    # obstacle patterns
    $ level_left_arr   = [1,0,1,1,0,1,1,0,0,1,0,0,1]
    $ level_mid_arr    = [1,1,1,0,0,0,1,1,0,1,0,1,0]
    $ level_right_arr  = [0,0,0,1,1,1,0,1,1,0,1,0,1]

    # starting state
    $ current_trap     = 0          # which obstacle pattern we're on
    $ player_xpos      = 1          # 0=left,1=mid,2=right
    $ conus_pauses     = True       # warm-up state
    $ timer_pause      = 5          # show "Avoid obstacles" for 3 sec
    $ points           = 0          # distance swum (ft)


screen main_game:
    modal True
    add "bg_tonnel_v3"

    if conus_pauses:
        # 5-second warm-up
        text "You must swim 150 ft"
        text "Start avoiding obstacles in " + str(timer_pause) + " sec" align .5, .5
        timer 1 repeat True action SetVariable("timer_pause", timer_pause-1)
        timer 3 action SetVariable("conus_pauses", False)

    else:
        # end at 150 ft
        timer 0.1 repeat True action If(points >= 150, Jump("minigame_end"))

        # accumulate distance
        timer 0.3 repeat True action SetVariable("points", points + 1)
        text "Swim - " + str(points) + " ft" xalign 0.5 ypos 10

        # filling progress bar
        bar value AnimatedValue(value=points, range=150) ypos 50 xalign 0.5 xmaximum 300

        # loop obstacle patterns every 1.5 sec
        timer 1.5 repeat True action SetVariable(
            "current_trap",
            (current_trap + 1) % len(level_left_arr)
        )

        # left obstacle
        if level_left_arr[current_trap] == 1:
            timer 1.2 action If(player_xpos == 0, Jump("gamez_over"))
            add "conus" at conus_move_left

        # middle obstacle
        if level_mid_arr[current_trap] == 1:
            timer 1.2 action If(player_xpos == 1, Jump("gamez_over"))
            add "conus" at conus_move_mid

        # right obstacle
        if level_right_arr[current_trap] == 1:
            timer 1.2 action If(player_xpos == 2, Jump("gamez_over"))
            add "conus" at conus_move_right

    # draw the player
    if player_xpos == 0:
        add "run_guy" xpos -450
    elif player_xpos == 1:
        add "run_guy" xpos 0
    elif player_xpos == 2:
        add "run_guy" xpos 450

    # lane-change buttons
    imagebutton:
        idle 'images/Basement/minigames/arrow_button.png'
        hover 'images/Basement/minigames/arrow_button.png'
        focus_mask True
        yalign 0.8 xalign 0.1
        at alpha_but_left
        action If(player_xpos > 0, SetVariable("player_xpos", player_xpos - 1))

    imagebutton:
        idle 'images/Basement/minigames/arrow_button.png'
        hover 'images/Basement/minigames/arrow_button.png'
        focus_mask True
        yalign 0.8 xalign 0.9
        at alpha_but_right
        action If(player_xpos < 2, SetVariable("player_xpos", player_xpos + 1))

    key "K_LEFT"  action If(player_xpos > 0, SetVariable("player_xpos", player_xpos - 1))
    key "K_RIGHT" action If(player_xpos < 2, SetVariable("player_xpos", player_xpos + 1))


screen gamez_over:
    modal True
    add 'images/Basement/minigames/bg bsmgrunnerdeath.png'

    vbox:
        xalign 0.5
        yalign 0.7     
        spacing 20

        text ''  

        hbox:
            spacing 10
            xalign 0.5   

            frame:
                textbutton 'TRY AGAIN' text_size 38 action Jump('BS_Drainway')
            frame:
                textbutton 'END GAME'  text_size 38 action Jump('bsquittomainmenu') 



label gamez_over:
    hide screen main_game
    play audio 'audio/bsmgbad_end.mp3'
    show screen gamez_over
$ renpy.pause(hard=True)


label bsmgrunnerstart:
    stop audio
    # reset everything for a fresh run
    $ player_xpos  = 1
    $ current_trap  = 0
    $ points        = 0
    $ conus_pauses  = True
    $ timer_pause   = 5

    hide screen navigation_menu
    hide screen navigation_button
    hide screen character_stats_hud

    stop music
    pause 1
    play music 'audio/bsmgrunner.wav' fadeout 1 loop volume 0.5
    # Pale white faces by Victor_Natas -- https://freesound.org/s/784662/ -- License: Attribution 4.0

    show screen main_game
    $ renpy.pause(hard=True)

# runs until 150 ft, then ends
label minigame_end:
    hide screen main_game
    stop music
    pause 0.3
    hide screen navigation_menu
    hide screen navigation_button
    hide screen character_stats_hud
    scene bg bsmanholecomingout with fade
    play audio "audio/bsclimbingout.wav" volume 1.0             # boots on aluminum ladder 02 by Eelke -- https://freesound.org/s/462599/ -- License: Attribution 4.0
    "That was crazy"
    $ renpy.pause(4.5)

    scene bg bsmanholeout with fade
    "I can't beleive I made it out"
    "It was a big mistake coming here"
    "I don't want stay here another second"

    stop audio
    stop music
    call bsmgscreens

    scene bg bsendgamescreen with fade
    play audio "audio/bsendgamemusic.flac" volume 0.6 loop          # Calm Hopeful Drone Loop by qubodup -- https://freesound.org/s/750921/ -- License: Attribution 4.0
    pause
    return
    

label bsquittomainmenu:
    return

