#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    # naive go-round: counter stores # occurences of each word in mag
    mag_count = Counter(magazine)
    
    # counter stores # occur of each word needed for note
    note_count = Counter(note)
    
    #compare the two hash tables to see if all note.keys are in mag.keys
    #"dumb" way with direct comparison and iteration
    for word in note_count:
        if not (word in mag_count.keys() and note_count[word]<=mag_count[word]):
            return 'No'
    #compare #occur for each word and return True if all magnum>notenum
    
    return 'Yes'
	
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
