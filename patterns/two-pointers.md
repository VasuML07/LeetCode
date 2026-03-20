# 🔶 Two Pointers

> **Pattern Overview:** Two Pointers technique uses two pointers to traverse an array/string, either from same direction or opposite ends. It reduces time complexity from O(n²) to O(n) for many problems involving pairs, triplets, or subarrays.

**When to Use:** Sorted arrays, finding pairs with specific sum, removing duplicates, palindrome checks, container problems, or when you need to compare elements from different positions.

---

## 📋 Problems

| # | Question | Difficulty | Link | Status |
|---|----------|------------|------|--------|
| 01 | Two Sum II - Input Array Is Sorted | 🟢 Easy | [Link](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | ⬜ |
| 02 | Valid Palindrome | 🟢 Easy | [Link](https://leetcode.com/problems/valid-palindrome/) | ⬜ |
| 03 | Remove Duplicates from Sorted Array | 🟢 Easy | [Link](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | ⬜ |
| 04 | Move Zeroes | 🟢 Easy | [Link](https://leetcode.com/problems/move-zeroes/) | ⬜ |
| 05 | 3Sum | 🟡 Medium | [Link](https://leetcode.com/problems/3sum/) | ⬜ |
| 06 | 3Sum Closest | 🟡 Medium | [Link](https://leetcode.com/problems/3sum-closest/) | ⬜ |
| 07 | 4Sum | 🟡 Medium | [Link](https://leetcode.com/problems/4sum/) | ⬜ |
| 08 | Container With Most Water | 🟡 Medium | [Link](https://leetcode.com/problems/container-with-most-water/) | ⬜ |
| 09 | Trapping Rain Water | 🔴 Hard | [Link](https://leetcode.com/problems/trapping-rain-water/) | ⬜ |
| 10 | Remove Nth Node From End of List | 🟡 Medium | [Link](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | ⬜ |
| 11 | Sort Colors | 🟡 Medium | [Link](https://leetcode.com/problems/sort-colors/) | ⬜ |
| 12 | Reverse String | 🟢 Easy | [Link](https://leetcode.com/problems/reverse-string/) | ⬜ |
| 13 | Longest Palindromic Substring | 🟡 Medium | [Link](https://leetcode.com/problems/longest-palindromic-substring/) | ⬜ |
| 14 | Next Permutation | 🟡 Medium | [Link](https://leetcode.com/problems/next-permutation/) | ⬜ |
| 15 | Valid Triangle Number | 🟡 Medium | [Link](https://leetcode.com/problems/valid-triangle-number/) | ⬜ |

---

## 📊 Pattern Statistics

| Difficulty | Count |
|------------|-------|
| 🟢 Easy | 5 |
| 🟡 Medium | 8 |
| 🔴 Hard | 2 |

---

## 💡 Key Concepts

1. **Opposite Direction:** Pointers start from both ends and move toward center (palindrome, container problems)
2. **Same Direction:** Both pointers move in same direction at different speeds (remove duplicates, cycle detection)
3. **Fast & Slow:** Also known as Floyd's algorithm for cycle detection

---

## 🔑 Common Templates

```
// Opposite Ends
int left = 0, right = n - 1;
while (left < right) {
    if (condition) left++;
    else right--;
}

// Same Direction (Fast/Slow)
int slow = 0, fast = 0;
while (fast < n) {
    if (condition) nums[slow++] = nums[fast];
    fast++;
}

// Triplets (Sort + Two Pointers)
sort(nums.begin(), nums.end());
for (int i = 0; i < n - 2; i++) {
    int left = i + 1, right = n - 1;
    while (left < right) {
        // Process triplet
    }
}
```

---

**← [Back to README](../README.md)**
