init:

    ### Backgrounds
    image home_office = 'office.jpg'

    ### Screen Init
    $ config.window_title = 'Chinatown Detective'

    ### Inventory System
    screen inventory_display:
        zorder 92
        frame:
            background "#9F99"
            xalign 0.05
            yalign 0.1

        hbox:
            textbutton "Inventory":
                action ToggleScreen("inventory_description")
                style "inv_button"
            textbutton "Objectives":
                action ToggleScreen("current_objectives")
                style "inv_button"

        on "hide" action Hide("inventory_description")

    default inventory_items = {}
    default item_description = ""
    default objectives = {}
    default objective_description = ""

    style inv_button is frame:
        xsize 200
        ysize 100

    style inv_button_text:
        xalign 0.5
        yalign 0.5

    screen inventory_description:
        
        window:
            background "#AAA9"
            xsize 600
            ysize 150
            xalign 0.5
            yalign 0.1
            text item_description:
                xfill True
                yfill True

        window:
            background "#99F9"
            xsize 1290
            ysize 600
            xalign 0.5
            yalign 0.7
            hbox:
                box_wrap True
                box_wrap_spacing 10
                spacing 10
                xoffset 20
                yoffset 20
                style_prefix "inv"
                for item in inventory_items:
                    textbutton item:
                        action SetVariable("item_description", inventory_items.get(item))
                        selected False

        on "hide" action SetVariable("item_description", "")

    ### Objectives
    screen current_objectives:

        window:
            background "#AAA9"
            xsize 600
            ysize 150
            xalign 0.5
            yalign 0.1

        window: 
            background "#99F9"
            xsize 1290
            ysize 600
            xalign 0.5
            yalign 0.7
            hbox:
                box_wrap True
                box_wrap_spacing 10
                spacing 10
                xoffset 20
                yoffset 20
                style_prefix "obj"
                for objective in objectives:
                    textbutton objective:
                        action SetVariable("objective_description", objectives.get(objective))
                        selected False

        on "hide" action SetVariable("objective_description", "")

    ### Gallery
    screen gallery:
        tag menu

        grid 3 2:
            xalign 0.5 yalign 0.5

            # Introduction Image 
            # add "unlocked_image_1.jpg" if persistent.image1_unlocked else "locked_image.jpg"
            textbutton "Return" action Return()

label start:
    
    # Transition 
    show screen inventory_display
    scene bg home_office with dissolve


    # Testing

    dre.character "Look you found 5 dollars in your pocket"
    $ inventory_items["5 Dollars"] = "A crisp five dollar bill."
    narrator "OBTAINED \[5 Dollars\]"
    $ objectives['Tutorial Quest'] = "kfnfknvfkldnlknfnv"

    # Script 
    client.character "Is this the detective agency? I called ahead."
    chi "Yeah, you said you had a problem? How can I help?"
    "The client looks around."
    client.character "I always thought they were bigger nowadays. I was a bit panicked so I went with the closest one, but I'm not sure this is the best option."
    chi "I can't blame you, but if it helps, my reviews have been pretty good, and we try to keep our prices low."
    client.character "We?"
    chi "We work with consultants that we call as needed for cases. I even have one for animals in case a lost animal is found by a shelter or something."
    client.character "Ah, well, sounds like you have a lot of experience, at least. In that case, can you help with a missing person's case?"
    chi "Sure. Tell me the story and why you're concerned."
    client.character "Basically, I had a bet with this friend of mine, and he lost."
    client.character "We've been friends since we were kids, so when he would complain about the bet amount, I told him we could back out, but I guess he was being stubborn." 
    client.character "Anyways, after he lost the bet, I figured I would give him some time to grieve before asking for the money."
    chi "How much was the amount, and what was the bet about?"
    client.character "5000, and whether the Mets were going to sweep their game against the Marlins."   
    "Writes down the information."
    chi "Gotcha, that was last Sunday, right?"
    client.character "Yeah."
    chi"So this would have been almost a week? Was this a long time for him not to contact you?"
    client.character "Yeah, well, we don't really chat much, but we like to hang out for poker night, and he would at least text one of us if he wasn't coming."
    chi "Okay. So, good news: I can take this case on. As a disclaimer, I am not allowed by law to tail anyone or offer surveillance in any restricted area. With those conditions, would you still like to hire our services?"
    client.character "Honestly, yeah. It's not like he or I are spies or anything. I just want to know if he's hiding in a hotel nearby or something. He can't have gotten far; his car is still parked nearby. Here, a key to his place; we keep each other's for emergencies before you ask about how I got it or whatever."
    chi "I guess it can't hurt. I know the building super, so at worst, it'll be an apology for wasting his time."

    client.character "Awesome. So are you saying you\'ll take the case?"
    narrator "He takes a small key fob out of his pocket, with one of the medium sized keys pointed out at you."
    
    menu:
        "Sure":
            chi "Sure I'll take the case."
            $ inventory_items["Key to Residence"] = "A key that supposedly opens the door to Bill\'s apartment door. We have been given permission to access it, but we should probably check with the super or doorman first."
        "This sounds a bit awkward":
            chi "Are you sure you are better off not reporting this to the cops?"
            client.character "I had a little bit of trouble with the police, honestly I\'d rather not deal with them."
            client.character "Oh especially since the reason he might have ran off is the betting."
            chi "Is it so bad if its just you two as friends?"
            client.character "I don\'t want to talk about it but its not just us."
            chi "Oh, I get it. No problem."
        "No":
            chi "No"
    client.character "Wow, you really know a lot of people."
    chi "Yeah, I specialize in the Forest Gardens area, so I figured you guys lived close by."
    chi "I'll go take a look later this morning. Anything I should know about before I go? Also, I'll need your contact information, email and phone, phone preferred."
    client.character "Oh yeah, got it. *scribbles* And nah, he lived alone, and he didn't mention a girlfriend or anything."
    chi "That works. Okay, if I find out anything, I'll send you a message. My rate is per job, but for something like this, I would charge per day. I recommend you file a missing person's report right after if you haven't already. It can be a bit awkward, but it's for safety."
    client.character "Got it. Do you mind starting that? I'm already late for my job, and I kind of expected to have 5 grand more than I currently do."
    chi "I can try, but you'll need to go down to the station across the street first. I can follow up for you, though. Don't worry, it takes five minutes. Just tell them Chi sent you."
    client.character "Awesome, honestly I feel great about this already. Thanks, man."
    chi "No problem, have a nice day."

    jump act_one

    return 

label act_one:

    scene outside_intro
    show screen inventory_display

    narrator "Stepping out into Austin Street, the strange combination of being very busy yet not particularly popular made the fusion that became Forest Hills."
    narrator "As he walked down the block, Song happened upon a regular customer and neighbor. A seventy year old widower with a son on the West Coast, Eva noticed him first."
    eva.character "Well look who it is, the helpful detective. Having a nice day? Mustn\'t to be too difficult, with weather like this."
    narrator "EVA motions up to the sky with a slight nod"
    chi "Good Afternoon, Miss Eva, is everything going well? Is your dog still safe and sound at home?"
    eva.character "Why yes and thank you so much again for that. I admit I did not expect a detec-"
    chi "Private Eye, ma\'am"
    eva.character "of course, I would think that working with pets would be too specific a case, but I guess you proved me wrong, and Muffins has you to thank."
    tutorial "This is Eva, a neighbor who you have helped on several occasions; as a result she has a lot of trust in your abilities, and a lot of gratitude for your help."
    tutorial "As a result she has stats that indicate her relationship and impression of you. Based on your dialouge options, you can improve or degrade certain impressions."
    tutorial "Try to play around with it! Getting too high or too low a score in any field isn\'t what you may want at first glance."

    ''' Add options here; since its a tutorial and its an RPG, you cant degrade it too poorly, but you can get an awkward interaction at worst, and a positive trivia at best '''

    scene bill_residence

    narrator "Walking up to the third story and wondering why people lived in buildings without an elevator, Song got to the unit listed on the key fob"
    chi "305. This seems to be it."
    narrator "The door opens after a little effort to overcome the friction of the door and the dirty rug."
    narrator "At first glance the room could best be described as hand-me-downs from grandpa. There was a trash can full of take out boxes visible from the entrance."
    narrator "On the ottoman in front of the couce, there were a few papers that looked like receipts"
    narrator "The kitchen counter also had an assortment of items on it, most of which were partially obscured by plastic bags and takeout boxes."
    narrator "Last but not least, there is a computer on a little end table, with the screen open up to what looks like a bunch of tabs."


label bill_residence_options:
    menu:
        "Check out the kitchen counter":
            narrator "The kitchen counter "
        "Check out the papers on the ottoman":
            narrator ""
        "Look for the bedroom":
            narrator "Looking around for a bedroom, it became quickly apparent that this was a studio apartment"
            chi "Lets see....yup theres a lever on the couch"
            menu:
                "Pull the lever":
                    narrator "Song pulls the lever, and the bed springs out suddently into a bed."
                    narrator "You hear a rip as the ottoman was damaged from a jagged edge of the old and worn couch pullout."
                    chi "Dang"
                    tutorial "In the course of your work, you may cause damage to the clients or the clients items."
                    tutorial "Depending on how you attempt to manipulate the situation, either by being honest"
                    tutorial "Or by being manipulatative"
                    tutorial "Or even by lying by omission"
                    tutorial "You can have different outcomes"
                    tutorial "For now, why don\'t you grab that piece of paper on the bedroll, and see what it has on it?"
                    $ inventory_items["Losing Betting Slip"] = "A slip of paper iunno im lazy."
                    jump bill_residence_options
        "Look inside the trash can":
            narrator "With an audible sigh, Song removes the trash lid, ready for whatever may happen."
            chi "Huh."
            narrator "There was nothing inside the bin, in fact the bag looked like it was recently replaced."
            jump bill_residence_options
        "I am done here":
            chi "Time to leave-"
            eva.character "Oh, Mr. Qi, what are you doing here? I saw Bill\'s door open and I was worried. I havent seen him in over a week."
            chi "I am actually here to investigate that."
            eva.character "Oh? That\'s concerning to hear, but if you are on the case I\'m sure it will turn out all right."
            eva.character "Don\'t let me get in the way, I will get out of your hair-"
            chi "Actually, I am quite glad you are here, do you mind if I ask a few questions?"
            eva.character "I have a roast in the oven but sure dear. "

            jump eva_questioning

label eva_questioning:

    menu:
        "What was your impression of him as a neighbor?":
            eva.character "Oh he was nice enough, he would have friends over quite often. They could get a bit loud at times"
            narrator "She pauses to think on what she said"
            eva.character "But honestly it was nice to have the sounds of people, it has been a while for me since my husband passed"
            menu:
                "I\'m sorry to hear that":
                    eva.character "Thank you dear, but I am sure he is in a good place, and I hope to get there too one day."
                    $ eva.relationship['Memory'] -= 10
                    $ eva.relationship['Respect'] -= 10
                "\[Community Manager\] There is a ballroom dance class at the rec center each Thursday.":
                    narrator "Eva noticably lit up at the news"
                    eva.character "Oh that sounds lovely dear, can you help me sign up? I can make time for it this week if possible"
                    chi "Of course, I\'ll see if I can\'t do it on the way back to my office."
                    narrator "Side Quest \[Sign Eva up for Ballroom\] Started"
                    $ current_objectives['Sign Eva up for Ballroom'] = "In Progress"

        # Test Script
        "I am here to find and kill him":
            $ eva.relationship['Fear'] += 30
            $ eva.relationship['Memory'] -= 15

    narrator "End of Act 1"

    jump act_two


label act_two:

    show screen inventory_display
    
    narrator "Blah"

    return





