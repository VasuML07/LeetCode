# 🔷 Sliding Window

> **Pattern Overview:** Sliding Window technique maintains a window of elements that slides through an array/string. It's optimal for problems involving subarrays or substrings where you need to find maximum, minimum, or specific conditions within a contiguous range.

**When to Use:** Fixed or variable window size problems, substring matches, maximum/minimum subarray sum, longest/shortest substring with constraints.

---

## 📋 Problems

| # | Question | Difficulty | Link | Status |
|---|----------|------------|------|--------|
| 01 | Maximum Average Subarray I | 🟢 Easy | [Link](https://leetcode.com/problems/maximum-average-subarray-i/) | ⬜ |
| 02 | Minimum Size Subarray Sum | 🟡 Medium | [Link](https://leetcode.com/problems/minimum-size-subarray-sum/) | ⬜ |
| 03 | Longest Substring Without Repeating Characters | 🟡 Medium | [Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | ⬜ |
| 04 | Permutation in String | 🟡 Medium | [Link](https://leetcode.com/problems/permutation-in-string/) | ⬜ |
| 05 | Find All Anagrams in a String | 🟡 Medium | [Link](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | ⬜ |
| 06 | Longest Repeating Character Replacement | 🟡 Medium | [Link](https://leetcode.com/problems/longest-repeating-character-replacement/) | ⬜ |
| 07 | Max Consecutive Ones III | 🟡 Medium | [Link](https://leetcode.com/problems/max-consecutive-ones-iii/) | ⬜ |
| 08 | Fruit Into Baskets | 🟡 Medium | [Link](https://leetcode.com/problems/fruit-into-baskets/) | ⬜ |
| 09 | Substrings of Size Three with Distinct Characters | 🟢 Easy | [Link](https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/) | ⬜ |
| 10 | Maximum Number of Vowels in a Substring of Given Length | 🟡 Medium | [Link](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) | ⬜ |
| 11 | Minimum Window Substring | 🔴 Hard | [Link](https://leetcode.com/problems/minimum-window-substring/) | ⬜ |
| 12 | Sliding Window Maximum | 🔴 Hard | [Link](https://leetcode.com/problems/sliding-window-maximum/) | ⬜ |
| 13 | Substring with Concatenation of All Words | 🔴 Hard | [Link](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) | ⬜ |
| 14 | Minimum Operations to Reduce X to Zero | 🟡 Medium | [Link](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/) | ⬜ |
| 15 | Longest Subarray with Absolute Diff Less Than or Equal to Limit | 🟡 Medium | [Link](https://leetcode.com/problems/longest-subarray-with-absolute-diff-less-than-or-equal-to-limit/) | ⬜ |

---

## 📊 Pattern Statistics

| Difficulty | Count |
|------------|-------|
| 🟢 Easy | 2 |
| 🟡 Medium | 10 |
| 🔴 Hard | 3 |

---

## 💡 Key Concepts

1. **Fixed Size Window:** Window size remains constant (e.g., "find max sum of k consecutive elements")
2. **Variable Size Window:** Window expands/shrinks based on conditions (e.g., "longest substring with...")
3. **Two Pointers + Hash Map:** Often combined for character frequency tracking

---

## 🔑 Common Templates

```
// Fixed Size Window
for (int i = 0; i < n; i++) {
    // Add element to window
    if (i >= k - 1) {
        // Process window
        // Remove leftmost element
    }
}

// Variable Size Window
while (right < n) {
    // Expand window
    while (condition violated) {
        // Shrink window from left
    }
    // Update result
}
```

---

**← [Back to README](../README.md)**
