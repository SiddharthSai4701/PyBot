# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 23:14:14 2022

@author: sidvs
"""
# PyBotKey XKL9WT-KQJLEEWK3H

import wolframalpha as w


client = w.Client("XKL9WT-KQJLEEWK3H")


import PySimpleGUI as sg                        # Part 1 - The import

sg.theme('DarkBlue')

# Define the window's contents
layout = [  [sg.Text("Type anything")], [sg.Input()], [sg.Button('Ok')], [sg.Button('Cancel')] ]

# Create the window
window = sg.Window('PyBot', layout)      # Part 3 - Window Defintion

while True:
    event, values = window.read()                   # Part 4 - Event loop or Window.read call    
    
    if event in (None, 'Cancel'):
        break
    res = client.query(values[0])
    # Do something with the information gathered
    sg.Popup(next(res.results).text)



# Finish up by removing from the screen
window.close()                                  # Part 5 - Close the Window