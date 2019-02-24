#!/usr/local/bin/python3.7
""" final-bacterial-communities.py
Author: Kevin Dick
Date: 2019-02-23
---
In this question, we must order the generation of sequences.

For a two generation problem (as in exercise 1),
we can simply compute the average intra-generational similarity
by computing the Levenshtein ratio between one sample with all
others in a generation.
A generation with a high average intra-generational Levenshtein 
similarity is likely to occur earlier than a generation with a
lower intra-generational similarity. Over time, these sequences 
will accrue additional mutations, resulting in their divergence.

Thus, average similarity can be leveraged as a proxy for
chronological ordering in time.
"""
import Levenshtein as lv
import dendropy

data_file = '../data/bacterial-communities/4.txt'
soln_file = '../solns/bacterial-communities/bact-comm-soln4.txt'
file_idx = 0

def avg_igls(ref, rest):
	""" average inter-generational Levenshtein similarity
	    Computes the avg. igls for a given ref. string and
	    list of other strings.
	""" 
	igls = [lv.ratio(ref, x) for x in rest]
	return sum(igls)/len(igls)

# Create out file
with open(soln_file, 'w') as f: pass

# Read in Data and format as FASTA with indexing ids
num_expt = int(open(data_file, 'r').readlines()[file_idx])
file_idx += 1
for i in range(num_expt):
	print('-' * 42)
	num_gen  = int(open(data_file, 'r').readlines()[file_idx])
	file_idx += 1
	samples  = {}
	avg_lvs  = []
	all_smpls = {}
	
	# Load the sequences for each generation; add to samples dict
	for j in range(num_gen):
		gen_id = f'gen_{j}'
		samples[gen_id] = [x.strip() for x in open(data_file, 'r').readlines()[file_idx].split()]
		file_idx += 1
	
		# Every sample from all generations are combined into a single dict
		smpl_id = 0
		for smpl in samples[gen_id]:
			all_smpls[f'{gen_id}.smpl_{smpl_id}'] = smpl
			smpl_id += 1
	
	# Convert the dict of all experiment samples into a dendropy object
	dna = dendropy.DnaCharacterMatrix.from_dict(all_smpls)
	
	#


	# For each generation, compute the average intra-generational Levenshtein similarity
	# between every sample and every other in the generation (all2all).
	for gen_id in samples.keys():
		all_lv_avgs = [avg_igls(x, samples[gen_id]) for x in samples[gen_id]]
		avg_lv = sum(all_lv_avgs)/len(all_lv_avgs)
		avg_lvs.append((gen_id, avg_lv))
		print(f'generation {gen_id} average sim: {avg_lv}')

	# Sort each similarity in decreasing order for chronological ordering
	avg_lvs = sorted(avg_lvs, key=lambda x: x[1], reverse=True)
	print(avg_lvs)
	
	# Write out Solutions
	with open(soln_file, 'a') as f: f.write(' '.join([avg_lvs[j][0].replace('gen_', '') for j in range(len(avg_lvs))]) + '\n')
