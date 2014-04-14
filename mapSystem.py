import curses
import pickle
import random
from enemyGoblin import *

class tile:
	def __init__(self, walk, icon, door):
		self.walk = walk
		self.icon = icon
		self.door = door

class room:
	def __init__(self, openings, screen, SYX, Id, dungeon, menu):
		empty = tile('FALSE', ' ', 'FALSE')
		wall = tile('FALSE', ' ', 'FALSE')
		floor = tile('TRUE', '.', 'FALSE')
		door = tile('TRUE', 'O', 'TRUE')
		chest = tile('FALSE', 'C', 'FALSE')
		self.length = random.randint(10, 22)
		self.height = random.randint(7, 10)
		self.wallL = self.length + 2
		self.wallH = self.height + 2
		self.screen = screen
		self.SYX = SYX
		self.floor = floor.icon * self.length
		self.wall = wall.icon * self.wallL
		self.Id = Id

		###########################################
		#                                         #
		#  This will set the origin of the left   #
		#  side of the room. IMPORTANT            #
		#                                         #
		###########################################
		self.drawHeight = self.SYX[0] - self.SYX[0]/3
		self.drawWidth = self.SYX[1] - self.SYX[1]/3
		self.leftOrigin = (self.drawWidth/2) - (self.wallL/2)
		self.topHeight = (self.drawHeight/2) - (self.wallH/2)
		if Id == 0:
			pass
		self.leftRoomX = self.leftOrigin
		self.leftRoomY = random.randint(self.topHeight + 1, self.topHeight + self.height)
		self.leftRoom = (self.leftRoomX, self.leftRoomY, door)
		self.rightRoomX = self.leftOrigin + self.length + 1
		self.rightRoomY = random.randint(self.topHeight + 1, self.topHeight + self.height)
		self.rightRoom = (self.rightRoomX, self.rightRoomY, door)

		# ENEMIES IN ROOM
		self.enemies = []
		enemiesNum = random.randint(1, 5)
		x = 0
		while x <= enemiesNum:
			enemy = goblin(self.screen, self.leftOrigin, self.topHeight, self.height, self.length, self, dungeon, x, menu)
			self.enemies.append(enemy)
			x += 1

	def drawRoom(self):
		x = 0
		while self.wallH >= x:
			curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)
			self.screen.addstr(self.topHeight + x, self.leftOrigin, self.wall, curses.color_pair(1))
			x += 1

		y = 0
		while (self.height) >= y:
			self.screen.addstr(self.topHeight + 1 + y, self.leftOrigin + 1, self.floor)
			y += 1

		if self.Id == 0:
			pass
		else:
			self.screen.addstr(self.leftRoom[1], self.leftRoom[0], self.leftRoom[2].icon)
		self.screen.addstr(self.rightRoom[1], self.rightRoom[0], self.rightRoom[2].icon)


class dungeon:
	def __init__(self, screen, SYX, menu):
		self.screen = screen
		self.SYX = SYX
		self.id = 0
		Room = room(2, self.screen, self.SYX, self.id, self, menu)
		self.rooms = []
		self.rooms.append(Room)
		self.menu = menu
	def draw(self):
		self.rooms[0+self.id].drawRoom()
		for enemy in self.rooms[0+self.id].enemies:
			enemy.draw()
	def update(self, player):
		for enemy in self.rooms[0+self.id].enemies:
			enemy.update(player)
	def right(self):
		self.id += 1
		try:
			self.rooms[0+self.id].drawRoom()
			new = 'FALSE'
		except:
			self.rooms.append(room(2, self.screen, self.SYX, self.id, self, self.menu))
			self.rooms[0+self.id].drawRoom()
			new = 'TRUE'
		x = self.rooms[0 + self.id].leftRoom[0] + 1
		y = self.rooms[0 + self.id].leftRoom[1]
		return x, y, new

	def left(self):
		self.id -= 1
		self.rooms[0+self.id].drawRoom()
		x = self.rooms[0 + self.id].rightRoom[0] - 1
		y = self.rooms[0 + self.id].rightRoom[1]
		return x, y