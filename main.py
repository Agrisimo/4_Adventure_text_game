import time

exit_time = 3
name = input("""Hello, what is your name?
:""")

# Question one loop

q1 = f"""{name}, do you want to play a game?
Type: Yes or No?
:"""

while True:
    a = input(q1).lower()
    if a == "no":
        print(f"""Sorry to hear that!
The program will terminate in {exit_time} seconds""")
        time.sleep(exit_time)
        quit()
    elif a == "yes":
        print("Great, lets start!")
        print("")
        time.sleep(1)
        break
    else:
        print(f"I did not get it, {name}! Try again!")
        time.sleep(0.5)

q2 = f"""You entered the hall of an old spooky house!
{name}, do you want to run back to your mommy, go left, go right or go straight?
Choose: run/left/right/straight?
:"""

current_room = "hall"

while True:
    a = input(q2).lower()
    if a == "run":
        print(f"""Sorry to hear that, pussy!
You can go back to your mommy, {name}!
The program will terminate in {exit_time} seconds""")
        time.sleep(exit_time)
        quit()
    elif a == "left":
        print(f"Okie {name}, you chose to go {a}.")
        current_room = "kitchen"
        print(f"You entered the {current_room}!")
        break
    elif a == "right":
        print(f"Okie {name}, you chose to go {a}.")
        current_room = "bedroom"
        print(f"You entered the {current_room}!")
        break
    elif a == "straight":
        print(f"Okie {name}, you chose to go {a}.")
        current_room = "living room"
        print(f"You entered the {current_room}!")
        break
    else:
        print("I did not get it")
        time.sleep(0.5)

time.sleep(1)


q3 = f"""You are now in the {current_room}, what is you next move, {name}?
Do you want to go back, go left, go right or go straight?
Choose: back/left/right/straight?
:"""

while True:
    a = input(q3).lower()
    if a == "back":
        print(f"""You just came from the hall, {name}!
You really want to go back to the hall?""")
        time.sleep(1)
        a_sub = input(f"Type - YES to go {a} to the hall or NO, stay in {current_room} and chose again?").lower()
        time.sleep(0.5)
        print("")
        if a_sub == "yes":
            print("You are in the hall now, I don`t like you, the game will end now!")
            time.sleep(exit_time)
            quit()
        elif a_sub == "no":
            print(f"Okie, {name}, you chose to stay in the {current_room}, where do you want to go next?")
    elif a == "left":
        print(f"Okie {name}, you chose to go {a}.")
        current_room = "west garden"
        print(f"You entered the {current_room}!")
        break
    elif a == "right":
        print(f"Okie {name}, you chose to go {a}.")
        current_room = "east garden"
        print(f"You entered the {current_room}!")
        break
    elif a == "straight":
        print(f"Okie {name}, you chose to go {a}.")
        current_room = "north garden"
        print(f"You entered the {current_room}!")
        break
    else:
        print("I did not get it")
        time.sleep(0.5)

time.sleep(1)
print("Enjoy the fresh air!")
print(f"The game will terminate in {exit_time} seconds!")
time.sleep(exit_time)
quit()
