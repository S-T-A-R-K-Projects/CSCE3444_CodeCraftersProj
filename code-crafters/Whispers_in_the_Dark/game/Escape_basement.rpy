#quest to excape from teh basement 
#emily quest 
#thomas quest
#escape 
# make the picture for the locket
################################################################################

screen locket_image():
    imagebutton:
        idle "images/First_Floor/MiniGame/emilysize_LKT.png"
        hover "images/First_Floor/MiniGame/emilysize_LKT_Exam.png"  # Changes cursor to a magnifying glass when hovering
        xpos 550 # Adjust to where the book is on the bookshelf
        ypos 650
        xsize 50 # Size of the hover area
        ysize 50
        action Show("examine_locket")  # Opens the examine menu

screen examine_locket():
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

            text "This looks like a emily locket..." size 28 color "#FFFFFF"
            textbutton "Close" action Hide("examine_locket") text_size 30

# make the picture for the book
################################################################################
screen bookshelf_thomasscreen():
    imagebutton:
        idle "images/First_Floor/MiniGame/Book_Item.png"
        hover "images/First_Floor/MiniGame/Book_Item_Exam.png"  # Changes cursor to a magnifying glass when hovering
        xpos 1000  # Adjust to where the book is on the bookshelf
        ypos 850
        xsize 75  # Size of the hover area
        ysize 61
        action Show("examine_thomasbk")  # Opens the examine menu

screen examine_thomasbk():
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

            text "i lived 1978 to 1984." size 28 color "#f30909"
            textbutton "Close" action Hide("examine_thomasbk") text_size 30

#create the nps that can intract once you get the locetk 


