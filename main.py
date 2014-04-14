import curses
import time
from mapSystem import dungeon
from menusClass import menus
from playerMain import player
import pickle

def mainLoop():
	config = pickle.load(open('config.txt', 'r'))

	screen = curses.initscr()   # Init curses
	curses.start_color()
	curses.cbreak()
	screen.keypad(1)

	SYX = screen.getmaxyx()     # Get the size info for the screen

	curses.noecho()             # Suppress key output to screen
	curses.curs_set(0)          # remove cursor from screen
	screen.keypad(1)            # set mode when capturing keypresses

	curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)

	menu = menus(screen, SYX)
	Map = dungeon(screen, SYX, menu)

	if config[0] == 'NO':
		screen.addstr(SYX[0]/2, SYX[1]/2-11, "A Donut with Sprinklez")
		screen.refresh()
		time.sleep(3)
		screen.clear()

		screen.addstr(SYX[0]/2, SYX[1]/2-4, "Presents")
		screen.refresh()
		time.sleep(3)
		screen.clear()

		screen.addstr(SYX[0]/2, SYX[1]/2-4, "Rogue Like Me")
		screen.refresh()
		time.sleep(5)
		screen.clear()

	else:
		pass

	menu.mainMenu()
	Player = player(screen, Map.rooms[0].leftOrigin, Map.rooms[0].topHeight, Map.rooms[0].length, Map.rooms[0].height, menu, Map)
	# N = normal mode
	# M = main menu
	# P = pause menu
	# D = dead
	# I = inventory
	mode = 'M'
	while 1:
		a = screen.getch()
		mode = menu.keypress(a, mode, Player, Map.rooms[0+Map.id], Map)
		if mode == 'N':
			mode = menu.updateMainGame(Player, mode, Map)
			Player.update()
			screen.clear()
			mode = menu.updateMainGame(Player, mode, Map)
			red = curses.color_pair(1)
			Map.draw()
			Player.draw()
		elif mode == 'I':
			pass

	screen.getch()
	curses.endwin()