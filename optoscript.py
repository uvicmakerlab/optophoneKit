'''
Script for playing optophonic sounds. Part of the Optophone Kit 
and the Kits for Cultural History series by the MLab at the 
University of Victoria (maker.uvic.ca).

Link to the Optophone Kit repository: github.com/uvicmakerlab/optophoneKit

This script matches each letter in a string to a corresponding 
sound file generated with toneGen.py, then plays them with PyGame.

'''

#Import libraries
import sys
import pygame as pg #PyGame

'''Create a dictionary of characters, each keyed to its tone. You can
modify the dictionary below to include your own files as long as you 
keep the correct syntax for Python. If the dictionary becomes too long,
you might want to keep it in a separate file and import it.

See http://www.tutorialspoint.com/python/python_dictionary.htm for more.
'''

'''The following line is the dictionary of tones. Inside the ''s before 
the :, type the character that the optophone detects (e.g. x). Inside 
the second pair of ''s, type the associated file to play when the 
computer reads that character (e.g. x-lo.wav).'''

tone_dict = {'a' : 'a-lo.wav', 'b' : 'b-lo.wav', 'c' : 'c-lo.wav'}
#Create an empty list to fill and pass to PyGame
tones = []

#Split each string into characters, create a list of characters
s = open('results.txt', 'r').read()
characters = list(s)

#For each character (item in the list), check it against the dictionary
#and append the corresponding tone to a separate list
for i in range(len(characters)):
	char = characters[i]
	if char in tone_dict:
		tones.append(tone_dict[str(char)])

#Pass the list of tones to PyGame. Play the list.
TRACK_END = pg.USEREVENT+1
track = 0

pg.init()
pg.display.set_mode((0,0))
pg.display.iconify()
pg.mixer.music.set_endevent(TRACK_END)
pg.mixer.music.load(tones[0])
pg.mixer.music.play()

while 1:
    for event in pg.event.get():
        if event.type == TRACK_END:
        	if track == len(tones)-1:
        		pg.display.quit()
        		pg.quit()
        		sys.exit()
        	else:
        		track += 1
           		pg.mixer.music.load(tones[track])
           		pg.mixer.music.play()
