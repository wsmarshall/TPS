#meanmedmode

# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import numpy as np
from collections import Counter

def mean_med_mode(el):
    mean = np.mean(el)
    med = np.median(el)
    count = Counter(el)
    max_count = max(count.values())
    mode_candidates = [n for n in count if count[n] == max_count]
    mode = min(mode_candidates)
    return f'{mean}\n{med}\n{mode}'

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    N = lines[0]
    elements = list(map(int, lines[1].split()))
    print(mean_med_mode(elements))