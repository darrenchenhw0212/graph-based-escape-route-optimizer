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

class Vertex:    

    def __init__(self, id):

        """
        Function description: a function to create a vertex 

        Input: an id of the vertex, which is an integer value 

        Output, return or postcondition: return a vertex created in class Vertex 

        Time complexity: O(1) 

        Time complexity analysis: linear operation 

        Space complexity: O(1)

        Space complexity analysis: linear operation 
        """
        # list
        self.edges = []
        self.id = id
        # self.distance = 0
        self.minute = float('inf')

        # for traversal 
        self.discovered = False
        self.visited = False
        self.previous = None

        # true_destination and true_source are only applicable for the solulu trees and its teleporting destination 
        self.true_destination = None 
        self.true_source = None

   
    def add_edge(self, edge):

        # constant operation 
        
        self.edges.append(edge)

    def added_to_discovered(self):
        # constant operaiton, to indicate a vertex is being added into the minheap 

        self.discovered = True

    def visited_node(self):

        # constant operaiton, indicating a vertex is visited and the minute travel to from the source is finalised
        self.visited = True

    def get_minutes(self):

        # constant operation
        return self.minute

class Edge:
      
    def __init__(self, u, v, w):
        """
        Function description: a function to create an Edge with vertices u and v and weight w

        Input: a list of edges E, where each edge is a tuple of u, v, and w (u, v, w)

        Output, return or postcondition: return an edge from u to v with weight w created in class Edge

        Time complexity: O(1) 

        Time complexity analysis: linear operation in this function

        Space complexity: O(1)

        Space complexity analysis: constant space complexity
        """
        self.u = u
        self.v = v
        self.w = w
    
class TreeMap:

    def __init__(self, roads, solulus):

        """
        Function description: a function to create a Treemap using classes Graph, Vertex, and Edge

        Approach description (if main function): create a Treemap by treating each tree as a vertex and each road as an edge, 
        and the graph is directed, the Graph class uses adjancency list to create the graph. In order to better solve the task, 
        I have created a flipped version of the original Treemap, where the direction of the edges is flipped. This is because my approach 
        to the solution is to run Dijskra once on the original graph(self.tree), where the source is the starting tree, and then run Dijskra
        once on the flipped graph(self.flip), where the source is the destination tree. This approach requires two runs of Dijskra, once each 
        in the original and flipped graph, and then combine the results to find the shortest path. In order to represent the solulu trees, I have 
        also decided to uses dummy vertices to represent the solulu trees, the dummy vertices are added to the end of the vertices list, the id of
        them are based on the already exsiting vertices, where the id of the dummy vertices are from maximum + 1 to maximum + len(solulus) and the 
        road connecting solulu trees with the dummy vertices will be the time taken in order to destroy the solulu tree. Then I have also flagged 
        out the true_destination and true_source of the dummy vertices in both versions of the TreeMap, it is then later used to find out the shortest paths. 

        Input: a list of roads and a list of solulus, where the list of roads is actually a list of edges used in graph creation, 
        the list of solulus is a list of vertices that are solulu trees

        Output, return or postcondition: return a Treemap as a graph by connecting each tree(vertex) according to the list of roads(edges), this 
        TreeMap is then named self.tree, self.tree will have |S| number of dummy vertices in order to represent the solulu tree. These dummy vertices 
        are connected with the original solulu tree with the minute it takes to destroy the representing solulu tree. Then create a flipped version
        of the original TreeMap, where the direction of the edges is flipped, this TreeMap is then named self.flip.

        Time complexity: O(|T|) + O(|R|)

        Time complexity analysis:  

        Inherently from the time complexity in class Graph, to go through the list of trees (vertices) |T|, required O(|T|) where the 
        length of the list is |T|, this can be seen as buliding a Graph with |T| vertices. Then to connect all (trees)vertices with all
        roads(edges) |R|, it will takes O(|R|) where |R| is the number of roads(edges). Combining both yields O(|T| + |R|). Since we are creating 
        two graph, hence the time complexity is O(2|T| + 2|R|). Ignoring constants gives us O(|T| + |R|). Since I have also included extra dummy vertices 
        in both TreeMap, where the number of the dummy vertices in the normal version of TreeMap self.tree can be as many as |T| if all trees are also 
        solulu tree, hence the vertices for the self.tree will be O(2|T|), worst case happens when all trees are also solulu trees, hence |T| + |T| = 2|T|.
        Then to connect solulu trees with their dummy vertices also require |S| edges, but since |S| is bounded by |T|, hence the time complexity is O(|T|).

        Until now the worst case time complexity of self.tree would be: O(|T| + |R|) + O(2|T|) + O(|T|) = O(4|T| + |R|). Ignoring constants gives us O(|T| + |R|).

        Then for the self.flip, my approach requires adding a single dummy vertex and treat this dummy vertex as the source by connecting it to all the possible exits 
        in the graph. This approach is aim to only run Dijsktra once on the self.flip while also enable the finding of the minute taken to travel from dummy vertex
        to all other trees. Hence buidling up a treemap with self.vertices(V) + a single dummy vertices requires O(T|| + 1), then connecting the already existing vertices 
        but in a flip manner yields another O(|R|). 

        Hence from the above, we can see that in creaitng self.flip will require O(|T| + 1 + |R|) = O(|T| + 1 + |R|). Ignoring constants gives us O(|T| + |R|).
         
        In the code below, to find the maximum tree(vertex) involves looping through all roads(edges) once to get the maximum tree(vertex).
        This yields a time complexity of O(|R|) where |R| is the number of roads. Below adding roads(edges) to each tree(vertex) contirbute 
        O(|R|), because all roads are to go through once to connect two trees. 

        By combining all the above, O(2|T| + 2|R|) + O(|T|). Ignoring constants gives us O(|T| + |R|).

        Space complexity: O(|T|+|R|), where |T| is the number of trees and |R| is the number of roads  

        Space complexity analysis: 

        Inherently from space complexity in class Graph, the space complexity is O(V), where we first establish a list of V vertices. 
        Then we called add_edge to connect all roads(edges) where E is the number of edges. By combining O(V) and O(E) we get O(V + E).
        By substituting V with |T| and E with |R|, we get the complexity of O(|T|+|R|). Creating a list of all (trees)vertices takes |T| 
        space, while connecting all roads(edges) between (trees)vertices takes |R| space. Adjancency list is used to create the graph 
        rather than using adjacency matrix is because in the assignment specification, states the number of |R| can be significantly 
        smaller than |T|, hence we can't assume the graph to be dense, So adjacency list is a better option. It is also notable that although 
        my approach requires the adding dummy vertices into self.tree where the number of the dummy vertices can be as many as |T| if all trees 
        are also solulu trees. Which in the sense of creating the graph, we essentially have 2|T| vertices where |T| original vertices and another 
        |T| dummy vertices. And to connect solulu trees with their dummy vertices also require |T| edges. Hence the space complexity is O(2|T| + |R|).
        graphs, hence the space complexity is O(2|T| + 2|R|). Ignoring constants gives us O(|T| + |R|). After creating self.tree where the graph is normal 
        and unflipped, we have used up a space complexity of O(|T| + |R|). Then for the self.flip, my approach requires adding a single dummy vertex 
        so the number of vertices in self.flip will be |T| + 1. Then connect the trees{vertices} with their original roads but in a flipped manner 
        requires O(|R|), until here the space complexity would be O(|T| + 1 + |R|). Ignoring constants gives us O(|T| + |R|).
        
        By combining the space used in self.tree and self.flip we can see that the total space complexity would be O(2|T| + 2|R|), where ingoring constants 
        yields O(|T| + |R|).  
        """

        # the vertices always start with 0 until V-1 
        # we only need to identify the largest vertex
        self.maximum = 0
        self.solulu_destination = []
        
        # complexity = O(|R|), where R is the set of roads 
        for road in roads: 
            if road[0] > self.maximum:
                self.maximum = road[0]
            if road[1] > self.maximum:
                self.maximum = road[1]

        # now we have the range of vertices, from minimum to maximum, create the graph 
        # range is exclusive, so we add 1, and the range will be from 0 to maximum
        # yields O(|T| + |R|)

        # the normal version of the TreeMap

        # creating dummy vertices to represent the solulu trees
        # the dummy vertices are added to the end of the vertices list, the id of the dummy vertices are from maximum + 1 
        # to maximum + len(solulus). Since we are also adding new edges from each solulu tree to their representing dummy vertices, 
        # hence here will yield time complexity of O(|S|) where |S| is the number of solulu trees. But since |S| is bounded by |T|, 
        # hence the worst case happens when |S| == |T|, the time complexity will then be O(|T|)
        self.tree = Graph(range(self.maximum + len(solulus) + 1))

        # the flipped version of the TreeMap
        self.flip = Graph(range(self.maximum + 2))

        # now self.tree has all the vertices, we can add the edges
        # setting False to indicate that the graph is unflipped, hence the direction of the edges is the same as the roads
        # complexity is O(|R|), where R is the set of roads
        self.tree.add_edge(roads, False)

        # now we add the solulu trees to the graph
        for i in range(len(solulus)):
            
            # connecting the solulu trees to the dummy vertices, worst case happenes when all trees are also solulu trees
            # hence we require |T| dummy vertices to represent the solulu trees, hence the time complexity is O(|T|)
            self.tree.vertices[solulus[i][0]].add_edge(Edge(solulus[i][0], self.maximum + i + 1, solulus[i][1]))

            # setting the true_destination of the dummy vertices to the destination of the solulu trees, is it then used in the escape()
            # when we are finding the shortest path from the source to the destination
            self.tree.vertices[self.maximum + i + 1].true_destination = solulus[i][2]

            # setting the true_source of the dummy vertices to the source of the solulu trees, is it then used in the escape() when we are 
            # finding the shortest path from the source to the destination
            self.flip.vertices[solulus[i][2]].true_source = solulus[i][2]

        # this is where we add in the edges into self.flip in a reverse manner 
        self.flip.add_edge(roads, True)

    def escape(self, start, exits):
        """
        Function description: a function to find the path with the smallest minute used to escape the forest from the start to one of the exits 
        by destroying one of the solulus. 

        Approach description (if main function): In order to exit the forest, my approach requires two graphs. The first one is the normal version 
        self.tree where the roads are connected in the original direction, and the second one is the flipped version self.flip where the roads are
        connected in the reverse direction. Then from self.tree, I aim to find the minute taken to travel to all the dummy vertices connected to their 
        representing solulu trees, including the time taken to destroy the solulu trees, from the starting tree. After running Dijkstra in self.tree, 
        we would have all the optimal minute taken to travel from start to all dummy vertices. Then we store the minute values from start to all dummy 
        vertices inside a list called start_to_solulu. Then in start_to_solulu, I sort the list based the true_destination in increasing order, which is 
        essentially sorting start_to_solulu in a manner where the teleporting destination is being sorted in an increasing manner. This will help in later 
        when we are connecting both self.tree and self.flip based their solulu trees and the destination trees they teleport to. Then I find the maximum_in_solulu
        tree(id) in start_to_solulu, and create a list called solulu_destination that are based on maximum_in_solulu + 1. the list solulu_destination is used to 
        store the smallest minutes yields for travelling to the dummy vertices from the start. solulu_destination will have None as the default values for all of its 
        elements. But if there exist at least one valid teleportation, then solulu_destination[index] will be updated. The purpose of it is to prevent when 
        there are multiple possible solulu trees that are connected to the same dummy vertex, which means that after destroying two different solulu trees, both 
        scenarios ended up in the same dummy vertex. Hence we use solulu_destination to filter out the larger minute, only left with the smallest. We then check the 
        solulu_destination, if it is not None, we add it into final_unique_solulu_destination. 
        
        Then for self.flip, I start with connecting the single dummy vertex in self.flip to all exits given in the input with a minute of 0. This is aim 
        to only run Dijkstra once to get the optimal minute from dummy vertex to all exits. Then we Then we run Dijkstra in self.flip, where the source is
        the dummy vertex. After running the Dijkstra in self.flip, we would have all the optimal minute taken to travel from the dummy vertex to all exits.
        But the only relevant vertices are the exits, which is being flagged by the true_source in the vertices. If the vertex has value other than None in the
        true_source attribute, we add it into exit_to_solulu.

        Then we add both the minute from start to all dummy vertices and the minute from dummy vertex to all exits together, and find the smallest pair. After getting t
        the smallest pair, we then find the shortest path from the start to the dummy vertex and from the dummy vertex to the exit. We then store the path in raw, then we 
        refine the raw[] by checking if there's any duplicate vertices, if there is, we remove the duplicates. Then we return the minute and the path. Porblem solved. 


        Input: a start vertex id, and a list of exits, where the exits are the trees that we can exit the forest

        Output, return or postcondition: return a tuple of the smallest minute used to escape the forest from the start to one of the exits by destroying one solulu tree, 
        and the path taken to escape the forest. If there is no possible way to escape the forest, return None. 

        Time complexity: O(|T| + |R|) 

        Time complexity analysis: O(|T|) + O(|T| + |R|) + O(|T|log|T|) + O(|T|) +O(|T|) + O(|T|) + O(|T|) + O(|T|) + O(|T| + |R|) + O(|T|) + O(|T|) + O(|T|) + O(|T|) + O(|T|) + 
        O(|T|) + O(|T|) + O(|T|) + O(|T|) ==> O(18|T| + |R|) ==> O(|T| + |R|)  

        I have documented down the part which contributes to the complexity below in comment format. Please refer to the comment for more information.

        Space complexity: O(|T|)

        Space complexity analysis: O(|T|) + O(|T|) + O(|T|) + O(|T|) + O(|T|) + O(|T|) + O(|T|) + O(|T|) + O(|T|) + O(|T|) + O(|T|) + O(|T|) = O(12|T|) ==> O(|T|)
        
        I have documented down the part which contributes to the complexity below in comment format. Please refer to the comment for more information.

        """

        # this is where we reset the the dummy vertex in self.flip to have no edges,
        # because we are going to connect the dummy vertex to all exits with a minute of 0
        # each run of the escape might require different exits, hence whenever we run escape, 
        # we need to reset the edges of the dummy vertex in self.flip back to []
        self.flip.vertices[-1].edges = []

        self.solulu_destination = [] 

        exit_to_solulu = []
        start_to_solulu = []
        shortest_path_first_half = []
        shortest_path_second_half = []

        # start = self.tree.vertices[start]

        # this is where we add the edges from the dummy vertex to all exits with a minute of 0
        # this yields complexity of O(|E|), where E is the set of exits, but since E is bounded by 
        # T where T is the number of trees, hence the time complexity is O(|T|)
        # space complexity: since we are adding the edges to the dummy vertex, hence the space complexity is O(|T|)
        # because it happens when all trees are also solulu trees, hence we require |T| edges to connect the dummy 
        # vertices to the exits

        for exit in exits:
            self.flip.vertices[-1].add_edge(Edge(len(self.flip.vertices)-1, exit, 0))

        # run Dijkstra on the normal version of the TreeMap from the start
        # time complexity is O(|T| + |R|), where T is the number of trees and R is the number of roads
        # space complexity is O(|T|), where T is the number of trees
        # we require |T| vertices in the heap, hence the space complexity is O(|T|)
        self.tree.dijkstra(start)

        # store the minute from start to all dummy vertices in start_to_solulu
        # since we are only interested in the dummy vertices, the time complexity here 
        # is O(|E|),  but since E is bounded by T, hence O(|T|), where T is the number of trees
        # space complexity is O(|T|), where T is the number of trees
        for i in range(self.maximum + 1, len(self.tree.vertices)):
            start_to_solulu.append((i, self.tree.vertices[i].true_destination, self.tree.vertices[i].minute))
        
        # since i am using the build-in sorting function in python
        # the complexity is O(|T|log|T|), where T is the number of trees
        start_to_solulu.sort(key=lambda x: x[1])

        # find the maximum_in_solulu, aka the largest tree(vertex) in start_to_solulu
        # complexity is O(|T|), where T is the number of trees
        maximum_in_solulu = 0

        for i in range(len(start_to_solulu)):
            if start_to_solulu[i][1] > maximum_in_solulu:
                maximum_in_solulu = start_to_solulu[i][1]

        # initialsing a list of solulu_destination with None as the default value
        # complexity is O(|T|), where T is the number of trees
        # space complexity is O(|T|), where T is the number of trees
        self.solulu_destination = [None] * (maximum_in_solulu + 1)

        # store the smallest minute from start to all dummy vertices in solulu_destination
        # if there are multiple possible solulu trees that are connected to the same dummy vertex,
        # then we only store the smallest minute, hence the time complexity is O(|T|)
        for i in range(len(start_to_solulu)):
            if self.solulu_destination[start_to_solulu[i][1]] == None:
                self.solulu_destination[start_to_solulu[i][1]] = start_to_solulu[i]

            elif self.solulu_destination[start_to_solulu[i][1]] != None:
                if self.solulu_destination[start_to_solulu[i][1]][2] > start_to_solulu[i][2]:
                    self.solulu_destination[start_to_solulu[i][1]] = start_to_solulu[i]
        
        # initialise a list of final_unique_solulu_destination
        final_unique_solulu_destination = []

        # filter out the None in solulu_destination
        # time complexity is O(|T|), where T is the number of trees
        # space complexity is O(|T|), where T is the number of trees
        for i in self.solulu_destination:
            if i != None:
                final_unique_solulu_destination.append(i)
        
        # running Dijskrta on the flipped version of the TreeMap from the dummy vertex
        # this yields time complexity of O(|T| + 1 + |R|), where T is the number of trees and R is the number of roads
        # Ignoring constants gives us O(|T| + |R|)
        # space complexity is O(|T|), where T is the number of trees
        self.flip.dijkstra(len(self.flip.vertices) - 1)

        # if the vertex has value other than None in the true_source attribute, we add it into exit_to_solulu
        # because it implies that it is a valid teleportation.
        # the time complexity is O(|T|), where T is the number of trees
        # space complexity is O(|T|), where T is the number of trees
        for i in range(len(self.flip.vertices)):
            if self.flip.vertices[i].true_source != None:
                exit_to_solulu.append((self.flip.vertices[i].id, self.flip.vertices[i].minute))

        # add the minute from the start to the dummy vertices and the minute from the dummy vertices to the exits together
        # the time complexity is O(|T|), where T is the number of trees
        for i in range(len(final_unique_solulu_destination)):

            final_unique_solulu_destination[i] = (final_unique_solulu_destination[i][0], final_unique_solulu_destination[i][1], final_unique_solulu_destination[i][2] + exit_to_solulu[i][1])

        # find the smallest pair that has the smallest minute taken to travel from the start to one of the exits
        smallest_pair = final_unique_solulu_destination[0]
        
        # time complexity is O(|T|), where T is the number of trees
        for i in range(1, len(final_unique_solulu_destination)):
            if final_unique_solulu_destination[i][2] < smallest_pair[2]:
                smallest_pair = final_unique_solulu_destination[i]
        
        # terminate earlier if there is no possible way to escape the forest
        # implies by the smallest_pair[2] == float('inf')
        if smallest_pair[2] == float('inf'):
            return None
        
        # if there is a possible way to escape the forest, then we find the shortest path from the start to the dummy vertex
        start_to_solulu_index = smallest_pair[0]
        start_to_solulu_index = self.tree.vertices[start_to_solulu_index].previous.id

        # while start_to_solulu_index != start:
        # doing backtracking to find the shortest path from the start to the smallest dummy vertex
        # by using vertex.previous.id
        # time complexity is O(|T|), where T is the number of trees
        # space complexity is O(|T|), where T is the number of trees
        while self.tree.vertices[start_to_solulu_index].previous != None:
            shortest_path_first_half.append(start_to_solulu_index)
            start_to_solulu_index = self.tree.vertices[start_to_solulu_index].previous.id

        # if the start_to_solulu_index is the start, then we add it into the shortest_path_first_half
        if start_to_solulu_index == start:
            shortest_path_first_half.append(start_to_solulu_index)

        # reversing the shortest_path_first_half, time complexity is O(|T|), where T is the number of trees
        shortest_path_first_half.reverse()

        # find the shortest path from the dummy vertex to the exit
        exit_to_solulu_index = smallest_pair[1]

        # doing backtracking to find the shortest path from the dummy vertex to the smallest exit
        # by using vertex.previous.id
        # time complexity is O(|T|), where T is the number of trees
        # space complexity is O(|T|), where T is the number of trees
        while self.flip.vertices[exit_to_solulu_index].previous != None:

            shortest_path_second_half.append(exit_to_solulu_index)
            exit_to_solulu_index = self.flip.vertices[exit_to_solulu_index].previous.id

        # building a raw path by simple doing concatenation of lists by connecting the start, 
        # shortest_path_first_half and shortest_path_second_half
        # time complexity is O(|T|), where T is the number of trees
        # space complexity is O(|T|), where T is the number of trees
        raw = [start] + shortest_path_first_half + shortest_path_second_half

        # initialise a list of refined with None as the default value
        # time complexity is O(|T|), where T is the number of trees
        # space complexity is O(|T|), where T is the number of trees
        refined = [None] * len(raw)

        # initialise a list of refined_double
        refined_double = []

        # remove the duplicate vertices in the raw path
        # time complexity is O(|T|), where T is the number of trees
        for i in range(len(raw) - 1):
            if raw[i] != raw[i+1]:
                refined[i] = raw[i]
        
        # add the last element in the raw path into refined
        # because it is not inclusive in above loop
        refined.append(raw[-1])

        # remove the None in the refined
        # time complexity is O(|T|), where T is the number of trees
        # space complexity is O(|T|), where T is the number of trees
        for j in range(len(refined)):
            if refined[j] != None:
                refined_double.append(refined[j])
        
        # if smallest_pair[2] is not infinity, then we return the smallest_pair[2] and refined_double
        if smallest_pair[2] != float('inf'):
            
            return (smallest_pair[2], refined_double)
    
        # if there is no possible way to escape the forest, then we return None
        return None
                
class MinHeap: 

    """
    This version of MinHeap is adapted from MaxHeap in the lecture notes from FIT1008. The main difference is that the heap 
    is a min heap, where the priority of sorting is based on the smallest minute value rather than largest. A mapping array is 
    included in order to keep track of the index of each tree(vertex) in the heap. Update function is also devised in order to 
    update the vertices in the minheap along the way of doing dijkstra
    """

    def __init__(self, argv_lst):

        """
        Function description: a function to create a MinHeap using a list of trees (vertices)

        Approach description (if main function): input is a list of (Trees) Vertices, creating a heap of size len(argv_lst) + 1, then use
        build_min_heap to build the heap by inserting all (trees)vertices into the heap

        Input: a list of Vertices(Trees) argv_lst
       
        Output, return or postcondition: return a MinHeap with a list of Vertices(Trees)

        Time complexity: O(|T|)

        Time complexity analysis: 
        
        Initialise the an empty MinHeap with a size of len(argv_lst) + 1, which is O(|T| + 1), where |T| is the length of the argv_lst,
        also can be read as the number of trees(vertices). Then initialising a mapping array of size O(|T|) as well where |T| is the number 
        of trees(vertices). Hence it would be O(|T| + 1) + O(|T|) = O(|T|). Since big O notation ignores constants. 

        Space complexity: O(|T|)

        Space complexity analysis: since we need an array of size |T| + 1 to store all the trees(vertices) in order to represent the heap,
        hence we have an auxiliary space of O(|T| + 1). While we also need another array called mapping array to keep track of the index of
        each tree(vertex) in the heap, hence we have another auxiliary space of O(|T|). By combining both, we get O(|T| + 1) + O(|T|) = O(|T|).
        Since Big O ignores constants, we can simplify it to O(|T|).

        """

        self.length = 0 

        # this is where we initialise a list of None with the size of len(argv_lst) + 1, yields time complexity O(|T|) where T 
        # is the number of trees (vertices), since it is used to represent the heap, space complexity is O(|T|) as well since 
        # we need a list of size |T| to represent all (trees)vertices

        self.heap = [None] * (len(argv_lst) + 1)

        # this is where we initialise a list of None with the size of len(argv_lst), yields time complexity O(|T|) where T is the
        # number of trres (vertices). This mapping array is used to keep track of the index of each tree(vertex) in the heap whenever
        # a sussessful rise/sink operation is performed

        # time complexity = O(|T|), going through the whole list of trees(vertices) to initialise the mapping array
        # space complexity = O(|T|), need a list of size |T| to represent all vertices 
        self.mapping_array = [None] * (len(argv_lst))

    def __len__(self):

        # constant operation
        # return the lenth of the minheap

        return self.length
    
    def is_full(self):

        # check if the minheap is full 

        # constant operation 

        return self.length + 1 == len(self.heap)    
    
    def rise(self, index):

        """
        Function description: a function to rise a tree(vertex) to the correct position in the heap

        Approach description (if main function): input is a tree(vertex) index, if the tree(vertex) minute is smaller than the parent then 
        we rise it up recursively until it is at the correct position. The relationship of the children and the parent nodes is when children 
        node is index[i], parent node will be (index - 1) // 2

        Input: an index of a tree(vertex) in the heap
       
        Output, return or postcondition: return a MinHeap with a list of Vertices(Trees) in correct order of a MinHeap

        Time complexity: O(log|T|)

        Time complexity analysis: 
        
        Since we are using a heap, by traversing the heap, time complexity will be O(log|T|), where T is the number of trees(vertices)
        worst case time complexity = O(log|T|),happens when the last tree.minute we added in is the smallest out of all the item.minute 
        in the heap, hence we need to rise for a total height of log|T| to get the smallest item.minute to the top of the heap

        Space complexity: O(1)

        Space complexity analysis: requires only constant space complexity

        """

        if index == 0:
            return 

        parent = (index - 1) // 2

        # check if the child node's minute is smaller than the parent node's minute 
        # if smaller, we perform rise since smaller minute is our priority 
        # while arranging the minheap order, it is also crucial to update the mapping array 

        if self.heap[index].minute < self.heap[parent].minute:

            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.mapping_array[self.heap[index].id], self.mapping_array[self.heap[parent].id] = self.mapping_array[self.heap[parent].id], self.mapping_array[self.heap[index].id]
            self.rise(parent)

    def sink(self, index):
            
        """
        Function description: a function to sink a tree(vertex) to the correct position in the heap

        Approach description (if main function): input is a tree(vertex) index, if the tree(vertex) minute is larger than the children then
        we sink it down recursively until it is at the correct position. By treating the input index as the smallest minute currently, and compare 
        with the child nodes of index, if one of them is larger then we swap the position of the parent and the smaller child node. Keep on repeating 
        until all are in correct position. 

        Input: an index of a tree(vertex) in the heap
       
        Output, return or postcondition: return a MinHeap with a list of Vertices(Trees) in correct order of a MinHeap

        Time complexity: O(log|T|)

        Time complexity analysis: 
        
        Since we are using a heap, by traversing the heap, time complexity will be O(log|T|), where T is the number of trees(vertices)
        worst case time complexity = O(log|T|),happens when the root of the heap has the largest tree.minute value out of all the tree.minute,
        hence we need to sink all the way to the bottom of the heap with a height of log|T| to get the largest tree.minute to the correct 
        position in order to maintain the correct order of a MinHeap.

        Space complexity: O(1)

        Space complexity analysis: requires only constant space complexity
        """
        
        # since in the heap, one node can have up to two child nodes, we can see them one as the left child and another is the right child 
        left_child = 2 * index + 1
        right_child = 2 * index + 2
    
        smallest = index
        
        # if the left child has smaller minute, we swap the value between smallest and left_child 
        if left_child < self.length and self.heap[left_child].minute < self.heap[smallest].minute:
            smallest = left_child

        # if the right child has smaller minute, we swap the value between smallest and right_child 
        if right_child < self.length and self.heap[right_child].minute < self.heap[smallest].minute:
            smallest = right_child
                
        # if after the above, and the smallest != the index, we can confirm that the minheap is not in correct position 
        # hence we can perform swapping, while swapping is occuring in minheap, it is also crucial to update the arrangement 
        # of the mapping array 

        if smallest != index: 
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.mapping_array[self.heap[index].id], self.mapping_array[self.heap[smallest].id] = self.mapping_array[self.heap[smallest].id], self.mapping_array[self.heap[index].id]
            self.sink(smallest)

    def serve(self):

        """
        Function description: a function to serve the tree(root) with the smallest minute in the heap

        Approach description (if main function): swap the root with the last tree(vertex) in the heap, then sink the root to the correct
        position by calling sink(0), then return the last tree(vertex) in the heap and decrese the length of the heap by 1

        Input: None
       
        Output, return or postcondition: return the tree(vertex) with the smallest minute in the heap

        Time complexity: O(log|T|)

        Time complexity analysis: 
        
        Swapping the root with the last tree(vertex) in the heap is a constant time operation, then we need to sink the root to the correct
        position by calling sink(0), inhenrently from the time complexity of sink, it is O(log|T|), where T is the number of trees(vertices)
        in which the worst case time complexity happens when the root of the heap has the largest tree.minute value out of all the tree.minute,
        hence we have to travesrse the heap all the way from the root to the bottom with a height of log|T| to position the largest tree.minute
        Hence O(1) + O(log|T|) = O(log|T|)

        Space complexity: O(1)

        Space complexity analysis: requires only constant space complexity

        """

        if self.length == 0:
            return None

        # decreasing the length by 1 because we are going to serve out the last item in the minheap 
        # swapping the root with the last item 
        # update the mapping array
        self.length -= 1
        self.heap[0], self.heap[self.length] = self.heap[self.length], self.heap[0]
        self.mapping_array[self.heap[self.length].id], self.mapping_array[self.heap[0].id] = self.mapping_array[self.heap[0].id], self.mapping_array[self.heap[self.length].id]

        # sinking index 0 that just being swapped up from the above
        self.sink(0)

        # setting the node as visited in the heap so that we know it's minute is finalised 
        self.heap[self.length].visited_node()

        return self.heap[self.length]
    
    def insert(self, vertex):

        # input: a Vertex object
        # output: a boolean value, True if the vertex is successfully added into the heap, False if the heap is full
        # time complexity: O(log|T|), where T is the number of trees(vertices). Worst case time complexity happens when 
        # the last tree.minute we added in is the smallest out of all the item.minute in the heap, hence we need to rise 
        # all the way to the root for a height of log|T| to get the smallest item.minute to the top of the heap
        # hence the time complexity is O(log|T|)

        """
        Function description: a function to insert a vertex into the heap

        Approach description (if main function): by setting the vertex into the last position of the heap, then rise the vertex to the
        appropriate position by calling rise, and increase the length of the heap by 1 

        Input: a Vertex/(Tree) object
       
        Output, return or postcondition: return True when the vertex(tree) is correctly inserted, return False when the heap is full

        Time complexity: O(log|T|)

        Time complexity analysis: 
        
        Setting the vertex into the last position of the heap is a constant time operation, then we need to rise the vertex to the
        appropriate position by calling rise, inhenrently from the time complexity of rise, it is O(log|T|), where T is the number of
        trees(vertices) in which the worst case time complexity happens when the last tree.minute we added in is the smallest out of all
        exsiting tree.minute in the heap, hence we need to rise all the way to the root for a height of log|T| to set the smallest 
        tree.minute to the top of the heap. Hence O(1) + O(log|T|) = O(log|T|)

        Space complexity: O(1)

        Space complexity analysis: requires only constant space complexity

        """

        # if the heap is full then return False 
        if self.is_full():
            return False

        self.heap[self.length] = (vertex)
        self.mapping_array[vertex.id] = self.length
        self.rise(self.length)
        self.length += 1

        return True
    
    def update(self, vertex, minute):
        """
        Function description: a function to update the minute of a vertex in the heap

        Approach description (if main function): first find the index of the vertex in the heap by using the mapping array, then update
        the minute of the vertex, then rise the vertex to the appropriate position by calling rise, and sink the vertex to the appropriate
        position by calling sink

        Input: a Vertex/(Tree) object, an integer minute
       
        Output, return or postcondition: return None, but the input vertex will be updated with the input minute

        Time complexity: O(log|T|)

        Time complexity analysis: 
        
        Finding the index of the vertex in the heap by using the mapping array is a constant time operation, then updating the minute of
        the vertex is a constant time operation, then we need to rise the vertex to the appropriate position by calling rise, and sink the
        vertex to the appropriate position by calling sink, inhenrently from the time complexity of rise and sink, it is O(log|T|), where T
        is the number of trees(vertices) in which the worst case time complexity happens when the vertex we updated has the smallest/largest
        minute and also at the last/root of the heap, hence we have to travese a height of log|T| in order to get it to the appropriate position. 

        Space complexity: O(1)

        Space complexity analysis: requires only constant space complexity

        """

        # finding the index of the input vertex by manipulating the mapping_array
        index = self.mapping_array[vertex.id]
        self.heap[index].minute = minute
        self.rise(index)
        self.sink(index)
        
    def build_min_heap(self, argv_lst):
        """
        Function description: a function to build a minheap by inserting the vertex on by one

        Approach description (if main function): for the input list, loop through the list and insert the item

        Input: a list of vertives 
       
        Output, return or postcondition: return None, but we will have a minheap built with input argv_lst

        time complexity: O(|T|log|T|)
        
        time complexity analysis: 
        
        O(|T|) where |T| is the number of trees(vertices). No matter what we are to go through |T| times to insert all the 
        trees(vertices) into the heap, hence the time complexity is hyO(|T|). Then for each insertion, we need to rise to the
        correct position, which is O(log|T|) inherented from function insert(vertex), hence the time complexity is O(|T|log|T|)

        space complexity : constant operation without additional space. Hence O(1)

        """
        for vertex in argv_lst:
            # self.insert(vertex)
            self.insert(vertex)
        