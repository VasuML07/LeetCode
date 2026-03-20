# 📚 Stack / Monotonic Stack

> **Pattern Overview:** Stack follows LIFO (Last In, First Out) principle. Monotonic Stack maintains elements in increasing or decreasing order, enabling O(n) solutions for problems involving next greater/smaller elements, histogram problems, and finding boundaries.

**When to Use:** Parentheses matching, expression evaluation, next greater/smaller element problems, largest rectangle in histogram, trapping rain water variants, or when you need to find nearest element satisfying some condition.

---

## 📋 Problems

| # | Question | Difficulty | Link | Status |
|---|----------|------------|------|--------|
| 01 | Valid Parentheses | 🟢 Easy | [Link](https://leetcode.com/problems/valid-parentheses/) | ⬜ |
| 02 | Min Stack | 🟡 Medium | [Link](https://leetcode.com/problems/min-stack/) | ⬜ |
| 03 | Evaluate Reverse Polish Notation | 🟡 Medium | [Link](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | ⬜ |
| 04 | Daily Temperatures | 🟡 Medium | [Link](https://leetcode.com/problems/daily-temperatures/) | ⬜ |
| 05 | Next Greater Element I | 🟢 Easy | [Link](https://leetcode.com/problems/next-greater-element-i/) | ⬜ |
| 06 | Next Greater Element II | 🟡 Medium | [Link](https://leetcode.com/problems/next-greater-element-ii/) | ⬜ |
| 07 | Largest Rectangle in Histogram | 🔴 Hard | [Link](https://leetcode.com/problems/largest-rectangle-in-histogram/) | ⬜ |
| 08 | Trapping Rain Water | 🔴 Hard | [Link](https://leetcode.com/problems/trapping-rain-water/) | ⬜ |
| 09 | Remove K Digits | 🟡 Medium | [Link](https://leetcode.com/problems/remove-k-digits/) | ⬜ |
| 10 | Remove Duplicate Letters | 🟡 Medium | [Link](https://leetcode.com/problems/remove-duplicate-letters/) | ⬜ |
| 11 | Online Stock Span | 🟡 Medium | [Link](https://leetcode.com/problems/online-stock-span/) | ⬜ |
| 12 | Car Fleet | 🟡 Medium | [Link](https://leetcode.com/problems/car-fleet/) | ⬜ |
| 13 | Asteroid Collision | 🟡 Medium | [Link](https://leetcode.com/problems/asteroid-collision/) | ⬜ |
| 14 | Maximal Rectangle | 🔴 Hard | [Link](https://leetcode.com/problems/maximal-rectangle/) | ⬜ |
| 15 | Sum of Subarray Minimums | 🟡 Medium | [Link](https://leetcode.com/problems/sum-of-subarray-minimums/) | ⬜ |

---

## 📊 Pattern Statistics

| Difficulty | Count |
|------------|-------|
| 🟢 Easy | 2 |
| 🟡 Medium | 10 |
| 🔴 Hard | 3 |

---

## 💡 Key Concepts

1. **Monotonic Increasing Stack:** Elements increase from bottom to top (useful for finding previous smaller)
2. **Monotonic Decreasing Stack:** Elements decrease from bottom to top (useful for finding next greater)
3. **Stack with Index:** Store indices instead of values for position-aware problems
4. **Circular Array:** Traverse 2n elements or use modulo for wrap-around

---

## 🔑 Common Templates

```
// Valid Parentheses
stack<char> st;
for (char c : s) {
    if (c == '(' || c == '{' || c == '[') st.push(c);
    else {
        if (st.empty()) return false;
        char top = st.top(); st.pop();
        if (!matches(top, c)) return false;
    }
}
return st.empty();

// Next Greater Element (Monotonic Decreasing Stack)
vector<int> result(n, -1);
stack<int> st;  // stores indices
for (int i = 0; i < n; i++) {
    while (!st.empty() && nums[st.top()] < nums[i]) {
        result[st.top()] = nums[i];
        st.pop();
    }
    st.push(i);
}

// Largest Rectangle in Histogram
stack<int> st;  // stores indices
int maxArea = 0;
for (int i = 0; i <= n; i++) {
    int h = (i == n) ? 0 : heights[i];
    while (!st.empty() && heights[st.top()] > h) {
        int height = heights[st.top()]; st.pop();
        int width = st.empty() ? i : i - st.top() - 1;
        maxArea = max(maxArea, height * width);
    }
    st.push(i);
}

// Previous Smaller (Monotonic Increasing Stack)
for (int i = 0; i < n; i++) {
    while (!st.empty() && nums[st.top()] >= nums[i]) st.pop();
    prevSmaller[i] = st.empty() ? -1 : st.top();
    st.push(i);
}
```

---

**← [Back to README](../README.md)**
