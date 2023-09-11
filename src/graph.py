import random

class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graph = {}
        
    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
    
    def remove_edge(self, u, v):
        if u in self.graph:
            if v in self.graph[u]:
                self.graph[u].remove(v)

    def has_edge(self, u, v):
        result = False
        if u in self.graph:
            if v in self.graph[u]:
                result = True
        return result

    def get_spanning_tree(self, start):
        spanning_tree = Graph(self.num_nodes)
        stack = []
        visited = [False]*self.num_nodes

        visited[start] = True
        stack.append(start)
        while stack:
            node = stack[len(stack)-1]
            unvisited_nodes = []
            for next_node in self.graph[node]:
                if not visited[next_node]:
                    unvisited_nodes.append(next_node)
            if unvisited_nodes:
                next_node = random.choice(unvisited_nodes)
                stack.append(next_node)
                visited[next_node] = True
                spanning_tree.add_edge(node, next_node)
                spanning_tree.add_edge(next_node, node)
            else:
                stack.pop()

        return spanning_tree

