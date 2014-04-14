import random

#dmgAdd, minlvl, durability
State = {'Perfect':[30, 20, 300, 'Perfect'], 'Good':[20, 15, 150, 'Good'], 'Average':[10, 8, 75, 'Average'], 'Bad':[0, 3, 50, 'Bad'], 'Terrible':[-1, 1, 20, 'Terrible']}
Type = {'wooden':[0, 0, 25, 'wooden'], 'stone':[4, 3, 50, 'stone'], 'iron':[8, 5, 125, 'iron'], 'bronze':[12, 8, 150, 'bronze'], 'gold':[16, 12, 30, 'gold'], 'platinum':[20, 15, 200, 'platinum']}
Sharpness = {'dull':[0, 0, 25, 'dull'], 'blunt':[3, 2, 50, 'blunt'], 'jagged':[6, 4, 30, 'jagged'], 'sharp':[9, 8, 100, 'sharp'], 'razor':[12, 12, 75, 'razor']}

class sharpType:
	def __init__(self, num1, num2, num3):
		if num1 < 2:
			StateI = State['Perfect']
		elif num1 < 20:
			StateI = State['Good']
		elif num1 < 40:
			StateI = State['Average']
		elif num1 < 65:
			StateI = State['Bad']
		else:
			StateI = State['Terrible']

		if num2 < 2:
			StateII = Type['platinum']
		elif num2 < 15:
			StateII = Type['gold']
		elif num2 < 30:
			StateII = Type['bronze']
		elif num2 < 55:
			StateII = Type['iron']
		elif num2 < 75:
			StateII = Type['stone']
		else:
			StateII = State['wooden']

		if num3 < 2:
			StateIII = Sharpness['razor']
		elif num3 < 20:
			StateIII = Sharpness['sharp']
		elif num3 < 40:
			StateIII = Sharpness['jagged']
		elif num3 < 65:
			StateIII = Sharpness['blunt']
		else:
			StateIII = Sharpness['dull']

		self.State = StateI
		self.Type = StateII
		self.Sharpness = StateIII

		self.durability = self.State[2] + self.Type[2] + self.Sharpness[2]
		self.minlvl = self.State[1] + self.Type[1] + self.Sharpness[1]
		self.dmg = self.State[0] + self.Type[0] + self.Sharpness[0]

class sword(sharpType):
	def start(self):
		self.name = self.State[3] + ' ' + self.Sharpness[3] + ' ' + self.Type[3] + ' sword'
		self.dmg += 3
		self.minlvl += 2

class dagger(sharpType):
	def start(self):
		self.name = self.State[3] + ' ' + self.Sharpness[3] + ' ' + self.Type[3] + ' dagger'
		self.dmg += 1

class axe(sharpType):
	def start(self):
		self.name = self.State[3] + ' ' + self.Sharpness[3] + ' ' + self.Type[3] + ' axe'
		self.dmg += 6
		self.minlvl += 4

