#!/usr/local/bin/python3.7
""" final-epigenomic-marks.py
Author: Kevin Dick
Date: 2019-02-23
---
Here we minimize the cross-entropy as a loss function.

"""
import random

BASELINE = 15.070097756683552

#def evaluate_soln(assigned_states):
	
def assign_state(num_states, inputs):
	s = sum(inputs)
	if s >= num_states: s = num_states - 1
	return s

data_file = '../data/epigenomic-marks/input_4.txt'
soln_file = '../solns/epigenomic-marks/epi-marks-soln4.txt'

# Create out file
with open(soln_file, 'w') as f: pass

# Read in Data
num_states = int(open(data_file, 'r').readlines()[0])
data = [[int(x) for x in line.strip()] for line in open(data_file, 'r').readlines()[1:]]
print(data)

"""
# Try a uniform assignment
assigned_state = []
# Naive Solution
for i in range(len(data[0])):
	assigned_state.append(str(random.choice(range(num_states))))
"""

assigned_state = []
# Better: Assign the sum of inputs as state
for i in range(len(data[0])):
	vect = [d[i] for d in data]
	assigned_state.append(str(assign_state(num_states, vect)))

print(assigned_state)
with open(soln_file, 'w') as f: f.write(' '.join(assigned_state))

#n,l,d = tuple([int(x) for x in open(data_file, 'r').readlines()[0].split()]) # First line
#seq   = open(data_file, 'r').readlines()[1].strip() # Second line

