#!/usr/local/bin/python3.7
""" bee-population.py
Dynamic Programming computation of the 
limit of bee populations.
"""
import os, sys
import re
import subprocess

def hamdist(str1, str2):
    """
    Count the # of differences between 
    equal length strings str1 and str2
    """    
    diffs = 0
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2: diffs += 1
    return diffs

def slide_window(template, superstring, tolerance):
    idxs = []
    mismatches = []
    position = 0
    while len(superstring) >= len(template):
        substring = superstring[0:len(template)]
        if hamdist(template, substring) <= tolerance: 
            mismatches.append(substring)
            idxs.append(position)
        superstring = superstring[1:] # Cut off first char
        position += 1
    return idxs, mismatches

def get_templates(superstring, window_size):
    templates = []
    while len(superstring) > window_size:
        template = superstring[:window_size]
        templates.append(template)
        superstring = superstring[1:] # Cut the first char
    return templates

def get_cigar_string(reference, query):
    cmd = f'./cigar-gen/cigargen {reference} {query}'
    print(cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output = p.communicate()[0].decode('utf-8')
    print(output)
    return output

data_file = '../data/transposable-elements/6.txt'
soln_file = '../solns/transposable-elements/trans-elem-soln6.txt'
plot_dir  = '../plots/'

# Create out file
with open(soln_file, 'w') as f: pass

# Read in Data
data = {}

n,l,d = tuple([int(x) for x in open(data_file, 'r').readlines()[0].split()]) # First line
seq   = open(data_file, 'r').readlines()[1].strip() # Second line

# Split String into all windows of size l, add d for padding of additional possible indels
templates = list(set(get_templates(seq, l)))
print(len(templates))
for temp in templates:
    positions, mismatches = slide_window(temp, seq, d)
    if len(positions) == n: 
        print('MATCH: ' + temp)
        print(mismatches)
        cigars = [get_cigar_string(temp, mismatch) for mismatch in mismatches]
        print(cigars)

        with open(soln_file, 'a') as f: 
             f.write(f'{temp}\n')
             for i in range(len(positions)): 
                 f.write(f'{positions[i] + 1} {cigars[i]}\n')
