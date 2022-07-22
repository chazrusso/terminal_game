import random

class Monster:
#Monster's Attributes
  def __init__(self, input_name):
    self.name = input_name
    self.level = random.randint(1,9)
    self.ac = random.randint(10,18)
    self.size = random.randint(1, 50)
    self.health = self.level * 10
    self.strength = random.randint(1,20)
    self.dexterity = random.randint(1,20)
    self.constitution = random.randint(1,20)
    self.intelligence = random.randint(1,20)
    self.wisdom = random.randint(1,20)
    self.charisma = random.randint(1,20)
    self.is_defeated = False
#Print info for monster
  def __repr__(self):
    if self.level >= 4 and self.size >= 10:
      return "You have stumbled upon a monster! It's name is {name}. It looks very powerful! It is {size} feet tall! You pee your pants a little.".format(size = self.size, name = self.name)
    elif self.level >= 4 and self.size >= 0:
      return "You have stumbled upon a monster! It's name is {name}. It looks very powerful! It is about {size} feet tall. Should be no problem!".format(size = self.size, name = self.name)
    elif self.level >= 0 and self.size >= 10:
      return "You have stumbled upon a monster! It's name is {name}. You can probably kick his ass! It is {size} feet tall! You pee your pants a little.".format(size = self.size, name = self.name)
    else:
      return "You have stumbled upon a monster! It's name is {name}. You can probably kick his ass! It is about {size} feet tall. Should be no problem!".format(size = self.size, name = self.name)
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













test_monster1 = Monster("Tim")
test_monster2 = Monster("Tam")
hero1 = Hero("Chaz")
hero2 = Hero("Kamryn")

print(test_monster1)
print(test_monster2)
print("for testing purposes, here are {name}'s stats: Lvl: {level}, AC: {ac}, Str: {strength}, Dex: {dexterity}, Con: {constitution}, Wis: {wisdom}, Int: {intelligence}, Char: {charisma}".format(name = test_monster1.name, level = test_monster1.level, ac = test_monster1.ac, strength = test_monster1.strength, dexterity = test_monster1.dexterity, constitution = test_monster1.constitution, wisdom = test_monster1.wisdom, intelligence = test_monster1.intelligence, charisma = test_monster1.charisma))
print("for testing purposes, here are {name}'s stats: Lvl: {level}, AC: {ac}, Str: {strength}, Dex: {dexterity}, Con: {constitution}, Wis: {wisdom}, Int: {intelligence}, Char: {charisma}".format(name = test_monster2.name, level = test_monster2.level, ac = test_monster2.ac, strength = test_monster2.strength, dexterity = test_monster2.dexterity, constitution = test_monster2.constitution, wisdom = test_monster2.wisdom, intelligence = test_monster2.intelligence, charisma = test_monster2.charisma))
print(hero1)
print(hero2)
print("for testing purposes, here are {name}'s stats: Lvl: {level}, AC: {ac}, Str: {strength}, Dex: {dexterity}, Con: {constitution}, Wis: {wisdom}, Int: {intelligence}, Char: {charisma}".format(name = hero1.name, level = hero1.level, ac = hero1.ac, strength = hero1.strength, dexterity = hero1.dexterity, constitution = hero1.constitution, wisdom = hero1.wisdom, intelligence = hero1.intelligence, charisma = hero1.charisma))
print("for testing purposes, here are {name}'s stats: Lvl: {level}, AC: {ac}, Str: {strength}, Dex: {dexterity}, Con: {constitution}, Wis: {wisdom}, Int: {intelligence}, Char: {charisma}".format(name = hero2.name, level = hero2.level, ac = hero2.ac, strength = hero2.strength, dexterity = hero2.dexterity, constitution = hero2.constitution, wisdom = hero2.wisdom, intelligence = hero2.intelligence, charisma = hero2.charisma))