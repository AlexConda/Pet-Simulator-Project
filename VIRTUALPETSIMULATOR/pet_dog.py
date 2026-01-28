from inputimeout import inputimeout, TimeoutOccurred
import numpy as np
import time
import random
import sys
import matplotlib.pyplot as plt
import os
import PetReactions as anim
import Gacha as gacha

#main coder Zeus Albiso
#edited by Alex Conda

def pet_dog():
    #print(f"Importing pet_cat.py, __name__ = {__name__}") #just for testing
    #matplotlib history
    hunger_history = []
    energy_history = []
    happiness_history = []
    hygiene_history = []
    age_history = []

    MAX_STAT = 100

    #animation to let user know stats are draining
    def no_actionTaken():
        anim.dog_neutral()
        for i in range(3):
            print("Draining" + "." * (i + 1), end="\r", flush=True)
            time.sleep(1)
        print(" " * 20, end="\r")

    #game over screen
    def GAMEOVER_SCREEN():
        time.sleep(2)
        plt.plot(hunger_history, label="Hunger")
        plt.plot(energy_history, label="Energy")
        plt.plot(happiness_history, label="Happiness")
        plt.plot(hygiene_history, label="Hygiene")
        plt.plot(age_history, label = "Age")

        plt.title("Pet's Stats Before Game Over")
        plt.xlabel("Turns")
        plt.ylabel("Stat Value")
        plt.legend()

        plt.show()

    #sleeping animation
    def sleeping_animation(duration=10):
        os.system('cls' if os.name == 'nt' else 'clear')
        dots = [" .  ", " .. ", " ..."]
        start = time.time()
        anim.dog_sleeping()

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

    #type out animation
    # faster type out speed
    def type_out(text, speed=0.03):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        print()

    messages_printed = False

    #INITIAL STATS
    hunger = MAX_STAT
    happiness = MAX_STAT
    hygiene = MAX_STAT
    energy = MAX_STAT
    age = 0

    total_gameplay = 30 
    warning_given = False

    game_over = False

    #PET NAME INPUT
    def get_pet_name():
        while True:
            name = input("Please enter your pet's name: ")
            if name:
                return name
            else:
                print("Pet name cannot be empty. Perhaps try Doge Melon.")

    pet_name = get_pet_name()

    time.sleep(1)

    #------------------------------------this is the stats menu---------------------------
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
            choice = inputimeout(prompt='Enter your choice: ', timeout=15).strip()
        except TimeoutOccurred:
            choice = ''     
        
        
        
        # Display signals only at the exact thresholds
        if hunger == 70:
            type_out(f"{pet_name} is a little hungry.")
            messages_printed = True
            time.sleep(1)
        if hunger == 50:
            type_out(f"{pet_name} is hungry! *cute eyes* <3")
            messages_printed = True
            time.sleep(1)
        if hunger == 30:
            print(f"{pet_name} refuses to do anything except eating!")
            messages_printed = True
            time.sleep(1)
        if hunger == 0:
            if not warning_given:
                print("\n⚠ WARNING: Your pet's hunger has reached a critical stat of 0!")
                print("You have one last chance to save your pet!\n")
                warning_given = True
            else:
                print(f"GAME OVER! Your Dog Just Died From Hunger")
                anim.dead()
                GAMEOVER_SCREEN()
                game_over = True
                break

        #warnings for energy    
        if energy == 70:
            type_out(f"{pet_name} wants to play!")
            messages_printed = True
            time.sleep(1)
        if energy == 50:
            type_out(f"{pet_name} scratches the door to go for a walk")
            messages_printed = True
            time.sleep(1)
        if energy == 30:
            type_out(f"{pet_name} lays down, too tired to play")
            messages_printed = True
            time.sleep(1)
        if energy == 0:
            if not warning_given:
                print("\n⚠ WARNING: Your pet's energy has reached a critical stat of 0!")
                print("You have one last chance to save your pet!\n")
                warning_given = True
            else:
                print(f"GAME OVER! {pet_name} is unresponsive and rushed to the vet")
                anim.dead()
                GAMEOVER_SCREEN()
                game_over = True
                break

        if age >= total_gameplay:
            if not warning_given:
                print("\n⚠ WARNING: Your pet is dying of old age!")
                type_out("Say your goodbyes...\n")
                messages_printed = True
                warning_given = True   

            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                anim.dead()
                print(f"{pet_name} died of old age :(")
                GAMEOVER_SCREEN()
                game_over = True
                break

        #warnings for fun
        if happiness == 70:
            type_out(f"{pet_name} jumps around happily!")
            messages_printed = True
            time.sleep(1)
        if happiness == 50:
            type_out(f"{pet_name} shows cute eyes")
            messages_printed = True
            time.sleep(1)
        if happiness == 30:
            type_out(f"{pet_name} looks sad and doesn't want to play")
            messages_printed = True
            time.sleep(1)
        if happiness == 0:
            if not warning_given:
                print("\n⚠ WARNING: Your pet's happiness has reached a critical stat of 0!")
                print("You have one last chance to save your pet!\n")
                warning_given = True
                break

            else:
                print(f"GAME OVER! {pet_name} refuses to play anymore")
                GAMEOVER_SCREEN()
                game_over = True
                break

        #warnings for hygiene
        if hygiene == 70:
            type_out(f"{pet_name} licks your feet")
            messages_printed = True
            time.sleep(1)
        if hygiene == 50:
            type_out(f"{pet_name} messes with the food")
            messages_printed = True
            time.sleep(1)
        if hygiene == 30:
            type_out(f"{pet_name} runs over the carpet with dirty feet")
            messages_printed = True
            time.sleep(1)
        if hygiene == 0:
            if not warning_given:
                print("\n⚠ WARNING: Your pet's hygiene has reached a critical stat of 0!")
                print("You have one last chance to save your pet!\n")
                warning_given = True
            
            else:
                print(f"GAME OVER! {pet_name} pooped on your PS5")
                anim.dog_turd()
                GAMEOVER_SCREEN()
                game_over = True
                break





        #---------------this is for the user actions--------------------------------
        if choice == '1': #hunger
            if hunger == MAX_STAT:
                    print(f"{pet_name} is already full!")
            
            else:
                restore = np.random.normal(loc=10, scale=1) #mean 8 with standard deviation of 2
                restore = max(1, int(restore))
                hunger = min(MAX_STAT, hunger + restore)
                print(f"You fed your pet! Hunger restored by {restore}.")
                anim.dog_eating()
                time.sleep(2)

        elif choice == '2': #sleep
            if energy == MAX_STAT:
                print(f"{pet_name} doesn't feel sleepy.")

            else:
                restore = np.random.normal(loc=35, scale=2)
                restore = max(1, int(restore))
                energy = min(MAX_STAT, energy + restore) #no trade-offs
                anim.dog_sleeping()
                sleeping_animation(duration=10)
                

                print(f"Your pet rested! Energy restored by {restore}.")

        elif choice == '3': #for happiness
            if hunger <= 30:
                print(f"{pet_name} refuses to play. Feed first!")
                time.sleep(1)
                continue

            if happiness == MAX_STAT:
                print(f"{pet_name} doesn't want to play.")

            else:
                restore = np.random.normal(loc=10, scale=2)
                restore = max(1, int(restore))
                happiness = min(MAX_STAT, happiness + restore)
                drain_hunger = np.random.normal(loc=[5], scale=[1]).astype(int)
                drain_energy = np.random.normal(loc=[5], scale=[1]).astype(int)
                hunger -= drain_hunger[0]
                energy -= drain_energy[0]
                anim.dog_playing()
                print(f"You played with your pet! Happiness restored by {restore}.")
                time.sleep(2)
                print(f"-{drain_hunger} hunger")
                print(f"-{drain_energy} energy")    

        elif choice == '4': #hygiene
            if hygiene == MAX_STAT:
                print(f"{pet_name} is already clean!")

            else:
                restore = np.random.normal(loc=10, scale=1)
                restore = max(1, int(restore))
                hygiene = min(MAX_STAT, hygiene + restore)
                drain = np.random.normal(loc=[5], scale=[1]).astype(int)
                happiness -= drain[0]
                print(f"You gave your pet a bath! hygiene restored by {restore}.")
                anim.dog_bathing()
                time.sleep(2)
                print(f"He didn't like it. -{drain} happiness")
                    



        elif choice == '':
            print("\nNo action taken.")
            time.sleep(1)
            

        else: #if user inputs invalid action it would take it as no action taken
            print("\nInvalid input, no action taken.")
            time.sleep(1)
        
        #-----------this is for the matplotlib----------------------------    
        hunger_history.append(hunger)
        energy_history.append(energy)
        happiness_history.append(happiness)
        hygiene_history.append(hygiene)
        age_history.append(age)

        no_actionTaken()
        time.sleep(1)
        
        if not game_over:   
            drain = np.random.normal(loc=[5, 5, 5, 5], scale=[1, 1, 1, 1])
            drain = np.maximum(drain, [1, 1, 1, 1]).astype(int)

        #indexing lng to guyz
            hunger -= drain[0]
            energy -= drain[1]
            happiness -= drain[2]
            hygiene -= drain[3]
        
        
        #you can change the chance to age just edit the following line
        if random.random() < 0.6:  # 60% chance to age
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
    pet_dog()