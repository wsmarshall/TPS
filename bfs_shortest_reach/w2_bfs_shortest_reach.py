# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 11:20:07 2020

@author: way
"""

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

# Complete the bfs function below.
def bfs(n, m, edges, s):
    """n - number of nodes in the graph
    m - number of edges in the graph
    edges -  2d array of start/end nodes
    s - the node to start traversals from"""
    
    # Want to search through 'nearest ones to s' first
    # by keeping track of which nodes are connected, we can more easily compare
    graph = defaultdict(list)
    # note the auto unpacking capability([1,2]->n1,n2)
    for node1,node2 in edges:
        graph[node1].append(node2)
        graph[node2].append(node1)
        
    #next, need to calculate the distances from s to each of n
    dists = defaultdict(lambda: -1)
    dists[s] = 0 # distance from start to start is 0
    # use queue to hold the elements whose connections must be checked
    queue = [s]
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if dists[neighbor] < 0:
                #if dist not determined yet, add 6 to start-vertex distance
                dists[neighbor] = dists[vertex] + 6
                queue.append(neighbor) # add the node to q for subgraph distances
                

    return [dists[i] for i in range(1,n+1) if i != s]
#
#edges_=[[1,2],[1,3]]
#n = 4
#m = 2
#s = 1
#
#print(bfs(n,m,edges_,s))
#
#edges2 = [[2,3]]
#m2 =1
#n2 = 3
#s2=2
#print(bfs(n2,m2,edges2,s2))
    
if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)
        print(result)