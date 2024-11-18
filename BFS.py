from collections import deque

"""
Breadth First Search using a while loop
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
    
    # BFS function with a while loop
    def bfs(self, node):
        if node not in self.adj:
            print(f"Node {node} is not in the graph.")
            return

        visited = set()
        q = deque([node])
        visited.add(node)

        while q:
            curr = q.popleft()
            print(curr, end=" ")
            for nei in self.adj[curr]:
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei) # Ensure nodes aren't added to the Q more than once

if __name__ == "__main__":
    g = Graph()
    g.insert_edge(0, 1)
    g.insert_edge(0, 2)
    g.insert_edge(0, 3)
    g.insert_edge(1, 2)
    g.insert_edge(3, 1)
    g.insert_edge(4, 5)

    g.bfs(0)
    print()
    
    g.bfs(2)
    print()

    g.bfs(4)
    print()

    g.bfs(5)
    print()

    g.bfs(6)
