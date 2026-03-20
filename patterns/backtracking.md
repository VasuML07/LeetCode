# 🔙 Backtracking

> **Pattern Overview:** Backtracking systematically explores all possible solutions by building candidates incrementally and abandoning those that fail to satisfy constraints. It's essentially DFS with pruning, using recursion to try all valid paths and backtrack when a path leads to a dead end.

**When to Use:** Permutation and combination problems, subset generation, constraint satisfaction problems, puzzle solving (N-Queens, Sudoku), path finding with obstacles, or when you need to enumerate all valid solutions.

---

## 📋 Problems

| # | Question | Difficulty | Link | Status |
|---|----------|------------|------|--------|
| 01 | Subsets | 🟡 Medium | [Link](https://leetcode.com/problems/subsets/) | ⬜ |
| 02 | Subsets II | 🟡 Medium | [Link](https://leetcode.com/problems/subsets-ii/) | ⬜ |
| 03 | Permutations | 🟡 Medium | [Link](https://leetcode.com/problems/permutations/) | ⬜ |
| 04 | Permutations II | 🟡 Medium | [Link](https://leetcode.com/problems/permutations-ii/) | ⬜ |
| 05 | Combination Sum | 🟡 Medium | [Link](https://leetcode.com/problems/combination-sum/) | ⬜ |
| 06 | Combination Sum II | 🟡 Medium | [Link](https://leetcode.com/problems/combination-sum-ii/) | ⬜ |
| 07 | Combination Sum III | 🟡 Medium | [Link](https://leetcode.com/problems/combination-sum-iii/) | ⬜ |
| 08 | Letter Combinations of a Phone Number | 🟡 Medium | [Link](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | ⬜ |
| 09 | Generate Parentheses | 🟡 Medium | [Link](https://leetcode.com/problems/generate-parentheses/) | ⬜ |
| 10 | Word Search | 🟡 Medium | [Link](https://leetcode.com/problems/word-search/) | ⬜ |
| 11 | N-Queens | 🔴 Hard | [Link](https://leetcode.com/problems/n-queens/) | ⬜ |
| 12 | N-Queens II | 🔴 Hard | [Link](https://leetcode.com/problems/n-queens-ii/) | ⬜ |
| 13 | Sudoku Solver | 🔴 Hard | [Link](https://leetcode.com/problems/sudoku-solver/) | ⬜ |
| 14 | Palindrome Partitioning | 🟡 Medium | [Link](https://leetcode.com/problems/palindrome-partitioning/) | ⬜ |
| 15 | Restore IP Addresses | 🟡 Medium | [Link](https://leetcode.com/problems/restore-ip-addresses/) | ⬜ |

---

## 📊 Pattern Statistics

| Difficulty | Count |
|------------|-------|
| 🟢 Easy | 0 |
| 🟡 Medium | 12 |
| 🔴 Hard | 3 |

---

## 💡 Key Concepts

1. **Decision Tree:** Each recursive call represents a decision point
2. **Pruning:** Skip invalid paths early to optimize
3. **State Restoration:** Undo changes when backtracking
4. **Duplicate Handling:** Sort + skip duplicates when needed

---

## 🔑 Common Templates

```
// Subset Pattern
void backtrack(vector<int>& nums, int start, vector<int>& path) {
    result.push_back(path);  // Record current subset
    for (int i = start; i < nums.size(); i++) {
        if (i > start && nums[i] == nums[i-1]) continue;  // Skip duplicates
        path.push_back(nums[i]);
        backtrack(nums, i + 1, path);
        path.pop_back();  // Backtrack
    }
}

// Permutation Pattern
void backtrack(vector<int>& nums, vector<int>& path, vector<bool>& used) {
    if (path.size() == nums.size()) {
        result.push_back(path);
        return;
    }
    for (int i = 0; i < nums.size(); i++) {
        if (used[i] || (i > 0 && nums[i] == nums[i-1] && !used[i-1])) continue;
        used[i] = true;
        path.push_back(nums[i]);
        backtrack(nums, path, used);
        path.pop_back();
        used[i] = false;
    }
}

// Combination Pattern
void backtrack(int start, int k, int target, vector<int>& path) {
    if (path.size() == k && target == 0) {
        result.push_back(path);
        return;
    }
    for (int i = start; i <= 9; i++) {
        if (target < i) break;  // Pruning
        path.push_back(i);
        backtrack(i + 1, k, target - i, path);
        path.pop_back();
    }
}
```

---

**← [Back to README](../README.md)**
