"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("There is no such vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise IndexError("There is no such vertex")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # print('*** bft ***')
        q = Queue()
        visited = set()
        # queue up the starting vertex
        q.enqueue(starting_vertex)
        
        while q.size() > 0:
            # dequeue the vertex
            vertex = q.dequeue()
            if vertex not in visited:
                # mark it as visited
                visited.add(vertex)
                
                # do something with the vertex
                print(vertex)
                
                # add the vertexe's neighbors to the queue
                neighbors = self.get_neighbors(vertex)
                for neighbor in neighbors:
                    q.enqueue(neighbor)
            
        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # print('*** dft ***')
        stack = Stack()
        visited = set()
        
        # add the first item to the stack
        stack.push(starting_vertex)
        
        while stack.size() > 0:
            vertex = stack.pop()
            
            if vertex not in visited:
            
                # do something with this vertex
                print(vertex)
                
                # add vertex to visited
                visited.add(vertex)
                
                # add all the vertex's neighbors to the stack
                neighbors = self.get_neighbors(vertex)
                for neighbor in neighbors:
                    stack.push(neighbor)
        

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        
        if starting_vertex in visited:
            return
        
        # add this to visited
        visited.add(starting_vertex)
        
        # do something with this vertex
        print(starting_vertex)
        
        # start by getting this vertex's neighbors
        neighbors = self.get_neighbors(starting_vertex)
        
        if len(neighbors) > 0:
            for neighbor in neighbors:
                self.dft_recursive(neighbor, visited)
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue of paths
        paths = Queue()
        # store the visited vertexes
        visited = set()
        # queue up the starting vertex
        paths.enqueue([starting_vertex])
        
        while paths.size() > 0:
            # dequeue the the path
            path = paths.dequeue()
            # grab the last vertex in the path
            vertex = path[-1]
            if vertex not in visited:
                # mark it as visited
                visited.add(vertex)
                if vertex == destination_vertex:
                    return path
                
                # add the vertex's neighbors to the queue
                neighbors = self.get_neighbors(vertex)
                for neighbor in neighbors:
                    # if you don't copy, it will just reference
                    # the same list
                    copied_path = list(path)
                    
                    copied_path.append(neighbor)
                    paths.enqueue(copied_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        paths = Stack()
        visited = set()
        
        # add the first item to the stack
        paths.push([starting_vertex])
        
        while paths.size() > 0:
            path = paths.pop()
            
            # grab the last vertex off the path
            vertex = path[-1]
            
            if vertex not in visited:
                
                # add vertex to visited
                visited.add(vertex)
                
                if vertex == destination_vertex:
                    return path
                
                # add all the vertex's neighbors to the stack
                neighbors = self.get_neighbors(vertex)
                for neighbor in neighbors:
                    # create a copy of the path
                    copied_path = list(path)
                    copied_path.append(neighbor)
                    paths.push(copied_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
            
        if path is None:
            path = []
            
        # make a copy of the path
        # so the recursion doesn't write
        # everything to the same path
        copy_path = list(path)
        
        if starting_vertex not in visited:
        
            # add this to visited
            visited.add(starting_vertex)
            copy_path.append(starting_vertex)
            
            # do something with this vertex
            if starting_vertex == destination_vertex:
                return copy_path
            
            # start by getting this vertex's neighbors
            neighbors = self.get_neighbors(starting_vertex)
            
            # if vertex has neighbors,
            for neighbor in neighbors:
                # recurse over each neighbor
                recurse_path = self.dfs_recursive(neighbor, destination_vertex, visited, copy_path)
                if recurse_path:
                    return recurse_path
        
        return None
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    # graph.add_vertex(1)
    # graph.add_vertex(2)
    # graph.add_vertex(3)
    # graph.add_vertex(6)
    # graph.add_vertex(4)
    # graph.add_vertex(5)
    # graph.add_vertex(7)
    # graph.add_vertex(8)
    
    # graph.add_edge(1, 2)
    # graph.add_edge(2, 3)
    # graph.add_edge(3, 6)
    # graph.add_edge(2, 4)
    # graph.add_edge(4, 5)
    # graph.add_edge(4, 7)
    # graph.add_edge(7, 6)
    # graph.add_edge(6, 8)
    # graph.add_edge(2, 8)
    
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    #print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    #graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    #graph.dft(1)
    #print('*** dft_reversive ***')
    #graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    #print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
    # print(graph.dfs(1, 8))
    # print(graph.dfs_recursive(1, 8))
