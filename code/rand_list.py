#!/usr/local/bin/python3.7
from random import shuffle
nums = list(range(1,101))
shuffle(nums)
with open('../solns/endangered-species/randnums', 'w') as f: f.write('\n'.join([str(n) for n in nums]))
