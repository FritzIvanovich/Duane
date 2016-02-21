label arcade:

    # Beginning of Tomoko Route

    scene bg arcade
    with dissolve
    play music "bgm/arcade.mp3"

    d "Hell yeah, thats what I'm TALKING about!"

    label arcade_runner:
        menu:
            "Play for some time":
                d "Now for some elite 420 tacticool gaming."
                d "Gonna rek sum scrublords in this here fa-shizzle my nizzle."
                d "Where the No scoping machine at?"

                if yassan == True and ran_away == False:
                    d "Eh?"
                    d "The only quickscoper machine is already occupied."
                    d "Hey? Are you finished soon you fukin' scrub?"
                    "The person standing at the machine turned around ..."
                    "Duane immediately recognized that it was someone he has seen before ..."
                    d "Oh fuck! I gotta use my Special Technique!"
                    "Duane learned Ability : <Joestar Family's Secret Technique>"

                    menu:
                        "Use <Joestar Family's Secret Technique>":
                            $ ran_away = True
                            "The girl stood up menacingly, a faint smile on her lips"
                            "Then she started slowly walking towards Duane"
                            d "There is no time! I have to use it NOW!"
                            d "Nigerun dayo!"
                            "Duane got away safely!"
                        "Stand your ground":
                            "Duane got rekt!"
                            "Duane lost 1 Sanity Point!"
                            d "Dayum, I better not challenge her ever again!"
                            d "That Girl is totally scary!"
                            jump arcade_runner

                elif yassan == True:
                    "But what if that girl is still around, I better be careful"
                    "Better to avoid going to the MLG section of the arcade!"
                    jump arcade_runner

                "Duane played Duanes Magical Weed Adventure."
                "Duane leveled up!"
                "Duanes Intelligence decreased by 1!"
                "Duanes Dextery increased by 1!"
                "Duane gained 420 experience!"
                "In the arcade game of course, what did you expect?"
                "This is not a fucking RPG!"
                "Now get on with the maingame, you fucking nerd."

                jump arcade_runner

            "Look around this place":

                d "Maybe I'll take a quick walk aroud and check this place out first"

                play sound "sfx/steps.mp3"
                with Fade(0.5, 3.0, 0.5)
                with hpunch

                un "uhm ... "
                un "e-e-e-e ..."
                un "... ex-excuse ..."
                d "Huh?"
                un "... ummmmm ..."
                un "e-excuse ..."
                un "... me ..."
                d "Eh?"
                "Where's that voice coming from?"
                "Am I just imagining things?"

        show tomo normal
        with dissolve
        un "Ummm ..."
        un "I'm s-s-s-sorry ... "
        un "... but ..."
        "Oh it was a girl ..."
        "But her voice is so weak, you can hardly hear her over the sound of the arcade games"

        d "What do you want from me?"

<<<<<<< HEAD

        jump elTomo

label elTomo:
    return
=======
        jump cafeTomo

label cafeTomo:
    # show starfucks cafe
    return
>>>>>>> fa467ac2a4981124bdb4f26999846c1aa872d9b0
