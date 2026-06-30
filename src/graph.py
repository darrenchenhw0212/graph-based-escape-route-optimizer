from .vertex import Vertex
from .edge import Edge
from .heap import MinHeap

class Graph:
    def __init__(self, V):
        """
        Function description: a function to create a graph with vertices using adjancency list 

        Approach description (if main function): create a graph with vertices using adjancency list by storing an array of vertices and 
        an array of edges(if adjacent) in each vertex

        Input: a list of vertices V

        Output, return or postcondition: return a graph with vertices created in class Vertex

        Time complexity: O(V)

        Time complexity analysis: To go through the list of vertices V, required O(V) where the length of the list is V. 

        Space complexity: O(V)

        Space complexity analysis: since adjancency list is used, we need to store all vertices in an array, which contribute the V part

        note: I did not include the complexity of O(E) in this function init because I am adding the edges in other step. Hence the mention 
        of complexity corresponding the edges will be delegated under the function add_edge(), thank you.
        """

        self.vertices = [None] * len(V)

        # this is where the O(V) time complexity comes from, we create all the vertices, which is length of V 
        for i in range(len(V)):
            self.vertices[i] = Vertex(V[i])


    def reset(self):

        """
        Function description: This is the function uses to reset the states(attributes) of a vertex, its existence is to reset all the 
        relevant values of each attributes accumulated from previous running of the escape function in the graph to default so that another 
        escape function can be run again on the same graph without using the previous incorrect values. 

        Approach description (if main function): resetting all relevant attributes of the vertices to the default values. 

        Input: None 

        Output, return or postcondition: The vertices of the TreeMap will have default values on the relevant attributes 

        Time complexity: O(1)

        Time complexity analysis: constant time operation, hence O(1)

        Space complexity: O(1)

        Space complexity analysis: require no space, hence O(1)
        """

        for vertex in self.vertices:

            vertex.minute = float('inf')
            vertex.discovered = False  
            vertex.visited = False
            vertex.previous = None 

    def add_edge(self, argv_edges, flipping = False):

        """
        Function description: a function to connect two vertices based on tuple of edges, and the graph is directed

        Approach description (if main function): connect two vertices u and v based on edge[0] and edge[1], while edge[2] is the weight
        of the edge. The graph is directed

        Input: a list of edges argv_edges, where each edge is a tuple of u, v, and w (u, v, w), and a boolean value argv_directed set to 
        True by default

        Output, return or postcondition: return nothing. But the graph created earlier in the __init__ function will be updated with
        the edges added

        Time complexity: O(E)

        Time complexity analysis:

        To go through the list of edges (argv_edges) E, required O(E) where the length of the list is E, and we have to go through all
        edges to connect two vertices.
        
        Space complexity: O(E)

        Space complexity analysis:

        since adjancency list is used, from the __init__ of the class Graph, we have already created all the vertices, which is V,
        by using the concept of separate chaining, we then append the edges to the vertices, which is the E part. Since we can only have 
        at most E edges, then we will just need to append all E edges separately to the vertices, hence the space complexity is O(E). 

        """
        # the flipping is an indicator used in order to see if we are creating the normal TreeMap or the flipped version TreeMap
        # further elaborate under class TreeMap

        # flipping is False, we are creating the normal TreeMap with original direction of the edges between vertices 
        if flipping == False: 
            for edge in argv_edges:
                u = edge[0]
                v = edge[1]
                w = edge[2]
                # add u to v
                current_edge = Edge(u,v,w)
                current_vertex = self.vertices[u]

                # adding the edge to current_vertex 
                current_vertex.add_edge(current_edge)

        # flipping is True, indicating we are creating the flipped version of the normal TreeMap
        # in order to flip the edges, we see u as v and v as u compare to the unflip version
        elif flipping == True:
            for edge in argv_edges:
                u = edge[1]
                v = edge[0]
                w = edge[2]
                # add u to v
                current_edge = Edge(u,v,w)
                current_vertex = self.vertices[u]

                current_vertex.add_edge(current_edge)

    def dijkstra(self, source):

        """
        Function description: Dijsktra's algorithm to find the shortest path from a source to all other vertices in the graph, 
        using a MinHeap to store the vertices in the graph. Source given is a vertex id 

        Approach description (if main function): first we call the reset function just in case there are values stored in the 
        vertices from previous computation. Then creating a minheap initialising discovered as a minheap with the list of vertices. 
        Setting all vertices' minute to float("inf") becauser it is a minheap, we prioritise smaller value. Hence choosing the polar extreme
        infinity as the default value. Before runnig Dijskra, update the minute of the input source as 0, meaning that it is the staring vertex(tree)
        hence there is no minute to travel to itself. Then use added_to_discovered() to indicate that it has been added into the heap.
        While the heap is not empty, we keep on serving by calling discovered.serve(). Whenever something is served. We use visited_node() to indicate 
        that the served vertex is visited, hence the minute of the vertex took to travel from the source is finalised. 

        Input: a source vertex id

        Output, return or postcondition: discovered(minheap) will be emptied. Because all vertices have been visited, and the shortest
        from the source to all other vertices has been identified, and stored under vertex.minute, the previous vertex to the current 
        vertex will also be saved inside the current vertex's attribute: previous 

        Time complexity: |E|log|V|

        Time complexity analysis:

        Creating a Minheap containing all None requires O|V| times, since |V| vertices indicates |V| slots in the Minheap. While building 
        the Minheap using build_min_heap() requires looping for |V| times. Since we are using a Minheap to perform Dijkstra on.where |E| 
        is the number of edges while |V| is the number of vertices, Because we have |E| edges, hence we have to do edge relaxation on 
        all edges. The time complexity inherited from the MinHeap is log|V|, where |V| is the number of vertices. Hence repeating log|V| 
        for |E| times gives us |E|log|V|.

        O|V| + O|V| + |E|log|V| = |E|log|V| 


        Space complexity: O(|V|)

        Space complexity analysis: Inherent from the space complexity in creating a MinHeap, the space complexity is O(V). Since we need a
        heap of |V| size and a mapping array of |V| size as well. O(|V|) + O(|V|) = O(|V|). Since Big O notation ignores constants.
        """

        # resetting the relevant attributes back to defaults if they are not already is
        self.reset()

        # creating a minheap called discovered
        discovered = MinHeap(self.vertices)

        # just to set all vertices to have a minute of infinity and none as previous
        for vertex in self.vertices:
            vertex.minute = float('inf')
            vertex.previous = None
    
        # bulid the minheap with self.vertices 
        ####
        discovered.build_min_heap(self.vertices)

        # update the source to have minute of 0
        discovered.update(self.vertices[source], 0)

        # indicating source has been added into the discovered 
        discovered.heap[discovered.mapping_array[source]].added_to_discovered()
        
        while len(discovered) > 0:
        #      #serve from 
            u = discovered.serve()
            u.added_to_discovered()
            u.visited_node() # mean i have visit u, minute is finalized 

            for edge in u.edges:
                v = edge.v

                if self.vertices[v].discovered == False: # meaning the minute is still inf
                
                    # indicator 
                    self.vertices[v].added_to_discovered()

                    # setting the minute took to travel from source to v as u.minute + the edge w
                    self.vertices[v].minute = u.minute + edge.w
                    
                    # setting the previous of vertex v as vertex u
                    self.vertices[v].previous = u

                    # update the discovered with vertex v and its newest minute 
                    discovered.update(self.vertices[v], self.vertices[v].minute)

                # it is in heap but not yet finalized
                elif self.vertices[v].visited == False:

                    # if i find a shorter path to v, change it 
                    if self.vertices[v].minute > u.minute + edge.w:

                        # update minute 
                        self.vertices[v].minute = u.minute + edge.w

                        # update the heap  
                        self.vertices[v].previous = u

                        discovered.update(self.vertices[v], self.vertices[v].minute) # update vertex v in heap , with distance v.minute 
