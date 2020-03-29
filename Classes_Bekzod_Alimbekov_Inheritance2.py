class Spell:
  def __init__(self, incantation, name):
    self.name = name
    self.incantation = incantation

  def __str__(self):
    return self.name + ' ' + self.incantation + '\n' + self.get_description()

  def get_description(self):
    return 'No description'

  def execute(self):
    print(self.incantation)

class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
    def get_description(self):
        return "This charm summons an object to the caster, potentially over a significant distance"


class Confundo(Spell):
  def __init__(self):
    Spell.__init__(self, 'Confundo', 'Confundus Charm')

  def get_description(self):
    return 'Causes the victim to become confused and befuddled.'

def study_spell(spell):
  print(spell)

spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())
print(Accio())

#1. What are the parent and child classes here?
""" Spell is Parent Class.
Accio is Child Class
Confundo is Child Class """
#2. What are the base and sub-classes?
""" Spell is a Base Class and Accio, Confundo are Sub-Classes """
#3. What is the output from this code?   Try without running if you can
""" spell = Accio() <- Initializes Accio class into an object called "Spell"
spell.execute() <- calls Execute method which is a method of a parent class called Spell
study_spell(spell) <- shows the __str__ of an object
study_spell(Confundo()) <- shows the __str__ of confundo spell, which will return the description of an object and a spell"""
#4. When study_spell(Confundo()) executes...what get_description method gets called and why?
""" It gets called by __str__ on a new line because it has been concatinated as a return in an __str__ method """
#5. The statement print Accio() needs to print ‘This charm summons an object to the caster, potentially over a significant distance’)? 
# Write down the code that we need to add and/or change.
""" Either we need to add to accio class:
def __str__(self):
    return "This charm summons an object to the caster, potentially over a significant distance"

or

def get_description(self):
    return "This charm summons an object to the caster, potentially over a significant distance" """