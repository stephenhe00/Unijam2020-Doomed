label breakout_room_2:
    $ shouko_message = False
    play music music_room_two fadein 10.0 loop
    scene blank
    show Nine_one at top_left_screen
    show Shouko_one at top_right_screen

    "You are last to join, no one seems to be talking. The girl appears to be on mute."
    Nine "Finally someone else is here!"
    Nine "Felt like I was talking to a brick wall with Miss Mute over here."
    Shouko "…"

    menu:
        "Miss Mute?":
            call MissMute from _call_MissMute
            pass
        "What were you guys talking about before?":
            Nine "Oh you know..."
            pass
    Nine "I was just saying how anyone fortunate enough to be on my team would absolutely ace this subject."

    if shouko_message:
        centered "{i}You receive a friend request from \"Shouko Oogushi\""
        menu:
            "Accept friend request":
                pass
            "Decline friend request":
                $ shouko_message = False
                pass

    Nine "Not to brag or anything but I’m 190\% sure I’m the smartest person in this tute."
    Nine "No offence to you or anything,"
    Nine "but you probably won’t do that well just by yourself haha."

    menu:
        "Continue to listen to his rant":
            pass
        "Attempt to cut him off":
            Nine "Uhh okay rude much? So anyways as I was saying..."
            pass

    Nine "Did I mention that I’m f**king loaded?"

    if shouko_message:
        call shouko_message1 from _call_shouko_message1

    Nine "I kinda got loads of connections here and there…"
    Nine "I mean I’m kinda the greatest aren’t I?"

    if shouko_message:
        call shouko_message2 from _call_shouko_message2

    Nine "I absolutely carried my team last sem so…"
    Nine "Ugh honestly aren’t I the best?"

    if shouko_message:
        call shouko_message3 from _call_shouko_message3

    Nine "So what do you say? Team up with me?"

    menu:
        "Yeah for sure!":
            Nine "Nice! Looking forward to it!"              # E N D     - TEAM MATE ACQUIRED - NINE
            scene blank
            show Nine_one at middle
            "(Shouko has left the room)"
            call add_Nine from _call_add_Nine
            jump b2_end

            pass
        "I don't know...":
            call Idontknow from _call_Idontknow
            pass
        "Could you shut the f*** up for once":
            call nine_be_angry from _call_nine_be_angry
            pass

    if shouko_message:
        call shouko_final_moments from _call_shouko_final_moments

    jump b2_end                                      # E N D ------
    return

label b2_end:
    stop music fadeout 5.0
    scene transition
    centered "{i}The Outbreak room has ended."

    if not Nine_joined_team:
        menu:
            "Will you invite Nine-One to join your team?"
            "Yes":
                call add_Nine from _call_add_Nine_1
                pass
            "No":
                pass

    if not Shouko_joined_team:
        menu:
            "Will you invite Shouko to join your team?"
            "Yes":
                call add_Shouko from _call_add_Shouko
                pass
            "No":
                pass

    return

label MissMute:
    Nine "Yeah that’s my nickname for her."
    Nine "Fitting don’t you think? She hasn’t said a word since I joined lmao"
    "{i}Shouko looks as if to speak but decides against it.{/i}"
    menu:
        "Prompt her to speak.":
            call PromptSpeak from _call_PromptSpeak
            pass
        "What were you guys talking about before?":
            Nine "Oh you know..."
            return
            pass
    return

label PromptSpeak:
    Shouko "I… uh… {size=-10}My name is...{/size} {size=-15}Shouko{/size}."
    menu:
        "I see that you like anime?":
            "{i}Shouko blushes but remains silent."
            $ shouko_message = True
            pass
        "Sorry, could you speak up?":
            Shouko "..."
            "{i}Shouko seems hurt by your comment."
            pass
        "What were you guys talking about before?":
            Nine "Oh you know..."
            return
            pass
    Nine "So anyways..."
    return

label shouko_message1:
    centered "{i}You have (1) new messages"
    centered "Shouko: Thanks for talking to me! That really made me feel appreciated (> <)"
    menu:
        "No worries at all!":
            pass
        "Lol what's with the weird emoticon?":
            $ shouko_message = False;
            pass
    return


label shouko_message2:
    centered "{i}You have (1) new messages"
    centered "Shouko: I really don’t think you should choose Nine as a teammate… (> <;)"
    menu:
        "I agree.. He seems a bit dodgy":
            pass
        "He seems like a cool dude":
            $ shouko_message = False;
            pass
    return
label shouko_message3:
    centered "{i}You have (1) new messages"
    centered "Shouko: Don’t listen to a word he’s saying XD Apparently last sem he got caught cheating and failed :P"
    menu:
        "Yikes...":
            pass
        "As long as I get a good mark right?":
            $ shouko_message = False;
            pass
    return

label Idontknow:
    Nine "Uhh okay? Why though?"
    menu:
        "I'm just a little indecisive":
            Nine "Right…"
            Nine "Decide fast though cause I’m sorta in high demand right now."
            Nine "REALLY"
            Nine "HIGH"
            Nine "DEMAND"
            scene blank
            show Shouko_one at middle
            "(Nine has left the room)"                      # NINE LEAVES
            pass
        "You seem like kinda a shitty person...":
            call nine_be_angry from _call_nine_be_angry_1
            pass
    return

label nine_be_angry:
    $ Nine_angry = True
    scene blank
    show Shouko_one at top_right_screen
    show Nine_two at top_left_screen
    Nine "{cps=*5}What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fuckin-{/cps}"
    scene blank
    show Shouko_one at middle
    "(Nine has left the room)"                              # NINE LEAVES
    return

label shouko_final_moments:
    Shouko "..."
    Shouko "Is he finally gone?"
    Shouko "Thank goodness..."

    menu:
        "What a relief":
            pass
        "Why are you still here?":
            scene blank
            show Shouko_three at middle
            Shouko "?!"
            Shouko "Am I not supposed to be?"
            Shouko "..."
            scene blank
            "(Shouko has left the room)"                   # E N D --- SHOUKO LEAVES
            $ Shouko_angry = True
            return
            pass

    Shouko "I know right."
    scene blank
    show Shouko_two at middle
    Shouko "Thank you for accepting my friend request"

    menu:
        "No worries!":
            pass
        "It was fun talking to you!":
            pass
    scene blank
    show Shouko_one at middle
    Shouko "I just wanted to warn you about Nine."
    Shouko "Thanks for believing me."

    player "How did you know Nine cheated?"

    Shouko "Do you know Alistair from our class?"

    menu:
        "Alistair Maffot?":
            "Yes that’s right!"
            pass
        "I'm not too sure...":
            pass

    Shouko "Well, him and Nine-One are both repeating the subject this semester."
    Shouko "But Alistair is actually a really nice and hardworking person!"
    Shouko "Alistair only failed because Nine cheated!"

    menu:
        "I see...":
            pass
        "Thanks for the heads up!":
            pass
        "That's a nice teddy bear you have at the back!":
            call b2_teddybear from _call_b2_teddybear
            pass
    centered "Outbreak room ends in 60 seconds."

    Shouko "It was nice talking to you!"
    Shouko "Hopefully I’ll get to talk to you again! (> <)"

    menu:
        "Hope to talk again soon too!":
            pass
        "See you!":
            pass
    return

label b2_teddybear:
    $ Shouko_mentioned_teddy = True
    scene blank
    show Shouko_two at middle
    Shouko "!"
    Shouko "Yeah I really like teddy bears..."                               # SHOUKO BLUSHES
    Shouko "They're just so adorable..."
    scene blank
    show Shouko_one at middle
    return
