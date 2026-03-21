# DSA Patterns Masterclass - Visual Guide

## Algorithm Patterns

**A Visual Guide to Algorithmic Thinking**

- 10 Core Patterns
- Visual Simulations  
- Step-by-Step

---

## Patterns Overview

| # | Pattern Name | # | Pattern Name |
|---|-------------|---|-------------|
| 01 | Sliding Window | 06 | Backtracking |
| 02 | Two Pointers | 07 | Greedy |
| 03 | Binary Search | 08 | Heap / Priority Queue |
| 04 | DFS / BFS | 09 | Graphs |
| 05 | Dynamic Programming | 10 | Stack |

---

# Pattern #1: Sliding Window

## Window Visualization

### CORE INTUITION

> **Expand → Break → Shrink → Repeat**

```
Array: [ 2  1  5  3  6 ]
           [====]
           left  right
```

**MENTAL MODEL**

Like a camera lens zooming in and out, adjusting focus until the picture is perfect.

---

## Visual Core

```
Initial State:
[ ]                    ← Empty window
1  2  3  4  5  6

After Expansion:
[=========]            ← Window covers elements
left       right       ← Pointers mark boundaries
```

**Key Properties:**
- **Window slides** - Moves across the array
- **Expands & contracts** - Size changes dynamically
- **Maintains a dynamic range** - Slides through the array

---

## How It Flows

### Flowchart

```
                    START
                      │
                      ▼
              ┌───────────────┐
              │   Expand      │
              │   Window      │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │   Check       │
              │   Condition   │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │  Condition    │─── NO ───▶ Shrink Window
              │  Met?         │           (Move left pointer)
              └───────┬───────┘
                      │
                     YES
                      │
                      ▼
              ┌───────────────┐
              │   Update      │
              │   Answer      │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │   Move        │
              │   Forward     │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │  REPEAT until │
              │  end reached  │
              └───────────────┘
```

---

## Step-by-Step Example

### Problem: Find maximum sum of subarray with size 2

**Input Array:** `[2, 1, 5, 1, 3, 2]`

---

### Step 1: Initial State

```
Array:  [2, 1, 5, 1, 3, 2]
         ↑  ↑
       left right

Window: [2, 1]

┌─────────────────────────────────────┐
│ left = 0                            │
│ right = 1                           │
│ sum = 2 + 1 = 3                     │
│ max_sum = 3                         │
└─────────────────────────────────────┘
```

---

### Step 2: Slide Right

```
Array:  [2, 1, 5, 1, 3, 2]
            ↑  ↑
          left right

Window: [1, 5]

┌─────────────────────────────────────┐
│ left = 1                            │
│ right = 2                           │
│ sum = 6 (3 - 2 + 5)                 │
│ max_sum = 6 ✓ NEW MAX FOUND!        │
│                                     │
│ Action: Subtract 2, Add 5           │
└─────────────────────────────────────┘
```

---

### Step 3: Continue Sliding

```
Array:  [2, 1, 5, 1, 3, 2]
               ↑  ↑
             left right

Window: [5, 1]

┌─────────────────────────────────────┐
│ left = 2                            │
│ right = 3                           │
│ sum = 6 (6 - 1 + 1)                 │
│ max_sum = 6 (unchanged)             │
│                                     │
│ Action: Subtract 1, Add 1           │
│ Note: Sum unchanged                 │
└─────────────────────────────────────┘
```

---

### Step 4: Final Result

```
Array:  [2, 1, 5, 1, 3, 2]
                  ↑  ↑
                left right

Window: [5, 3]  (Note: This is one of the final windows checked)

┌─────────────────────────────────────┐
│ ╔═══════════════════════════════╗   │
│ ║    FINAL ANSWER: 8            ║   │
│ ║    max_sum from window [5,3]  ║   │
│ ╚═══════════════════════════════╝   │
│                                     │
│ Previous windows traced:            │
│ [2,1]=3 → [1,5]=6 → [5,1]=6 →       │
│ [1,3]=4 → [3,2]=5                   │
│                                     │
│ Maximum found: [5,3]=8 ✓            │
└─────────────────────────────────────┘
```

---

## Template Code

### Pseudocode

```python
def sliding_window(arr):
    left = 0
    right = 0
    result = initial_value
    
    while right < len(arr):
        # EXPAND PHASE: Grow window by moving right pointer
        # Add arr[right] to current window state
        
        while condition_fails():  # SHRINK PHASE
            # Contract window by moving left pointer
            # Remove arr[left] from current window state
            left += 1
        
        # UPDATE ANSWER: Store optimal result
        result = optimal(result, current_window)
        
        right += 1  # Move forward
    
    return result
```

### Time Complexity: O(n)

Each element is visited at most twice (once by right, once by left).

---

## When to Use

### Pattern Matching Triggers

| Problem Keyword | Pattern to Use | Example Problems |
|-----------------|----------------|------------------|
| "Subarray / Substring" | Sliding Window | Longest substring without repeating characters |
| "Contiguous Elements" | Sliding Window | Maximum sum subarray of size K |
| "Max / Min Sum" | Sliding Window | Minimum size subarray sum |
| "Window Size" | Sliding Window | Sliding window maximum |

> **Tip:** Look for these keywords in problem statements

---

## Types of Sliding Window Problems

### 1. Fixed Size Window

```python
def fixed_size_window(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # Slide window
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

**Use Cases:**
- Maximum sum subarray of size K
- First negative number in every window of size K
- Maximum of all subarrays of size K

---

### 2. Variable Size Window

```python
def variable_size_window(arr, target):
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0
```

**Use Cases:**
- Minimum size subarray sum
- Longest substring with at most K distinct characters
- Longest substring without repeating characters

---

## Watch Out! Common Mistakes to Avoid

### Mistake #1: Forgetting to Update Left Pointer

```python
# ❌ WRONG - Infinite loop
while condition_fails():
    # Forgot to increment left!
    pass

# ✅ CORRECT
while condition_fails():
    left += 1  # Always move left to shrink
```

**Consequence:** Infinite loop, program never terminates.

---

### Mistake #2: Not Handling Empty Windows

```python
# ❌ WRONG - Edge case crash
while left <= right:  # Window can become empty
    if arr[left] == target:
        return left

# ✅ CORRECT - Handle empty window
while left <= right:
    if left > right:  # Check for empty window
        break
    if arr[left] == target:
        return left
    left += 1
```

**Consequence:** IndexError or incorrect results when window empties.

---

### Mistake #3: Off-by-One Errors

```python
# Clarify your window bounds:
# [left, right]  - inclusive on both ends (size = right - left + 1)
# [left, right)  - exclusive on right (size = right - left)

# ❌ WRONG - Mixing conventions
window_size = right - left  # But using inclusive bounds!

# ✅ CORRECT - Consistent convention
window_size = right - left + 1  # For [left, right]
```

**Consequence:** Incorrect window size calculation.

---

### Mistake #4: Using Nested Loops Incorrectly

```python
# ❌ WRONG - O(n²) complexity
for i in range(n):
    for j in range(i, n):
        # This is NOT sliding window!

# ✅ CORRECT - O(n) sliding window
left = 0
for right in range(n):
    # Expand
    while condition():
        # Shrink
        left += 1
```

**Consequence:** Time Limit Exceeded on large inputs.

---

## Edge Cases to Test

| Edge Case | Example | Expected Behavior |
|-----------|---------|-------------------|
| Empty array | `[]` | Return 0 or handle gracefully |
| Single element | `[5]` | Return the element |
| All same elements | `[3, 3, 3, 3]` | Works normally |
| All negative numbers | `[-1, -2, -3]` | Track maximum correctly |
| Window size = array length | `arr=[1,2,3], k=3` | Return sum of all |
| Window size > array length | `arr=[1,2], k=5` | Handle gracefully |
| Target larger than sum | `arr=[1,2,3], target=100` | Return appropriate value |

---

## Sliding Window vs Two Pointers

### Comparison Table

| Aspect | Sliding Window | Two Pointers |
|--------|----------------|--------------|
| **Type** | Dynamic Range | Fixed Positions |
| **Window Size** | Changes dynamically | Pointers maintain relative positions |
| **Movement** | Expand & contract on demand | Both pointers move in tandem |
| **Focus** | Contiguous elements (subarrays) | Pairs meeting conditions |
| **Example Problem** | Maximum sum subarray of size K | Two sum in sorted array |

### When to Use Which?

```
Sliding Window:
- Need a CONTIGUOUS range of elements
- Window size may change
- Optimizing sum/count within window

Two Pointers:
- Looking for PAIRS that satisfy condition
- Usually on sorted arrays
- Pointers move independently based on condition
```

---

## Classic Problems

### Problem 1: Longest Substring Without Repeating Characters

```python
def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

### Problem 2: Minimum Window Substring

```python
from collections import Counter

def min_window(s: str, t: str) -> str:
    if not s or not t:
        return ""
    
    target_counts = Counter(t)
    required = len(target_counts)
    
    left = 0
    formed = 0
    window_counts = {}
    
    ans = (float('inf'), 0, 0)  # (length, left, right)
    
    for right, char in enumerate(s):
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in target_counts and window_counts[char] == target_counts[char]:
            formed += 1
        
        while left <= right and formed == required:
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            left_char = s[left]
            window_counts[left_char] -= 1
            if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                formed -= 1
            
            left += 1
    
    return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]
```

---

# Pattern #2: Two Pointers

## CORE INTUITION

> **Two anchors, converging or diverging**

```
→         ←
L         R

Pointers can move:
- Toward each other (converging)
- Away from each other (diverging)
- Same direction (fast/slow)
```

**MENTAL MODEL**

Like two detectives searching from opposite ends of a crime scene, meeting in the middle.

---

## Visual Core

```
L →                           ← R
1       3       4       6       8       9
0       1       2       3       4       5

┌─────────────────────────────────────────────┐
│ Start: L = 0, R = n - 1                     │
│ Move:  L++ or R-- based on condition        │
│ Stop:  L >= R (pointers cross)              │
└─────────────────────────────────────────────┘
```

---

## How It Flows

### Flowchart

```
        ┌─────────────────┐
        │   INITIALIZE    │
        │  L = 0, R = n-1 │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │   WHILE LOOP    │◀─────────────────┐
        │   L < R         │                  │
        └────────┬────────┘                  │
                 │                           │
                 ▼                           │
        ┌─────────────────┐                  │
        │    COMPARE      │                  │
        │ arr[L] vs arr[R]│                  │
        └────────┬────────┘                  │
                 │                           │
                 ▼                           │
        ┌─────────────────┐                  │
        │ Match or Move?  │                  │
        └────────┬────────┘                  │
                 │                           │
        ┌────────┴────────┐                  │
        │                 │                  │
      MATCH           NO MATCH               │
        │                 │                  │
        ▼                 ▼                  │
┌───────────────┐  ┌───────────────┐         │
│    FOUND!     │  │ MOVE POINTERS │         │
│ Return result │  │ L++ or R--    │─────────┘
└───────────────┘  └───────────────┘
```

---

## Step-by-Step Example

### Problem: Find two numbers that sum to target = 9

**Input Array:** `[1, 2, 3, 4, 5, 6, 7, 8]` (sorted)

---

### Step 1: Initial State

```
Array: [1, 2, 3, 4, 5, 6, 7, 8]
       L                    R
       0                    7

┌─────────────────────────────────────┐
│ Left Pointer:  L = 0                │
│ Right Pointer: R = 7                │
│ arr[L] = 1, arr[R] = 8              │
│ Current Sum: 1 + 8 = 9              │
│ Target: 9                           │
└─────────────────────────────────────┘
```

---

### Step 2: Compare

```
Array: [1, 2, 3, 4, 5, 6, 7, 8]
       L                    R

┌─────────────────────────────────────┐
│ ╔═════════════════════════════════╗ │
│ ║    COMPARISON RESULT:           ║ │
│ ║    arr[L] = 1                   ║ │
│ ║    arr[R] = 8                   ║ │
│ ║    Sum = 9, Target = 9 ✓        ║ │
│ ║                                 ║ │
│ ║    FOUND MATCH!                 ║ │
│ ╚═════════════════════════════════╝ │
│                                     │
│ Result: Indices [0, 7], Values [1, 8]│
└─────────────────────────────────────┘
```

---

## Adjusting Pointers Example

### Problem: Find two numbers that sum to target = 10

**Input Array:** `[1, 2, 3, 4, 5, 6]` (sorted)

---

### Iteration 1

```
Array: [1, 2, 3, 4, 5, 6]
       L              R
       0              5

┌─────────────────────────────────────┐
│ arr[L] = 1, arr[R] = 6              │
│ Sum = 7, Target = 10                │
│                                     │
│ Decision: 7 < 10 → Need LARGER sum  │
│ Action: Move L right (L++)          │
│                                     │
│ Why? Moving L right increases sum   │
│ (array is sorted ascending)         │
└─────────────────────────────────────┘
```

---

### Iteration 2

```
Array: [1, 2, 3, 4, 5, 6]
          L           R
          1           5

┌─────────────────────────────────────┐
│ arr[L] = 2, arr[R] = 6              │
│ Sum = 8, Target = 10                │
│                                     │
│ Decision: 8 < 10 → Need LARGER sum  │
│ Action: Move L right (L++)          │
└─────────────────────────────────────┘
```

---

### Iteration 3

```
Array: [1, 2, 3, 4, 5, 6]
             L        R
             2        5

┌─────────────────────────────────────┐
│ arr[L] = 3, arr[R] = 6              │
│ Sum = 9, Target = 10                │
│                                     │
│ Decision: 9 < 10 → Need LARGER sum  │
│ Action: Move L right (L++)          │
└─────────────────────────────────────┘
```

---

### Iteration 4

```
Array: [1, 2, 3, 4, 5, 6]
                L     R
                3     5

┌─────────────────────────────────────┐
│ arr[L] = 4, arr[R] = 6              │
│ Sum = 10, Target = 10 ✓             │
│                                     │
│ ╔═══════════════════════════════╗   │
│ ║    FOUND!                     ║   │
│ ║    Indices: [3, 5]            ║   │
│ ║    Values: [4, 6]             ║   │
│ ╚═══════════════════════════════╝   │
└─────────────────────────────────────┘
```

---

## Template Code

### Pseudocode

```python
def two_pointers(arr, target):
    # Initialize Opposite Ends
    L = 0
    R = len(arr) - 1
    
    # Compare & Move
    while L < R:
        current_sum = arr[L] + arr[R]
        
        if current_sum == target:
            return [L, R]  # Found!
        elif current_sum < target:
            L += 1  # Need larger sum
        else:
            R -= 1  # Need smaller sum
    
    return [-1, -1]  # Not found
```

### Complexity Analysis

| Metric | Value | Explanation |
|--------|-------|-------------|
| Time Complexity | O(n) | Single pass through array |
| Space Complexity | O(1) | Only uses two pointers |

---

## Types of Two Pointers

### Type 1: Opposite Direction (Converging)

```python
# Left and Right pointers move toward each other
L, R = 0, len(arr) - 1
while L < R:
    if condition:
        L += 1
    else:
        R -= 1
```

**Use Cases:**
- Two Sum (sorted array)
- Valid Palindrome
- Container With Most Water
- Trapping Rain Water

---

### Type 2: Same Direction (Fast/Slow)

```python
# Both pointers move in same direction at different speeds
slow = fast = 0
while fast < len(arr):
    slow += 1
    fast += 2  # Fast moves twice as fast
```

**Use Cases:**
- Remove duplicates from sorted array
- Move zeros
- Linked list cycle detection
- Find middle of linked list

---

### Type 3: Parallel Pointers

```python
# Two pointers on different arrays
i = j = 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        i += 1
    else:
        j += 1
```

**Use Cases:**
- Merge two sorted arrays
- Intersection of two arrays
- Find median of two sorted arrays

---

## When to Use Two Pointers

| Problem Indicator | Example Problem |
|-------------------|-----------------|
| Sorted array | Two Sum II |
| Find pairs | 3Sum, 4Sum |
| Palindrome check | Valid Palindrome |
| Container problems | Container With Most Water |
| In-place modification | Remove Duplicates |
| Merging | Merge Sorted Arrays |

---

## Edge Cases to Test

| Edge Case | Example | Expected Behavior |
|-----------|---------|-------------------|
| Empty array | `[]` | Return not found |
| Single element | `[5]` | Can't form pair |
| No solution | `[1, 2, 3], target=100` | Return not found |
| Multiple solutions | `[1,2,3,4,5], target=5` | Return first found |
| Negative numbers | `[-3, -1, 0, 2, 4]` | Works with sorted |
| Duplicate values | `[1, 1, 2, 2, 3, 3]` | Handle correctly |

---

## Classic Problems

### Problem 1: Valid Palindrome

```python
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True
```

### Problem 2: Container With Most Water

```python
def max_area(height: list) -> int:
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        # Calculate current area
        current_area = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, current_area)
        
        # Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water
```

### Problem 3: 3Sum

```python
def three_sum(nums: list) -> list:
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates for first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result
```

---

# Pattern #3: Binary Search

## CORE INTUITION

> **Cut the search space in half each time**

**MENTAL MODEL**

Like finding a word in a dictionary — you never start from page 1, you jump to the middle and narrow down.

```
[1, 3, 5, 7, 9, 11, 13]
Sorted Array → O(log n) Search Time
```

---

## Visual Core

### Divide & Conquer

Always check the middle, then choose a side.

```
               MID
                ↓
1     3     5     7     9     11     13     15
                  │
         ┌────────┴────────┐
         │                 │
    Search Left      Search Right
    (if target < mid) (if target > mid)
```

### Binary Search Steps

```
Step 1: Compare with Mid
         │
         ▼
Step 2: Discard Half
         │
         ▼
Step 3: Repeat
```

---

## Template & When to Use

### Basic Template

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # or: left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found
```

### When to Use

| Indicator | Requirement |
|-----------|-------------|
| **Sorted Array** | Array must be sorted |
| **Find Index** | Locate target position |
| **O(log n) Required** | Need fast search time |

**Time Complexity:** O(log n)

---

## Binary Search Variants

### 1. Find First Occurrence (Lower Bound)

```python
def find_first_occurrence(arr, target):
    left, right = 0, len(arr)
    result = -1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1
    
    return left if left < len(arr) and arr[left] == target else -1
```

### 2. Find Last Occurrence (Upper Bound)

```python
def find_last_occurrence(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1
    
    return left - 1 if arr[left - 1] == target else -1
```

### 3. Search in Rotated Sorted Array

```python
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1
```

---

## Edge Cases for Binary Search

| Edge Case | Example | Consideration |
|-----------|---------|---------------|
| Empty array | `[]` | Return -1 immediately |
| Single element | `[5]` | Check if equal to target |
| Target not present | `[1,2,3], target=5` | Return -1 |
| All same elements | `[3,3,3,3]` | Use lower/upper bound |
| Integer overflow | Large indices | Use `mid = left + (right - left) // 2` |
| Duplicates | `[1,2,2,2,3]` | Decide which occurrence to return |

---

## Common Binary Search Problems

### Problem 1: Find Minimum in Rotated Sorted Array

```python
def find_min(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    return nums[left]
```

### Problem 2: Search Insert Position

```python
def search_insert(nums, target):
    left, right = 0, len(nums)
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left
```

---

# Pattern #4: DFS / BFS

## Depth-First Search vs Breadth-First Search

| DFS (Depth-First Search) | BFS (Breadth-First Search) |
|--------------------------|----------------------------|
| **CORE INTUITION:** Go as deep as possible first | **CORE INTUITION:** Explore all neighbors at current level |
| **MENTAL MODEL:** Like exploring a maze keeping one hand on the wall | **MENTAL MODEL:** Like ripples spreading from a stone dropped in water |
| **Data Structure:** Stack (or recursion) | **Data Structure:** Queue |
| **Memory:** O(h) where h is height | **Memory:** O(w) where w is width |

---

## Visual Exploration

### DFS Path: A → B → D → E → C → F

```
DFS Traversal Order:
A → B → D → E → C → F

Tree Structure:
        A (Start, Level 0, 1st visited)
       / \
      B   C
     / \   \
    D   E   F

Visitation Order:
A: Level 0 (Start)
B: Level 1 (2nd)
D: Level 2 (3rd)
E: Level 2 (4th)  ← Backtrack from D
C: Level 1 (5th)  ← Backtrack from E
F: Level 2 (6th)

Strategy: Go Deep → Backtrack → Repeat
```

### BFS Path: A → B → C → D → E → F

```
BFS Traversal Order:
A → B → C → D → E → F

Tree Structure:
        A (Level 0)
       / \
      B   C (Level 1)
     / \   \
    D   E   F (Level 2)

Visitation Order:
A: Level 0 (Start)
B: Level 1 (2nd)
C: Level 1 (3rd)
D: Level 2 (4th)
E: Level 2 (5th)
F: Level 2 (6th)

Strategy: Level by Level → All Neighbors First
```

---

## DFS Templates

### Recursive DFS

```python
def dfs_recursive(node, visited):
    if node in visited:
        return
    
    visited.add(node)
    # Process node
    
    for neighbor in get_neighbors(node):
        dfs_recursive(neighbor, visited)
```

### Iterative DFS (Stack)

```python
def dfs_iterative(start):
    stack = [start]
    visited = set()
    
    while stack:
        node = stack.pop()
        
        if node in visited:
            continue
        
        visited.add(node)
        # Process node
        
        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                stack.append(neighbor)
```

---

## BFS Templates

### Standard BFS (Queue)

```python
from collections import deque

def bfs(start):
    queue = deque([start])
    visited = set([start])
    
    while queue:
        node = queue.popleft()
        # Process node
        
        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### Level-order BFS

```python
from collections import deque

def bfs_level_order(start):
    queue = deque([start])
    visited = set([start])
    
    while queue:
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            # Process node at current level
            
            for neighbor in get_neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
```

---

## When to Use DFS vs BFS

| Use DFS When... | Use BFS When... |
|-----------------|-----------------|
| Find any path | Find shortest path |
| Check if path exists | Level-order traversal |
| Find all paths | Minimum steps to reach target |
| Cycle detection | Connected components size |
| Topological sort | Web crawler |

---

## Edge Cases for Graph Traversal

| Edge Case | Consideration |
|-----------|---------------|
| Empty graph | Handle no nodes |
| Single node | Process correctly |
| Disconnected components | May need multiple traversals |
| Self-loops | Avoid infinite loops |
| Cycles | Always track visited |
| Directed vs Undirected | Neighbor relationship differs |

---

# Pattern #5: Dynamic Programming

## CORE INTUITION

> **Store solutions to subproblems**

### Building Solutions from Subproblems

**MENTAL MODEL**

Like building a pyramid from the bottom up — each level relies on the one below.

```
Fibonacci Sequence: 1, 1, 2, 3, 5, 8
DP Array:          [0][1][2][3][4][5]

Each cell depends on previous solutions:
dp[i] = dp[i-1] + dp[i-2]
```

---

## Template

```python
def dynamic_programming(n):
    # Initialize DP array
    dp = [0] * (n + 1)
    dp[0] = base_case_0
    dp[1] = base_case_1
    
    # Fill DP table
    for i in range(2, n + 1):
        dp[i] = optimal(dp[i-1], dp[i-2], ...)
    
    return dp[n]
```

---

## When to Use

| Indicator | Description |
|-----------|-------------|
| **Optimal Substructure** | Can break into smaller problems |
| **Overlapping Subproblems** | Can reuse computed results |

---

## Types of DP

### 1. 1D DP

```python
# Example: Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

### 2. 2D DP

```python
# Example: Unique Paths
def unique_paths(m, n):
    dp = [[0] * n for _ in range(m)]
    
    # Initialize first row and column
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    
    # Fill DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]
```

### 3. Space-Optimized DP

```python
# Example: Fibonacci with O(1) space
def fibonacci_optimized(n):
    if n <= 1:
        return n
    
    prev, curr = 0, 1
    
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr
```

---

## Common DP Problems

### Problem 1: Coin Change

```python
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1
```

### Problem 2: Longest Common Subsequence

```python
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]
```

---

# Pattern #6: Backtracking

## CORE INTUITION

> **Try all paths, undo if stuck**

### Decision Tree: Explore & Backtrack

```
            A
           / \
          B   C
         / \
        ✗   ✓
     backtrack  Valid Solution!
```

**MENTAL MODEL**

Like a maze solver — try a path, hit a wall? Back up and try another.

---

## Template

```python
def backtrack(path, choices):
    # Base case: found a solution
    if is_complete(path):
        result.append(path[:])  # Make a copy!
        return
    
    # Try each choice
    for choice in choices:
        # Make choice
        path.append(choice)
        
        # Recurse
        backtrack(path, remaining_choices)
        
        # Undo choice (backtrack)
        path.pop()
```

---

## When to Use

| Problem Type | Example |
|--------------|---------|
| All Combinations | Subsets, Combination Sum |
| Permutations | Permutations, Next Permutation |
| Constraint Satisfaction | N-Queens, Sudoku |
| All Paths | All paths from source to target |

---

## Classic Backtracking Problems

### Problem 1: Subsets

```python
def subsets(nums):
    result = []
    
    def backtrack(start, path):
        result.append(path[:])
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result
```

### Problem 2: Permutations

```python
def permute(nums):
    result = []
    
    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False
    
    backtrack([], [False] * len(nums))
    return result
```

### Problem 3: N-Queens

```python
def solve_n_queens(n):
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    def is_safe(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check diagonal (upper left)
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i, j = i - 1, j - 1
        
        # Check diagonal (upper right)
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i, j = i - 1, j + 1
        
        return True
    
    def backtrack(row):
        if row == n:
            result.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'
    
    backtrack(0)
    return result
```

---

## Edge Cases for Backtracking

| Edge Case | Consideration |
|-----------|---------------|
| Empty input | Return empty result |
| Single element | Handle as base case |
| Duplicates | May need to skip |
| Large search space | Consider pruning |
| No valid solution | Return empty |

---

# Pattern #7: Greedy Algorithms

## CORE INTUITION

> **Make the best local choice at each step**

### Example: Activity Selection

```
Step 1: Sort by end time
        [A:2-5, B:1-3, C:4-7]
        
Step 2: Take earliest ending
        B:1-3 ✓
        
Step 3: Next non-overlapping
        A:2-5 ✓
        
Result: Selected 2 activities (optimal!)
```

**MENTAL MODEL**

Like a mountain climber always choosing the steepest path up — sometimes it works perfectly!

---

## Template

```python
def greedy(choices):
    sort(choices)  # Sort by some criteria
    
    result = []
    for choice in choices:
        if is_valid(choice):
            result.append(choice)  # Take it
    
    return result
```

---

## When to Use

| Indicator | Example |
|-----------|---------|
| Optimization problems | Minimum coins, Maximum activities |
| Local = Global optimum | Greedy choice property |
| Activity selection | Interval scheduling |
| Huffman coding | Data compression |

---

## Greedy vs DP

| Aspect | Greedy | Dynamic Programming |
|--------|--------|---------------------|
| Time Complexity | O(n log n) | O(n²) or higher |
| Space Complexity | O(1) or O(n) | O(n) or O(n²) |
| When it works | Local optimal = Global optimal | Always finds optimal |
| Simplicity | Simpler | More complex |

> **Greedy is simpler when it works!**

---

## Classic Greedy Problems

### Problem 1: Jump Game

```python
def can_jump(nums):
    max_reach = 0
    
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
    
    return True
```

### Problem 2: Meeting Rooms

```python
def can_attend_meetings(intervals):
    intervals.sort(key=lambda x: x[0])
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    
    return True
```

---

# Pattern #8: Heap / Priority Queue

## CORE INTUITION

> **Always get the min/max efficiently**

### Heap Structure

**Min-Heap:**
```
      1         ← Smallest at root
     / \
    3   2
   / \
  5   4
```

**Max-Heap:**
```
      9         ← Largest at root
     / \
    7   8
   / \
  5   6
```

**MENTAL MODEL**

Like a VIP line at a club — the most important element always gets served first.

---

## Template

```python
import heapq

# Min-heap (default)
heap = []
heapq.heappush(heap, item)
smallest = heapq.heappop(heap)

# Max-heap (negate values)
max_heap = []
heapq.heappush(max_heap, -item)
largest = -heapq.heappop(max_heap)
```

**Time Complexity:** O(log n) per operation

---

## When to Use

| Use Case | Example Problems |
|----------|------------------|
| K-th Largest | Kth Largest Element |
| Top K Elements | Top K Frequent Elements |
| Merge K Lists | Merge K Sorted Lists |
| Scheduling | Task Scheduler |
| Streaming | Median of Data Stream |

---

## Classic Heap Problems

### Problem 1: Kth Largest Element

```python
import heapq

def find_kth_largest(nums, k):
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]
```

### Problem 2: Merge K Sorted Lists

```python
import heapq

def merge_k_lists(lists):
    heap = []
    
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))
    
    dummy = ListNode(0)
    current = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next
```

---

# Pattern #9: Graph Algorithms

## CORE INTUITION

> **Model relationships and connections**

### Graph Structure

```
    B ─────── C
   /          |
  A           |
   \          |
    D ─────── E

Nodes: A, B, C, D, E
Edges: A-B, B-C, C-E, A-D, D-E
```

**MENTAL MODEL**

Like a social network — nodes are people, edges are friendships.

---

## Template

```python
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph
```

---

## Common Graph Patterns

| Pattern | Use Case |
|---------|----------|
| **BFS** | Shortest path in unweighted graph |
| **DFS** | Cycle detection, topological sort |
| **Union-Find** | Connected components |
| **Dijkstra** | Weighted shortest path |
| **Topological Sort** | Dependency resolution |

---

## Classic Graph Algorithms

### Algorithm 1: BFS for Shortest Path

```python
def shortest_path(graph, start, end):
    queue = deque([(start, 0)])
    visited = set([start])
    
    while queue:
        node, distance = queue.popleft()
        
        if node == end:
            return distance
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    
    return -1
```

### Algorithm 2: Union-Find

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        
        return True
```

---

# Pattern #10: Stack / Monotonic Stack

## CORE INTUITION

> **LIFO structure with monotonic property**

### Stack Structure

**Basic Stack (LIFO):**
```
4  ← TOP (Last In, First Out)
3
2
1  ← BOTTOM
```

**Monotonic Increasing Stack:**
```
8  ← TOP
6
4
2  ← BOTTOM

Property: Elements increase from bottom to top
```

**MENTAL MODEL**

Like a stack of plates — only the top plate is accessible, maintaining order is key.

---

## Template

```python
def monotonic_stack(nums):
    stack = []
    result = [0] * len(nums)
    
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            idx = stack.pop()
            result[idx] = i - idx  # Distance to next greater
        
        stack.append(i)
    
    return result
```

**Operations:**
- **Push** - Add to top
- **Pop** - Remove from top
- **Maintains Order** - Monotonic property

---

## When to Use

| Problem | Description |
|---------|-------------|
| Next Greater Element | Find next larger element |
| Valid Parentheses | Check balanced brackets |
| Largest Histogram | Largest rectangle in histogram |
| Temperature Problem | Daily temperatures |

---

## Classic Stack Problems

### Problem 1: Valid Parentheses

```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    
    return len(stack) == 0
```

### Problem 2: Next Greater Element

```python
def next_greater_element(nums):
    n = len(nums)
    result = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    
    return result
```

### Problem 3: Largest Rectangle in Histogram

```python
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Sentinel
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area
```

---

## Edge Cases for Stack

| Edge Case | Consideration |
|-----------|---------------|
| Empty stack | Handle pop on empty |
| Single element | Process correctly |
| All same elements | Monotonic property |
| Descending/Ascending | Different behaviors |
| Circular array | Need two passes |

---

# Pattern Selection Quick Guide

## Decision Flow

```
Decode problem → Choose pattern → Solve
```

## Pattern Matching Table

| Problem Keywords | Pattern to Use |
|------------------|----------------|
| Subarray, Substring | Sliding Window |
| Sorted Array, Pairs | Two Pointers |
| Find Index, O(log n) | Binary Search |
| Shortest Path, Level Order | BFS |
| All Paths, Cycle Detect | DFS |
| All Combinations | Backtracking |
| Optimal Substructure | Dynamic Programming |
| Local = Global Optimum | Greedy |
| K-th Element, Top K | Heap / Priority Queue |
| Connections, Relationships | Graphs |
| Next Greater Element | Monotonic Stack |
| Valid Parentheses | Stack |

---

## Pattern Combination Tips

> **Pro Tip:** Many problems combine multiple patterns. Start with the most obvious one!

### Common Combinations

| Combination | Example Problem |
|-------------|-----------------|
| Sliding Window + Hash Map | Longest Substring Without Repeating |
| Two Pointers + Sorting | 3Sum |
| DFS + Backtracking | N-Queens |
| BFS + Priority Queue | Dijkstra's Algorithm |
| Binary Search + Greedy | Split Array Largest Sum |
| DP + Binary Search | Longest Increasing Subsequence (O(n log n)) |

---

# Master DSA Patterns

## Practice makes perfect

### 4-Step Mastery Framework

| Step | Focus | Action |
|------|-------|--------|
| **1. Identify the Pattern** | Match problem keywords to pattern types | Read problem carefully, spot keywords |
| **2. Understand the Flow** | Visualize state changes and pointer movements | Draw diagrams, trace examples |
| **3. Master the Templates** | Memorize core code patterns for each type | Practice templates until automatic |
| **4. Avoid Common Mistakes** | Learn from pitfalls and edge cases | Test edge cases systematically |

---

## Quick Reference Cheat Sheet

### Pattern → Time/Space Complexity

| Pattern | Typical Time | Typical Space |
|---------|-------------|---------------|
| Sliding Window | O(n) | O(1) or O(k) |
| Two Pointers | O(n) | O(1) |
| Binary Search | O(log n) | O(1) |
| DFS | O(V + E) | O(V) |
| BFS | O(V + E) | O(V) |
| Dynamic Programming | O(n²) typical | O(n) or O(n²) |
| Backtracking | O(n! or 2^n) | O(n) |
| Greedy | O(n log n) | O(1) or O(n) |
| Heap | O(n log k) | O(k) |
| Stack | O(n) | O(n) |

---

## Final Tips

1. **Always clarify the problem** before jumping to code
2. **Start with brute force** to understand the problem
3. **Look for optimizations** using patterns
4. **Test edge cases** before submitting
5. **Practice consistently** - patterns become intuitive with repetition

> **Start practicing on LeetCode today!**

---

## Recommended Practice Order

| Level | Patterns | Problems |
|-------|----------|----------|
| Beginner | Sliding Window, Two Pointers, Binary Search | 50-100 problems |
| Intermediate | DFS, BFS, Stack | 100-150 problems |
| Advanced | DP, Backtracking, Graphs | 150-200 problems |
| Expert | Heap, Greedy, Combinations | 200+ problems |

---


