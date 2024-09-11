# 184 | 252
label start:
    
    # Transition 
    show screen inventory_display
    scene bg home_office with dissolve

    # Introduction Scene 

    narrator "You are a private eye by the name of Song Qi"
    narrator "Aged 32 years, you work on cases for the local community of Forest Hills"
    narrator "Forest Hills, an area of Queens, New York with a population of 100,000 people and growing"
    narrator "Having led a life of full but nonetheless incomplete stories"
    narrator "This led you to try to make a living solving a variety of low risk but nonetheless important problems"
    narrator "Starting in high school and then going on to college, you focused primarily on..."
    menu:
        "Getting into the best college":
            narrator "And as a result, you managed to get into one of your target school, but with a full ride, so few tears were shed there."
            narrator "Keeping in line with your ambition, you decided to study computer science"
            narrator "After long hours and long applications, you worked in Silicon Valley for a while"
            narrator "But the tedium and tickets got to you, and after saving up, you got a small place back home in New York and quit."
            narrator "\[Tech Sector\],\[Gamer\],\[Side Hustle\] Increased" 
            $ chi.character.path = 'Tech Bro'
            $ chi.character.stats['Tech Sector'] += 50
            $ chi.character.stats['Gamer'] += 50
            $ chi.character.stats['Side Hustle'] += 50
            $ chi.character.stats['Checking Account'] += 4000
        "I wanted to see the world":
            narrator "You knew academics were important, but you also knew life was meant to be lived."
            narrator "You applied for a larger liberal arts college in the middle of nowhere, before proceeding to be nowhere in the country for most of the year."
            narrator "Costs were something you tried hard to budget for, but traveling around was never going to be free, either."
            narrator "\[Debt\] Increased Moderately"
            narrator "\[Socialite\],\[Reader\],\Eating Out\],,\[Casual Sex\] Increased"
            $ chi.character.path = 'Traveler'
            $ chi.character.stats['Socialite'] += 20
            $ chi.character.stats['Reader'] += 20
            $ chi.character.stats['Eating Out'] += 50
            $ chi.character.stats['Casual Sex'] += 30
            $ chi.character.stats['Checking Account'] -= 2000
        "Having fun while my body and time were mine":
            narrator "It wasn\'t being bad at school that stopped you from caring. It was just not as interesting as what life had to offer."
            narrator "After making friends with some people that didn\'t take things as seriously, you started, for the first time since you were a kid, having fun."
            narrator "You were smart enough to keep yourself out of most trouble, but looking for novelty and quite honestly fun led to a few bumps and scars. But you liked that."   
            narrator "When you came back to settle down a bit you were out of money, but a world of experience meant you built up friends quickly."
            narrator "\[Socialite\],\[Raver\],\Eating Out\],,\[Casual Sex\],,\[Community Manager\],\[Jogging\],\[Side Hustle\] Increased"            
            $ chi.character.path = "Party Animal"
            $ chi.character.stats['Socialite'] += 30
            $ chi.character.stats['Raver'] += 20
            $ chi.character.stats['Eating Out'] += 50
            $ chi.character.stats['Casual Sex'] += 30
            $ chi.character.stats['Community Manager'] += 50
            $ chi.character.stats['Checking Account'] -= 4000

    narrator "Great, what a life you\'ve led up till now. Here, have a little gift. Now let us get started."
    narrator "OBTAINED \[20 Dollars\]"
    $ inventory_items['20 Dollar Bill'] = "A Crisp Twenty Dollar Bill"
    $ objectives['Complete Act One'] = "In Progress"
    tutorial "Maybe you should go to the bank to deposit this. Or maybe you can buy yourself a lunch"

    # Options per path
    narrator "The story begins with you at your desk, managing some paper work. The jobs that come in are never that quick, so theres plenty of time to take case notes and file the neccisary paperwork."
    tutorial "If you were being honest with yourself, it has actually been slower than usual. So much so you decided to try learning a new language"
    menu:
        "Chinese":
            narrator "Mandarin or Can- never mind you are learning Mando, for your families sake."
        "French":
            narrator "You never went to France, but you secretly always thought the language seemed sexy."
        "German":
            narrator "You met a German girl once, and on the off chance all German girls are like that, you want to be prepared this time."
    
    tutorial "Oh look, I think someone is coming up the stairs to your office now."
    narrator "A man walks in, wearing a plaid shirt and jeans, neither of which is tucked or sized properly. You see his undershirt visibly but you decide it is not worth mentioning."
    
    # Script 
    client.character "Is this the...Qi detective agency? Sorry, I called ahead but I don\'t want to butcher the name."
    chi.character "Yeah, you said you had a problem with finding a friend? How can I help?"
    narrator "The client takes a long glance around the space you call an office"
    client.character "I always thought they were bigger nowadays. I was also a bit short on time and panicked so I went with the closest one"
    client.character "Sorry I am new to this, but I am not sure this is the best option?"
    chi.character "I can't blame you, but if it helps, my reviews have been pretty good, and we try to keep our prices low."
    client.character "We?"
    chi.character "I work with consultants that are called as needed for cases. I even have one for animals in case a lost animal is found by a shelter or something."
    client.character "Ah, well, sounds like you have a lot of experience, at least. In that case, can you help with a missing person's case?"
    chi.character "Sure. Tell me the story and why you're concerned."
    client.character "Basically, I had a bet with this friend of mine, and he lost."
    client.character "We've been friends since we were kids, so when he would complain about the bet amount, I told him we could back out, but I guess he was being stubborn." 
    client.character "Anyways, after he lost the bet, I figured I would give him some time to grieve before asking for the money."
    chi.character "How much was the amount, and what was the bet about?"
    client.character "1000, and whether the Mets were going to sweep their game against the Marlins."   
    "Writes down the information."
    chi.character "Gotcha, that was last Sunday, right?"
    client.character "Yeah."
    chi.character "So this would have been almost a week? Was this a long time for him not to contact you?"
    client.character "Yeah, well, we don't really chat much, but we like to hang out for poker night, and he would at least text one of us if he wasn't coming."
    chi.character "Okay. So, good news: I can take this case on. As a disclaimer, I am not allowed by law to tail anyone or offer surveillance in any restricted area. With those conditions, would you still like to hire our services?"
    client.character "Honestly, yeah. It's not like he or I are spies or anything. I just want to know if he's hiding in a hotel nearby or something. He can't have gotten far; his car is still parked nearby. Here, a key to his place; we keep each other's for emergencies before you ask about how I got it or whatever."
    chi.character "I guess it can't hurt. I know that building has a super, so at worst, it'll be an apology for wasting his time."
    client.character "Yea, I have the keys to his place, so I can let you in with it."

    client.character "Awesome. So are you saying you\'ll take the case?"
    narrator "He takes a small key fob out of his pocket, with one of the medium sized keys pointed out at you."
    
    menu:
        "Sure":
            chi.character "Sure I'll take the case."
            narrator "Key to Residence OBTAINED"
            $ inventory_items["Key to Residence"] = "A key that supposedly opens the door to Bill\'s apartment door. We have been given permission to access it, but we should probably check with the super or doorman first."
        "This sounds a bit awkward":
            chi.character "Are you sure you are better off not reporting this to the cops?"
            client.character "I had a little bit of trouble with the police, honestly I\'d rather not deal with them."
            client.character "Oh especially since the reason he might have ran off is the betting."
            chi.character "Is it so bad if its just you two as friends?"
            client.character "Yea I think he would get mad at me if he found out I got the cops to look through his place"
            client.character "He likes to smoke-"
            client.character "Never mind"
            chi.character "Oh, I get it. No problem."
        "No":
            chi.character "I have some more questions, otherwise I cannot accept"
            client.character "Why not, I answered all your questions"
            chi.character "Once again, I am not law enforcement. Your story sounds a bit odd, and potentially breaking into someones apartment-"
            client.character "I have the key what do you mean breaking in?"
    client.character "Wow, you really know a lot of people."
    chi.character "Yeah, I specialize in the Forest Gardens area, so I figured you guys lived close by."
    client.character "About 5 blocks away. For both of us I think."
    chi.character "I'll go take a look later this morning. Anything I should know about before I go? Also, I'll need your contact information, email and phone, phone preferred."
    chi.character "I have an upfront deposit of five hundred dollars, for a case like this..."
    menu:
        "Lie \[900 plus fees\]":
            chi.character "The total cost for finding him is 900, and if my costs exceed the initial 500 you give me, I will notify you and charge extra."
         "Tell the truth \[500 plus fees\]":
            chi.character "The total cost for finding him is 500, and if my costs exceed the initial 500 you give me, I will notify you and charge extra."   
    client.character "Oh yeah, got it. *scribbles* And nah, he lived alone, and he didn't mention a girlfriend or anything."
    chi.character "That works. Okay, if I find out anything, I'll send you a message. I recommend you file a missing person's report right after if you haven't already. It can be a bit awkward, but it's for safety."
    client.character "Got it. Do you mind starting that? I'm already late for my job, and I kind of expected to have 5 grand more than I currently do."
    chi.character "I can try, but you'll need to go down to the station across the street first. I can follow up for you, though. Don't worry, it takes five minutes. Just tell them I sent you."
    client.character "Awesome, honestly I feel great about this already. Thanks, man."
    chi.character "No problem, have a nice day. Did you make sure to leave me your contact information?"
    client.character "Oh yea you have my number on the form. I didn\'t give you my email though."
    chi.character "Should be fine"
    client.character "Ok detective, looking forward to hearing from you. Is it weird I think this is kinda cool?"
    chi.character "I guess not, it is why I started doing it in the first place. And yes I will update you with anything I find."

    jump act_one

    return 

label act_one:

    scene outside_intro
    show screen inventory_display

    narrator "Stepping out into Austin Street, the strange combination of being very busy yet not particularly popular made the fusion that became Forest Hills."
    narrator "As he walked down the block, Song happened upon a regular customer and neighbor. A seventy year old widower with a son on the West Coast, Eva noticed him first."
    eva.character "Well look who it is, the helpful detective. Having a nice day? Mustn\'t to be too difficult, with weather like this."
    narrator "EVA motions up to the sky with a slight nod"
    chi.character "Good Afternoon, Miss Eva, is everything going well? Is your dog still safe and sound at home?"
    eva.character "Why yes and thank you so much again for that. I admit I did not expect a detec-"
    chi.character "Private Eye, ma\'am"
    eva.character "of course, I would think that working with pets would be too specific a case, but I guess you proved me wrong, and Muffins has you to thank."
    tutorial "This is Eva, a neighbor who you have helped on several occasions; as a result she has a lot of trust in your abilities, and a lot of gratitude for your help."
    tutorial "As a result she has stats that indicate her relationship and impression of you. Based on your dialouge options, you can improve or degrade certain impressions."
    tutorial "Try to play around with it! Getting too high or too low a score in any field isn\'t what you may want at first glance."

    ''' Add options here; since its a tutorial and its an RPG, you cant degrade it too poorly, but you can get an awkward interaction at worst, and a positive trivia at best '''

    scene bill_residence

    narrator "Walking up to the third story and wondering why people lived in buildings without an elevator, Song got to the unit listed on the key fob"
    chi.character "305. This seems to be it."
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
            chi.character "Lets see....yup theres a lever on the couch"
            menu:
                "Pull the lever":
                    narrator "Song pulls the lever, and the bed springs out suddently into a bed."
                    narrator "You hear a rip as the ottoman was damaged from a jagged edge of the old and worn couch pullout."
                    chi.character "Dang"
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
            chi.character "Huh."
            narrator "There was nothing inside the bin, in fact the bag looked like it was recently replaced."
            jump bill_residence_options
        "I am done here":
            chi.character "Time to leave-"
            eva.character "Oh, Mr. Qi, what are you doing here? I saw Bill\'s door open and I was worried. I havent seen him in over a week."
            chi.character "I am actually here to investigate that."
            eva.character "Oh? That\'s concerning to hear, but if you are on the case I\'m sure it will turn out all right."
            eva.character "Don\'t let me get in the way, I will get out of your hair-"
            chi.character "Actually, I am quite glad you are here, do you mind if I ask a few questions?"
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
                    chi.character "Of course, I\'ll see if I can\'t do it on the way back to my office."
                    narrator "Side Quest \[Sign Eva up for Ballroom\] Started"
                    $ objectives['Sign Eva up for Ballroom'] = "In Progress"
                    narrator "The Objective \[Sign Eva up for Ballroom\] has been started"
                    tutorial "This is a side objective that you can complete while playing through each act"
                    tutorial "Completion is optional, but you can gain some benefits from helping out the people around you."
                    tutorial "This can be in the form of \[Stat Boosts\], \[Favors\] , or \[Perks\]"
                    tutorial "Stats refer to gaining benefits for individual members, such as more trust or less fear"
                    tutorial "Favors are consumable passes that allow you to bypass certain events or gain items you may have missed."
                    tutorial "Perks allow you to benefit from getting further embedded in certain communities."

    narrator "End of Act One"

    jump act_two


label act_two:

    show screen inventory_display
    
    narrator "Act Two Begins"

    return





