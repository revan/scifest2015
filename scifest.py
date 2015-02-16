#!/usr/bin/python2
# a dumb little demo to print peoples' names in Minecraft
# made by Revan Sopher for Rutgers SciFest 2015

print 'Initializing...'

from pyfiglet import Figlet
f = Figlet(font='banner4')

from mcpi import minecraft
mc = minecraft.Minecraft.create()
mc.postToChat("SciFest demo initialized.")
print 'Done'

