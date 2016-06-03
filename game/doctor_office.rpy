label doctor_office: 

scene poster
with fade

sign "This is a safe and healthy procedure. Heart removal is just taking the easy steps from childhood into adulthood."

sign "Lose the baby weight, become an independent adult. What's there to lose? Try it today!"

scene doctor_office

"You look away from the sign, towards the rounded doctor. This is it, this is your time to shine."

show doctor

doctor "If I could just have you sign here, we can get started immediately."

"The doctor hands you a clipboard."

python:
    yourname = renpy.input("Please sign here.")
    yourname = yourname.strip()
    yourname = yourname.capitalize()
doctor "Thank you [yourname]. Wait for just a moment while I file this away."

hide doctor
with dissolve

jump mirror