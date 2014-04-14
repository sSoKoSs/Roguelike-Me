import curses
import pickle
import random

class player:
	# self.screen, self.leftOrigin, self.topHeight, self.height, self.length
	def __init__(self, screen, originX, originY, width, height, menu, dungeon):
		self.HP = 20
		self.maxHP = 20
		self.XP = 0
		self.lvlup = 10
		self.lvl = 1
		self.screen = screen
		self.x = (originX + width) - (width / 2)
		self.y = (originY + height) - (height / 2)
		self.inv = []
		self.maxPickup = 50
		# currentWeight = 0
		# For item in inv:
		#     current weight += item.weight
		# if currentWeight <= self.maxPickup + itemPickup:
		#     inv.append(itemPickup)
		#     self.menu.toast('Player picked up ' + item.name + '.')
		# else:
		#     self.menu.toast('Cannot pickup ' + item.name + ' because you are carrying too much.')
		self.menu = menu
		self.dungeon = dungeon

		# Armor:
		# Chest plate
		self.chestPlate = 'NULL'
		# Pants
		self.pants = 'NULL'
		# Gloves
		self.gloves = 'NULL'
		# Feet
		self.shoes = 'NULL'
		# helmet
		self.helmet = 'NULL'

		#Weapons
		# Left hand
		self.leftHand = 'NULL'
		# Right hand
		self.rightHand = 'NULL'

	def attack(self, enemy, Num, room):
		try:
			rightDMG = self.rightHand.dmg()
		except:
			rightDMG = 0
		try:
			leftDMG = self.leftHand.dmg()
		except:
			leftDMG = 0
		self.attackDMG = self.lvl + rightDMG + leftDMG
		attack = random.randint(0, self.attackDMG)
		enemy.HP -= attack
		enemy.attacked = 1
		enemy.attack(self)
		self.menu.toast('Player attacked ' + enemy.name + ' for ' + str(attack) + ' damage.')
		if enemy.HP < 1:
			self.menu.toast('Player defeated ' + enemy.name + ' and recieved: ' + str(enemy.XP) + ' XP!')
			self.XP += enemy.XP
			pause = enemy.id
			self.dungeon.rooms[self.dungeon.id + 0].enemies.pop(enemy.id)
			for enemy1 in room.enemies:
				if enemy1.id > pause:
					enemy1.id -= 1
				else:
					pass
			# Check to see if drop is true (A 1:5 chance of dropping loot)
			drop = random.randint(1,5)
			if drop == 1:
				pass

	def walk(self, room, Dir, dungeon):
		if Dir == ord('w'):
			move = 1
			enemyN = -1
			for enemy in room.enemies:
				if enemy.x == self.x and enemy.y == self.y - 1 and move > 0:
					enemyN += 1
					self.attack(enemy, enemyN, room)
					move -= 1
				else:
					pass
			if self.y > room.topHeight + 1 and move > 0:
				self.y -= 1
				move -= 1
			else:
				pass

		elif Dir == ord('s'):
			move = 1
			enemyN = -1
			for enemy in room.enemies:
				if enemy.x == self.x and enemy.y == self.y + 1 and move > 0:
					enemyN += 1
					self.attack(enemy, enemyN, room)
					move -= 1
				else:
					pass
			if self.y < room.topHeight + room.height + 1 and move > 0:
				self.y += 1
				move -= 1
			else:
				pass
			move = 1

		elif Dir == ord('a'):
			move = 1
			enemyN = -1
			for enemy in room.enemies:
				if enemy.y == self.y and enemy.x == self.x - 1 and move > 0:
					enemyN += 1
					self.attack(enemy, enemyN, room)
					move -= 1
				else:
					pass
			if self.x > room.leftOrigin + 1 and move > 0:
				self.x -= 1
				move -= 1
			elif room.Id != 0 and Dir == ord('a') and self.x - 1 == room.leftRoom[0] and self.y == room.leftRoom[1]:
				self.x, self.y = dungeon.left()
			else:
				pass
			move = 1
		elif Dir == ord('d'):
			move = 1
			enemyN = -1
			for enemy in room.enemies:
				if enemy.y == self.y and enemy.x == self.x + 1 and move > 0:
					enemyN += 1
					self.attack(enemy, enemyN, room)
					move -= 1
				else:
					pass
			if self.x < room.leftOrigin + room.length and move > 0:
				self.x += 1
				move -= 1
			elif Dir == ord('d') and self.x + 1 == room.rightRoom[0] and self.y == room.rightRoom[1]:
				self.x, self.y, new = dungeon.right()
				if new == 'TRUE':
					self.XP += 3
					self.menu.toast('You delve deeper into the dungeon.')
				else:
					pass
			move = 1
		else:
			pass

	def draw(self):
		curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
		self.screen.addstr(self.y, self.x, 'P', curses.color_pair(3))

	def update(self):
		if self.lvlup <= self.XP:
			self.lvlup += 5 * self.lvl
			self.lvl += 1
			self.maxHP += 5 * self.lvl
			self.XP = 0
			self.HP = self.maxHP
			self.menu.toast('You are now level: ' + str(self.lvl))