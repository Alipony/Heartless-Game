# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image black = "images/black.jpg"
image poster = "images/heart_removal_poster.png"
image mirror = im.Scale("images/Main character.png", 1200, 800)
image doctor_office = "images/room_before_surgery.png"
image dark_office = "images/waking_up_room.png"
image office_after = "images/waking_up_room_full.png"
image ceiling_light = "images/ceiling_light.jpg"
image ceiling_dark = "images/ceiling_dark.png"
image doctor = im.Scale("images/doctor.png", 1200,800)
# Declare characters used by this game.

define sign= Character('Poster', color="#010101")
define you = Character('[yourname]', color="#630381")
define doctor = Character('Doctor', color="#464646")
define obama = Character('Obama', color="#A92626")


# The game starts here.
label start:

play music "sounds/Doctors Office.mp3"

jump doctor_office
