label after_surgery:

scene black
with fade

play music "sounds/Doctors Office Dark.mp3"

"You awake with a tremendous amount of pain around your chest."

show black
with dissolve

show ceiling_dark
with fade

"As you open your eyes, the light is blinding."

"The light hurts so much, more than it ever has."

show ceiling_light
with dissolve

"You sit up."

show dark_office
with fade

"As your eyes adjust, you realize that the world is devoid of color."

show office_after
with dissolve

"It is mostly gray, with barely any splashes of blues and purples."

"The welcoming feeling is gone."

"The office is eerily empty. You get up and turn toward the door."

"You notice that there is a mirror on the back of it."

"What do you want to do?"

menu:
    "Certainly not look in it, if that's what you were asking.":
        "I mean, you're going to have to go through the door eventually."
        jump mirror_2


    "I mean, I guess it would make me feel better to see my hair.":
        "I'll go out into the hallway after looking at the mirror."
        jump mirror_2

    "I wonder if I have a cool scar.":
        "Why is there nobody here?"
        jump mirror_2




