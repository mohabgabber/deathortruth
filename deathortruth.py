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
print(" Death Or Truth  Copyright (C) 2022  Mohab Gabber
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions; Read The LICENSE file for details.")
Hello = print("Hello Buddy This Is The Death Or Truth Game, Play At Your Own risk\n")
age = int(input("What`s Your Age? "))
if age >= 18:
    print("Here`s The Instructions: \n1-Play At Your Own Risk \n2-If You Lose You`ll Be Cursed\n3-If You Live you`ll Wish you were Dead \n4-It Doesn`t Matter")
    out_search = input("now let`s begin.. you Begin In A House, An Empty One, will you Search The Building Or Get Out (Search/Get Out)? ").lower()
    if out_search == "search":
      print("You Searched The House And Found Nothing.. But You Heard A Voice Upstairs!\n")
      up_ignore = input("Should You Go Upstairs Or Ignore The Voice (Upstairs/ignore)? ").lower()
      if up_ignore == "upstairs":
        print("no one was here, but you found a knife and Shotgun\n")
        knife_shotgun = input("Which One Do You Pick (knife/Shotgun)? ").lower()
        if knife_shotgun == "knife":
          print("you took the knife. now you went down stairs but the stairs wood was broken and you fell down to a basement and you found matches and cigerattes")
    elif out_search == 'get out':
      print("You Went Out, And Found An Executioner, You Can't Escape Him!\n")
      death_beheading = input("You Better Just Die (beheading/hanging)? ").lower()
      if death_beheading == 'beheading' or death_beheading == 'hanging':
        print("You Died, Yup, It's Hard. You're Just A Body Now")
else:
    print("Go The Fuck Away")
