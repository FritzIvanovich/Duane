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
    y "I need to pick up a birthday cake for my little sister there."
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
    ab "A school that allows weed, huh?"
    ab "Don't think I got the whole night to talk with you."
    ab "I gotta go now, I've got more important things to do."
    
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
            "Maybe she will even invite me over for dinner if she sees me there!"
            play sound "sfx/dinner.wav"
            "Well, maybe not, but I can't ignore this opportunity that just presented itself to me!"
            "Duane followed Audrey like an Ukranian Ninja!"
            jump stalkMb
        "Go Party even harder than you work":
            "It's a beautiful night to have a Party!"
            # What a horrible night to have a curse!
            d "What the...?!"
            "Suddenly time stopped and some weird shit was floating in the air."
            "What the heck, well it doesn't matter anyways."
            "I'll just go to the next club, gotta show 'em my sick moves!"
            "Let's do this shit!"
            jump discoMb

    return

label stalkMb:
    show street
    with Fade(0.5, 2.0, 0.5)
    "..."
    d "Damn! I lost her ..."
    d "Who could have thought she is THAT fast on her legs!"
    d "If I didn't know any better I'd think she wante to get away from me."
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
    #Watch this, Cloud.


    return