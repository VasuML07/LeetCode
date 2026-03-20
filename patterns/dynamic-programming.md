# 🧠 Dynamic Programming

> **Pattern Overview:** Dynamic Programming solves complex problems by breaking them into overlapping subproblems with optimal substructure. It stores solutions to subproblems to avoid redundant calculations, trading space for time efficiency.

**When to Use:** Optimization problems (max/min), counting problems, problems with overlapping subproblems, decision-making problems, or when greedy doesn't work and you need to explore all possibilities.

---

## 📋 Problems

| # | Question | Difficulty | Link | Status |
|---|----------|------------|------|--------|
| 01 | Climbing Stairs | 🟢 Easy | [Link](https://leetcode.com/problems/climbing-stairs/) | ⬜ |
| 02 | House Robber | 🟡 Medium | [Link](https://leetcode.com/problems/house-robber/) | ⬜ |
| 03 | Maximum Subarray | 🟡 Medium | [Link](https://leetcode.com/problems/maximum-subarray/) | ⬜ |
| 04 | Unique Paths | 🟡 Medium | [Link](https://leetcode.com/problems/unique-paths/) | ⬜ |
| 05 | Coin Change | 🟡 Medium | [Link](https://leetcode.com/problems/coin-change/) | ⬜ |
| 06 | Longest Increasing Subsequence | 🟡 Medium | [Link](https://leetcode.com/problems/longest-increasing-subsequence/) | ⬜ |
| 07 | Longest Common Subsequence | 🟡 Medium | [Link](https://leetcode.com/problems/longest-common-subsequence/) | ⬜ |
| 08 | Word Break | 🟡 Medium | [Link](https://leetcode.com/problems/word-break/) | ⬜ |
| 09 | Combination Sum IV | 🟡 Medium | [Link](https://leetcode.com/problems/combination-sum-iv/) | ⬜ |
| 10 | House Robber II | 🟡 Medium | [Link](https://leetcode.com/problems/house-robber-ii/) | ⬜ |
| 11 | Decode Ways | 🟡 Medium | [Link](https://leetcode.com/problems/decode-ways/) | ⬜ |
| 12 | Palindromic Substrings | 🟡 Medium | [Link](https://leetcode.com/problems/palindromic-substrings/) | ⬜ |
| 13 | Edit Distance | 🔴 Hard | [Link](https://leetcode.com/problems/edit-distance/) | ⬜ |
| 14 | Regular Expression Matching | 🔴 Hard | [Link](https://leetcode.com/problems/regular-expression-matching/) | ⬜ |
| 15 | Burst Balloons | 🔴 Hard | [Link](https://leetcode.com/problems/burst-balloons/) | ⬜ |

---

## 📊 Pattern Statistics

| Difficulty | Count |
|------------|-------|
| 🟢 Easy | 1 |
| 🟡 Medium | 11 |
| 🔴 Hard | 3 |

---

## 💡 Key Concepts

1. **1D DP:** Single state transition (climbing stairs, house robber)
2. **2D DP:** Two-dimensional state (grid paths, LCS)
3. **Interval DP:** Problems on intervals (burst balloons, matrix chain)
4. **State Machine DP:** Multiple states with transitions (stock problems)
5. **Knapsack Variants:** 0/1 knapsack, unbounded knapsack

---

## 🔑 Common Templates

```
// 1D DP (Bottom-Up)
vector<int> dp(n + 1);
dp[0] = base_case;
for (int i = 1; i <= n; i++) {
    dp[i] = recurrence_relation;
}
return dp[n];

// 2D DP (Grid)
vector<vector<int>> dp(m, vector<int>(n));
for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
        dp[i][j] = recurrence_from_dp[i-1][j]_and_dp[i][j-1];
    }
}

// Space Optimization (1D from 2D)
for (int i = 1; i <= n; i++) {
    for (int j = capacity; j >= weight[i]; j--) {
        dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);
    }
}
```

---

**← [Back to README](../README.md)**
