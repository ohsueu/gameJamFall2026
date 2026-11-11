define a = Character("husky")

default variable = 0


label start:

    scene bg room
    show a default
    $ variable = 0

label q1:
    show a talking 
    a "question 1"
    show a default 
    menu:
        "choice 1":
            a "result for choice 1 (+1)"
            $ variable += 1;
            jump q2
        "choice 2":
            a "result for choice 2 (0)"
            jump q3

label q2:
    show a talking 
    a "question 2"
    show a default 
    menu:
        "choice 1":
            a "result for choice 1 (0)"
            jump q3
        "choice 2":
            a  "result for choice 2 (+1)"
            $ variable += 1;
            jump q3

label q3:
    show a talking 
    a "question 3"
    show a default 
    menu:
        "question 3"
        "choice 1":
            a "result for choice 1 (+1)"
            $ variable += 1;
            jump q4
        "choice 2":
            a "result for choice 2 (+2)"
            $ variable += 2;
            jump q4

#6 different possiblilities
#1 path for 4 (choice 1 -> 2 -> 2)
#2 paths for 3 (choice 1 -> 2 -> 1 || 1 -> 1 -> 2)
#2 paths for 2 (choice 1 -> 1 -> 1 || 2 -> 2)
#1 path for 1 (2 -> 1)
label q4:
    "calculating total score ... (click to continue)"
    pause 1.0
    if variable == 4:
        jump best_ending
    if variable >= 2:
        jump good_ending
    elif variable == 1:
        jump bad_ending
    else:
        jump error_screen

label best_ending:
    a "best ending achieved (4 points)"
    menu:
        "go back to menu":
            jump start
        "exit":
            jump end

label good_ending:
    a "good ending achieved (2-3 points)"
    menu:
        "go back to menu":
            jump start
        "exit":
            jump end

label bad_ending:
    a "bad ending achieved (1 point)"
    menu:
        "go back to menu":
            jump start
        "exit":
            jump end

label error_screen:
    a "An error occured, what would you like to do?"
    menu:
        "go back to menu":
            jump start
        "exit":
            jump end

label end:
    a "thank you for playing!"
    $ renpy.quit()
