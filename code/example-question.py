#!/usr/local/bin/python3.7
""" Example A + B
Sum the integers on the lines in the input file.
"""
data_file = '../data/example-input.txt'
soln_file = '../solns/example_soln.txt'

# Create out file
with open(soln_file, 'w') as f: pass

# Read in Data
data = [line.strip() for line in open(data_file, 'r').readlines()]

for line in data[1:]: # Skip the header line
	with open(soln_file, 'a') as out: out.write(f'{int(line.split()[0]) + int(line.split()[1])}\n')
	
	
