# 🕸️ Graphs

> **Pattern Overview:** Graph algorithms handle problems involving nodes and edges. Key techniques include BFS/DFS for traversal, Dijkstra's for shortest paths, Union-Find for connectivity, Topological Sort for ordering, and algorithms for cycle detection and minimum spanning trees.

**When to Use:** Network/relationship problems, shortest path queries, connectivity checks, dependency resolution, cycle detection, or any problem that can be modeled as nodes and edges.

---

## 📋 Problems

| # | Question | Difficulty | Link | Status |
|---|----------|------------|------|--------|
| 01 | Number of Islands | 🟡 Medium | [Link](https://leetcode.com/problems/number-of-islands/) | ⬜ |
| 02 | Clone Graph | 🟡 Medium | [Link](https://leetcode.com/problems/clone-graph/) | ⬜ |
| 03 | Course Schedule | 🟡 Medium | [Link](https://leetcode.com/problems/course-schedule/) | ⬜ |
| 04 | Course Schedule II | 🟡 Medium | [Link](https://leetcode.com/problems/course-schedule-ii/) | ⬜ |
| 05 | Number of Connected Components in an Undirected Graph | 🟡 Medium | [Link](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | ⬜ |
| 06 | Graph Valid Tree | 🟡 Medium | [Link](https://leetcode.com/problems/graph-valid-tree/) | ⬜ |
| 07 | Pacific Atlantic Water Flow | 🟡 Medium | [Link](https://leetcode.com/problems/pacific-atlantic-water-flow/) | ⬜ |
| 08 | Network Delay Time | 🟡 Medium | [Link](https://leetcode.com/problems/network-delay-time/) | ⬜ |
| 09 | Cheapest Flights Within K Stops | 🟡 Medium | [Link](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | ⬜ |
| 10 | Alien Dictionary | 🔴 Hard | [Link](https://leetcode.com/problems/alien-dictionary/) | ⬜ |
| 11 | Word Ladder II | 🔴 Hard | [Link](https://leetcode.com/problems/word-ladder-ii/) | ⬜ |
| 12 | Reconstruct Itinerary | 🔴 Hard | [Link](https://leetcode.com/problems/reconstruct-itinerary/) | ⬜ |
| 13 | Min Cost to Connect All Points | 🟡 Medium | [Link](https://leetcode.com/problems/min-cost-to-connect-all-points/) | ⬜ |
| 14 | Accounts Merge | 🟡 Medium | [Link](https://leetcode.com/problems/accounts-merge/) | ⬜ |
| 15 | Critical Connections in a Network | 🔴 Hard | [Link](https://leetcode.com/problems/critical-connections-in-a-network/) | ⬜ |

---

## 📊 Pattern Statistics

| Difficulty | Count |
|------------|-------|
| 🟢 Easy | 0 |
| 🟡 Medium | 11 |
| 🔴 Hard | 4 |

---

## 💡 Key Concepts

1. **Adjacency List:** Most common representation for sparse graphs
2. **Union-Find (Disjoint Set):** Efficient for connectivity queries and cycle detection
3. **Dijkstra's Algorithm:** Shortest path with non-negative weights
4. **Bellman-Ford:** Shortest path with negative weights (detects negative cycles)
5. **Topological Sort:** Ordering of vertices in DAG
6. **Tarjan's Algorithm:** Find bridges, articulation points, and SCCs

---

## 🔑 Common Templates

```
// Union-Find with Path Compression & Union by Rank
class UnionFind {
    vector<int> parent, rank;
public:
    UnionFind(int n) : parent(n), rank(n, 0) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    bool unite(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return false;
        if (rank[px] < rank[py]) swap(px, py);
        parent[py] = px;
        if (rank[px] == rank[py]) rank[px]++;
        return true;
    }
};

// Dijkstra's Algorithm
vector<int> dist(n, INT_MAX);
dist[source] = 0;
priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
pq.push({0, source});
while (!pq.empty()) {
    auto [d, u] = pq.top(); pq.pop();
    if (d > dist[u]) continue;
    for (auto [v, w] : adj[u]) {
        if (dist[u] + w < dist[v]) {
            dist[v] = dist[u] + w;
            pq.push({dist[v], v});
        }
    }
}

// Topological Sort (Kahn's Algorithm)
vector<int> indegree(n);
for (auto& edges : adj)
    for (int v : edges) indegree[v]++;
queue<int> q;
for (int i = 0; i < n; i++)
    if (indegree[i] == 0) q.push(i);
while (!q.empty()) {
    int u = q.front(); q.pop();
    result.push_back(u);
    for (int v : adj[u])
        if (--indegree[v] == 0) q.push(v);
}
```

---

**← [Back to README](../README.md)**
