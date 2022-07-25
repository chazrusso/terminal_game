#This section holds all of our imported modules. The next section (Objects) starts on line 4
import random
from tkinter.messagebox import YES

#This section is dedicated to the creation of our objects. 
#The first object is for the dice. Available options are to be specified upon calling the class. Options include: 4, 6, 8, 10, 20
class Dice:
     def __init__(self, size):
        self.size = size
     def roll(self, size):
        self.size = size
        return random.randint(1, size)
        
#This object is for the creation of our 'monster' in the game. Stats will be randomly generated according to the monster creation rules of DnD.
class Monster:
#Monster's Attributes
  def __init__(self, input_name = 'Virus'):
    self.name = input_name
    self.level = random.randint(1,5)
    self.ac = 11 + self.level
    self.health = self.level * 10
    self.strength = 10 + Dice.roll(self, 8)
    self.dexterity = 10 + Dice.roll(self, 8)
    self.constitution = 10 + Dice.roll(self, 8)
    self.intelligence = 10 + Dice.roll(self, 8)
    self.wisdom = 10 + Dice.roll(self, 8)
    self.charisma = 10 + Dice.roll(self, 8)
    self.is_defeated = False
#Print info for monster
  def __repr__(self):
    if self.level >= 4:
      return "You have stumbled upon a virus! It looks very powerful! It is carrying a folder named 'dank-memes', and for some reason, our user's mother's maiden name! This is a powerful foe indeed. You pee your pants a little."
    elif self.level >= 0:
      return "You have stumbled upon a virus! It is carrying a folder named 'dank-memes'. This must be the one. It is just sitting there, virtually giggling at a meme from 2016. Taking this thing out should be no problem!"
    else:
      return "Something weird happened... Game dev plz help..."

#method 3
  def final_form(self):
    sadness = random.randint(2,100)
    if self.health == 0 and sadness >= 75:
      self.health += 25
#first method
  def strong_attack(self, target):
    success = random.randint(1, 25)
    damage = self.strength + random.randint(1,8)
    if success >= target.ac:
      return "{name} swings with all of it's might! The attack hits! it does {dmg} amount of damage! Ouch!".format(dmg = damage, name = self.name)
      target.health -= random.randint(7, 20)
    else:
      return "{name} swings with all of it's might! {name} misses. That would have freaking killed you! Whew.".format(name = self.name)
#second method
  def take_damage(self, amount):
    self.health -= amount
    if self.health >= 20:
      return "Dude... it looks like you didn't even scratch {name}... this might be bad".format(name = self.name)
    elif self.health >= 10:
      return "You might have a chance to end {name} soon!".format(name = self.name)
    elif self.health >= 0:
      return "{name} looks hurt! and scared... FINISH IT!".format(name = self.name)
    else:
      self.health = 0
      self.final_form()
      if self.health == 0:
        return "You.... you did it.... {name} lies dead in front of you...".format(name = self.name)
      else:
        return "No.... Not this... {name} has a final FORM???? Maybe you should have taken over the families tavern and lived a  simple life... Good luck.".format(name = self.name)
#third method


class Hero:
  def __init__(self, input_name):
    self.name = input_name
    self.level = random.randint(1,12)
    self.ac = random.randint(10, 18)
    self.health = self.level * 10
    self.strength = random.randint(1,20)
    self.dexterity = random.randint(1,20)
    self.constitution = random.randint(1,20)
    self.intelligence = random.randint(1,20)
    self.wisdom = random.randint(1,20)
    self.charisma = random.randint(1,20)
    self.is_defeated = False

  def __repr__(self):
    if self.level >= 4:
      return "Look at you, {name}. You are a freaking level {level}! I bet you are so strong and have so many tricks up your sleeve.".format(level = self.level, name = self.name)
    else:
      return "Dude. You're only a level {level}. C'mon, {name}. Why are you even adventuring? You should go back to your family's tavern and live a simple life... No? You want to adventure on? Don't say I didn't warn you...".format(level = self.level, name = self.name)

  def attack(self, target):
    success = random.randint(1, 25)
    damage = self.strength + random.randint(1,8)
    if success >= target.ac:
      return "{name} swings! The attack hits! it does {dmg} amount of damage! Ouch!".format(dmg = damage, name = self.name)
      target.health -= random.randint(7, 20)
    else:
      return "{name} swings! {name} misses. Bummer.".format(name = self.name)



test_monster1 = Monster()


print("""


Welcome, traveller, to the wonderful world of your computer terminal!

A computer terminal is a wonderful land where nothing makes sense, and there are no pictures or diagrams to help explain. I hope you can read (roll for intelligence) 

Let's cut to the chase. This computer terminal needs the help of a strong, independent woman who don't need no man. It has suffered the attacks of viruses, mountain-dew floods, and dust bunnies since it's initial boot sequence. 

We don't ask that you defeat every monster in the terminal and save us from this numerical prison that encapsulates us, we are simply overrun at the moment and could use some help with a low-level virus that is corrupting a photo album containing our main-user's meme collection. The loss of this folder could send him into a rage that would end us all. 

Can you help us?

(please type 'yes' or 'no')

""")

yono = input()
if yono == 'yes':
      print("Wonderful! What is your name, brave traveller?")
      hero_name = input()
elif yono == 'no':
      print("Don't be such a weiner. Tell me your name and get ready to fight. What is your name?")
      hero_name = input()
else: 
      print("Sorry, you must be speaking a language I do not understand. Please restart the game and try again." )
      exit()

hero1 = Hero(hero_name)

print(test_monster1)
print("for testing purposes, here are {name}'s stats: Lvl: {level}, AC: {ac}, Str: {strength}, Dex: {dexterity}, Con: {constitution}, Wis: {wisdom}, Int: {intelligence}, Char: {charisma}".format(name = test_monster1.name, level = test_monster1.level, ac = test_monster1.ac, strength = test_monster1.strength, dexterity = test_monster1.dexterity, constitution = test_monster1.constitution, wisdom = test_monster1.wisdom, intelligence = test_monster1.intelligence, charisma = test_monster1.charisma))
#print("for testing purposes, here are {name}'s stats: Lvl: {level}, AC: {ac}, Str: {strength}, Dex: {dexterity}, Con: {constitution}, Wis: {wisdom}, Int: {intelligence}, Char: {charisma}".format(name = test_monster2.name, level = test_monster2.level, ac = test_monster2.ac, strength = test_monster2.strength, dexterity = test_monster2.dexterity, constitution = test_monster2.constitution, wisdom = test_monster2.wisdom, intelligence = test_monster2.intelligence, charisma = test_monster2.charisma))
#print(hero1)
#print("for testing purposes, here are {name}'s stats: Lvl: {level}, AC: {ac}, Str: {strength}, Dex: {dexterity}, Con: {constitution}, Wis: {wisdom}, Int: {intelligence}, Char: {charisma}".format(name = hero1.name, level = hero1.level, ac = hero1.ac, strength = hero1.strength, dexterity = hero1.dexterity, constitution = hero1.constitution, wisdom = hero1.wisdom, intelligence = hero1.intelligence, charisma = hero1.charisma))