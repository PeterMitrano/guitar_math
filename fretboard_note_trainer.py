#!/usr/bin/env python
# coding: utf-8
import random
string_names = ['low E', 'A', 'D','G', 'B', 'high E']
nested_pitches = [[c+ "♭", c, c+"♯"] for c in [chr(i+65) for i in list(range(7))]]
pitches = [p for sublist in nested_pitches for p in sublist]
n_completed = 0
while True:
    print(f"{n_completed:5d}\tPlay {random.choice(pitches):2s} on the {random.choice(string_names):6s} string", end='')
    input()
    n_completed += 1
    
