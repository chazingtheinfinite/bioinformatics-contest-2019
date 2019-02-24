#!/usr/local/bin/python3.7
""" final-endangered-species.py
Author: Kevin Dick
Date: 2019-02-23
---
This problem requires matching male/females to ensure the maximum
genetic diversity in their off-spring. We must accound for possible
genetic recombination following Haldane's model.
"""
import random
import math 

def score_match(m,f):
	scr = 0
	for i in range(len(m)):
		#print(f'idx: {i} | m[i]: {m[i]} | f[i]: {f[i]}')
		if   m[i] == '0/0' and f[i] == '1/1': scr += 1
		elif m[i] == '0/0' and f[i] == '0/1': scr += 0.5
		elif m[i] == '0/0' and f[i] == '1/0': scr += 0.5
		elif m[i] == '0/0' and f[i] == '0/0': scr += 0
		elif m[i] == '0/1': scr += 0.5
		elif m[i] == '1/0': scr += 0.5
		elif m[i] == '1/1' and f[i] == '1/1': scr += 0
		elif m[i] == '1/1' and f[i] == '0/1': scr += 0.5
		elif m[i] == '1/1' and f[i] == '1/0': scr += 0.5
		elif m[i] == '1/1' and f[i] == '0/0': scr += 1
	return scr

def recombine(m_site, f_site):
	""" recombine
	    Performs the recombination of two given sites in the
	    male and female genome.
	"""
	new_m = m_site.split('/')[0] + '/' + f_site.split('/')[0]
	new_f = f_site.split('/')[1] + '/' + m_site.split('/')[1]
	return new_m, new_f

def recomb_prob(dist):
	""" recomb_prob
	    Returns the probability that this site will recombine.
	"""
	return 0.5 * (1 - math.e ** (-2 * dist * 10 ** (-8)))

def recomb_site(m_vect, f_vect, idx, poly_sites):
	""" recomb site
	    For a single poly site, we want to determine what the 
	    resulting offspring genotype might be while taking into
	    account the probability of recombination. 
	"""
	pos1 = 0
	pos2 = 0
	if idx == 0: # This is the first poly site
		_, pos2 = poly_sites['p0']
	else:
		chrm1, pos1 = poly_sites[f'p{idx-1}'] # get preceeding site
		chrm2, pos2 = poly_sites[f'p{idx}']   # get current site
		if chrm1 != chrm2: pos1 = 0 # This is the start of another chromosome

	#print(f'm_vect: {m_vect} | f_vect: {f_vect}')
	# Recombine if probable and return the new vector with changed site
	if random.uniform(0,1) <= recomb_prob(pos2 - pos1): m_vect[idx], f_vect[idx] = recombine(m_vect[idx], f_vect[idx])
	return m_vect, f_vect
	
def recomb_match(m_vect, f_vect, poly_sites):
	""" recomb match
	    For a given male-female pairing, we need to determine
	    what their putative recombinations may be such that
	    we can score them.	
	"""
	for i in range(len(m_vect)): m_vect, f_vect = recomb_site(m_vect, f_vect, i, poly_sites)
	
	# From the resulting recombination on this match, score it!
	return score_match(m_vect,f_vect)

def list_diff(l1, l2): 
    ldiff = [i for i in l1 + l2 if i not in l1 or i not in l2] 
    return ldiff 

def greedy_search(matches, males, females, poly_sites):
	all_the_single_ladies = [i for i in range(len(matches)) if i not in matches]
	print(f'All the Single Ladies: {all_the_single_ladies}')
	best_match = -1
	best_pair  = (-1, -1)
	for m in range(len(matches)):
		if matches[m] != -1: continue
		# Compare current male against all available ladies
		for f in all_the_single_ladies:
			match_val = recomb_match(males[f'm{m}'], females[f'f{f}'], poly_sites)
			print(f'Match Value for m{m} and f{f}: {match_val}')
			if match_val > best_match:
				best_match = match_val
				best_pair  = (m, f)
			# With some stochasticity, we can play around with ties...
			if match_val == best_match and random.uniform(0,1) > 0.24:
				best_match = match_val
				best_pair  = (m, f)
	# At the end of all this, our best matched couple are in 'best_match/pair'
	print(f'Assigning m{best_pair[0]} and f{best_pair[1]} with score {best_match}')
	matches[best_pair[0]] = best_pair[1]
	return matches

def greedy_matching(males, females, poly_sites):
	""" greedy matching
	    Performs a greedy matching search in O(n^2).
	    Find the highest scoring matching, then assert the match.
	    Repeat for all remaining unmatched individuals.
	"""
	# Initialize list of male as indecies
	matches = [-1] * len(males)

	while -1 in matches: 
		matches = greedy_search(matches, males, females, poly_sites)
		print(f'Current Matches: {matches}')
	return matches	

data_file = '../data/endangered-species/3.in'
soln_file = '../solns/endangered-species/end-spec-soln3.txt'
file_idx = 0

# Create out file
with open(soln_file, 'w') as f: pass

num_chrome, num_poly = [int(x) for x in open(data_file, 'r').readlines()[file_idx].split(' ')]
file_idx += 1
poly_sites = {}
for i in range(num_poly):
	chrome, poly =  [int(x) for x in open(data_file, 'r').readlines()[file_idx].split(' ')]
	poly_sites[f'p{i}'] = (chrome, poly)
	file_idx += 1
print(poly_sites)

num_org = int(open(data_file, 'r').readlines()[file_idx])
file_idx += 1

males   = {}
females = {}

# Load Males First
for i in range(num_org):
	org_id   = f'm{i}'
	print(org_id)
	genotype = []
	for j in range(num_poly):
		genotype.append(open(data_file, 'r').readlines()[file_idx].strip())
		file_idx += 1
	males[org_id] = genotype
	file_idx += 1

# Load Females
for i in range(num_org):
	org_id   = f'f{i}'
	print(org_id)
	genotype = []
	for j in range(num_poly):
		genotype.append(open(data_file, 'r').readlines()[file_idx].strip())
		file_idx += 1
	females[org_id] = genotype
	file_idx += 1	
print(males)
print(females)

# Apply our greedy search to generate our matching:
matches = greedy_matching(males, females, poly_sites)


# Write out Solutions;must increment indecies by one for 1-indexing
with open(soln_file, 'a') as f: f.write('\n'.join([str(x + 1) for x in matches]))
