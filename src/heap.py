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
        