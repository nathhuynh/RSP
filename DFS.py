"""
Depth First Search using recursion
"""
class Graph:
    def __init__(self):
        self.adj = {}

    def insert_edge(self, u, v):
        if v not in self.adj:
            self.adj[v] = []
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)
        self.adj[v].append(u)
    
    # Recursive Depth First Search function
    def dfs(self, node, visited):
        if node not in self.adj:
            print(f"Node {node} is not in the graph.")
            return

        print(node, end=" ")
        visited.add(node)
        # Call DFS recursively on neigbhours that have not been visited yet
        for nei in self.adj[node]:
            if nei not in visited:
                self.dfs(nei, visited)

if __name__ == "__main__":
    g = Graph()
    g.insert_edge(0, 1)
    g.insert_edge(0, 2)
    g.insert_edge(0, 3)
    g.insert_edge(1, 2)
    g.insert_edge(3, 1)
    g.insert_edge(4, 5)

    g.dfs(0, set())
    print()
    
    g.dfs(2, set())
    print()

    g.dfs(4, set())
    print()

    g.dfs(5, set())
    print()
