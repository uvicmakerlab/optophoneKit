'''
Script for creating optophonic sounds. Part of the Optophone Kit 
and the Kits for Cultural History series by the MLab at the 
University of Victoria (maker.uvic.ca).

Link to the Optophone Kit repository: github.com/uvicmakerlab/optophoneKit

This script synthesizes tones of a particular frequency and
duration into a single .wav file.

'''

import math
import wave
import struct

frate = 44100.00  
amp = 8000.0 
sine_list = []
datasize = 0

#Define function for combining sounds, synthesizing into one chord
#freq = pitch, coef = amplitude, datasize = length, fname = name of wav file
def synthComplex(freq=[], coef=[], datalength=10000):
    #returns a tone for each number in datasize and appends it to a list
    for x in range(datalength):
        samp = 0
        for k in range(len(freq)): 
            samp = samp + coef[k] * math.sin(2*math.pi*freq[k]*(x/frate)) #the equation for creating a pure sine wav
        sine_list.append(samp)

#Synthesize the sounds
#synthComplex([784, 740, 659, 587, 523], [1, 1, 1, 1, 1], 2500)
#synthComplex([], [], 2500)

#Write the sounds into a single .wav file
def synthMelody():
    wav_file=wave.open("name.wav","w")
    nchannels = 1
    sampwidth = 2
    framerate = int(frate)
    nframes=datasize
    comptype= "NONE"
    compname= "not compressed"
    wav_file.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
    for s in sine_list:
        wav_file.writeframes(struct.pack('h', int(s*amp/2)))
    wav_file.close()

synthMelody()