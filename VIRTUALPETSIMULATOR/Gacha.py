import random
import time
import pandas as pd
import PetAnim as Panim
import os

def gacha_system():
    def menu():
        os.system("cls" if os.name == "nt" else "clear")
        print(" ⋆ Main Menu ⋆  ".center(114, "="))
        print("₊✩‧₊˚  ౨  ৎ  ˚  ₊✩‧₊   ₊✩‧₊˚  ౨  ৎ  ˚  ₊✩‧₊                 ₊✩‧₊˚  ౨  ৎ  ˚  ₊✩‧₊   ₊✩‧₊˚  ౨  ৎ  ˚  ₊✩‧₊".center(114))
        print("-"*114)
        print("        |___/,|   (`)                 (\\_____/ )                     ႔  ႔                        ႔> ~              ")
        print("      _.|o o  |_   ) )                 ( • 3 • )                    ᠸᵕ ᵕ   𐅠                   (ᵕᴗᵕ )                ")
        print("--------(((---(((----------------------/  <  < \\-----------------------------------------------/(   )>------------")
        
    def load_unlocks():
        try:
            return pd.read_csv("pet_unlocks.csv")
        except FileNotFoundError:
            # No file yet → create default set with consistent capitalization
            return pd.DataFrame([
                    {"pet_type": "cat", "unlocked": False},
                    {"pet_type": "dog", "unlocked": False},
                    {"pet_type": "bird", "unlocked": False},
                    {"pet_type": "capybara", "unlocked": False},
                ])

    def save_unlocks(df):
        df.to_csv("pet_unlocks.csv", index=False)

    def gacha_pull(pets_df):
        pet = random.choice(pets_df["pet_type"].tolist())
        already = pets_df.loc[pets_df["pet_type"] == pet, "unlocked"].values[0]

        if not already:
            pets_df.loc[pets_df["pet_type"] == pet, "unlocked"] = True
            save_unlocks(pets_df)
            print(f"🎉 NEW PET UNLOCKED: {pet}!")
        else:
            print(f"{pet} (already unlocked)")

        return pet

    def pets_locked(pets_df):
        while True:
            choice = input("Pull gacha? (y/n): ").lower()
            if choice == "y":
                print()
                for i in range(3):
                    print("Rolling" + "." * (i + 1), end="\r", flush=True)
                    time.sleep(0.5)
                print(" " * 20, end="\r")
                gacha_pull(pets_df)
            elif choice == "n":
                break
            else:
                print("Please type y/n only!")

    def choose_pet(pets_df):
        unlocked = pets_df[pets_df["unlocked"] == True]

        if unlocked.empty:
            return None

        print("\nChoose a pet to play:")
        unlocked = unlocked.reset_index(drop=True)

        for i, row in unlocked.iterrows():
            print(f"{i + 1}. {row['pet_type']}")
        print("randomized (r)")

        while True:

            choice = input("Enter the number of the pet you want: ")

            if choice.isdigit():    #checks if the input is a digit
                idx = int(choice) - 1   #converts the choice into an integer and subtracts one as the menu showed is different from what the index number actually is
                if 0 <= idx < len(unlocked):    #checks if it is a valid index and ensures it is not negative
                    pet_name = unlocked.iloc[idx]["pet_type"] #gers the row at idx
                    print(f"You chose: {pet_name}")
                    return pet_name
                
            elif choice.lower() == 'r':
                pet_name = random.choice(unlocked["pet_type"].tolist())
                print(f"Randomly selected pet: {pet_name}")
                return pet_name
                
            else:    
                print("Invalid choice, try again.")

    def main():
        pets = load_unlocks()

        while True:
            menu()
            print("\n1. Pull Gacha (try to unlock a new pet)")
            print("2. Choose Pet to Play")
            print("3. Quit")

            choice = input("\nEnter choice (1-3): ").lower()

            if choice == "1":
                pets_locked(pets)  # This lets user pull gacha once or multiple times
            elif choice == "2":
                chosen_pet = choose_pet(pets)
                if chosen_pet == 'cat':
                    import pet_cat as PC
                    Panim.cat_anim()
                    time.sleep(1)
                    PC.pet_cat()   # pet cat gameplay here
                   
                elif chosen_pet == 'dog':
                    import pet_dog as PD
                    Panim.dog_anim()
                    time.sleep(1)
                    PD.pet_dog() 
                
                elif chosen_pet == 'capybara':
                    import pet_capybara as PCAP
                    Panim.capybara_anim()
                    time.sleep(1)
                    PCAP.pet_capybara()

                elif chosen_pet == 'bird':
                    import pet_bird as PB
                    Panim.bluejay_anim()
                    time.sleep(1)
                    PB.pet_bird()
                    
                else:
                    print("\nNo pets unlocked yet. Please unlock pets from gacha first.")
            
            
            elif choice == "r": #randomly selects pet for user
                unlocked = pets[pets["unlocked"] == True]
                if unlocked.empty:
                    print("\nNo pets unlocked yet! Play gacha to unlock pets first.")
                else:
                    pet_name = random.choice(unlocked["pet_type"].tolist())
                    print(f"Randomly selected pet: {pet_name}")

                    if pet_name == 'cat':
                        import pet_cat as PC
                        Panim.cat_anim()
                        time.sleep(1)
                        PC.pet_cat()

                    elif pet_name == 'dog':
                        import pet_dog as PD
                        Panim.dog_anim()
                        time.sleep(1)
                        PD.pet_dog()

                    elif pet_name == 'capybara':
                        import pet_capybara as PCAP
                        Panim.capybara_anim()
                        time.sleep(1)
                        PCAP.pet_capybara()

                    elif pet_name == 'bird':
                        import pet_bird as PB
                        Panim.bluejay_anim()
                        time.sleep(1)
                        PB.pet_bird()
                            
            elif choice == "3":
                print("Thanks for playing! Goodbye.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")


    main()


if __name__ == "__main__":
    gacha_system()
