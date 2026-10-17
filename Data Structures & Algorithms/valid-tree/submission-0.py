class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        
        adj = [[] for i in range(n)] # n vertices and n-1 edges

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        print(adj)

        visit =set()
        def dfs(node, root):
            if node in visit: # we already saw it 
                return False

            visit.add(node)
            for nei in adj[node]:
                if nei == root: # ignore this edge
                    continue
                if not dfs(nei, node):
                    return False
            return True


        return dfs(0, -1) and len(visit) == n

