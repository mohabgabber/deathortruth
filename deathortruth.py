'''
    Death Or Truth. A Simple CLI Python Game
    Copyright (C) 2022  Mohab Gabber

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import playsound
print('''Death Or Truth  Copyright (C) 2022  Mohab Gabber
       This program comes with ABSOLUTELY NO WARRANTY.
       This is free software, and you are welcome to redistribute it
       under certain conditions; Read The LICENSE file for details.''')
Hello = print("Hello Buddy This Is The Death Or Truth Game, Play At Your Own risk\n")
age = int(input("\nWhat`s Your Age? "))
if age >= 18:
  music = str(input("would you perhaps like, some background music (ok/no)? "))
  if music == 'ok':
    playsound.playsound('sound.mp3', False)
    print('\nwell, here you go, Don\'t Enjoy The Game')
  else:
    print("\nwell, doesn't matter, I'm Not Offended At All")
  print("\nHere`s The Instructions: \n1-Play At Your Own Risk \n2-If You Lose You`ll Be Cursed\n3-If You Live you`ll Wish you were Dead \n4-It Doesn`t Matter\n")
  out_search = input("\nnow let`s begin.. you are In A House, An Empty One, will you Search The Building Or Get Out (Search/Get Out)? ").lower()
  if out_search == "search":
    print("\nYou Searched The House And Found Nothing.. But You Heard A Voice Upstairs!\n")
    up_ignore = input("\nShould You Go Upstairs Or Ignore The Voice (Upstairs/ignore)? ").lower()
    if up_ignore == "upstairs":
      print("\nno one was here, but you found a knife and Shotgun\n")
      knife_shotgun = input("\nWhich One Do You Pick (knife/Shotgun)? ").lower()
      if knife_shotgun == "knife":
        print("\nyou took the knife. now you went down stairs but the stairs wood was broken and you fell down to a basement and you found matches and cigerattes\n")
  elif out_search == 'get out':
    print("\nYou Went Out, And Found An Executioner, You Can't Escape Him!\n")
    death_beheading = input("\nYou Better Just Die (beheading/hanging)? ").lower()
    if death_beheading == 'beheading' or death_beheading == 'hanging':
      print("\nYou Died, Yup, It's Hard. You're Just A Body Now\n")
else:
    print("Go The Fuck Away")
