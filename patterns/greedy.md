# 💰 Greedy

> **Pattern Overview:** Greedy algorithms make locally optimal choices at each step with the hope of finding a global optimum. Unlike DP, greedy doesn't reconsider previous choices—once a decision is made, it's final.

**When to Use:** Interval problems (scheduling, merging), activity selection, minimization/maximization where local optimum leads to global optimum, or when you can prove greedy choice property and optimal substructure.

---

## 📋 Problems

| # | Question | Difficulty | Link | Status |
|---|----------|------------|------|--------|
| 01 | Maximum Subarray | 🟡 Medium | [Link](https://leetcode.com/problems/maximum-subarray/) | ⬜ |
| 02 | Jump Game | 🟡 Medium | [Link](https://leetcode.com/problems/jump-game/) | ⬜ |
| 03 | Jump Game II | 🟡 Medium | [Link](https://leetcode.com/problems/jump-game-ii/) | ⬜ |
| 04 | Gas Station | 🟡 Medium | [Link](https://leetcode.com/problems/gas-station/) | ⬜ |
| 05 | Candy | 🔴 Hard | [Link](https://leetcode.com/problems/candy/) | ⬜ |
| 06 | Assign Cookies | 🟢 Easy | [Link](https://leetcode.com/problems/assign-cookies/) | ⬜ |
| 07 | Lemonade Change | 🟢 Easy | [Link](https://leetcode.com/problems/lemonade-change/) | ⬜ |
| 08 | Minimum Number of Arrows to Burst Balloons | 🟡 Medium | [Link](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | ⬜ |
| 09 | Non-overlapping Intervals | 🟡 Medium | [Link](https://leetcode.com/problems/non-overlapping-intervals/) | ⬜ |
| 10 | Merge Intervals | 🟡 Medium | [Link](https://leetcode.com/problems/merge-intervals/) | ⬜ |
| 11 | Insert Interval | 🟡 Medium | [Link](https://leetcode.com/problems/insert-interval/) | ⬜ |
| 12 | Queue Reconstruction by Height | 🟡 Medium | [Link](https://leetcode.com/problems/queue-reconstruction-by-height/) | ⬜ |
| 13 | Partition Labels | 🟡 Medium | [Link](https://leetcode.com/problems/partition-labels/) | ⬜ |
| 14 | Task Scheduler | 🟡 Medium | [Link](https://leetcode.com/problems/task-scheduler/) | ⬜ |
| 15 | Minimum Deletions to Make Character Frequencies Unique | 🟡 Medium | [Link](https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/) | ⬜ |

---

## 📊 Pattern Statistics

| Difficulty | Count |
|------------|-------|
| 🟢 Easy | 2 |
| 🟡 Medium | 12 |
| 🔴 Hard | 1 |

---

## 💡 Key Concepts

1. **Sorting First:** Many greedy problems require sorting as preprocessing
2. **Interval Problems:** Sort by start or end time, then process greedily
3. **Local Optimal Choice:** Make the best choice at current step
4. **Proof Strategies:** Exchange argument, greedy stays ahead, contradiction

---

## 🔑 Common Templates

```
// Interval Scheduling (max non-overlapping intervals)
sort(intervals.begin(), intervals.end(), 
    [](auto& a, auto& b) { return a[1] < b[1]; });
int count = 0, end = INT_MIN;
for (auto& interval : intervals) {
    if (interval[0] >= end) {
        count++;
        end = interval[1];
    }
}

// Jump Game (minimum jumps)
int jumps = 0, currentEnd = 0, farthest = 0;
for (int i = 0; i < n - 1; i++) {
    farthest = max(farthest, i + nums[i]);
    if (i == currentEnd) {
        jumps++;
        currentEnd = farthest;
    }
}

// Task Scheduler
int maxFreq = *max_element(count.begin(), count.end());
int idleSlots = (maxFreq - 1) * n;
// Fill idle slots with other tasks...
```

---

**← [Back to README](../README.md)**
