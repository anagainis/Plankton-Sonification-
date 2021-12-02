#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 15:18:36 2021

@author: ariananagainis
"""
import numpy as np
import mido
import pygame.midi
import time
import matplotlib.pyplot as plt
import pandas as pd
import pygame, pygame.sndarray
import math


###################### INITIALIZE GLOBAL VALUES #############################
pygame.mixer.init(frequency=14100, size=-16, channels=1)

data = pd.read_csv('M6.csv')

area = data["AREA"]
frame = data["# FRAME"]
xc = data["XC"]
yc = data["YC"]
ID = data["ID"]

MAX_FRAME = 65 #np.max
MIN_AREA=50


###################### MAIN #############################
pygame.midi.init() #initilizes midi
print (pygame.midi.get_default_output_id()) 
print (pygame.midi.get_device_info(1))

player = pygame.midi.Output(2)
def make_music2(frameCount, objCount, area, xc, yc):
    print(frameCount, objCount, area, xc, yc)
    

def make_music(frameCount, objCount, area, xc, yc):
    print(area)
    note=int(area/2)
    if note > 100: 
        note = 20
    if note < 20:
        note = 100
    print('playing note', note)
    player.note_on(note, 100) # start note
    time.sleep(2) #duration of note (seconds)            
    player.note_off(note, 0) # stop note
    
def make_chord(note_list):
    #turn all notes on
    for area in note_list:
        note=int(area/2)
        if note > 100: 
            note = 20
        if note < 20:
            note = 100
        player.note_on(note, 100) 
    time.sleep(0.3)
    #turn notes off
    for area in note_list:
        note=int(area/2)
        if note > 100: 
            note = 20
        if note < 20:
            note = 100
        player.note_off(note, 100)
        


    