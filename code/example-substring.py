#!/usr/local/bin/python3.7
""" example_substring.py
Search for a substring position in a string!
"""
from suffix_trees import STree

data_file = '../data/example-substring.txt'
soln_file = '../solns/substring-soln.txt'

# Create out file
with open(soln_file, 'w') as f: pass

# Read in Data
data = [line.strip() for line in open(data_file, 'r').readlines()][1:] # Skip the header line

strings = data[::2]  # All Even line entries
targets = data[1::2] # All Odd line entries

for i in range(len(strings)):
	string = strings[i]
	target = targets[i]

	st   = STree.STree(strings[i])
	idxs = [str(idx + 1) for idx in st.find_all(target)]
	#print(idxs)
	
	with open(soln_file, 'a') as out: out.write(' '.join(idxs) + '\n')
