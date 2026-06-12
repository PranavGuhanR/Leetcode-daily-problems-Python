MAXN = 100_001
depth = [0] * MAXN
parent = [0] * MAXN
up = [[0] * MAXN for _ in range(MAXN.bit_length())]

class Solution:
    def assignEdgeWeights(self, edges, queries) -> List[int]:
        n = len(edges) + 1
        blocks = n.bit_length()
        depth[1] = 1
        parent[1] = 1

        for u, v in sorted(edges):
            u, v = min(u, v), max(u, v)
            depth[v] = depth[u] + 1
            parent[v] = u

        for v in range(1, n + 1):
            up[0][v] = parent[v]
        for k in range(1, blocks):
            for v in range(1, n + 1):
                up[k][v] = up[k-1][up[k-1][v]]

        def lca(u, v):
            if depth[u] < depth[v]: u, v = v, u
            diff = depth[u] - depth[v]
            for k in range(blocks):
                if (diff >> k) & 1:
                    u = up[k][u]
            if u == v: return u
            for k in range(blocks - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u, v = up[k][u], up[k][v]
            return up[0][u]

        for i, (u, v) in enumerate(queries):
            path = depth[u] + depth[v] - 2 * depth[lca(u, v)]
            queries[i] = pow(2, path - 1, 1_000_000_007) if path else 0
        return queries