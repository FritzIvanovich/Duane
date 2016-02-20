# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image black = Solid((0, 0, 0, 255))
image white = Solid((255, 255, 255, 255))

image aniki 1 = "aniki"
image el aniki = "elaniki"
image leather = "leatherman"
image nigga = "nigga_character"
image nigga 1 = "nigga1"
image nigga 2 = "nigga2"
image carlton 1 = "carlton1"

image adachi blush = "adachi_blush"
image adachi blushthinking = "adachi_blushthinking"
image adachi flustered = "adachi_flustered"
image adachi = "adachi_neutral"
image adachi perplex = "adachi_perplex"
image adachi pissed = "adachi_pissed"
image adachi shocked = "adachi_shocked"
image adachi smile = "adachi_smile"
image adachi talking = "adachi_talking"
image adachi thinking = "adachi_thinking"
image adachi troubled = "adachi_troubled"
image adachi twisted = "adachi_twisted"

#image reimu = "reimu3"
#image reimu neutral = "reimu1"
#image reimu laugh = "reimu2"
image reimu neutral = "reimu"
image reimu stupit = "omg_reimu"

image luvia neutral = "luvia_normal"
image luvia look = "luvia_look"
image luvia ohoho = "luvia_ohoho"
image luvia intrigue = "luvia_intrigued"
image luvia understand = "luvia_annerstand"

image mb adachi = "audrey_adachi"
image mb love = "audrey_blushing"
image mb normal = "audrey_adachi"

image tomo normal = "tomoko_cheery"

image mtndew = "dew"
image popipo = "popipo_dew"

image yakuza = "yakuza1"

image bg ghetto = "ghetto"
image bg locker = "lockerroom"
image ghetto street = "ghetto2"
image bg dewstore = "dewstore"
image bg supa = "supermarket_inside"
image bg nihon = "japan"
image bg cherry = "cherry_blossom"
image bg forest = "forest"
image bg forest2 = "forest2"
image bg mountain = "mountain"
image bg shrine = "shrine"
image bg town = "town"
image bg riverside = "riverside"
image bg mall = "mall"
image bg sidestreet = "sidestreet"
image bg gameover = "gameover"
image bg arcade = "arcade"
image bg street = "street"
image bg disco = "disco"

image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)

# Declare characters used by this game.
# define e = Character('Eileen', color="#c8ffc8")
define d = Character('Duane', color="#c8ffc8")
define a = Character('Billy Herrington', color="#c8ffc8")
define ea = Character('El Aniki', color="#c8ffc8")
define l = Character('Leatherman', color="#c8ffc8")
define n = Character('Ultra Nigga', color="#c8ffc8")
define c = Character('Carlton Banks', color="#c8ffc8")
define ad = Character('Tooru Adachi', color="#c8ffc8")
define r = Character('Reimu Hakurei', color="#c8ffc8")
define mb = Character('Mega Bitch', color="#c8ffc8")
define ab = Character('Audrey Belrose', color="#c8ffc8")
define t = Character('Tomoko Kuroki', color="#c8ffc8")
define lu = Character('Luviagelita Edelfelt', color="#c8ffc8")
define un = Character('???', color="#c8ffc8")
define y = Character('Jolly Ol\' Companion', color="#c8ffc8")

init:
    $ metAtForest = False
    $ pointless = 0
    $ stupit = False
    $ wentToTown = False
    $ riversideEvent = False
    $ luviaInteraction = 0
    $ aimless = False
    $ yassan = False
    $ ran_away = False
    $ lovePoints = 0

label splashscreen:
    scene black
    with Pause(1)

    show text "Ernesto and Esteban present..."
    with Pause(3)
    hide text with dissolve

    show text "The dankest visual novel experience to ever be conceived..."
    with Pause(3)
    hide text with dissolve

    $ renpy.movie_cutscene('video/faze.ogv')

    #show text "Let's rek sum scrubs m9!"
    #with Pause(2)
    #hide text with dissolve

    return


# The game starts here.
label start:

    scene bg ghetto:
        zoom 1.5
    with dissolve

    "Just another day in the ghetto."
    "Nothing particularly \[MLG\] going on, when suddenly..."
    d "Maaaaaan."
    d "I'm all outta MTN DEW! And it's dew today!"
    d "Faze will kick me out at this rate!"
    d "How can I be a professional \[MLG\] quickscoper that way?!"
    d "Better get some quick!"
    "Duane heads off to the next store in hope of finding some MTN DEW."

    scene black
    with dissolve

    d "I'll try this one!"

    scene bg locker
    with dissolve

    d "I wonder if they got the dew here..."
    "I'll just ask this dude, he looks pretty swell."

    show aniki
    with dissolve
    play music "bgm/aniki_theme.mp3"

    d "Ayyy does this place got some Red Cherry Dew?"
    a "Hey buddy I think you got the wrong door."
    a "The Dew Store is two blocks down."
    d "Oh shit I'm sorry."
    a "Sorry for what?"
    "What was I even thinking looking for MTN DEW here."
    "There's no way they sell it here!"
    "Man this really sucks!"
    "I don't deserve this shit."
    "I should've listened to the Leatherman and..."
    "Oh wait, isn't that him?"

    hide aniki
    with dissolve

    d "Hey Leatherman! It's me, the boy next door! Remember?"

    show leatherman
    with dissolve

    l "..."
    d "Maaan what a shitty gym, doesn't even got no dew."
    l "......"
    d "What are you even dewing here, Leatherman?"
    d "Get it? Dewing?"
    l "........."
    d "Aaaaanyway, shouldn't you be in class? I'm gonna tell the teacher!"
    l "Fuck you."
    "That's a bit harsh."

    hide leatherman
    show leatherman at right
    with dissolve

    show aniki at left
    with dissolve

    a "Don't you think you are being a bit rude there?"
    l "Fuck you too."
    a "No fuck you, Leatherman. Why don't you and I settle this in the ring if you think you're so tough."
    l "..."
    l "I have no time for this. I gotta get to class."

    hide leatherman
    with dissolve

    hide aniki
    show aniki

    a "Tch, I would've showed him who's boss of this gym."
    d "Oh Leatherman! Always with the busy schedule, even when he's skipping class."
    a "Anyway kid, want me to show you where to get your Dew?"
    a "I just got done with my workout."
    a "If you're looking for it now you must be late."
    d "Yeah that'd be great, uh..."
    a "Just call me Aniki."
    d "What is this, some kinda weeb name?"
    a "Whatever, kid. Let's go."

    hide aniki

    scene black
    with dissolve

    "And so Duane and Aniki went off to get the Dew."
    "If only optaining it would be that easy."

    jump dewquest

label dewquest:

    scene ghetto street:
        zoom 1.5
    with dissolve

    play music "bgm/hood.mp3"
    "Back in the hood."
    "Dewin ain't easy."
    d "Once I got my dew all those scrubs from other clans can fuck right off!"
    d "It's not like they got any skill anyway."
    d "Bunch of fucking hicks."

    show nigga at left
    with dissolve

    n "Ay what the fuck man, you got a fucking problem?"
    d "Huh?"
    n "Fucking Faze scrub."
    n "Talking shit about other clans without any dew on you."
    d "Yo, I'm just trying to get some right now, not my fault y'all can't even close fgt_csl.exe!"

    hide nigga
    show nigga2

    n "I'll rip yer fucking head off you goddamn shitty casual."
    "He looks pissed, and he's definitely tough."
    "I'll just..."

    menu:
        "Handle this myself":

            d "I'll take you on, you filthy scrublord!"
            n "Get ready to be destroyed, you little bitch!"

            scene black
            with dissolve

            play sound "sfx/beatdown.mp3"
            scene white
            with dissolve
            with Pause(2)
            scene black
            play sound "sfx/wrestle_converted.wav"
            with Pause(1)
            scene white
            scene black
            with dissolve

            d "I'm not done yet..."
            n "Want more, huh?"
            n "Say hello to the people in Jersey for me!"

            scene white
            play sound "sfx/wrestle_converted.wav"
            with Pause(2)
            scene black
            with dissolve

            scene ghetto street:
                zoom 1.5
            with dissolve

            show nigga1:
                zoom 1.3
            with dissolve

            d "Ugh..."
            n "Better watch yourself from now on, nigga."
            "I shouldn't have tried to take him on by myself..."
            "I'm just not \[MLG\] enough yet..."
            "I guess this is it..."

            scene bg gameover
            with dissolve
            play music "bgm/sadhorn.mp3"
            "And so, Duane's story finds an untimely end."
            "Fighting by himself was pretty courageous, but ultimately not very clever."
            "Seriously, did you think he could take on the Ultra Nigga?"
            "Like really?"
            "Did you even take a look at him before deciding?"
            "Is you fucking retarded? Jesus..."
            "Well anyway you fucked up."
            "GAME OVER"

            return

        "Ask Aniki for help":

            "Shit I don't think I can take him on by myself."
            d "Aniki! Could you please handle this?"
            n "I don't care which of you faggots I'll have to break!"

            hide nigga2
            with dissolve

            show aniki 1
            with dissolve

            a "Leave this to me."
            a "It is Aniki's duty to protect the weak."
            d "You wot m-"

            play music "bgm/standoff2.mp3"

            hide aniki 1

            show el aniki
            with dissolve

            "Aniki readies his fighting stance."
            "I mean, it doesn't look much different from his usual stance."
            "But he'll make it work, I guess."

            hide aniki 1
            with dissolve

            show el aniki at right
            with dissolve

            show nigga at left
            with dissolve

            n "That stance...!"
            n "Impossible...! Is he really going to use THAT?!"
            n "Inconceivable! Can he really be THE MAN OF LEGEND?!"
            ea "Hola, soy el Aniki!"
            ea "Yo soy el destructor del mal."
            ea "Comete esta!"
            n "Yo wait wait wait!"
            n "I don't want no trouble man!"
            n "I din do nuffin, I'm a good boy!"
            n "Please let me off man!"
            ea "Entiendo, amigo."
            ea "Vaya con dios..."

            play sound "sfx/steps.mp3"
            hide nigga
            with dissolve

            hide el aniki
            show el aniki

            "Ultra Nigga ran away."
            "Thankful that his life was spared."
            n "But you haven't seen the last of me~!"
            a "Qué?"
            n "Uh, I mean, nuffin man!"

            a "..."
            "Aniki focuses his mind, slowly returning to his normal stance."
            hide el aniki

            show aniki 1
            with dissolve

            play music "bgm/aniki_theme.mp3"

            d "I have no idea what the hell just happened but this was pretty fucking dank Aniki!"
            d "He just went and ran away!"
            a "Haha, that's nothing kid."
            a "You've not seen anything yet."
            a "He made a good decision to run away, he's apparently not as dumb as he looks."
            play sound "sfx/shotsfired.mp3"
            d "Shot's fired!"

            a "Anyway kid, if you don't want to get in trouble at the \[MLG\] academy we'd better go and hurry to the Dew Store."
            d "True true."
            scene black
            with dissolve

            "What a reliable companion Duane found in Aniki!"
            "With this, Duane was able to avert the first of many dangers."
            "However, this is merely the beginning of this grand adventure."
            "For now, it's on to the Dew Store!"

            play music "bgm/takeonme.mp3"
            scene bg dewstore
            with dissolve

            d "Is that it?"

            show aniki 1
            with dissolve

            a "Take a wild guess."
            d "Yes! Thanks m9."
            a "Don't sweat it."
            a "Anyway, it's been fun but I'll have to go now."
            a "I have some business to attend to."
            a "I'm sure we'll run into each other again sometime."
            a "Try to be on time with your academic assignments from now on."
            d "I'll try!"
            a "Stay safe, kid."

            hide aniki 1
            with dissolve

            d "I knew that guy was swell."
            d "Finally I'm able to get my dew!"
            d "Better hurry now, or else I'll really be late."
            "Finally the dew was in reach for our hero."
            "Little did he know that nothing is quite as it seems at this store."
            "Well it pretty much is, but it's slightly off."
            "You catch my drift right?"

            jump store

label store:

            scene black
            with dissolve
            scene white
            with dissolve
            play music "bgm/postal.mp3"
            scene bg supa
            with dissolve

            d "So this is it."
            d "Makes more sense to get Dew here than in the locker room I suppose."

            show carlton 1
            with dissolve

            c "Well hello there."
            c "I'm Carlton."
            c "Carlton."
            c "It's Carlton you're talking to."
            c "That's Carlton."
            c "Carlton."
            c "It's Carlton."
            play sound "sfx/sandwhich.mp3"
            c "Could you make me a sandwhich?"

            play sound "sfx/nooo2.mp3"
            d "NoooOOOooo!"
            d "What the fuck man."
            d "I'm just here to buy some shit."
            d "Not to make some casual faggot a sandwich."

            c "Dew?"
            c "Doritoes?"
            c "Weed?"
            c "You want it?"
            c "It's yours my friend."
            c "As long as you..."
            play sound "sfx/sandwhich.mp3"
            c "Make me a sandwich."

            jump shopping

label shopping:

    d "Uhhh..."
    d "Whatever."
    "I think I'll take some..."

    menu:
        "Dew":
            d "I'll just have some Mountain Dew."
            c "I'm sorry we're all out of regular dew."
            c "Except..."
            c "Maybe you want to try some new stuff?"
            d "What?!"
            d "Who could deny new dew?"
            d "A true MLG noscoper gotta always know his dew."
            d "Count me the fuck in!"
            c "I appreciate your enthusiasm!"
            c "You just have to sign this."
            d "Sure whatever."
            c "It's just in case something happens."
            d "Wha-"
            c "Nothing. Don't worry about it."
            c "This shit's completely new, it's genetically modified Dew Plant designed to be inhaled through smoking!"
            c "That way you can absorb 200\% more Hi-MLG Particles."
            d "Shit sounds dank."
            c "So..."
            play sound "sfx/sandwhich.mp3"
            c "Could you make me a sandwich?"
            d "I actually wanted to keep this one..."
            d "But this is worth it."
            "Duane hands Carlton the sandwich he saved up."
            d "Here you go, keep the change."
            c "You're my favorite customer."
            c "Here you go!"
            c "Try it right now!"
            d "Did you bring a lighter?"
            play sound "sfx/nooo2.mp3"
            c "NoooOOOooo!"
            d "Damn."
            c "Just kidding, here you go!"
            d "Thanks m80."

            $ renpy.movie_cutscene('video/carlton.webm')
            jump japan


        "Doritoes":
            d "One dozen doritoes please."
            c "I'm sorry Duane, I can't give credit."
            c "Come back when you have a little more..."
            c "Mmmmhhh"
            c "Sandwiches."
            "Shit, I can't afford that."
            "Wasn't there something else I had to get?"

            jump shopping

        "Weed":
            d "I'll have some weed."
            c "This is illegal you know."

            menu:
                "I was just kidding":
                    d "I was just kidding."
                    "What was it that I wanted again?"
                    jump shopping

                "Just give me the weed":
                    d "What the fuck?"
                    d "You just offered it to me."
                    c "No I didn't."
                    d "Just give me the weed you fucking scrub!"
                    d "I'll fucking 360 noscope you!"
                    c "Seems like I gotta call the PoPo on you."
                    d "What?!"
                    play sound "sfx/popo.mp3"
                    "Shit this wasn't supposed to happen!"
                    "What was I thinking?!"
                    "That trap was so obvious."
                    scene black
                    with dissolve

                    scene bg gameover
                    with dissolve

                    play music "bgm/sadhorn.mp3"

                    "Maaan, how could you ask for weed in a store?"
                    "The popo is listening 24/7"
                    "Young nigga got it bad cause I'm brown."
                    "GAME OVER"

                    return

label japan:

    scene bg cherry
    play music "bgm/Zencho.mp3"

    "..."
    d "Ugh..."
    "What the hell just happened?"
    "I can't remember anything after I said goodbye to Aniki..."
    "Anyway, where in god's name am I?"
    d "There's cherry blossoms everywhere."
    "It almost feels like this is another country all together."
    "What should I do?"
    "I have no idea where I am and I didn't make any progress with my dew assignment either."
    "I see some mountains in the distance."
    "Maybe I can find someone there who can tell me where exactly this is."
    "There's also a forest close by."
    "Maybe I should try my luck there?"
    "Given the circumstances, the most MLG decision would be..."

    menu:
        "The Mountains":
            jump mountain

        "The Forest":
            d "It's a shot in the dark whatever I pick, so I might as well try the forest."

            scene black
            with dissolve

            play sound "sfx/steps.mp3"
            "And so Duane went to the forest in search of someone who could explain this predicament to him."
            "Chances to find someone were slim, but he had to do something."
            d "Maaan, it was further away than I thought."

            scene bg forest
            with dissolve

            d "So this is it."
            d "There's stairs here, so there must be some kind of civilisation around here."
            "Duane wandered the forest in search of other people."
            d "Helloooooo! Is anyone there?"
            "No answer"
            d "This is hella weird, how the fuck did I end up like this."
            d "Man this really sucks."
            d "I don't deserve this shit."
            d "I should've listened to my old man and joined the navy."
            d "But I hated the smell of seawater and now I'm stuck."
            d "Running around wherever the hell without any clue where to go to."
            d "Like some goddamned casual."
            "As Duane walks around aimlessly, cursing his fate he spots something in the distance."
            d "Wait, what's that?"
            d "Rather, who's that?"

            show reimu neutral
            with dissolve
            d "It's..."
            d "A girl!"
            "Some fancy kind of clothes she's wearing."
            d "This is my chance to find out where I am."
            d "Heeeey! You there!"
            "Mysterious Girl" "..."

            play sound "sfx/steps.mp3"
            hide reimu neutral
            with dissolve

            "She's leaving."
            d "Yoooo what the fuck?"
            d "Did I say something wrong?"
            d "Anyway this is no time to think about shit like that."
            d "I must find out where I am, so I gotta go after her!"

            play sound "sfx/steps.mp3"
            scene black
            with dissolve

            "Duane chased after the mysterious girl with all his might."
            "Even though he wasn't a slow runner, he had no hopes of catching up to her."
            play sound "sfx/steps.mp3"
            d "Fuck!"
            d "She's just too fast."

            "Due to Duane's MLG quickscoper eyes, he managed to follow her movements for a while."
            "But it just wasn't possible for him to keep it up for long."
            "He eventually lost her when he reached a mountain area."

            $ metAtForest = True

            jump mountain

label mountain:

    scene bg mountain
    with dissolve

    d "What a pretty mountain area."
    d "Mountain area..."
    d "Mountain..."
    d "SHIT! This just makes me crave some Mountain Dew!"

    if metAtForest == True:
        d "But enough of that!"
        d "I gotta find that girl! Or anyone for that matter."
        d "If only she weren't that fast."
        d "I completely lost her."

    d "Gotta get my mind together."
    d "Where would there be people in such an area?"
    "I remember those old Kung Fu movies."
    "They often took place in a mountaineous area which had a shrine."
    "Is it possible for one to be located here?"

    if metAtForest == True:
        "Considering there was this girl here, there must be some place for people to stay at."
        "It can't be she wanders around here by herself."
        "Especially with that fancy getup of hers."

    d "Guess I just gotta keep looking for something."

    scene black
    with dissolve

    "After countless hours of walking around the mountains, and several instances of just wanting to ragequit everything..."

    scene bg shrine
    with dissolve

    play music "bgm/Madoka.mp3"

    d "What the hell!"
    d "I knew it!"
    d "My quickscoper senses never fail me after all!"

    show reimu neutral
    with dissolve

    "Mysterious Girl" "..."
    "Mysterious Girl" "How did you find this shrine?"

    menu:
        "It's you!" if metAtForest == True:
            d "I've seen you before in the forest!"
            "Mysterious Girl" "No you haven't."
            jump pointless1

        "Finally I found someone!":
            d "Finally I found someone!"
            jump shrine

label pointless1:
    menu:
       "Yes I have!":
            $ pointless += 1
            if pointless >= 10:
                hide reimu neutral
                show reimu stupit
                with dissolve
                $ stupit = True

            jump pointless2

       "Aaanyway..." if pointless % 3 == 0:
            jump shrine

label pointless2:

    d "Yes I have!"
    "Mysterious Girl" "No you haven't."
    jump pointless1

label shrine:

    d "Could you please tell me where this place is?"
    "Mysterious Girl" "What do you mean \"This place\"?"
    d "Well, I have no idea how I even got here."
    d "Like, where is this shrine located?"
    d "How do I get to MLG Academy from here?"
    d "And where's the next Dew Store?"
    d "I still haven't gotten any for my class."
    "Mysterious Girl" "MLG Academy?"
    "Mysterious Girl" "Dew Store?"
    "Mysterious Girl" "There are no such things in this world."
    d "Yoooo, how can you EVEN live?"
    d "Wait what do you mean this world?"
    "Mysterious Girl" "I thought I noticed something strange about you the first time I saw you..."
    "Mysterious Girl" "You are not originally part of this world."
    "Mysterious Girl" "You must have stumbled in here somehow."
    d "Yo are you high, lady?"
    "Mysterious Girl" "The name is Reimu."
    r "And no."
    r "This is the Animu Land."
    d "Anime? So it's a world full of weebshit?"
    d "Though there used to be some pretty MLG anime on TV."
    r "So our reality is visible in your televison, interesting."
    d "Whatever, how the hell do I get back?!"
    d "I'm so late for my Dew!"
    r "I am not aware of any way to venture through realms."
    r "But since you already did it once there surely must be a way."
    r "I can't directly help you, but maybe you'll find someone to assisst you in the next town."
    r "Here take this map, it will lead you there."
    "---Duane received a map of the Animu Land---"
    d "It won't even be visible on my HUD?"
    d "Maaan."
    d "But thanks, I suppose."
    r "Stay safe."
    r "This world is likely very different to yours."
    r "I'm sure we'll cross paths again."
    d "Thanks!"
    "What did she mean by that?"

    scene black
    with dissolve
    play sound "sfx/steps.mp3"

    "And so Duane made way for the next big city."
    "What will he encounter on his bizarre adventure through this new world?"
    "I'm sure that even here, lots of MLG adventures await our hero!"

    jump town

label town:

    scene white
    with dissolve
    play sound "sfx/steps.mp3"
    scene black
    with dissolve

    d "So this is it, huh?"

    scene bg town
    with dissolve
    play music "bgm/personatown.mp3"

    d "This is one big city."
    d "Reimu said, I should look around and talk to people in order to find out how to get back."
    "Where do I start?"
    "Let's see..."
    "I can see an Arcade over there."
    "It's been a while since I practiced my quickscoping, so a quick game wouldn't hurt."
    "And maybe I'll find someone to help me out there."
    "There's also a mall close by."
    "I could go there to check if they have some dew."
    "Though Reimu said there's no such thing here..."
    "There's even a river going through the town."
    "Isn't that where tough guys have their manly battles and romances start to bloom in anime?"
    "Not that I watch any of that."
    "But maybe there'll be something of use there."
    "I could also just try to talk to some of the people walking around here."
    "At least one of them has got to know something right?"
    "Hmm, I think I'll..."
    jump townHub

label townHub:

    if wentToTown == True:
        scene bg town
        with dissolve
        play music "bgm/personatown.mp3"

    $ wentToTown = True

    if aimless == True:
        d "How the fuck did I end up here again?"
        d "I really suck at this!"
        $ aimless = False

    menu:
        "Go to the Arcade":
            "Time to vent some stress and quicksope some n00bs"
            "But where do I find a good place to do that, I wonder?"
            "I guess that arcade over there seems like a good spot"
            jump arcade

        "Go to the Mall":
            "I really need to get that dew now."
            "Might as well check the mall."
            jump mall

        "Go to the Riverside":
            jump riverside

        "Talk to that Man":
            "That Man" "Harro!"
            $ wentToTown = False
            jump townHub

        "Talk to that Girl":
            show luvia ohoho
            with dissolve
            lu "Ohohohohoho!"
            $ wentToTown = False
            hide luvia ohoho
            $ wentToTown = False
            jump townHub

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

        jump routeTomo

label mall:

    scene bg mall
    with dissolve
    play music "bgm/casino.mp3"

    d "This mall is fucking huge."
    d "I wonder if I'll even be able to locate any dew in here."
    d "Even though I was told there is no dew here, I can not believe such a thing."
    d "How would the people live without it?"
    d "There must be something that's at least similiar to dew here."
    d "I will..."

    menu:
        "Check the mall out myself":
            d "It can't be that hard to find something here."
            scene black
            with dissolve
            "Duane spent a couple of hours looking through the mall."
            $ aimless = True
            jump townHub

        "Ask someone":
            d "I don't think I'll be able to find anything in here by myself."
            d "I'll just ask that girl over there I suppose."

            show mb adachi
            with dissolve

            d "Yo excuse me!"
            mb "Eh?"
            mb "What the fuck?"
            mb "You talking to me?"
            "This chick's kinda hot."
            "Better watch out what I'm gonna say next."

            menu:
                "Excuse me, could you please show me the way to the next Dew Store?":
                    mb "What kind of stuck up little bitch are you?"
                    jump mbRoute

                "Ay bby were da dew at?":
                    mb "Ugh... Excuse me?"
                    mb "Could you fucking ask me that in a human language again?"
                    jump mbRoute

                "Sorry. Store. Dew. Where?":
                    mb "..."
                    mb "Are you fucking retarded or something?"
                    jump mbRoute


label routeTomo:
    return

label riverside:

    d "For some reason I feel compelled to go to the Riverside."
    scene black
    with dissolve
    play sound "sfx/steps.mp3"

    scene bg riverside
    with dissolve
    play music "bgm/yassan.mp3"

    if riversideEvent == True:
        d "There's nothing else for me to do here."
        d "I should get back to the city and pick another spot"
        jump townHub

    "Duane arrived at the riverside on his search for information."

    "The wind is pretty strong today."
    d "Hmm, it looks pretty neat here."
    d "My dank sense is tingling."
    d "Even the wind seems somewhat..."
    d "I feel a strange kind of atmosphere here."
    d "troubled."
    d "There doesn't seem to be anyone around."
    d "It won't help me at all with my problem but..."
    d "Maybe I should sit down for a while and review stuff for class."
    d "It seems pretty chill here."
    d "That may be just a waste of time though."
    d "I need to find someone to help me after all."
    d "I think I'll..."

    menu:
        "Sit at the Riverside":

            d "Maaan, I can spare a bit of time here."
            d "There's something about this place."

            scene black
            with dissolve
            $ renpy.movie_cutscene('video/yassan_scene.webm')

            scene bg riverside
            with dissolve

            d "What the fuck was this all about?"
            d "Why did I turn into such an autistic spaghetty monster there?!"
            d "FUCK! FUCK! FUCK!"
            d "That was in no way MLG!"
            d "Should've just gone with \"The wind is troubled.\" or some stupid shit like that."
            d "Fucking friendzoned again."
            d "Jesus."
            d "Moping around here will not get me anywhere either though."
            d "I should get back to the city and make a plan on where to go next."
            $ riversideEvent = True
            $ wentToTown = True
            $ yassan = True
            jump townHub

        "Go back to the town":

            d "As inviting as this looks, I simply lack the time to sit around here."
            d "I'll head back to the town to see where I'll go next."

            scene black
            with dissolve
            play sound "sfx/steps.mp3"

            "As Duane left a feeling striked him."
            "A feeling that made him aware that he missed out on something important."
            "A fated encounter so to speak."
            "There was something about this place after all."
            "Is Duane's Spring of Youth now over?"
            "Will he not encounter any romance in the days of his passionate youth?"
            "One can only continue to watch him on his adventure to find out."
            $ wentToTown = True
            $ riversideEvent = True
            jump townHub

    return

label timewaster:

    d "I still have some time left."
    d "So I'll..."

    menu:
        "Have a look around":
            scene black
            with dissolve
            d "Wow there's so much to do, so much to see!"
            d "It's impossible to explore everything in just a single day!"
            scene bg mall
            with dissolve
            jump timewaster

        "Just leave":
            d "I think there's nothing else to do here."
            d "For now...."
            d "I'll just head back."
            jump saveMb
