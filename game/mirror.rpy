label mirror:

scene mirror
with dissolve


"You get up and look at yourself in the mirror."

"You have always had such a big heart."

"A hundred years ago that would have been a compliment. But not anymore."


"You hear the doctor start to open the door and quickly sit back down."

scene doctor_office

show doctor

doctor "Alrighty [yourname]! Are you ready?"

menu:

    "Nod your head willingly":
      jump doctor

    "Stare straight ahead":
      jump doctor

    "No"
      jump doctor

label doctor:

doctor "Okay, Here we go!"

show ceiling_light
with fade

"For a second, you think about asking if they could wait a minute before they start."

"But it's too late. You can already feel the anesthesia entering your system."

show ceiling_dark
with dissolve

doctor "Okay, just breathe deeply. You're going to look so much better after this is done."

stop music

show black
with fade

show black
with fade

jump after_surgery