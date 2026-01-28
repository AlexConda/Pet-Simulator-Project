import time
import Gacha as GA
import sys


#please run this
def type_out(text, speed=.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()
        

print("="*114)
print("⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘".ljust(30), "ฅ^._.^ฅ = WELCOME TO OUR PET SIMULATOR = ૮₍ • ᴥ • ₎ა".center(25), "⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘⚘".rjust(30))
print("="*114,"")
print("⋆.˚☁️⋆"*22)
print("=    "*22)
print("\n")

type_out(" In this game, you’ll take care of your very own virtual pets, each with their own personality and needs! ".center(114))
time.sleep(1)
type_out(" Feed them, play with them, keep them happy, and watch them grow over time. Your choices shape their lives. ".center(114))
time.sleep(1)
type_out(" so be sure to give them all the love and attention they deserve! ".center(114))
time.sleep(2)
print()
type_out(" Ready to meet your new companions? ".center(114))
print("\n")

time.sleep(1)

for i in range(3):
    loading = "Loading" + "." * (i + 1)
    print(loading.center(117), end="\r", flush=True)
    time.sleep(0.5)
    print(" " * 20, end="\r")


while True:
    GA.gacha_system()