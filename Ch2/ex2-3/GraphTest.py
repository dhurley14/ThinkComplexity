import string

from Graph import Vertex
from Graph import Edge
from Graph import Graph

import GraphWorld as graphw

def main(script, n='6', *args):
    # Construct our graph..
    # create n Vertices
    n = int(n)
    labels = string.ascii_lowercase + string.ascii_uppercase
    vs = [Vertex(c) for c in labels[:n]]

    # create a graph and a layout
    g = Graph(vs)
    #g.add_all_edges()
    g.add_regular_edges(4)
    #print len(g.edges()) == 45 # making sure it is a K10
    layout = graphw.CircleLayout(g)

    # draw the graph
    gw = graphw.GraphWorld()
    gw.show_graph(g, layout)
    gw.mainloop()

if __name__ == '__main__':
    import sys
    main(*sys.argv)
