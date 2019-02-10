#!/usr/local/bin/python3.7
""" seq-errors.py
Computes the exact solutions for the 
number of expected errors in a read
of sequences.
"""
import itertools
list(itertools.permutations([1, 2, 3]))
l = 10
n = 3
k = 4
p = 0.05

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

combs = list(combinations(range(l-n),4))
print(combs)
# Remove combinations that are non-contiguous
perm = list(itertools.permutations(range(l-n)))
print(perm)
"""
data_file = '../data/bee-population.txt'
soln_file = '../solns/bee-population-soln.txt'
plot_dir  = '../plots/'
LIMIT_ITER = 100000000

# Create out file
with open(soln_file, 'w') as f: pass

# Read in Data
data = {}

data = [[float(x) for x in line.split()] for line in open(data_file, 'r').readlines()][1:] # Skip the header line

pop_size = []

for vals in data:
    ni, a, b = vals
    iteration = 0
    next_n = ni
    while iteration < LIMIT_ITER:
        prev_n = next_n
        try:
            next_n = a*next_n - b*(next_n ** 2)
        except:
            pop_size.append(str(-1))
            break

        if next_n <= 0: 
            pop_size.append(str(-1))
            print(str(vals) + ': Neagtive Population on iter ' + str(iteration))
            break
        if abs(prev_n - next_n) < 0.0000001:
            pop_size.append(str(next_n))
            print(str(vals) + ': Converged on iter ' + str(iteration) + '!')
            break
        iteration += 1
    if iteration == LIMIT_ITER: 
        pop_size.append(str(-1))
        print('HIT THE MAX...')

# Write out solutions
with open(soln_file, 'a') as out: out.write('\n'.join(pop_size))
"""
