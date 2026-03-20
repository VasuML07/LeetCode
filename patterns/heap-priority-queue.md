# 📊 Heap / Priority Queue

> **Pattern Overview:** Heaps provide O(log n) insertion and O(1) access to min/max elements. Priority queues (often implemented as heaps) are essential for problems requiring frequent access to the largest/smallest elements or maintaining a sorted stream of data.

**When to Use:** Top-K problems, finding kth largest/smallest, merging sorted lists, scheduling problems, median of data stream, or when you need efficient access to extreme elements.

---

## 📋 Problems

| # | Question | Difficulty | Link | Status |
|---|----------|------------|------|--------|
| 01 | Kth Largest Element in a Stream | 🟢 Easy | [Link](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | ⬜ |
| 02 | Last Stone Weight | 🟢 Easy | [Link](https://leetcode.com/problems/last-stone-weight/) | ⬜ |
| 03 | Kth Largest Element in an Array | 🟡 Medium | [Link](https://leetcode.com/problems/kth-largest-element-in-an-array/) | ⬜ |
| 04 | Top K Frequent Elements | 🟡 Medium | [Link](https://leetcode.com/problems/top-k-frequent-elements/) | ⬜ |
| 05 | Merge K Sorted Lists | 🔴 Hard | [Link](https://leetcode.com/problems/merge-k-sorted-lists/) | ⬜ |
| 06 | Find Median from Data Stream | 🔴 Hard | [Link](https://leetcode.com/problems/find-median-from-data-stream/) | ⬜ |
| 07 | Task Scheduler | 🟡 Medium | [Link](https://leetcode.com/problems/task-scheduler/) | ⬜ |
| 08 | IPO | 🔴 Hard | [Link](https://leetcode.com/problems/ipo/) | ⬜ |
| 09 | K Closest Points to Origin | 🟡 Medium | [Link](https://leetcode.com/problems/k-closest-points-to-origin/) | ⬜ |
| 10 | Sort Characters By Frequency | 🟡 Medium | [Link](https://leetcode.com/problems/sort-characters-by-frequency/) | ⬜ |
| 11 | Reorganize String | 🟡 Medium | [Link](https://leetcode.com/problems/reorganize-string/) | ⬜ |
| 12 | Meeting Rooms II | 🟡 Medium | [Link](https://leetcode.com/problems/meeting-rooms-ii/) | ⬜ |
| 13 | Minimum Cost to Connect Sticks | 🟡 Medium | [Link](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) | ⬜ |
| 14 | Find K Pairs with Smallest Sums | 🟡 Medium | [Link](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | ⬜ |
| 15 | Sliding Window Median | 🔴 Hard | [Link](https://leetcode.com/problems/sliding-window-median/) | ⬜ |

---

## 📊 Pattern Statistics

| Difficulty | Count |
|------------|-------|
| 🟢 Easy | 2 |
| 🟡 Medium | 9 |
| 🔴 Hard | 4 |

---

## 💡 Key Concepts

1. **Min-Heap:** Smallest element at root (default in C++, use negative in Java)
2. **Max-Heap:** Largest element at root (default in Python, use negative in C++)
3. **Two Heaps:** Use min-heap and max-heap together for median problems
4. **Heapify:** O(n) to build heap from array, O(log n) for insert/remove

---

## 🔑 Common Templates

```
// Min-Heap (C++)
priority_queue<int, vector<int>, greater<int>> minHeap;

// Max-Heap (C++)
priority_queue<int> maxHeap;

// Custom Comparator
auto cmp = [](pair<int, int>& a, pair<int, int>& b) {
    return a.second > b.second;
};
priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> pq(cmp);

// Kth Largest (maintain size k min-heap)
priority_queue<int, vector<int>, greater<int>> pq;
for (int num : nums) {
    pq.push(num);
    if (pq.size() > k) pq.pop();
}
return pq.top();

// Two Heaps for Median
priority_queue<int> maxHeap;  // left half (smaller)
priority_queue<int, vector<int>, greater<int>> minHeap;  // right half (larger)
// Balance sizes: |maxHeap.size() - minHeap.size()| <= 1
```

---

**← [Back to README](../README.md)**
