# The MIT License (MIT)

# Copyright (c) 2014 Simon Hook

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import re
import pygame, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

res_x = 1024
res_y = 768
screen = pygame.display.set_mode((res_x, res_y))

size_x = 100
size_y = 100
nodes = []

try:
	path = sys.argv[1]
except IndexError:
	print "No Path given. Try something like this:"
	print ">> python visualize_castalia.py Simulations/radioTest/"
	pygame.quit()
	sys.exit()


blue = pygame.Color(0,0,255)
white = pygame.Color(255,255,255)



### Read omnetpp.ini file to get field size ###
inifile = path + 'omnetpp.ini'
ini = open(inifile, 'r')
regex = re.compile(r"(\d+)")
for line in ini:
	if "SN.field_x" in line:
		match = regex.search(line)
		size_x = int(match.group(1))
		print ("size_x set to %d" %size_x)
	elif "SN.field_y" in line:
		match = regex.search(line)
		size_y = int(match.group(1))
		print ("size_y set to %d" %size_y)
	# elif "SN.numNodes" in line:
	# 	match = regex.match(line)
ini.close()


### Open Tracefile ###
tracefile = path + 'Castalia-Trace.txt'
f = open(tracefile, "r")
regex = re.compile(r"([0-9]+[\.[0-9]*]*)\D*([0-9]+)\D*([0-9]+[\.[0-9]*]*):([0-9]+[\.[0-9]*]*):([0-9]+[\.[0-9]*]*)")



### parse a line from the trace file and check for mobility ###
def parseline(f):
	line = f.readline()
	if "initial location" in line:
		match = regex.match(line)
		if match:
			# print match.group(2)
			# print str(match.group(1)) + ", " + str(match.group(2)) + ", " + str(match.group(3)) + ":" + str(match.group(4)) + ":" + str(match.group(5))
			node = int(match.group(2))
	  		(x,y) = (int(float(match.group(3))), int(float(match.group(4))))
	  		# print node, x, y
			new_node = (match.group(2),(match.group(3), match.group(4)))
			nodes.append(new_node)

 	if "changed location" in line:
  		match = regex.match(line)
  		if match:
	  		node = int(match.group(2))
	  		(x,y) = (int(float(match.group(3))), int(float(match.group(4))))
	  		# print node, x, y
	  		nodes[node] = (node, (x,y))

  	return nodes


### Main loop of "Game" ###
while True:
	nodes = parseline(f)
	screen.fill(white)

	# print nodes

	for node in nodes:
		# print "node " + str(node)
		# print node[1][0]
		x = int(int(node[1][0]) * res_x/size_x)
		y = int(int(node[1][1]) * res_y/size_y)
		pygame.draw.circle(screen, blue, (x,y), 10, 0)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			f.close()
			sys.exit()

		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.event.post(pygame.event.Event(QUIT))

	pygame.display.update()
	fpsClock.tick(30)