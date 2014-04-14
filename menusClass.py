import pickle
import curses
from mapSystem import *

class command:
	def __init__(self, x, y, screen, SYX):
		self.screen = screen
		self.SYX = SYX

class menus:
	def __init__(self, screen, SYX):
		self.screen = screen
		self.SYX = SYX
		self.line7 = ''
		self.line6 = ''
		self.line5 = ''
		self.line4 = ''
		self.line3 = ''
		self.line2 = ''
		self.line1 = ''

	def mainMenu (self):
		self.screen.clear()
		self.screen.addstr(self.SYX[0]/4, self.SYX[1]/2-5, "Gone Rogue")
		self.screen.addstr(self.SYX[0]/2 - 1, self.SYX[1]/2-4, "Play (p)")
		self.screen.addstr(self.SYX[0]/2, self.SYX[1]/2-4, "Help (h)")
		self.screen.addstr(self.SYX[0]/2 + 1, self.SYX[1]/2-5, "Credits (c)")
		self.screen.addstr(self.SYX[0]/2 + 2, self.SYX[1]/2-4, "Exit (e)")
		self.screen.addstr(self.SYX[0]-1, self.SYX[1]-9, 'r0b0a0d1')
		self.screen.refresh()

	def pause(self):
		self.screen.clear()
		self.screen.addstr(self.SYX[0]/4, self.SYX[1]/2-4, "Paused")
		self.screen.addstr(self.SYX[0]/2-1, self.SYX[1]/2-5, "Resume (p)")
		self.screen.addstr(self.SYX[0]/2, self.SYX[1]/2-4, "Quit (q)")
		self.screen.refresh()

	def credits(self):
		self.screen.clear()
		self.screen.addstr(0, 0, "Gone Rogue")
		self.screen.addstr(2, 0, "Produced by: A Donut with Sprinklez")
		self.screen.addstr(3, 0, "Coded by: Nichom Olasher")
		self.screen.addstr(5, 0, "Started work on: March 24, 2014")
		self.screen.addstr(self.SYX[0]-1, self.SYX[1]-21, "Press (m) to go back")
		self.screen.refresh()

	def mainGame(self):
		Map = dungeon(self.screen, self.SYX, self)
		height = self.SYX[0] - self.SYX[0]/3
		width = self.SYX[1] - self.SYX[1]/3
		self.screen.clear()
		# Set the area for GUI
		while height >= 0:
			self.screen.addstr(height, self.SYX[1] - self.SYX[1]/3, '#')
			height -= 1
		while width >= 0:
			self.screen.addstr(self.SYX[0] - self.SYX[0]/3, width, '#')
			width -= 1

		self.height = self.SYX[0] - self.SYX[0]/3
		self.width1 = self.SYX[1] - self.SYX[1]/6
		width2 = self.SYX[1] - self.SYX[1]/3

		self.screen.refresh()

	def inventory(self, player):
		a = 0
		b = 0
		for obj in player.inv:
			b += 1
			elf.screen.addstr(a, 0, str(b) + '. ' + obj.name)
			a += 1

	def death(self, player):
		self.screen.clear()
		self.screen.addstr(self.SYX[1]/2, (self.SYX[0]/2) - (len('You have died.')/2), 'You have died.')
		self.screen.refresh()

	def updateMainGame(self, player, mode, Map):
		height = self.SYX[0] - self.SYX[0]/3
		width = self.SYX[1] - self.SYX[1]/3
		self.screen.clear()
		# Set the area for GUI
		while height >= 0:
			self.screen.addstr(height, self.SYX[1] - self.SYX[1]/3, '#')
			height -= 1
		while width >= 0:
			self.screen.addstr(self.SYX[0] - self.SYX[0]/3, width, '#')
			width -= 1

		self.height = self.SYX[0] - self.SYX[0]/3
		self.width1 = self.SYX[1] - self.SYX[1]/6
		width2 = self.SYX[1] - self.SYX[1]/3
		# HP calculations
		HPAA = player.maxHP/10
		HPAAA = player.HP / HPAA
		if HPAAA > 10:
			HPAAA = 10
		HPA = '0' * HPAAA

		lvl = player.lvl

		self.screen.addstr(0, self.width1 - 3, 'Stats:')
		self.screen.addstr(2, self.width1 - 1, 'HP')
		self.screen.addstr(3, self.width1 - len(HPA)/2, HPA)
		self.screen.addstr(5, self.width1 - 1, 'XP')
		self.screen.addstr(6, self.width1 - len(str(player.XP) + ' / ' + str(player.lvlup))/2, str(player.XP) + ' / ' + str(player.lvlup))
		self.screen.addstr(8, self.width1 - len('level ')/2, 'Level')
		self.screen.addstr(9, self.width1 - len(str(player.lvl)), str(player.lvl))
		self.screen.addstr(11, self.width1 - len(str('Dungeon Room'))/2, 'Dungeon Room')
		self.screen.addstr(12, self.width1 - len(str(Map.id + 1)), str(Map.id + 1))

		self.screen.addstr(self.SYX[0] - 1, 0, self.line7)
		self.screen.addstr(self.SYX[0] - 2, 0, self.line6)
		self.screen.addstr(self.SYX[0] - 3, 0, self.line5)
		self.screen.addstr(self.SYX[0] - 4, 0, self.line4)
		self.screen.addstr(self.SYX[0] - 5, 0, self.line3)
		self.screen.addstr(self.SYX[0] - 6, 0, self.line2)
		self.screen.addstr(self.SYX[0] - 7, 0, self.line1)
		if player.HP < 1:
			mode = 'D'
		else:
			mode = mode
		return mode

	def toast(self, toast):
		self.line7 = self.line6
		self.line6 = self.line5
		self.line5 = self.line4
		self.line4 = self.line3
		self.line3 = self.line2
		self.line2 = self.line1
		self.line1 = toast

	def keypress(self, a, mode, player, room, Map):
		if a == ord('p') and mode == 'N' or a == ord('P') and mode == 'N':
			self.pause()
			mode = 'P'
			return mode

		elif a == ord('p') and mode == 'M' or a == ord('P') and mode == 'M':
			self.updateMainGame(player, mode, Map)
			self.toast('You begin your journey.')
			mode = 'N'
			return mode

		elif a == ord('p') and mode == 'P' or a == ord('P') and mode == 'P':
			self.mainGame()
			mode = 'N'
			return mode

		elif a == ord('m') and mode == 'C' or a == ord('M') and mode == 'C':
			self.mainMenu()
			mode = 'M'
			return mode

		elif mode == 'M' and a == ord('e') or mode == 'M' and a == ord('E'):
			self.screen.addstr(0, 0, "Hit any key to exit.")

		elif mode == 'M' and a == ord('c') or mode == 'M' and a == ord('C'):
			self.credits()
			mode = 'C'
			return mode

		elif mode == 'N' and a == ord('w') or mode == 'N' and a == ord('s') or mode == 'N' and a == ord('a') or mode == 'N' and a == ord('d'):
			player.walk(room, a, Map)
			mode = self.updateMainGame(player, mode, Map)
			Map.update(player)
			return mode
		elif mode == 'D':
			self.death(player)
		else:
			self.screen.addstr(self.SYX[0]-1, 0, 'Invalid keypress.')
			return mode