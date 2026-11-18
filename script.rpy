define a = Character("husky")

default variable = 0


label start:
    play music "gamejam_songs - Track 01 (Roll Em).wav"

    scene bg room
    show a default
    $ variable = 0

label q1:
    show a talking 
    a "Hello, welcome to the quiz! You will be asked 5 questions, and your score will be calculated at the end. Good luck!"
    a "What is the best color?"
    show a default 
    menu:
        "purple":
            a "Correct!"
            $ variable += 1;
            jump q2
        "blue":
            a "Incorrect."
            jump q2

label q2:
    show a talking 
    a "What is the best city?"
    show a default 
    menu:
        "Seattle":
            a "Not quite.."
            jump q3
        "Tacoma":
            a "Correct!" 
            $ variable += 1;
            jump q3

label q3:
    show a talking 
    a "What is my name?"
    show a default 
    menu:
        "Dubs":
            a "Incorrect..." 
            $ variable += 0;
            jump q4
        "Hendrix":
            a "Correct! I am named after Jimi Hendrix."
            $ variable += 2;
            jump q4

label q4:
    show a talking 
    a "What is the best animal?"
    show a default 
    menu:
        "Dog":
            a "Yes... perfect."
            $ variable += 1;
            jump q5
        "Cat":
            a "..." 
            jump q5

label q5:
    show a talking 
    a "What is the best department?"
    show a default 
    menu:
        "School of Engineering and Technology":
            a "Trick question they are all great! Deducting 2 points."
            $ variable -= 2;
            jump results
        "...":
            a "So hard to choose! They are all great, aren't they?" 
            jump results

label results:
    "calculating total score ... (click to continue)"
    pause 1.0
    if variable == 5:
        jump best_ending
    if variable >= 2:
        jump good_ending
    elif variable >= -2:
        jump bad_ending
    else:
        jump error_screen

label best_ending:
    a "Perfect score (5 points)!"
    menu:
        "go back to menu?":
            jump start
        "exit":
            jump end

label good_ending:
    a "Passing score (2 to 4 points)! Good job!"
    menu:
        "go back to menu?":
            jump start
        "exit":
            jump end

label bad_ending:
    a "Failing score (-2 to 1 point). Better luck next time!"
    menu:
        "go back to menu?":
            jump start
        "exit":
            jump end

label error_screen:
    a "An error occured, what would you like to do?"
    menu:
        "go back to menu?":
            jump start
        "exit":
            jump end

label end:
    a "thank you for playing!"
    $ renpy.quit()
