from Graph import Vertex
from Graph import Edge
from Graph import Graph

import random

class RandomGraph(Graph):
    """
    Erdos-Renyi model for a random graph
    """
    def add_random_edges(self,p):
        for vertex in self.vertices():
            for vert in self.vertices():
                ranNum = random.random()
                if ranNum < p and vertex != vert:
                    self.add_edge(Edge(vertex,vert))



if __name__ == '__main__':
    v_s = ['a','b','c','d','e']
    RG = RandomGraph(Graph([Vertex(item) for item in v_s]))
    RG.add_random_edges(.5)
    print len(RG.edges())
        

