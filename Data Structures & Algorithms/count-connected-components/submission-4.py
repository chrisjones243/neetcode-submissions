class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()

        def dfs(i):
            if i in visited:
                return

            visited.add(i)
            for neighbour in adj[i]:
                dfs(neighbour)

        num = 0
        for i in adj.keys():
            if i not in visited:
                dfs(i)
                num += 1

        return num