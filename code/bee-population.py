#!/usr/local/bin/python3.7
""" bee-population.py
Dynamic Programming computation of the 
limit of bee populations.
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
