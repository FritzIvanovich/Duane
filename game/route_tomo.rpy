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
                "Duane gained 420 experience!"
                play sound "sfx/skillUp.mp3"
                "Duane leveled up!"
                "Duanes Intelligence decreased by 1!"
                "Duanes Dextery increased by 1!"
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
        # some conversation
        " Filler"
        d "Gotta go now, bye!"
        hide tomo far
        with dissolve
        show black
        with dissolve
        "Oh man ... filler"
        jump cafeTomo


label cafeTomo:

    # something that leads to duane finding this place
    play music "bgm/seamoon.mp3"
    scene bg cafetomo
    with dissolve

    d "This is a really nice place. I crave for some freshly coffee so badly!"
    "After I met that strange girl earlier, I feel strangly exhausted."
    "A cup of coffee ought to bring me back up to speed!"

    sk "Well, hello there fellow!"
    show bear at left
    with dissolve
    sk "How may I help you?"
    menu:
        "A Polar bear ?!":
            d "Wha-?"
            "What the fuck is a bear doing in here?!"
            sk "Don't worry. I'm not dangerous."
            d "Whoa, I almost had a heart attack right there!"
            d "What's a polar bear doing here?"
            sk "Haha, I get that a lot."
            sk "I'm the owner of this place, Café Tomo."
            sk "And my name is Shirokuma, nice to meet you."
            "Wow, i was shocked for a second, but it seems like this guy is a pretty swell dude!"
            d "Oh, uuuh..."
            d "I'm Duane!"
            d "The best Quickscoper on this side of the Grand Line!"
            "Duane thumbs his chest with pride"
            "But he doesn't realize how stupid this really looks like"
            d "What the fuck did you just say?!"
            "I mean, who brags with stupid shit like that?"
            d "Oy, come on, this game is all about MLG! Of course this happens!"
            "Ah well, then it can't be helped ..."
            d "Dont give me that!"
            d "What's MLG to you then?!"
            "Psssht, you should stop talking to yourself there matey, the polarbear looks confused"
            d "Ah fu--, I mean ..."
            d "*cough* *cough*"
            sk "Oooo-kaaay? ..."
            sk "Well, it's not really worth asking who you are talking to, I guess."
        "Run!":
            d "Oh fuck! Better run!"
            sk "Don't be so hasty!"
            sk "I'm not after your life."
            sk "I'm just a shopowner here."
            "Why am I still here, I should have run away like sanic!"
            "But something tells me I can trust this creature."
            "Duanes Trust increased by 2"
            d "Okay, I'll stay, for now ..."
            d "So ... What's the deal with you?"
            sk "Well, simply put..."
            sk "I own this here Café Tomo."
            sk "My name is Shirokuma. As you can see I'm a polarbear."
            d "Duh, no shit sherlock!"
            d "But that's really suprising."
            d "A bear leading business and all ..."
            sk "What are you talking about, as far as I know there's a lot of other stores like this here around town."
            "Oh fuck, it seems like I haven't explored this town enough."
            d "Oh, haha, sorry."
            "Better find some cheap excuse ... and quick."
            d "But actually ... I'm not from around these parts."
            "That's technically true, i guess."
            sk "Really? Oh, where are you from then. I love sharing stories with foreigners."
            "Damn, that backfired."
            "But what am I going to tell him now ..."
            menu:
                "Tell him the truth":
                    "Better just stick to the truth I guess."
                    d "Well, actually ..."
                    jump interrupt_tomo
                "Lie again":
                    d "I'm from a Land before your time!"
                    d "That's right. I'm actually a time traveller!"
                    d "Call me the Mad Scientist Doujin Kyouma!"
                    sk "Aaaha, so 'Mr. Mad Scientist' you say ..."
                    sk "What year are you from then?"
                    d "Behold, for I am from the myterious future year of over 9000!"
                    sk "Wow, sugoi!"
                    sk "But ..."
                    sk "We actually are in the year 42.000 A.N. right now."
                    sk "So, you are actually from the past and travelled the wrong way, or what?"
                    "Dickfarts, my lie was totally fucked from the beginning!"
                    "How should I have known that they have a different timeline and calendar and shit."
                    "Well, I better just tell the truth now or else they might think I'm a crazy lunatic."
                    d "Hahaha, that was just a joke, couldn't you tell?"
                    "The polarbear has a look of pity in his eyes"
                    d "Umm, so ..."
                    "This is embarrassing, I wish I could die right now"
                    d "Can we just forget this ever happened?"
                    sk "Yeah, I think that's better."
                    sk "For both of us."
    sk "So, what leads you here anyways?"
    sk "Want some coffee or tea?"
    sk "Maybe you want something to eat?"
    sk "We have a special offer today too."
    sk "If you're interested."

    # Some funny discussion Here
    "Filler"
    label interrupt_tomo:
        show tomo normal at right
        with hpunch
        tm "*huff*"
        tm "I ... found you ... *huff*"
    jump cafeTomo
