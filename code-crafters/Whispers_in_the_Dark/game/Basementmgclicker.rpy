init python:
    # center the game window on screen
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    # automatic image declaration
    config.automatic_images_minimum_components = 1
    config.automatic_images = [' ', '_', '/']
    config.automatic_images_strip = ['images']

    # flash effects
    flash  = Fade(.25, 0, .5, color="#fff")
    flash2 = Fade(.25, 0, .5, color="#222")

    # ─── game settings ────────────────────────────────────────────
    # maximum gauge value
    max_points = 100
    # base image name (without frame numbering)
    img_name   = "bg bstvjumpscare"
    # first and last animation frames
    minN = 1
    maxN = 14
    # amount added to gauge per click (i.e., difficulty: 2.0 = very hard, 3.0 = easy)
    points_plus = 2.5

    # ─── default variables ───────────────────────────────────────
    # optionally adjust this to fine-tune game balance
    points_minus = 1.0
    # allowed time between clicks or animation speed (seconds per frame)
    ani_time = .1
    # current frame
    number = 0
    # frame increment (+1 or -1)
    plus = 1
    # current gauge value
    points = 0
    # was there a recent click?
    clicked = True

    # advance animation if clicked recently, then redraw screen
    def NextFrameF():
        global points, number, plus, clicked

        # if clicked recently, continue animation; otherwise pause
        if clicked:
            # next or previous frame
            number += plus
            # if beyond frame range, reverse direction
            if number > maxN:
                number = maxN - 1
                plus = -plus
            if number < minN:
                number = minN + 1
                plus = -plus

        # decrease gauge if not clicked recently
        points -= points_minus
        if points < 0:
            points = 0

        clicked = False
        # redraw screen
        renpy.restart_interaction()

    # wrap function as an action
    NextFrame = renpy.curry(NextFrameF)


# ─── clicker screen ────────────────────────────────────────────
screen clicker:
    # prevent the game from advancing on any click outside our button
    modal True

    # reset animation and click flag when showing this screen
    on "show" action [
        SetVariable("number", 0),
        SetVariable("plus",   1),
        SetVariable("clicked", True)
    ]

    # timer to update frame and check for loss
    timer ani_time repeat True action [
        NextFrame(),
        If(points <= 0,
        true=Return(False),
        false=NullAction())
    ]

    # draw the animated image
    add img_name + str(number)

    # invisible full-screen button: increases gauge and sets clicked flag
    button:
        text _(" ")
        xfill True
        yfill True
        background "#00000001"
        action [
            SetVariable("points", points + points_plus),
            SetVariable("clicked", True),
            If(points >= max_points,
            true=Return(True),
            false=NullAction())
        ]

    # alternative input via keyboard
    key "K_SPACE" action [
        SetVariable("points", points + points_plus),
        SetVariable("clicked", True),
        If(points >= max_points,
        true=Return(True),
        false=NullAction())
    ]

    # gauge indicator
    vbar value StaticValue(points, max_points):
        align       (3, 0.9)       # position on screen
        maximum     (384,384)   # size
        left_bar    "bsmgredskull" # empty heart image
        right_bar   "bsmgblackskull"      # full heart image
        thumb       None         # no thumb separator
        thumb_shadow None        


label bsclickermg:
    # some initial visual setup
    scene expression (img_name + "0")
    pause .5
    show expression Text("Get ready! to start clicking FAST") at truecenter as txt
    with dissolve
    pause
    hide txt

    # start with 10 points so you don't lose immediately
    $ points = 10

    # ─── run the clicker mini-game ───────────────────────────────
    call screen clicker

    # ─── show results ────────────────────────────────────────────
    if _return:
        # fast-forward animation to last frame
        while number < maxN:
            $ number += 1
            scene expression (img_name + str(number))
            $ renpy.pause(ani_time, hard=True)
        scene expression (img_name + str(maxN))
        with flash
        $ setattr(renpy.store, current_hotspot["state_var"], True)
        play sound "audio/bsmgclickerscream.wav" volume 0.6 # Ghost Scream by onderwish -- https://freesound.org/s/469141/ -- License: Creative Commons 0
        $ renpy.pause(2.5, hard=True)
        show expression Text("Victory! \nYou have received explosives\nLook around the basement to use them ") at truecenter as txt
        $ bsexplosives_found = True
        $ renpy.pause(3.8, hard=True)
        jump expression current_hotspot["win_lose_exit_label"]
    else:
        # fast-forward animation back to first frame
        while number > 1:
            $ number -= 1
            scene expression (img_name + str(number))
            $ renpy.pause(ani_time, hard=True)
        scene expression (img_name + "0")
        with flash2
        show expression Text("Defeat.") at truecenter as txt
        play sound "audio/bsmgclickerexplosion.wav" volume 0.6 # Self Destruct/Alpha-11 Warhead Explosion by FusionWolf3740 -- https://freesound.org/s/568877/ -- License: Creative Commons 0
        scene bg bstvjumpscare00 with fade
        menu:
            "Try again":
                $ setattr(renpy.store, current_hotspot["state_var"], False)
                jump expression current_hotspot["win_lose_exit_label"]

            "No, quit to the main menu.":
                return

    # hard pause in case the player is still mashing the button
    $ renpy.pause(1.0, hard=True)
    hide txt
    with dissolve
    