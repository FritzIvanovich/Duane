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
                un "ummmmm ... "
                extend "e-e-excuse ... "
                extend "me ..."
                d "Eh?"
                "Where's that voice coming from?"
                "Am I just imagining things?"

        show tomo normal
        with dissolve
        un "Ummm..."
        show tomo flip
        extend "I'm s-s-s-sorry..."
        show tomo blush
        extend "but..."
        show tomo shy
        "Oh it was a girl ..."
        "But her voice is so weak, you can hardly hear her over the sound of the arcade games"
        d "What do you want from me?"

        show tomoko_normal
        un "Aaaah!" with vpunch
        "Aaaah! "
        extend "Why did she just scream like that! "
        "That startled me!"
        d "Calm down."
        menu:
            "Just ...":
                d "Just ... "
                extend "what do you wanna tell me?"
                d "Spit it out!"
                un "Eeeek!" with hpunch
                "Damn, looks like she's one of THOSE types..."
                "??? will remember this..."
                $ lovePoints -= 1

            "* Calm her down *":
                d "Breathe in ..."
                extend "and out"
                tm "*breathing in heavily*"
                tm "*exhaling loudly*"
                d "Yeah, feeling better now?"
                d "Then start again, what do you want?"
                $ lovePoints += 2

            "Ask slowly so even a baby can understand":
                d "Okay"
                d "Now, "
                extend "tell "
                extend "me "
                extend "what "
                extend "you "
                extend "want "
                extend "from "
                extend "me."
                $ lovePoints += 1

        tm "Ummmmm..."
        tm "You ... you see ..."
        tm "You lost your b-b-bottle of something"
        scene arcade with None
        show popipo
        with dissolve
        d "What's that?"
        d "I don't remeber owning somthing like that."
        "On closer inspection though ..."
        "It looks similar to MTN DEW I must admit"
        d "Where'd you find this?"
        hide popipo
        show tomo normal
        with dissolve
        un "When, umm, you ran into me earlier."
        un "It fell down and i picked it up."
        show tomo blush
        un "Heh, heheh ..."
        show tomo shy

        d "Uhm, thanks ... "
        extend "I guess?"
        d "Whats your name?"
        un "Aaaaah" with vpunch
        show tomo blush
        un "My-my ... "
        extend "name ... "
        extend "is To-"
        extend "tomo-"
        un "mo ..."
        extend " moko ..."
        d "Ah okay, got it!"
        d "By the way I'm Duane! The most awesome MLG quickscoper in the milky way!"
        d "Anyways, thanks for the bottle!"
        "Duane received ???-bottle"
        tm "Ah ... "
        show tomo shy
        extend "hah hah ... "
        extend "heh heh ... "
        extend "No problem ..."

        d "Nice to meet ya, but I gotta go now!"
        d "Momoko...? "
        extend "Was it? Right? "
        extend "See ya!"
        show tomo annoyed
        tm "Eh ... "
        extend "w-w-w-wait... "
        extend "My name is not..."
        hide tomo annoyed
        with dissolve
        show black
        with dissolve
        jump cafeTomo

label cafeTomo:

    # something that leads to duane finding this place
    play music "bgm/seamoon.mp3"
    scene bg cafetomo
    with dissolve

    d "This is a really nice place. I suddenly crave for some freshly coffee so badly!"
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
            play sound "sfx/skillUp.mp3"
            "Duanes Trust increased!"
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
    menu:
        "Tomo Blend":
            d "Oh Boy! I'm so thirsty, I could drink an octorok!"
            sk "Wha-?"
            d "You know-"
            jump interrupt_tomo

        "Cofee and Tea and then Special Offer":
            sk "Isn't that a bit much at once?"
            d "I don't think so, Tim."
            sk "Wha-?"
            jump interrupt_tomo

        "Huh?":
            jump interrupt_tomo
    label interrupt_tomo:
        show tomo normal at right
        with hpunch
        tm "*huff*"
        tm "I ... found you ... *huff*"
        tm "Aren't you..."
        extend " that famous youtube anime reviewer?"
        d "The what now?"
        show tomo shy at right
        tm "Don't you..."
        show tomo blush at right
        extend " I mean..."
        show tomo normal at right
        extend " the one who acted dimiky."
        sk "I'll just leave you two lovebirds alone."
        sk "Call me if you want to order something."
        hide bear with dissolve
        hide tomo normal at right
        show tomo normal
        d "You wot?"
        d "Hey, don't leave me now Bearman!"
        show tomo blush
        tm "Heh..."
        extend " heh..."
        extend " hehe..."
        tm "So we look like..."
        extend " a..."
        extend " c-"
        show tomo shy
        extend "couple?"
        show tomo blush
        d "Ayyy yo, wait a minute!"
        menu:
            "I guess she is kinda cute":
                d "I guess."
                play sound "sfx/slinkUp2.mp3"
                "Momoko liked that!"
                $ lovePoints += 2

            "No.":
                play sound "sfx/nooo2.mp3"
                d "NoooOOOooo!"
                show tomo annoyed
                "Momoko is hurt by that."
                $ lovePoints -= 1

            "Change the topic":
                "Huh? I don't like where this conversation is going."
                "I better change that there topic to something else."
                d "So..."
                extend " you like coffee, huh?"
                show tomo blush
                tm "Ah..."
                show tomo shy
                extend " that means..."
                show tomo blush
                extend " you're inviting me?"
                d "Uhh..."
                menu:
                    "I'm sorry, I can't hear you very well.":
                        d "I'm sorry, I can't hear you very well."
                        d "I'd like to make an appointment with the dactor."
                        show tomo annoyed
                        tm "Eh?"
                        tm "Oh..."
                        "Dodged a bullet there."
                        "I am the fucking limbo champion!"
                        "I ain't got no money on me."

                    "No.":
                        play sound "sfx/nooo2.mp3"
                        d "NoooOOOooo!"
                        show tomo annoyed
                        "Momoko will remember this..."
                        $ lovePoints -= -1
                        tm "Oh..."
                        tm "I see..."

                    "Yeah... Sure... I guess...":
                        d "Fine whatever..."
                        d "I wanted some coffee anyways."
                        show tomo shy
                        tm "R-"
                        extend "Really?"
                        show tomo blush
                        play sound "sfx/slinkUp2.mp3"
                        "Momoko seems pleased."
                        $ lovePoints += 2
                        tm "Hehe..."
                        extend " Hehehe..."
                        d "Bearman!"
                        d "We want to order!"
                        show tomo blush at right
                        show bear at left with dissolve
                        sk "How may I help you?"
                        d "Two cups of coffee please."
                        sk "Coming right up!"
                        hide bear with dissolve
                        play sound ('sfx/hot_coffee.mp3')
                        with Fade(0.1, 3.0, 0.5)
                        show bear at left with dissolve
                        sk "Ok, here you go."
                        "Wow, the coffe smells surprisingly nice!"
                        d "Ok, thanks bearman!"
                        sk "You're Welcome!"
                        hide bear with dissolve
                        show tomo blush
                        d "Here, you go Momoko!"
                        show tomo shy
                        tm "T-"
                        extend "t-"
                        extend "t-"
                        extend "thanks."
                        show tomo blush
                        "You drink the fresh and hot coffee."
                        "You instantly feel refreshed and energized again!"
                        play sound ('sfx/itemGet.mp3')
                        "Duane got fully healed!"
                        d "Whew, that really hit the spot!"
                        d "It's no Mountain Dew, but ..."
                        d "I could get addicted to this too."

        d "So, Momoko? What do you want from me?"
        tm "Actually,"
        show tomo shy
        extend "I followed you from the arcade."
        show tomo normal
        tm "I was really close behind you, but you didn't notice me."
        d "Really?"
        tm "Yes!"
        tm "You seemed like ... "
        show tomo blush
        extend "kind of like a nice guy."
        "Uh oh, this seems kind of dangerous."
        "But I don't really know why ..."
        d "That's the reason?"
        tm "Yeah, you're the first guy who was ever nice to me"
        show tomo normal
        tm "So, "
        show tomo blush
        extend "do you want to go out with me?"

        "Crap, she looks so adorable like this."
        "I hardly know her at all!"
        "But getting a girlfriend seems tempting too!"
        "I will ..."
        label choice_tomo:
        menu:
            "Give it a try!":
                d "'Kay"
                tm "Really!"
                "Tomoko seems really happy!"
                tm "Heh-"
                extend "hehe-"
                extend "heh ..."
                jump yandere_tomo
            "Say Nothing":
                d "..."
                "She's still looking at me with puppy dog eyes."
                "It seems like i have to give an answer to her, no matter what."
                $ lovePoints -= 0.1
                jump choice_tomo

            "Better not stick my dick in crazy!" if lovePoints < 3:
                "Yeah right! There's no way a chick could fall for me that quickly!"
                "This seems too fishy!"
                "There must be something wrong with her!"
                d "Sorry, but i refuse!"
                show tomo annoyed
                tm "Oh, "
                extend "is that so ..."

label yandere_tomo:
    scene bg station_entrance
    "Duane arrived at the promised meeting spot."
    d "What's up with this place?"
    d "Is this really a famous meeting spot?"
    d "Looks like some abandoned facility to me."
