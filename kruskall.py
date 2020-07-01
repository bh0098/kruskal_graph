"""
Created on Tue Jun  9 19:24:21 2020
@author: sahand and behnam esmaeilbeigi
"""

import time
class graph():
    """
    A class used to represent a graph
    ...
    Attributes
    ----------
    v : list
        list of vertices
    E : list
        list of edges
    Methods
    -------
    getv()
        returns the vertices list
    """

    def __init__(self, v: list, e: list):
        """ctor for graph
        Args:
            v (list): list of vertices
            e (list): list of edges
        """
        self.v = v
        self.e = e

    def getv(self) -> list:
        """returns the vertices list
        Returns:
            list: a list of vertices
        """
        return self.v


class d_set():
    dst = {}

    def __init__(self, g):
        for v in g.v:
            self.dst[v] = v
# find root and make root parent of ch
    def find(self, ch):
        tmp = ch
        while self.dst[tmp] != tmp:
            tmp = self.dst[tmp]
        return tmp

# union two sets a and b
# making both parents one node
    def union(self, a, b):
        cha = self.find(a)
        chb = self.find(b)
        self.dst[chb] = cha


def kruskal(g: graph) -> list:
    a = []
    cnt = 0
    dist_Set = d_set(g)
    egs = sorted(g.e, key=lambda x: x[2]) # sorting edges
    for e in egs:
        if dist_Set.find(e[0]) != dist_Set.find(e[1]):#check for cycle
            a.append(e)#add edge
            dist_Set.union(e[0], e[1])
            print(cnt," : ",a)
            cnt+=1#number of added edge
    return a



