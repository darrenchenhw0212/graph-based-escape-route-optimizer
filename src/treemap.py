from .graph import Graph
from .edge import Edge

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
                