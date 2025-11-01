class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = [1] * (len(edges) + 1)
        parent = [0] * (len(edges) + 1)

        for i in range(len(edges) + 1):
            parent[i] = i

        def find(node):
            node = parent[node]
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(node1, node2):
            n1, n2 = find(node1), find(node2)

            if n1 == n2:
                # same parent
                return False
            
            if rank[n1] > rank[n2]:
                rank[n1] += rank[n2]
                parent[n2] = n1
            
            else:
                rank[n2] += rank[n1]
                parent[n1] = n2
            
            return True
        
        for u, v in edges:
            if not union(u, v):
                return (u, v)
