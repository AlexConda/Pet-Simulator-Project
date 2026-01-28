from inputimeout import inputimeout, TimeoutOccurred
import numpy as np
import time
import random
import sys
import matplotlib.pyplot as plt
import os
import Gacha as gacha
import PetReactions as anim


#Main programmer Rain Jarren
#edited by Alex Conda



def pet_bird():
    #print(f"Importing pet_cat.py, __name__ = {__name__}") #just for testing
    # matplotlib history
    hunger_history = []
    energy_history = []
    happiness_history = []
    hygiene_history = []
    age_history = []


    MAX_STAT = 100

    def no_actionTaken():  # animation to let user know stats are draining
        anim.bird_neutral()
        for i in range(3):
            print("Draining" + "." * (i + 1), end="\r", flush=True)
            time.sleep(0.5)
        print(" " * 20, end="\r")


    def GAMEOVER_SCREEN():
        time.sleep(2)
        plt.plot(hunger_history, label="Hunger")
        plt.plot(energy_history, label="Energy")
        plt.plot(happiness_history, label="Happiness")
        plt.plot(hygiene_history, label="Hygiene")
        plt.plot(age_history, label="Age")

        plt.title("Pet's Stats Before Game Over")
        plt.xlabel("Turns")
        plt.ylabel("Stat Value")
        plt.legend()
        plt.show()

    def sleeping_animation(duration):
        os.system('cls' if os.name == 'nt' else 'clear')
        dots = [" .  ", " .. ", " ..."]
        start = time.time()
        anim.bird_sleeping()

        while True:
            elapsed = time.time() - start
            if elapsed >= duration:
                break
            remaining = int(duration - elapsed)
            minutes = remaining // 60
            seconds = remaining % 60
            timer = f"{minutes:02d}:{seconds:02d}"
            for d in dots:
                if time.time() - start >= duration:
                    break
                sys.stdout.write(f"\rSleeping{d}  |  Time left: {timer}")
                sys.stdout.flush()
                time.sleep(0.5)
        sys.stdout.write("\rSleep finished!                  \n")

    def type_out(text, speed=0.02):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        print()


    warning_given = False

    def get_pet_name():
        while True:
            name = input("Please enter your pet's name: ").strip()
            if name:
                return name
            else:
                print("Pet name cannot be empty. Please try again.")

    pet_name = get_pet_name()
    time.sleep(0.5)

    hunger = MAX_STAT
    energy = MAX_STAT
    happiness = MAX_STAT
    hygiene = MAX_STAT
    age = 0  
    total_gameplay = 25

    # Game state helpers and timers
    game_over = False

    time.sleep(1)

    # Main loop

    while not game_over:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("="*114)
        print("⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘".ljust(30), f"ฅ^._.^ฅ = {pet_name}'s STATS = ૮₍ • ᴥ • ₎ა".center(25), "⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘".rjust(30))
        print("="*114,"")
        print(f"\nHunger: {hunger}/100 \nEnergy: {energy}/100 \nHappiness: {happiness:}/100 \nHygiene: {hygiene}/100 \nAge: {age:.2f} years".center(114))

        print(" ⋆ Main Menu ⋆  ".center(114, "="))
        print("₊✩‧₊˚  ౨  ৎ  ˚  ₊✩‧₊   ₊✩‧₊˚  ౨  ৎ  ˚  ₊✩‧₊                 ₊✩‧₊˚  ౨  ৎ  ˚  ₊✩‧₊   ₊✩‧₊˚  ౨  ৎ  ˚  ₊✩‧₊".center(114))
        print("-"*114)
        print("\nWhat would you like to do?")
        print("1 - Feed your pet (+Hunger)")
        print("2 - Let your pet rest (+Energy)")
        print("3 - Play with your pet (+Happiness)")
        print("4 - Give your pet a bath (+Hygiene)")
        print("Press Enter or wait 15 seconds to do nothing.")
        print()
   

        try:
            choice = inputimeout(prompt='Enter your choice: ', timeout=15).strip() #time for user to react
        except TimeoutOccurred:
            choice = ''




        if happiness <= 0:
            if not warning_given:
                print("\n⚠ WARNING: Your pet's happiness has reached a critical stat of 0!")
                print(f"{pet_name} is destroying things in your house!\n")
                warning_given = True

            else:
                print(f"{pet_name} left and flew away.")
                anim.bird_angry()
                GAMEOVER_SCREEN()
                game_over = True
                break              

        # If Hygiene <= 35 and neglected for 10 sec:
        # The Blue Jay gets stressed and will leave you and there's a 50% chance he will die
        if hygiene <= 35:
            if random.random() < 0.6: #60 percent chance of reminding user
                anim.dog_turd()
                type_out(f"\n {pet_name} is pooping everywhere!")
                #insert anim
                messages_printed = True
                time.sleep(1)
        if hygiene == 0 :
                if not warning_given:
                    print("\n⚠ WARNING: Hygiene is 0! The Blue Jay is stressed.")
                    warning_given = True

                if random.random() < 0.5: # 50% chance to leave/die
                    restore = np.random.normal(loc=5, scale=2) 
                    restore = max(1, int(restore))
                    hygiene = min(MAX_STAT, hygiene + restore)
                    anim.bird_angry()
                    print("The Blue Jay stayed, but is very stressed. Improve hygiene soon.")
                    time.sleep(2)                  
                else:
                    print("The Blue Jay got too stressed... it has left or died due to the stress.")
                    anim.bird_dead()
                    GAMEOVER_SCREEN()
                    game_over = True
                    break

        # If Energy == 0 -> Blue Jay falls asleep for 1 minute. Player cannot interact except Hygiene actions.
        if energy <= 0:
            if not warning_given:
                print("\nThe Blue Jay has run out of energy and falls asleep for 60 seconds..")
                warning_given = True
                #insert sleeping anim
                sleeping_animation(60)
                restore = np.random.normal(loc=5, scale=2) 
                restore = max(1, int(restore))
                energy = min(MAX_STAT, energy + restore)
                print(f"\nThe Blue Jay wakes up naturally. Energy restored by {restore}.")

        if hunger <= 0:
            if not warning_given:
                print(f"\n⚠ WARNING: {pet_name} is starving!")
                print("You have one last chance to save your pet!\n")
                warning_given = True

            else:
                print("\nGAME OVER: The Blue Jay starved.")
                anim.bird_dead()
                GAMEOVER_SCREEN()
                game_over = True
                break

        if age >= total_gameplay:
            if not warning_given:
                print(f"\n⚠ WARNING: {pet_name} has reached old age!")
                print("You have one last chance to say goodbye!\n")
                warning_given = True
            else:
                print(f"\n {pet_name} lived a good life...")
                anim.bird_dead()
                GAMEOVER_SCREEN()
                game_over = True
                break


        if hunger <= 75:
            # raid (but not every loop)
            if random.random() < 0.3:
                type_out(f"\n⚠ {pet_name}  is hungry and raids the kitchen!")
                # get any random food: random reduction between 10-30 hunger (reduce hunger)
                drain = np.random.normal(loc=[3], scale=[1]).astype(int)
                hygiene -= int(drain)

                print(f"The Blue Jay grabbed some food. Hunger reduced by {drain}.")
                time.sleep(3)
            else:
                pass

        # Hunger == 25 warning 
        if hunger <= 25:
            if random.random() < 0.6: #60 percent chance of reminding user
                type_out(f"\n {pet_name} is screeching loudly")
                messages_printed = True
                time.sleep(1)


        # Small random reminders (as in original code), adjusted to new semantics
        if hunger <= 50:
            if random.random() < 0.4:   # 30% chance
                type_out(f"\n{pet_name} is getting hungry!")
                messages_printed = True
                time.sleep(0.5)

        if happiness <= 70:
            if random.random() < 0.3:
                type_out(f"\n{pet_name} wants to play!")
                messages_printed = True
                time.sleep(0.5)

        if hygiene <= 40:
            if random.random() < 0.6:
                type_out(f"\n{pet_name} is getting dirty...")
                messages_printed = True
                time.sleep(0.5)



        # -------------------- Player actions --------------------
        if choice == '1':
            if hunger == MAX_STAT:
                print(f"{pet_name} is full!")

            else:
                # Feed: reduces hunger
                restore = np.random.normal(loc=8, scale=2) # hunger reduced by ~8
                restore = max(1, int(restore))
                hunger = min(MAX_STAT, hunger + restore)
                anim.bird_eating()
                time.sleep(2)

                print(f"You fed your Blue Jay! Hunger reduced by {restore}.")

                # Trade-off: cleaning/hygiene may go down slightly when feeding  (cleaning/bath reduces happiness; when you play it will get hungry)
                drain = np.random.normal(loc=[3], scale=[1]).astype(int)
                hygiene -= int(drain)


        elif choice == '2':
            if energy == MAX_STAT:
                print(f"{pet_name} is full of energy!")

            else:
                # Rest: user waits 20 seconds to replenish 35 Energy 
                print("\nLetting the Blue Jay rest... (20 seconds)")
                anim.bird_sleeping()
                sleeping_animation(20)
                restore = np.random.normal(loc = 20, scale = 2)
                restore = max(1, int(restore))
                energy = min(MAX_STAT, energy + restore)
                print(f"Your Blue Jay rested! Energy restored by {restore}.")


        elif choice == '3':
            if happiness == MAX_STAT:
                print(f"{pet_name} is already happy!")
                
            else:
                # Play: increases happiness, makes hungry ("When you play with bluejay it will get hungry.")
                restore = int(max(1, np.random.normal(loc=6, scale=2)))
                happiness = (happiness + restore)
                drain = int(max(1, np.random.normal(loc=10, scale=1)))  # gets hungrier
                hunger -= drain
                anim.bird_happy()
                time.sleep(2)
                print(f"You played with your Blue Jay! Happiness +{restore}.")
                print(f"As a result, it got hungrier. Hunger -{drain}).")

        elif choice == '4':
            if hygiene == MAX_STAT:
                print(f"{pet_name} is already clean!")

            else:
                # Bath: increases hygiene; "When you clean/bath blue jay, the happiness bar will go down"
                restore = int(max(1, np.random.normal(loc=15, scale=2)))  # typical bath boost
                hygiene = (hygiene + restore)
                # Tradeoff: reduces fun/happiness when bathing
                drain = int(max(1, np.random.normal(loc=5, scale=1)))
                happiness -= drain
                anim.bird_bathing()
                print(f"You bathed your Blue Jay! Hygiene +{restore}. Happiness -{drain} (it didn't like it).")
                time.sleep(2)

        elif choice == '':
            print("\nNo action taken.")
            time.sleep(1)

        else:
            print("\nInvalid input or action not allowed now.")
            time.sleep(1)

        # -------------------- After-action logging --------------------
        hunger_history.append(hunger)
        energy_history.append(energy)
        happiness_history.append(happiness)
        #print(f"DEBUG hygiene type: {type(hygiene)}, value: {hygiene}")
        hygiene_history.append(hygiene)
        age_history.append(age)

        no_actionTaken()
        # -------------------- Passive drains (per original but adjusted) --------------------
        # We will drain each tick by small random amounts




        if not game_over:   
            drain = np.random.normal(loc=[5, 8, 10, 15], scale=[1, 1, 1, 1])
            drain = np.maximum(drain, [1, 1, 1, 1]).astype(int)

            #indexing lng to guyz
            hunger -= int(drain[0])
            energy -= int(drain[1])
            happiness -= int(drain[2])
            hygiene -= int(drain[3])



            if random.random() < 0.6:  #60% chance to age
                age += 0.2

            aging_factor = min(age / total_gameplay, 1)
            mean_restore = 8 * (1 - aging_factor)
            restore = np.random.normal(loc=mean_restore, scale=1)
            restore = max(0, restore)

            age = min(age, age + restore)
            hunger = max(0, hunger)
            energy = max(0, energy)
            happiness = max(0, happiness)
            hygiene = max(0, hygiene)



    #-------------if game over it will ask user if it wants to keep playing
    if game_over:
        os.system('cls' if os.name == 'nt' else 'clear') #clears the terminal
        print("=" * 70)
        print("GAME OVER".center(70))
        print("=" * 70)
        pick = input("Do you want to go back to the main menu? (Y/N): ").upper()
        print("-" * 70)

        if pick == "Y":
            os.system('cls' if os.name == 'nt' else 'clear')
            gacha.gacha_system()

        else:
            print("Thank you for playing!.")
            
if __name__ == "__main__":
    pet_bird()


