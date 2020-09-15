#!/bin/python3

import math
import os
import random
import re
import sys
from collections import counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
	# naive go-round: counter stores # occurences of each word in mag
	mag_dict = Counter()
	
	# counter stores # occur of each word needed for note
	
	#compare the two hash tables to see if all note.keys are in mag.keys
	
	#compare #occur for each word and return True if all magnum>notenum
	
	
	
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
