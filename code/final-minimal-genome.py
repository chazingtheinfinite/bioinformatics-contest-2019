#!/usr/local/bin/python3.7
""" final-minimal-genome.py
Author: Kevin Dick
Date: 2019-02-23
---
This problem requires reverse transcribing amino acids
and having them fit into as small a genome as possible.
In essence, this is a minimum super-string problem with
the added complexity of permitting rever compliments via
reverse compliments.
"""
import mapping_module as mm
import itertools as it
import sys 

def compliment(base):
	if   base == 'A': return 'T'
	elif base == 'T': return 'A'
	elif base == 'G': return 'C'
	elif base == 'C': return 'G'
	return ''

def compliment_strand(original):
	return ''.join([compliment(b) for b in original[::-1]])

def convert_strand(original):
	return ''.join([mm.AA2DNA[base][0] for base in original])

data_file = '../data/minimal-genome/1.txt'
soln_file = '../solns/minimal-genome/min-gen-soln1.txt'
file_idx = 0

# Create out file
with open(soln_file, 'w') as f: pass

num_prots = int(open(data_file, 'r').readlines()[0])
seqs = [line.strip() for line in open(data_file, 'r').readlines()[1:]]

print(f'Original Order: {seqs}')
# Order sequences by length
seqs = sorted(seqs, key=len, reverse=True)
print(f'Sorted Order: {seqs}')


candidate_aa = seqs[0]
for s in seqs[1:]:
	idx = candidate_aa.find(s)
	if idx < 0: print(f'failed: {s}')
sys.exit(0)

# Grow sequence from the largest while checking for substrings
candidate_dna = convert_strand(seqs[0])
candidate_rev = compliment_strand(candidate_dna)

# Naive forward search in DNA-space
failed = []
for s in seqs[1:]:
	s_dna = convert_strand(s)
	idx = candidate_dna.find(s_dna)
	if idx >= 0: 
		print(f'Contains Forward at {idx}: {s_dna}') 
		continue
	# Try on the reverse compliment
	idx = candidate_rev.find(s_dna)
	if idx >= 0:
		print(f'Contains Reverse at {idx}: {s_dna}')
		continue	
	failed.append(s_dna)
print(f'Num Failed: {len(failed)}\n{failed}')

# Naive forward search in DNA-space
#candidate_dna = convert_strand(candidate_aa)
#for s in failed:
#	idx = candidate_dna.find(s)
	

"""
SEQUENCES = seqs
LONGEST_SUPERSTRING = ''.join(SEQUENCES)

def find_shortest_superstring():
    current_shortest = LONGEST_SUPERSTRING
    trim = len(current_shortest)-1
    seen_prefixes = set()
    for perm in it.permutations(SEQUENCES):
        candidate_string = ''.join(perm)[:trim]
        if candidate_string in seen_prefixes:
            continue
        seen_prefixes.add(candidate_string)
        while is_superstring(candidate_string):
            current_shortest = candidate_string
            candidate_string = candidate_string[:-1]
            trim = len(current_shortest)-1
    return current_shortest

def is_superstring(s):
    return all(seq in s for seq in SEQUENCES)

ss = find_shortest_superstring()
print('Found shortest superstring containing all strings:\n{}'.format(ss))
"""

# Write out Solutions;must increment indecies by one for 1-indexing
#with open(soln_file, 'a') as f: f.write('\n'.join([str(x + 1) for x in matches]))
