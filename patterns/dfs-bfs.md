# 🌳 DFS / BFS

> **Pattern Overview:** DFS (Depth-First Search) explores as deep as possible before backtracking, using recursion or stack. BFS (Breadth-First Search) explores level by level using a queue. Both are fundamental for tree and graph traversal problems.

**When to Use:** Tree traversals, finding connected components, shortest path in unweighted graphs, level-order processing, island problems, flood fill algorithms, and pathfinding.

---

## 📋 Problems

| # | Question | Difficulty | Link | Status |
|---|----------|------------|------|--------|
| 01 | Binary Tree Level Order Traversal | 🟡 Medium | [Link](https://leetcode.com/problems/binary-tree-level-order-traversal/) | ⬜ |
| 02 | Maximum Depth of Binary Tree | 🟢 Easy | [Link](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | ⬜ |
| 03 | Same Tree | 🟢 Easy | [Link](https://leetcode.com/problems/same-tree/) | ⬜ |
| 04 | Invert Binary Tree | 🟢 Easy | [Link](https://leetcode.com/problems/invert-binary-tree/) | ⬜ |
| 05 | Path Sum | 🟢 Easy | [Link](https://leetcode.com/problems/path-sum/) | ⬜ |
| 06 | Number of Islands | 🟡 Medium | [Link](https://leetcode.com/problems/number-of-islands/) | ⬜ |
| 07 | Surrounded Regions | 🟡 Medium | [Link](https://leetcode.com/problems/surrounded-regions/) | ⬜ |
| 08 | Clone Graph | 🟡 Medium | [Link](https://leetcode.com/problems/clone-graph/) | ⬜ |
| 09 | Pacific Atlantic Water Flow | 🟡 Medium | [Link](https://leetcode.com/problems/pacific-atlantic-water-flow/) | ⬜ |
| 10 | Rotting Oranges | 🟡 Medium | [Link](https://leetcode.com/problems/rotting-oranges/) | ⬜ |
| 11 | Word Ladder | 🔴 Hard | [Link](https://leetcode.com/problems/word-ladder/) | ⬜ |
| 12 | Serialize and Deserialize Binary Tree | 🔴 Hard | [Link](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | ⬜ |
| 13 | Course Schedule | 🟡 Medium | [Link](https://leetcode.com/problems/course-schedule/) | ⬜ |
| 14 | Binary Tree Right Side View | 🟡 Medium | [Link](https://leetcode.com/problems/binary-tree-right-side-view/) | ⬜ |
| 15 | Walls and Gates | 🟡 Medium | [Link](https://leetcode.com/problems/walls-and-gates/) | ⬜ |

---

## 📊 Pattern Statistics

| Difficulty | Count |
|------------|-------|
| 🟢 Easy | 4 |
| 🟡 Medium | 9 |
| 🔴 Hard | 2 |

---

## 💡 Key Concepts

1. **DFS (Recursive):** Uses call stack, good for path finding, tree traversals
2. **DFS (Iterative):** Uses explicit stack, avoids stack overflow
3. **BFS (Level Order):** Uses queue, shortest path in unweighted graphs
4. **Multi-source BFS:** Multiple starting points (rotting oranges, walls and gates)

---

## 🔑 Common Templates

```
// DFS Recursive
void dfs(TreeNode* node) {
    if (!node) return;
    // Process node
    dfs(node->left);
    dfs(node->right);
}

// BFS Level Order
queue<TreeNode*> q;
q.push(root);
while (!q.empty()) {
    int size = q.size();
    for (int i = 0; i < size; i++) {
        TreeNode* node = q.front(); q.pop();
        // Process node
        if (node->left) q.push(node->left);
        if (node->right) q.push(node->right);
    }
    // End of level
}

// Grid DFS (Island Problems)
void dfs(vector<vector<char>>& grid, int r, int c) {
    if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] != '1')
        return;
    grid[r][c] = '0';  // Mark visited
    dfs(grid, r+1, c); dfs(grid, r-1, c);
    dfs(grid, r, c+1); dfs(grid, r, c-1);
}
```

---

**← [Back to README](../README.md)**
