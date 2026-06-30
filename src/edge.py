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