"""
Undirected Graph using adjacency list
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

    def get_neighbours(self, v):
        if v in self.adj:
            return self.adj[v]
        return None

    def display_graph(self):
        for (u, v) in self.adj.items():
            print(f"Node {u} -> {v}")

if __name__ == "__main__":
    g = Graph()
    g.insert_edge(0, 1)
    g.insert_edge(0, 2)
    g.insert_edge(0, 3)
    g.insert_edge(1, 2)
    g.insert_edge(3, 1)
    g.display_graph()

    print(f"Neighbours of node 1 {g.get_neighbours(1)}")
