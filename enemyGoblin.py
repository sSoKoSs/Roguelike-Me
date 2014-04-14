import random
import curses

class goblin():
	def __init__(self, screen, originX, originY, height, width, room, dungeon, x, menu):
		self.name = 'Goblin'
		self.id = x
		self.lvl = random.randint(1, dungeon.id+2)
		self.dmg = self.lvl
		self.HP = self.lvl * 3
		self.icon = 'G'
		self.screen = screen
		self.x = random.randint(originX + 1, originX + width - 1)
		self.y = random.randint(originY + 1, originY + height - 1)
		self.room = room
		self.minY = self.room.topHeight + 1
		self.maxY = self.room.topHeight + self.room.height + 1
		self.minX = self.room.leftOrigin + 1
		self.maxX = self.room.leftOrigin + self.room.length
		self.move = 'TRUE'
		self.XP = self.lvl * 4
		self.attacked = 0
		self.menu = menu

	def draw(self):
		curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
		self.screen.addstr(self.y, self.x, self.icon, curses.color_pair(2))

	def attack(self, player):
		attack = random.randint(0, self.dmg)
		player.HP -= attack
		self.menu.toast(self.name + ' attacked player for ' + str(attack) + ' damage.')
	def update(self, player):
		if self.attacked == 0:
			TRY = random.randint(0,4)
		else:
			TRY = 0
		if TRY == 0:
			pass
		elif TRY == 1 and self.x < self.maxX and self.attacked < 1:
			self.x += 1
		elif TRY == 2 and self.x > self.minX and self.attacked < 1:
			self.x -= 1
		elif TRY == 3 and self.y < self.maxY and self.attacked < 1:
			self.y += 1
		elif TRY == 4 and self.y > self.minY and self.attacked < 1:
			self.y -= 1
		elif self.attacked > 0 and player.x + 1 == self.x and player.y == self.y or self.attacked > 0 and player.x - 1 == self.x and player.y == self.y or self.attacked > 0 and player.x == self.x and player.y + 1 == self.y or self.attacked > 0 and player.x == self.x and player.y - 1 == self.y:
			self.attack(player)
