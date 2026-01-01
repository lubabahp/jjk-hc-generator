# jjk hc generator.py

import random

jjk_boys = [
  "gojo",
  "yuji",
  "megumi",  
  "nanami",
  "toji",
  "inumaki"]

jjk_girls = [
  "nobara",
  "maki",
  "miwa",
  "utahime"
]  

fave_women = []

fave_men = []


characters = jjk_boys + jjk_girls  # okk we learn how to merge core


def menu():
  print("""
  welcome to the crappy jjk characters hc generator! u can pick your poison:
  1. choose fave JJK men
  2. choose fave JJK women
  3. make hcs about ur chosen men/women
  4. make hcs about totally random characters
  5. i wanna quit wth is this
  """)





def men():
  fave_man = input("choose a jjk man lol: ")

  if fave_man in jjk_boys:
    fave_men.append(fave_man)
    return
  else:
    print("bro that's not a jjk dude (or creator of this script is stupid)")

  return  

def women():
  fave_woman = input("choose a jjk girlie hehe: ")

  if fave_woman in jjk_girls:
    fave_women.append(fave_woman)
    return
  else:
    print("that's not a jjk girlie wth (or creator of this script is tweaking)")

  return

def character_hc():
  pass  

def random_hc():
  # char1 = random.choice(characters)
  # char2 = random.choice(characters)

  # if char1 == char2:  # was tryna do the thing where so that both char1 nd 2 dont end up the same but yh

  char1, char2 = random.sample(characters, 2)   # much cleaner now, won't repeat
   

  hcs = [
    f"{char1} and {char2} are in love",
    f"{char1} hates {char2} lol",
    f"{char1} loves to feed {char2} chocolate",
    f"{char1} is a menace to {char2}",
    f"{char1} and {char2} have secretly french kissed"
  ]

  hc = random.choice(hcs)

  print(hc)


def quit_program():    # DO NOT DO "QUIT()" THAT IS CURSED CAUSE ITS A BULT IN
  print("oki byee")


def main():
  menu()
  user_choice = input()

  if user_choice == "1":
    men()
  elif user_choice == "2":
    women()
  # elif user_choice == "3":
    # chosen one icba now
  elif user_choice == "4":
    random_hc()
  elif user_choice == "5":  
    quit_program()  
  else:
    print("invalid choice")  


main()

# variables in fucntions die after the function
