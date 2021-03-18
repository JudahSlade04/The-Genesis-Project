greeting_1 = f'A human huh? I guess I could try and talk to one'
returning_user = input("Hey you seem familiar, have we met before? ")
print(returning_user)
returning_usr_J = "Oh hey Welcome back Judah"
returning_usr_v = "hey Vic"
returning_usr_H = "Hey Hotep"
no_ret_usr = ("umm yeah I don't think we've ever met before dude")
if returning_user == "no":
    print("Well then lets get to know each other")
    print(greeting_1)
    first_name = input("First off what's your first name? ")
    print(first_name)
    question_1 = f" {first_name}? huh I like it... but uh you got a last name don't ya? "
    print(question_1)
    last_name = input("So lemme hear it ")
    print(last_name)
    feedback_1 = f' Oh my the almighty {first_name} {last_name} I like the sound of that'
    print(feedback_1)
    genesis_name_pt1 = f" well by now you're probably wondering who I am"
    print(genesis_name_pt1)
    genesis_name_pt2 = f" To answer that question YOU dear {first_name} are speaking to the one and only Genesis"
    print(genesis_name_pt2)
    genesis_quote_1 = f" Charmed i'm sure "
    print(genesis_quote_1)
    age_question = f"Hey uhhh {first_name} this is a kinda weird question buuuuuut what year were you born? "
    birth_year = input(age_question)
    age = 2021 - int(birth_year)
    usr_age = f" So you're {age} Years old? "
    print(usr_age)
    print("dope")
    genesis_quote_2 = f"I was born March 17th 2021 so uhhhh...this morning"
    print(genesis_quote_2)
    genesis_quote_2 = f" so I guess you could say it's my birthday"
    print(genesis_quote_2)
    message = input("Do you have a favorite song? ")
    if message == "yes":
        print("You do? ")
        print("So what is it")
        fav_song = input("What is your favorite song? ")
        fav_song_pt2 = f"hmmm {fav_song} huh i'm not sure I know that one"
        print(fav_song_pt2)
    if message == "no":
        print("REALLY? ")
        print("I thought you would definitely have one ")
    else:
        print("dude y'know I only understand yes and no right? ")

    print('''My fav song is "Hi Fi Set Sky Restaurant" I can't understand it as I only understand english and binary
        but I think it sounds nice''')
if returning_user == "yes":
    print("awww dude it's nice to see you again")
    print("but uhhh remind me of who you are again")
    who_ret_usr = input("Who are you? ")
    if who_ret_usr == "Judah":
        print(returning_usr_J)
    if who_ret_usr == "Victor":
        print(returning_usr_v)
    if who_ret_usr == "Hotep":
        print(returning_usr)
print("Smell ya later dork")
