import time
import os

def capybara_anim():
    capybara_frames = [
r"""
   (\_______/)
   (    • 3 •)
   /   >  >  \
  / |=====   |\
 (__|________|_)
""",
r"""
   (\_____/)
   ( • 3 • )
   /  <  < \
  / |=====| \
 (__|_____|__)
""",
r"""
   (\_____/)
   (• 3 •  )
   /<   <  \
  / |====|  \
 (__|____|___)
"""
    ]

    # Run animation for 3 seconds (about 15 loops)
    for _ in range(3):
      for f in capybara_frames:
          os.system("cls" if os.name == "nt" else "clear")
          print(f)
          time.sleep(0.3)

            
def cat_anim():
    
    cat_frames = [
r"""
 /\_/\ 
( o.o )
 > ^ <
""",
r"""
 /\_/\ 
( -.- )
 > ^ <
""",
r"""
 /\_/\ 
( o.o )
 > ^ <
""",
r"""
 /\_/\ 
( o.o )
  ^ ^ 
"""
]
    for _ in range(3):
      for f in cat_frames:
          os.system("cls" if os.name == "nt" else "clear")
          print(f)
          time.sleep(0.3)

def dog_anim():
    dog_frames = [
r"""
    ႔ ႔
  ᠸᵕ ᵕ 𐅠
""",
r"""
    ႔  ႔
  ᠸᵕ ᵕ   𐅠
""",
r"""
     ႔ ႔
   ᠸᵕ ᵕ 𐅠
""",
r"""
    ႔   ႔
  ᠸᵕ ᵕ    𐅠
"""
    ]

    for _ in range(3):
      for f in dog_frames:
          os.system("cls" if os.name == "nt" else "clear")
          print(f)
          time.sleep(0.3)

            
            
def bluejay_anim():
    bluejay_frames = [
r"""
     ႔>
   (ᵕᴗᵕ )
  /(   )>
   "" ""
""",
r"""
     ႔>
   (ᵕᴗᵕ )/
  /(   ) 
   "" ""
""",
r"""
     ႔> ~
   (ᵕᴗᵕ )
  /(   )>
   "" ""
""",
r"""
     ႔>
  \(ᵕᴗᵕ )
   (   )>
   "" ""
"""
]
    for _ in range(3):

      for f in bluejay_frames:
          os.system("cls" if os.name == "nt" else "clear")
          print(f)
          time.sleep(0.3)