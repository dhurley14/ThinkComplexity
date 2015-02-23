""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

class Vertex(object):
    """A Vertex is a node in a graph."""

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        """Returns a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Edge(tuple):
    """An Edge is a list of two vertices."""

    def __new__(cls, *vs):
        """The Edge constructor takes two vertices."""
        if len(vs) != 2:
            raise ValueError, 'Edges must connect exactly two vertices.'
        return tuple.__new__(cls, vs)

    def __repr__(self):
        """Return a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Graph(dict):
    """A Graph is a dictionary of dictionaries.  The outer
    dictionary maps from a vertex to an inner dictionary.
    The inner dictionary maps from other vertices to edges.
    
    For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists."""

    def __init__(self, vs=[], es=[]):
        """Creates a new graph.  
        vs: list of vertices;
        es: list of edges.
        """
        for v in vs:
            self.add_vertex(v)
            
        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """Add a vertex to the graph."""
        self[v] = {}

    def add_edge(self, e):
        """Adds and edge to the graph by adding an entry in both directions.

        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self, v1, v2):
        """ takes two vertices and returns the edge between them
        if it exists, and NONE otherwise. """

        try:

            return self[v1][v2]

        except: 

            return None 

    def remove_edge(self, edge):
        """ removes an edge in the graph """

        self[edge[0]][edge[1]] = None
        self[edge[1]][edge[0]] = None   

    def vertices(self):
        """ returns a list of vertices in a graph """
        return self.keys() # changed this on February 22nd, 2015
        #return set(self)

    def edges(self):
        """ returns a list of edges in a graph """

        listOfEdges = []

        for ver1 in self.vertices():
            for ver2 in self.vertices():
                #print ver1, ver2
                if ver1 != ver2:
                    if self.get_edge(ver1, ver2) != None:
                        listOfEdges.append(self.get_edge(ver1, ver2))
            #listOfEdges.append(self[v1][v2])
            #print v1

        return set(listOfEdges)

    def out_vertices(self, vert1):

        vertices = []

        for edge in self.edges():
            if edge[0] == vert1:
                vertices.append(edge[1])
            elif edge[1] == vert1:
                vertices.append(edge[0])
                
        return (vertices)

    def out_edges(self, vertex):

        edges = []
        
        for vertex2 in self.out_vertices(vertex):
            edges.append(self.get_edge(vertex,vertex2))

        return set(edges)
        


    def add_all_edges(self):

        for vertex1 in self.vertices():
            for vertex2 in self.vertices():
                if vertex2 != vertex1:
                    self.add_edge(Edge(vertex1, vertex2))




    def add_regular_edges(self,k):
        n = self.vertices()
        print n
        num_vertices = len(n)
        print num_vertices
        print k
        if k < num_vertices and (num_vertices%2 == 0 or k%2 == 0):
            print True
            if k%2 == 0:
                # k is even, ipso facto compute k=2m
                m = k/2
                print "m: ",m
                for vertex_index in range(num_vertices):
                    for i in range(m):
                        old_vertex = n[vertex_index]
                        print "old vertex = ",str(old_vertex)
                        # add +1 to i since it starts at 0..
                        try:
                            new_vert = n[vertex_index+i+1]
                            print "new_vert before if in try.. ", str(new_vert)
                            if old_vertex == new_vert:
                                new_vert = n[vertex_index+i+2]
                                print "new vert = old vert in try"
                            print "new_vert: "+str(new_vert)

                        except:
                            #new_vert = n[num_vertices - (vertex_index+i+1)] # try switching these around.. ?
                            new_vert = n[(vertex_index+i+1) - num_vertices]
                            print "new_vert before if in except.. ", str(new_vert)
                            if old_vertex == new_vert:
                                new_vert = n[(vertex_index+i+2) - num_vertices]
                                print "new vert = old vert in except"
                            print "new_vert: "+str(new_vert)

                        print "adding edge from: " +str(n[vertex_index]) + " to " + str(new_vert)
                        if self.get_edge(n[vertex_index],new_vert) == None and self.get_edge(new_vert,n[vertex_index]) == None and n[vertex_index] != new_vert:
                            self.add_edge(Edge(n[vertex_index],new_vert))

                        else:
                            print "doing nothing.."
                            
                    


            else:
                # k is odd, compute k = 2m + 1
                m = (k-1)/2
                print "m: ",m
                for vertex_index in range(num_vertices):
                    for i in range(m):
                        old_vertex = n[vertex_index]
                        print "old vertex = ",str(old_vertex)
                        # add +1 to i since it starts at 0..
                        try:
                            new_vert = n[vertex_index+i+1]
                            print "new_vert before if in try.. ", str(new_vert)
                            if old_vertex == new_vert:
                                new_vert = n[vertex_index+i+2]
                                print "new vert = old vert in try"
                            print "new_vert: "+str(new_vert)

                        except:
                            #new_vert = n[num_vertices - (vertex_index+i+1)] # try switching these around.. ?
                            new_vert = n[(vertex_index+i+1) - num_vertices]
                            print "new_vert before if in except.. ", str(new_vert)
                            if old_vertex == new_vert:
                                new_vert = n[(vertex_index+i+2) - num_vertices]
                                print "new vert = old vert in except"
                            print "new_vert: "+str(new_vert)

                        print "adding edge from: " +str(n[vertex_index]) + " to " + str(new_vert)
                        if self.get_edge(n[vertex_index],new_vert) == None and self.get_edge(new_vert,n[vertex_index]) == None and n[vertex_index] != new_vert:
                            self.add_edge(Edge(n[vertex_index],new_vert))
                            # add a vertex going from old vert to one directly across it.
                            try:
                                self.add_edge(Edge(n[vertex_index],n[vertex_index+((num_vertices)/2)]))
                            except:
                                self.add_edge(Edge(n[vertex_index],n[(vertex_index+((num_vertices)/2))-num_vertices]))

                        else:
                            print "doing nothing.."
                #print "hi"
                
        else:
            print "k is too big, or number of vertices / edges is not even.  Ugh."




def main(script, *args):
    v = Vertex('v')
    a = Vertex('a')
    b = Vertex('b')
    x = Vertex('x')
    y = Vertex('y')
    #print v
    w = Vertex('w')
    #print w
    e = Edge(v, w)
    e2 = Edge(a,b)
    e3 = Edge(x,y)
    e4 = Edge(y, a)
    e5 = Edge(x, v)
    print e
    g = Graph([v,w,a,b,x,y], [e,e2,e3,e4,e5])
    print g
    print "\nget the edge between v and w\n\n",g.get_edge(v, w)
    #print "\nremoving edge: ", g.remove_edge(e), g.get_edge(v, w) == None
    print "\ngetting the list of all vertices: ", g.vertices()
    print "\n\n\nthe edges: ", g.edges()
    print "\n\nthe vertices connected to vertex 5 are: ", g.out_vertices(x)
    g2 = Graph([v,w,a,b,x,y],[])
    print "edge count for g2: ", len(g2.edges())
    print "adding edges between all vertices..."
    g2.add_all_edges()
    print "edge count for g2 after add_all_edges: ", len(g2.edges())
    print "\n\nout edges: ",g2.out_edges(a)
    

    
if __name__ == '__main__':
    import sys
    main(*sys.argv)
