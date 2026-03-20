# 🔍 Binary Search

> **Pattern Overview:** Binary Search divides the search space in half at each step, achieving O(log n) time complexity. Beyond simple array search, it applies to finding boundaries, optimizing answer spaces, and solving problems with monotonic conditions.

**When to Use:** Sorted arrays, finding first/last occurrence, searching in rotated arrays, finding minimum/maximum that satisfies a condition, or when you can define a monotonic predicate function.

---

## 📋 Problems

| # | Question | Difficulty | Link | Status |
|---|----------|------------|------|--------|
| 01 | Binary Search | 🟢 Easy | [Link](https://leetcode.com/problems/binary-search/) | ⬜ |
| 02 | First Bad Version | 🟢 Easy | [Link](https://leetcode.com/problems/first-bad-version/) | ⬜ |
| 03 | Search Insert Position | 🟢 Easy | [Link](https://leetcode.com/problems/search-insert-position/) | ⬜ |
| 04 | Guess Number Higher or Lower | 🟢 Easy | [Link](https://leetcode.com/problems/guess-number-higher-or-lower/) | ⬜ |
| 05 | Find Minimum in Rotated Sorted Array | 🟡 Medium | [Link](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | ⬜ |
| 06 | Search in Rotated Sorted Array | 🟡 Medium | [Link](https://leetcode.com/problems/search-in-rotated-sorted-array/) | ⬜ |
| 07 | Find First and Last Position of Element in Sorted Array | 🟡 Medium | [Link](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | ⬜ |
| 08 | Single Element in a Sorted Array | 🟡 Medium | [Link](https://leetcode.com/problems/single-element-in-a-sorted-array/) | ⬜ |
| 09 | Peak Index in a Mountain Array | 🟡 Medium | [Link](https://leetcode.com/problems/peak-index-in-a-mountain-array/) | ⬜ |
| 10 | Find Peak Element | 🟡 Medium | [Link](https://leetcode.com/problems/find-peak-element/) | ⬜ |
| 11 | Median of Two Sorted Arrays | 🔴 Hard | [Link](https://leetcode.com/problems/median-of-two-sorted-arrays/) | ⬜ |
| 12 | Find Minimum in Rotated Sorted Array II | 🔴 Hard | [Link](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/) | ⬜ |
| 13 | Sqrt(x) | 🟢 Easy | [Link](https://leetcode.com/problems/sqrtx/) | ⬜ |
| 14 | Capacity To Ship Packages Within D Days | 🟡 Medium | [Link](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | ⬜ |
| 15 | Split Array Largest Sum | 🔴 Hard | [Link](https://leetcode.com/problems/split-array-largest-sum/) | ⬜ |

---

## 📊 Pattern Statistics

| Difficulty | Count |
|------------|-------|
| 🟢 Easy | 5 |
| 🟡 Medium | 7 |
| 🔴 Hard | 3 |

---

## 💡 Key Concepts

1. **Classic Binary Search:** Find exact element in sorted array
2. **Lower/Upper Bound:** Find first position where element can be inserted
3. **Rotated Array Search:** Handle pivot point and search appropriate half
4. **Binary Search on Answer:** Search the answer space instead of array indices

---

## 🔑 Common Templates

```
// Classic Binary Search
int left = 0, right = n - 1;
while (left <= right) {
    int mid = left + (right - left) / 2;
    if (nums[mid] == target) return mid;
    else if (nums[mid] < target) left = mid + 1;
    else right = mid - 1;
}

// Find Lower Bound (first >= target)
while (left < right) {
    int mid = left + (right - left) / 2;
    if (nums[mid] >= target) right = mid;
    else left = mid + 1;
}

// Binary Search on Answer Space
int lo = minPossible, hi = maxPossible;
while (lo < hi) {
    int mid = lo + (hi - lo) / 2;
    if (canAchieve(mid)) hi = mid;
    else lo = mid + 1;
}
```

---

**← [Back to README](../README.md)**
