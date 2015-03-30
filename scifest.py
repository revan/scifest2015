#!/usr/bin/python2
# a dumb little demo to print peoples' names in Minecraft
# made by Revan Sopher for Rutgers SciFest 2015

print 'Initializing...'

from pyfiglet import Figlet
f = Figlet(font='banner4')

from mcpi import minecraft, block
mc = minecraft.Minecraft.create()
mc.postToChat("SciFest demo initialized.")

max_to_clear = 0
start_x = -80

while True:
	input = raw_input('Write your name and hit <Enter>: ')
	mc.player.setPos(start_x + 10, 10, 10)
	p_x = start_x
	for text in input.split():
		pattern = f.renderText(text)

		rows = pattern.split('\n')
		height = len(rows)
		length = len(rows[0])

		# clear space
		max_to_clear = max(max_to_clear, p_x - start_x)
		mc.setBlocks(p_x,0,0, p_x + max_to_clear, height, 20, block.AIR.id)

		# frame
		mc.setBlocks(p_x,0,0, p_x + length + 2, 0, 0, block.STONE_BRICK.id)
		mc.setBlocks(p_x,height,0, p_x + length + 2, height, 0, block.STONE_BRICK.id)

		# set pattern
		for y,row in enumerate(rows):
			for x,type in enumerate(row):
				mc.setBlock(p_x + x, height - y - 1, 0, block.WOOL.id, 14 if type=='#' else 15)

		p_x += length

		# set glass spacer
		mc.setBlocks(p_x, 1, 0, p_x + 2, height-1, 0, block.GLASS.id)

		p_x += 2
