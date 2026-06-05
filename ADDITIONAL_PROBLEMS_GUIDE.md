# Additional DSA Problems - Skill-Matched Variants 🚀

This document explains the 30 additional DSA problems added to strengthen your fundamentals. Each new problem is paired with an original problem and targets the same algorithmic skills.

## Overview

- **Original Problems:** 35 (across 15 categories)
- **Additional Problems:** 30 (new variants with same skills)
- **Total Problems:** 65
- **Difficulty Range:** Easy to Hard

Each new problem includes:
- ✅ Skill focus area
- 🔗 Link to similar original problem
- 📊 Difficulty level
- 💡 Hints and approach
- ⏱️ Estimated time to solve

---

## Category-by-Category Breakdown

### 1. Sliding Window (3 original → 6 total)

**sw-4: Longest Substring Without Repeating Characters (Variant)**
- **Skill Focus:** Sliding window with hash map tracking
- **Similar to:** sw-1
- **Key Concepts:** Two-pointer window, character frequency tracking
- **Approach:** Maintain a window [left, right] and use hash map to track character positions

**sw-5: Max Consecutive Ones III**
- **Skill Focus:** Sliding window with counter constraint
- **Similar to:** sw-2
- **Key Concepts:** Constraint-based window, counter management
- **Approach:** Expand window while tracking zeros, contract when exceeding k

**sw-6: Minimum Window Substring (Variant)**
- **Skill Focus:** Sliding window with multiple requirements
- **Similar to:** sw-3
- **Key Concepts:** Complex window with frequency matching
- **Approach:** Two hash maps for target and window character frequencies

---

### 2. Array (1 original → 4 total)

**arr-2: Container With Most Water (Variant)**
- **Skill Focus:** Array traversal with greedy optimization
- **Similar to:** arr-1
- **Key Concepts:** Two-pointer, greedy strategy
- **Approach:** Start wide, move pointer at shorter height inward

**arr-3: Rotate Array**
- **Skill Focus:** In-place array manipulation
- **Similar to:** arr-1
- **Key Concepts:** Array rotation, reverse operations
- **Approach:** Use reversal technique on array segments

**arr-4: Best Time to Buy and Sell Stock**
- **Skill Focus:** Array traversal with state tracking
- **Similar to:** arr-1
- **Key Concepts:** Single pass, state management
- **Approach:** Track minimum price, calculate profit at each step

---

### 3. Binary Search (1 original → 4 total)

**bs-2: Search in Rotated Sorted Array**
- **Skill Focus:** Binary search with pivot detection
- **Similar to:** bs-1
- **Key Concepts:** Sorted half identification, conditional search
- **Approach:** Identify which half is sorted, search accordingly

**bs-3: Find First and Last Position of Element**
- **Skill Focus:** Binary search for boundaries
- **Similar to:** bs-1
- **Key Concepts:** Leftmost and rightmost search
- **Approach:** Two binary searches for boundaries

**bs-4: Peak Index in Mountain Array**
- **Skill Focus:** Binary search without explicit target
- **Similar to:** bs-1
- **Key Concepts:** Comparison-based search, peak finding
- **Approach:** Compare mid with neighbors, adjust search direction

---

### 4. DFS-BFS (4 original → 8 total)

**dfs-5: Number of Islands (Variant)**
- **Skill Focus:** DFS/BFS for connected components
- **Similar to:** dfs-1
- **Key Concepts:** Component counting, grid traversal
- **Approach:** DFS to mark connected cells, increment counter per component

**dfs-6: Clone Graph**
- **Skill Focus:** DFS with node mapping
- **Similar to:** dfs-2
- **Key Concepts:** Graph traversal with cloning, cycle handling
- **Approach:** Hash map for node tracking, DFS for traversal

**dfs-7: Course Schedule (Topological Sort)**
- **Skill Focus:** DFS for cycle detection and ordering
- **Similar to:** dfs-3
- **Key Concepts:** Topological sorting, cycle detection
- **Approach:** Color-coded DFS for cycle detection and ordering

**dfs-8: Word Ladder**
- **Skill Focus:** BFS for shortest path
- **Similar to:** dfs-4
- **Key Concepts:** Level-order BFS, shortest path
- **Approach:** Implicit graph construction, BFS exploration

---

### 5. Tree Traversal (2 original → 5 total)

**tree-3: Lowest Common Ancestor of BST**
- **Skill Focus:** Tree traversal with value comparison
- **Similar to:** tree-1
- **Key Concepts:** BST property, path finding
- **Approach:** Use BST property for efficient LCA finding

**tree-4: Binary Tree Maximum Path Sum**
- **Skill Focus:** Post-order traversal with state tracking
- **Similar to:** tree-2
- **Key Concepts:** DP on trees, path computation
- **Approach:** Post-order DFS to calculate max paths through each node

**tree-5: Serialize and Deserialize Binary Tree**
- **Skill Focus:** Pre-order traversal with encoding
- **Similar to:** tree-1
- **Key Concepts:** Tree encoding, reconstruction
- **Approach:** Pre-order traversal with null markers for serialization

---

### 6. Dynamic Programming (3 original → 6 total)

**dp-4: Longest Increasing Subsequence**
- **Skill Focus:** DP with state array tracking
- **Similar to:** dp-1
- **Key Concepts:** State definition, optimal substructure
- **Approach:** dp[i] = LIS length ending at i

**dp-5: Coin Change**
- **Skill Focus:** DP with bounded knapsack
- **Similar to:** dp-2
- **Key Concepts:** Unbounded knapsack, state transitions
- **Approach:** dp[i] = min coins for amount i

**dp-6: Word Break II**
- **Skill Focus:** DP with backtracking and memoization
- **Similar to:** dp-3
- **Key Concepts:** DP + backtracking, memoization
- **Approach:** DP for valid points, backtracking for combinations

---

### 7. Intervals (3 original → 6 total)

**int-4: Non-overlapping Intervals**
- **Skill Focus:** Greedy interval selection
- **Similar to:** int-1
- **Key Concepts:** Greedy strategy, overlap detection
- **Approach:** Sort by end time, greedily select non-overlapping

**int-5: Insert Interval**
- **Skill Focus:** Interval insertion and merging
- **Similar to:** int-2
- **Key Concepts:** Interval comparison, merging logic
- **Approach:** Three-case handling: before, overlap, after

**int-6: Minimum Meeting Rooms**
- **Skill Focus:** Interval scheduling with priority queue
- **Similar to:** int-3
- **Key Concepts:** Scheduling optimization, priority queue
- **Approach:** Sort meetings, use min-heap for room management

---

### 8. Two Pointers (2 original → 4 total)

**tp-3: 3Sum**
- **Skill Focus:** Two pointers with fixed element
- **Similar to:** tp-1
- **Key Concepts:** Pointer technique, duplicate handling
- **Approach:** Sort, fix element, two pointers for complement

**tp-4: Trapping Rain Water**
- **Skill Focus:** Two pointers with state tracking
- **Similar to:** tp-2
- **Key Concepts:** Two-pointer, state management
- **Approach:** Track left/right max, move smaller pointer

---

### 9. Sum (1 original → 3 total)

**sum-2: Two Sum II - Input Array is Sorted**
- **Skill Focus:** Two pointer sum finding with sorted input
- **Similar to:** sum-1
- **Key Concepts:** Optimization with sorting, two pointers
- **Approach:** Two pointers from both ends

**sum-3: Subarray Sum Equals K**
- **Skill Focus:** Prefix sum with hash map
- **Similar to:** sum-1
- **Key Concepts:** Prefix sum technique, hash map
- **Approach:** Cumulative sum with hash map tracking

---

### 10. Monotonic Stack (1 original → 3 total)

**ms-2: Largest Rectangle in Histogram**
- **Skill Focus:** Monotonic stack for range queries
- **Similar to:** ms-1
- **Key Concepts:** Stack-based range finding, area calculation
- **Approach:** Find left/right boundaries for each height

**ms-3: Daily Temperatures**
- **Skill Focus:** Monotonic decreasing stack
- **Similar to:** ms-1
- **Key Concepts:** Next greater element, index tracking
- **Approach:** Monotonic stack with temperature tracking

---

### 11. Word Break (1 original → 3 total)

**wb-2: Word Pattern**
- **Skill Focus:** Pattern matching with bidirectional mapping
- **Similar to:** wb-1
- **Key Concepts:** Bidirectional mapping, pattern validation
- **Approach:** Two hash maps for consistent mapping

**wb-3: Concatenated Words**
- **Skill Focus:** DFS/DP word composition
- **Similar to:** wb-1
- **Key Concepts:** Word composition, recursive checking
- **Approach:** DP to check word formation from other words

---

### 12. Bit Manipulation (2 original → 4 total)

**bit-3: Single Number III**
- **Skill Focus:** XOR with bit manipulation
- **Similar to:** bit-1
- **Key Concepts:** XOR properties, bit partitioning
- **Approach:** XOR all, use differing bit to partition

**bit-4: Number of 1 Bits**
- **Skill Focus:** Bit counting techniques
- **Similar to:** bit-1
- **Key Concepts:** Bit manipulation, Brian Kernighan's algorithm
- **Approach:** n & (n-1) to remove rightmost set bit

---

### 13. Trie (1 original → 3 total)

**trie-2: Word Search II**
- **Skill Focus:** Trie with DFS on board
- **Similar to:** trie-1
- **Key Concepts:** Trie + grid traversal, backtracking
- **Approach:** Build trie, DFS on board checking trie

**trie-3: Replace Words**
- **Skill Focus:** Trie for prefix matching and replacement
- **Similar to:** trie-1
- **Key Concepts:** Prefix matching, string manipulation
- **Approach:** Find shortest roots using trie

---

### 14. Combination (1 original → 3 total)

**comb-2: Combinations of Phone Number**
- **Skill Focus:** Combination generation with constraints
- **Similar to:** comb-1
- **Key Concepts:** Backtracking with mapping, string building
- **Approach:** Digit-to-letter mapping with backtracking

**comb-3: Combination Sum**
- **Skill Focus:** Combination with repetition allowed
- **Similar to:** comb-1
- **Key Concepts:** Backtracking with reuse, pruning
- **Approach:** Backtrack with repetition allowed

---

### 15. Backtracking (3 original → 6 total)

**bt-4: Sudoku Solver**
- **Skill Focus:** Backtracking with constraint satisfaction
- **Similar to:** bt-1
- **Key Concepts:** Complex constraints, state management
- **Approach:** Try each digit, validate, backtrack

**bt-5: Generate Parentheses**
- **Skill Focus:** Backtracking with balance tracking
- **Similar to:** bt-2
- **Key Concepts:** Count tracking, valid sequence generation
- **Approach:** Backtrack with open/close counts

**bt-6: Palindrome Partitioning**
- **Skill Focus:** Backtracking with validation
- **Similar to:** bt-3
- **Key Concepts:** Palindrome checking, string partitioning
- **Approach:** Find palindromes, backtrack with remaining string

---

## How to Use These Problems

### Learning Path

1. **Solve the original problem first** - Build foundational understanding
2. **Identify the key skill** - What technique/pattern is being used?
3. **Solve the new variant** - Apply same skill to different scenario
4. **Compare approaches** - Both problems should use similar algorithmic approach
5. **Optimize** - Can you improve time/space complexity?

### Example: Sliding Window

**Original (sw-1):** Longest substring without repeating chars
- Learn sliding window with hash map

**New (sw-4):** Same concept, similar approach
- Deepen understanding with new scenario

**New (sw-5):** Sliding window with constraints
- Extend to constraint-based windows

**New (sw-6):** Complex multi-requirement window
- Master advanced sliding window patterns

---

## Tips for Success

### 1. Pattern Recognition
- Notice how the same technique applies differently
- Build intuition for when to use which approach

### 2. Complexity Analysis
- Compare time/space complexity between variants
- Understand trade-offs in different approaches

### 3. Code Reusability
- Similar problems often share code structure
- Look for opportunities to generalize solutions

### 4. Difficulty Progression
- Start with easier variants
- Gradually tackle harder problems
- Build confidence as you progress

### 5. Time Tracking
- Track time spent on each problem
- Notice improvement over time
- Adjust difficulty based on performance

---

## Problem Difficulty Distribution

| Difficulty | Original | New | Total |
|-----------|----------|-----|-------|
| Easy | 1 | 3 | 4 |
| Medium | 18 | 17 | 35 |
| Hard | 16 | 10 | 26 |

---

## Category Expansion

| Category | Original | New | Total | Expansion |
|----------|----------|-----|-------|-----------|
| Sliding Window | 3 | 3 | 6 | 100% |
| Array | 1 | 3 | 4 | 300% |
| Binary Search | 1 | 3 | 4 | 300% |
| DFS-BFS | 4 | 4 | 8 | 100% |
| Tree Traversal | 2 | 3 | 5 | 150% |
| Dynamic Programming | 3 | 3 | 6 | 100% |
| Intervals | 3 | 3 | 6 | 100% |
| Two Pointers | 2 | 2 | 4 | 100% |
| Sum | 1 | 2 | 3 | 200% |
| Monotonic Stack | 1 | 2 | 3 | 200% |
| Word Break | 1 | 2 | 3 | 200% |
| Bit Manipulation | 2 | 2 | 4 | 100% |
| Trie | 1 | 2 | 3 | 200% |
| Combination | 1 | 2 | 3 | 200% |
| Backtracking | 3 | 3 | 6 | 100% |

---

## Recommended Study Schedule

### Week 1-2: Fundamentals
- Array problems (1-4)
- Sum problems (sum-1, sum-2)
- Basic Sliding Window (sw-1, sw-4)

### Week 3-4: Searching & Pointer Techniques
- Binary Search (bs-1 through bs-4)
- Two Pointers (tp-1 through tp-4)
- Advanced Sliding Window (sw-5, sw-6)

### Week 5-6: Tree & Graph
- Tree Traversal (tree-1 through tree-5)
- DFS-BFS (dfs-1 through dfs-8)
- Topological Sort (dfs-7)

### Week 7-8: Advanced Techniques
- Dynamic Programming (dp-1 through dp-6)
- Bit Manipulation (bit-1 through bit-4)
- Monotonic Stack (ms-1 through ms-3)

### Week 9-10: String & Pattern
- Trie (trie-1 through trie-3)
- Word Break (wb-1 through wb-3)
- Combination (comb-1 through comb-3)

### Week 11-12: Complex Problems
- Intervals (int-1 through int-6)
- Backtracking (bt-1 through bt-6)
- Mixed challenges

---

## Resources

- **Main Configuration:** `dsa-templates.json` (35 original problems)
- **Additional Problems:** `additional-dsa-problems.json` (30 new problems)
- **Manager Script:** `dsa_manager.py` (to access problems programmatically)
- **Skills Config:** `copilot-skills.json` (GitHub Copilot integration)

---

## Contributing

Found a better variant? Have suggestions for additional problems?

1. Fork the repository
2. Create a feature branch
3. Add your problem variant
4. Submit a PR with explanation

See `CONTRIBUTING.md` for detailed guidelines.

---

## Next Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/SwatiNH/dsa-daily-solver.git
   cd dsa-daily-solver
   git checkout feat/additional-dsa-problems
   ```

2. **Review both files:**
   - `dsa-templates.json` - Original 35 problems
   - `additional-dsa-problems.json` - New 30 problems

3. **Start solving!**
   - Pick a category
   - Solve original problem
   - Solve variant
   - Compare approaches

4. **Track your progress**
   - Use `PROGRESS_TEMPLATE.md`
   - Update daily
   - Review weekly

---

**Happy Learning! 🚀**

*Master each skill with multiple problems. Consistency builds expertise.*

