#!/usr/bin/python3.7
""" final-graph-decomposition.py
Author: Kevin Dick
Date: 2019-02-23
---

"""

data_file = '../data/graph-decomposition.txt'
soln_file = '../solns/graph-decomposition.txt'

# Create out file
with open(soln_file, 'w') as f: pass

# Read in Data
num_tests = int(open(data_file, 'r').readlines()[0])
data = {}

# TODO:: Finish this question

n,l,d = tuple([int(x) for x in open(data_file, 'r').readlines()[0].split()]) # First line
seq   = open(data_file, 'r').readlines()[1].strip() # Second line

