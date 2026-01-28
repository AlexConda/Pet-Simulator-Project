from inputimeout import inputimeout, TimeoutOccurred
import os
import numpy as np
import time
import random
import sys
import matplotlib.pyplot as plt
import PetReactions as Anim
import Gacha as gacha

#main coder Alex Conda
#edited by John Carlo Samson

def pet_cat():
    #print(f"Importing pet_cat.py, __name__ = {__name__}") #just for testing
    #matplotlib history
    hunger_history = []
    energy_history = []
    happiness_history = []
    hygiene_history = []
    age_history = []



    def no_actionTaken(): #animation to let user know stats are draining
        Anim.cat_neutral()
        for i in range(3):
            print("Draining" + "." * (i + 1), end="\r", flush=True)
            time.sleep(1)
        print(" " * 20, end="\r")


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

    def sleeping_animation(duration):
        os.system('cls' if os.name == 'nt' else 'clear')
        dots = [" .  ", " .. ", " ..."]
        start = time.time()
        #Animation for no.2 choice
        Anim.cat_resting()

        while True:
            elapsed = time.time() - start
            if elapsed >= duration:
                break

            remaining = int(duration - elapsed)

            # Format time as MM:SS
            minutes = remaining // 60
            seconds = remaining % 60
            timer = f"{minutes:02d}:{seconds:02d}"
    

            for d in dots:
                if time.time() - start >= duration:
                    break

                # Print animation + timer
                sys.stdout.write(f"\rSleeping{d}  |  Time left: {timer}")
                sys.stdout.flush()
                time.sleep(0.5)

        sys.stdout.write("\rSleep finished!                  \n")

    def type_out(text, speed=0.10):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        print()
        
    messages_printed = False

    MAX_STAT = 100 #just for easy testing


    hunger = MAX_STAT
    energy = MAX_STAT
    happiness = MAX_STAT
    hygiene = MAX_STAT
    age = 0
    total_gameplay = 20

    game_over = False
    warning_given = False



    def get_pet_name():
        while True:
            name = input("Please enter your pet's name: ").strip()
            if name:
                return name
            else:
                print("Pet name cannot be empty. Please try again.")



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


    #----------------------------------------this is for critical values---------------------
        if hunger == 0 :
            if not warning_given:
                print("\n⚠ WARNING: Your pet's hunger has reached a critical stat of 0!")
                print("You have one last chance to save your pet!\n")
                warning_given = True

            else:
                print("GAME OVER! \n Your cat scratched you and ran away")
                Anim.game_over()
                GAMEOVER_SCREEN()
                game_over = True
                break
        if energy == 0:
            if not warning_given:
                print("\n⚠ WARNING: Your pet's energy has reached a critical stat of 0!")
                warning_given = True
            else:
                print("You're pet is sleeping, shhhh...\n")
                sleeping_animation(duration=120)
                restore = np.random.normal(loc=60, scale=2)
                restore = max(1, int(restore))
                energy = min(MAX_STAT, energy + restore) #no trade-offs
                print(f"Your pet rested! Energy restored by {restore}.")

        if happiness == 0:
            if not warning_given:
                print("\n⚠ WARNING: Your pet's happiness has reached a critical stat of 0!")
                print("You have one last chance to save your pet!\n")
                warning_given = True

            else:
                print("GAME OVER! \n You're cat scratched your couch")
                Anim.game_over()
                GAMEOVER_SCREEN()
                game_over = True
                break

        if hygiene == 0:
            if not warning_given:
                print("\n⚠ WARNING: Your pet's hygiene has reached a critical stat of 0!")
                print("You have one last chance to save your pet!\n")
                warning_given = True
            else:
                print("GAME OVER! \n You died from the smell of the litterbox")
                Anim.dead()
                GAMEOVER_SCREEN()
                game_over = True
                break
        if age >= total_gameplay:
            if not warning_given:
                print("\n⚠ WARNING: Your pet's has reached its max age!")
                print("You have 15 seconds to say goodbye to your pet\n")
                warning_given = True
                
            else:
                print("\nYour pet lived a happy life.")
                Anim.dead()
                GAMEOVER_SCREEN()
                game_over = True
                break
        
        try:
            choice = inputimeout(prompt='Enter your choice: ', timeout=15).strip() #time for user to react
        except TimeoutOccurred:
            choice = '' #if user has no input for 15 seconds it will automatically move on


    #this is the percent chance of when it will remind the user that the pet is hungry
        if hunger <= 50:
            if random.random() < 0.3:   # 30% chance
                type_out(f"\n{pet_name} is hungry :<")
                Anim.hungry_cat()
                messages_printed = True
                time.sleep(1)

    #this is the percent chance of when it will remind the user that the pet is bored
        if happiness <= 70:
            if random.random() < 0.3:   # 30% chance
                type_out(f"\n{pet_name} wants to play!")
                Anim.want_play()
                messages_printed = True
                time.sleep(1)
    
    #this is the percent chance of when it will remind the user that the pet is dirty
        if hygiene <= 40:
            if random.random() < 0.6: #60 percent chance of reminding user
                type_out(f"\nthe litter box is starting to stink...")
                Anim.stinky_cat()
                messages_printed = True
                time.sleep(1)



    #---------------this is for the user actions--------------------------------

        if choice == '1':  # feed

            if hunger == MAX_STAT:
                print(f"{pet_name} is already full!")

            else:
                restore = np.random.normal(loc=8, scale=2) #mean 8 with standard deviation of 2
                restore = max(1, int(restore))
                hunger = min(MAX_STAT, hunger + restore)
                print(f"You fed your pet! Hunger restored by {restore}.")
                Anim.cat_eating()
                time.sleep(2)
                drain = np.random.normal(loc=[3], scale=[1]).astype(int)
                hygiene -= drain[0]

                print(f"-{drain} hygiene")


        elif choice == '2':  # rest

            if energy == MAX_STAT:
                print(f"{pet_name} doesn't feel sleepy.")
            
            else:
                restore = np.random.normal(loc=35, scale=2)
                restore = max(1, int(restore))
                energy = min(MAX_STAT, energy + restore) #no trade-offs
                sleeping_animation(duration=30)

                print(f"Your pet rested! Energy restored by {restore}.")

        elif choice == '3':  # play

            if happiness == MAX_STAT:
                print(f"{pet_name} doesn't want to play.")

            else:
                restore = np.random.normal(loc=6, scale=2)
                restore = max(1, int(restore))
                happiness = min(MAX_STAT, happiness + restore)
                drain = np.random.normal(loc=[10], scale=[1]).astype(int)
                hunger -= drain[0]
                print(f"You played with your pet! Happiness restored by {restore}.")
                Anim.cat_playing()
                time.sleep(2)
                print(f"-{drain} hunger")
        
        elif choice == '4':  # hygiene

            if hygiene == MAX_STAT:
                print(f"{pet_name} is already clean!")

            else:
                restore = np.random.normal(loc=6, scale=2)
                restore = max(1, int(restore))
                hygiene = min(MAX_STAT, hygiene + restore)
                drain = np.random.normal(loc=[10], scale=[1]).astype(int)
                happiness -= drain[0]
                print(f"You ghave your pet a bath! hygiene restored by {restore}.")
                Anim.cat_bathing()
                time.sleep(2)
                print(f"She didn't like it. -{drain} happiness")
                Anim.cat_nolike()
                time.sleep(2)


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
        
        no_actionTaken() #this will tell the user that the stats are draining

    #wait 1 second before looping again
        time.sleep(1)


    # eto guys ung sa pag drain ung loc ay mean, ang scale ay standard deviation
        if not game_over:   
            drain = np.random.normal(loc=[5, 10, 5, 5], scale=[1, 1, 1, 1])
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
    pet_cat()