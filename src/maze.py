from graph import Graph

class Maze:
    def __init__(self, size):
        self.size = size
        self.nodes = []
        self.graph = Graph(size*size)

        # label the nodes from 0 to (N*N)-1
        for i in range(0, self.size):
            self.nodes.append([])
            for j in range(0, self.size):
                self.nodes[i].append(i*self.size + j)

        # each node in the graph is connected to UP, DOWN, LEFT, RIGHT (if they exist)
        for i in range(0, self.size):
            for j in range(0, self.size):
                node = self.nodes[i][j]
                if i > 0:
                    up = self.nodes[i-1][j]
                    self.graph.add_edge(node, up)
                if i < self.size-1:
                    down = self.nodes[i+1][j]
                    self.graph.add_edge(node, down)
                if j > 0:
                    left = self.nodes[i][j-1]
                    self.graph.add_edge(node, left)
                if j < self.size-1:
                    right = self.nodes[i][j+1]
                    self.graph.add_edge(node, right)
    
    def generate_maze(self):
        spanning_tree = self.graph.get_spanning_tree(0)
        for i in range(0, self.graph.num_nodes):
            for j in range(0, self.graph.num_nodes):
                if spanning_tree.has_edge(i, j):
                    self.graph.remove_edge(i, j);
                    
    def print(self):
        result = ' '+('_ ' * (self.size-1))+'_\n'
        for i in range(self.size):
            result+='|'
            for j in range(self.size):
                node = self.nodes[i][j]
                # check the floor (bottom wall)
                if i < self.size-1 and self.graph.has_edge(node, self.nodes[i+1][j]):
                    result+='_'
                elif (i == self.size-1):
                    result+='_'
                else:
                    result+=' '

                # check the right wall
                if j < self.size-1 and self.graph.has_edge(node, self.nodes[i][j+1]):
                    result+='|'
                elif i < self.size-1 and j < self.size-1:
                    result+=' '
                elif i == self.size-1 and j < self.size-1:
                    result+='_'
            result+='|\n'
        print(result)

