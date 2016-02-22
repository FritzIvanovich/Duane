label mbRoute:

    mb "Whatever."
    mb "Just... like..."
    mb "Go over there."
    d "Thanks a lot bye!"
    mb "..."
    mb "What a dweeb."
    hide mb adachi
    with dissolve

    scene black
    with dissolve

    "Duane went into the general direction he was pointed to."
    "He actually managed to find some dew!"

    show dew
    with dissolve

    "But on close inspection, he noticed something was off."
    "Much to his dissapointment it was only a knockoff."

    hide dew
    with dissolve
    show popipo
    with dissolve

    "Some kind of Japanese vegetable juice."
    d "Well, I already went all this way."
    d "And I'm way too late to be picky anyway."
    d "Might as well get this..."
    "Duane paid exactly 200 Yen."
    play sound "sfx/itemGet.mp3"
    "---Duane received Popipo---"

    scene bg mall
    with dissolve

    d "It's better than nothing I suppose."
    jump timewaster

label saveMb:

    scene black
    with dissolve

    scene sidestreet
    with dissolve
    play music "bgm/personatown.mp3"

    d "It's kinda late already."
    "As Duane walks down the street, he notices someone familiar."
    show mb adachi at right
    with dissolve
    show yakuza at left
    with dissolve
    y "Excuse me Miss, but could you please point me to the direction of this district's French Bakery?"
    y "I need to pick up a birthday cake for my sick little sister there."
    y "Even though she has to spend it in the hospital, I'd like her to have the best possible birthday."
    mb "Ugh..."
    mb "Do I look like a fucking tourist guide to you?"
    mb "I don't know no French Bakery around here."
    "Huh, she's with somebody else."
    "I can't really tell what their talking about, but she looks kinda distressed."
    "That guy is obviously dangerous!"
    "I gotta step in!"
    y "I'm terribly sorry to have bothered you then."
    y "I will go and ask somebo-"
    d "Hey! What the hell do you think you're doing?"
    d "Could you piss off and leave her alone!?"
    y "Huh?"
    y "Are you perhaps talking to me?"
    d "Damn straight I am."
    d "Now make like a fly and fuck off m8."
    d "Better back the fuck up before you get smacked the fuck up!"
    y "Excuse me young man! I didn't realize I was such a bother."
    y "I will take leave immediately."
    y "Have a good evening, sir."
    y "And to you too M'Lady."
    y "*Tips Katana*"
    hide yakuza
    with dissolve
    hide mb adachi
    show mb normal
    "With that the Yakuza left."
    d "Everything alright..."
    "I just realized I don't even know her name yet."
    d "Ah you're that girl from before!"
    d "I didn't even ask you for your name yet."
    d "You really helped me out back there."
    "Sorta."
    mb "Sure."
    mb "Whatever."
    mb "You know what? Normally I wouldn't talk to guys like you."
    mb "But since you got that annoying dick off my back, I guess can make an exception."
    ab "The name's Audrey Belrose."
    ab "But don't get any ideas. Don't get used to such treatment."
    "Audrey Belrose, what a lovely name."
    d "My name's Duane, and I got the sickest moves at MLG Academy."
    ab "MLG Academy..., you still go to school?"
    ab "What a fucking waste of time."
    d "Watch it m80."
    d "That shit's off the hook."
    d "We smoke weed everday, drink dew, eat doritoes and noscope scrublords everday."
    ab "Weed?"
    ab "In school?"
    ab "Are you like, for real?"
    d "It is MLG academy after all."
    hide mb normal
    show mb love
    ab "What the fuck?"
    ab "It might not be such a waste of time after all."
    hide mb love
    show mb normal
    ab "Anyway."
    ab "Don't think I got the whole night to talk to you."
    ab "I gotta go now, I've got more important things to do."
    ab "See ya."

    play sound "sfx/steps.mp3"
    hide mb adachi
    with dissolve

    "Whoa what a hottie!"
    "I'll rate 8/8 m80."
    "And she has obviously completely fallen for me."

    if yassan == True:
        "Unlike that weird girl at the riverside, I'm sure I won't get friendzoned this time!"

    "But what should I do now? The night is still young."
    menu:
        "I should follow her, this is a great chance!":
            "Now I can find out where she lives! This is a huge chance!"
            play sound "sfx/dinner.wav"
            "Maybe she will even invite me over for dinner if she sees me there!"
            "Well, maybe not, but I can't ignore this opportunity now that it has just presented itself to me!"
            "Duane followed Audrey like an Ukranian Ninja!"
            jump stalkMb

        "Go Party even harder than you work":
            "It's a beautiful night to have a Party!"

            stop music
            play sound "sfx/horrible.wav"
            un "What a horrible night to have a curse."

            scene bg sidestreetN
            with dissolve

            play music "bgm/night.mp3"

            d "What the...?!"
            d "Who the hell just said that?"
            "Suddenly time stopped and some weird shit was floating in the air."
            "There's a guy walking around throwing bottles of water on the ground."
            d "I don't get any of this."
            d "Those are some sick moves for normal walking though!"
            d "Maybe I should try walking like this..."
            d "Well it doesn't matter anyways."
            d "Ain't nobody got time for that."
            d "I'll just go to the next club, gotta show 'em my sick moves!"
            d "Let's do this shit!"
            jump discoMb

    return

label stalkMb:
    show street
    with Fade(0.5, 2.0, 0.5)
    "..."
    d "Damn! I lost her ..."
    d "Who could have thought she is that..."
    play sound "sfx/sanic.mp3"
    d "FAST!"
    d "If I didn't know any better I'd think she wanted to get away from me."
    d "Yeah right!"
    d "Might as well just party at that disco over there."

    jump discoMb

label discoMb:
    show disco
    with dissolve
    play music "bgm/myon.mp3"

    "Aww yeah, this is awesome!"
    "The dancefloor is packed with people and the music is something all true MLG's strive for!"
    menu:
        "Lets show me my moves!":
            play sound "sfx/mymoves.wav"
            d "Alright Guys! Lets do some dancing!"
            play sound "sfx/mymoves2.wav"
            d "Let's show me my moves!"
            $ renpy.movie_cutscene('video/duanedancing.webm')
            $ danced = True
            d "Oh yeah!"
            d "How'd you like that!?"
            jump drinks

        "Let's get some drinks!":
            jump drinks

label drinks:
    if danced == True:
        d "I really worked up a sweat there."
    "I'm thirsty as a motherfucker!"
    "I need to drink something fast."
    "That reminds me..."
    "I still got that weird drink I mistook for dew with me."
    "I can also just get me some drinks at this club's bar."
    d "I guess I'll..."

    menu:
        "Drink Popipo":
            jump popipo

        "Get some drinks":
            jump barMb

label popipo:
    show popipo
    with dissolve
    d "It looks just like any other drink."
    d "Might as well try this shit!"
    d "Here goes nothing!"

    scene black
    with dissolve
    play sound "sfx/gulp.wav"
    "Duane chugs the bottle empty in one go."
    d "Phew!"

    scene bg disco
    with dissolve
    d "This has some wack ass taste."
    d "Oh well, I don't think it was tha-"
    d "Never mind, I don't feel so MLG anymore. I think I'll go out for a bit."

    scene black
    with dissolve
    play sound "sfx/steps.mp3"
    "Duane left the disco."

    stop music
    scene street
    with dissolve

    play music "bgm/Bile.ogg"

    d "Oh man what the hell was this shit?!"
    d "I thought vegetable juice is supposed to be healthy or some shit?!"
    d "This just makes me feel like I'm dying."
    d "Is this what people around here drink?"
    d "I need to walk for a bit to catch a breather."
    play sound "sfx/steps.mp3"
    "..."
    d "Yeah..."
    d "I'm feeling better already..."
    d "Why did this need to happen...?"
    d "I wanted..."
    d "to meet that qt again..."
    d "There is no doubt about it..."
    d "I'm positive..."
    d "She has..."
    d "acquired the power..."
    d "of my love..."
    d "I can't..."
    d "leave it like that..."
    d "Not in a place... like this..."
    d "Just a bit more..."
    d "And I can... go back to partying..."
    d "And finally..."
    d "Have my happy end..."
    d "Just..."
    d "JUST"

    scene black
    play sound "sfx/fall.wav"
    "..."
    "Duane collapsed on the street!"
    stop music
    jump wakeUp

label barMb:
    d "I don't think I feel up to try this weird shit yet."
    d "I'll visit the bar after all."
    d "Huh? That girl smoking weed over there, isn't that-"

    show mb love
    with dissolve

    if danced == True:
        ab "Dude! I don't even know if it's because I'm so fucking high right now but..."
        ab "Those moves of yours were something else."
        ab "You seemed like a totally different person on the dance floor."
        ab "Like..."
        ab "Not as much of a dweeb, you know?"
        $ lovePoints += 2
        play sound "sfx/slinkUp2.mp3"
        "Audrey is impressed!"
        "Oh yeah!"
        "Bitches are all over my moves!"

    d "Is that some weed you're smoking?"
    ab "What the hell else would it be?"

    menu:
        "This is illegal you know.":
            d "This is illegal you know."
            hide mb love
            show mb normal
            "Audrey will remember that."
            ab "What the fuck are you on about?"
            ab "Are you like, for real?"
            ab "Like, seriously?"
            ab "Ugh!"
            ab "Do I look like I give a fuck?"
            ab "Didn't you endlessly talk about weed at your school before?"
            ab "You can like piss right off with your bullshit."
            ab "And I even started to think you weren't such a fucking loser."
            d "Uh..."
            "WHY THE LITERAL FUCK DID I JUST SAY THAT?!"
            "I'M ALL ABOUT THAT SHIT!"
            "EVERY SECOND SENTENCE I UTTER IS ABOUT WEED!"
            "IT FLOWS THROUGH MY VEINS!"
            "AND MY FIRST IDEA WHEN TALKING TO A HOT GIRL IS THAT?!"
            "I turned super autismal there for a moment."
            "Jesus..."
            d "Haha! Nah, it was a joke!"
            d "Don't get your panties up in a bunch over it!"
            d "Haha!"
            ab "..."
            ab "Dweeb."
            d "Haha..."
            $ lovePoints -= 2
            "Audrey disliked that."
            "Shit, gotta recover from that."
            jump drinkingGameStart

        "Give me some of that":
            d "Yo, give me some of that dank shit too!"
            ab "You wish!"
            ab "Get some yourself, cunt."
            ab "Like, who the fuck do you think you are?"
            ab "Ugh..."
            ab "Find yourself some fake ass hoe to leech off."
            ab "Cause I sure as hell ain't the one."
            d "Yeah I see that."
            d "♂♂♂ You gave me good advice. ♂♂♂"
            ab "What? Do you star in gay porn now?"
            "She's pretty protective of her weed."
            "Pretty dank characteristic!"

        "Dank shit.":
            d "Dank shit."
            "Audrey will remember that."
            ab "The dankest there is."
            ab "You sure seem to know your shit."
            d "I'm one of the top ranked students of MLG Academy after all!"
            d "Snoop Dogg-sensei taught us a lot about that there dank."
            ab "You know that academy of yours sounds more and more interesting the more you talk about it."
            ab "You need to tell me more about it sometime~♥"
            "Wow, I think I made a good impression on her."
            play sound "sfx/slinkUp1.mp3"
            "Audrey is impressed!"
            $ lovePoints += 1

label drinkingGameStart:

    d "Anyway, how about we have some drinks together?"
    ab "You know what? Why the fuck not? Sure."
    "Nice!"
    "I can use this chance to get her blastered!"
    "That way I can work my magic even better!"

    "---You will now enter the drinking game---"
    "---TUTORIAL---"
    "---Select the drinks you want to give to Audrey.---"
    "---Keep going until you think she had enough.---"
    "---Just as in real life, be careful not to give her too much.---"
    "---The right dosage might lead to something great.---"
    "---Giving her too much can have fatal results.---"
    "---Though these results may lead to an all new adventure!---"
    "---But don't forget.---"
    "---Winners don't do drugs!---"
    "---Stay safe, kid.---"
    d "Aight, here we go!"
    jump drinkingGame

label drinkingGame:

    if drunk == 0:
        ab "Bring it!"
    elif drunk <= 2:
        ab "I'm just getting started!"
    elif drunk <= 5:
        ab "I'm starting to really feel it now!"
    elif drunk <= 9:
        ab "This is the greatest party of all time! ♥"
        ab "Woooooooo~!"
    elif drunk == 10:
        ab "You know me well! I'm finally back~"
        "She's looking..."
        "Genki as hell!"
    elif drunk <= 11:
        ab "I feel like~ like..."
        ab "I..."
        ab "ZZZzzzZZZ..."
        "Seems like there's no point to continue anymore."
    elif drunk > 11:
        stop music
        show mb normal
        "..."
        hide mb normal
        play sound "sfx/fall.wav"
        with hpunch
        scene black
        with dissolve
        "..."
        "Ominous Voice" "You shouldn't have done that."
        "..."
        "..."
        "..."
        jump courtEnding

    menu:
        "Whiskey":
            play sound "sfx/gulp.wav"
            "Audrey annihilates the Whiskey."
            $ drunk += 5
            jump drinkingGame

        "Long Island Ice Tea":
            play sound "sfx/gulp.wav"
            "Audrey conquers the Long Island... Ice Tea."
            $ drunk += 3
            jump drinkingGame

        "Beer":
            play sound "sfx/gulp.wav"
            "Audrey obliterates the beer."
            $ drunk += 1
            jump drinkingGame

        "Vodka Lemon":
            play sound "sfx/gulp.wav"
            "Audrey vanquishes the vodka lemon."
            $ drunk += 3
            jump drinkingGame

        "You've had enough for tonight.":
            jump drinkingGameResult

label drinkingGameResult:

    "I think that's enough!"

    return
