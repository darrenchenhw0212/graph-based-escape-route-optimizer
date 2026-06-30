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