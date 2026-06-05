# Contributing to DSA Daily Solver

Thank you for helping build this resource for aspiring engineers! We welcome contributions in the form of solutions, improvements, and feedback.

## 📋 Contribution Guidelines

### Types of Contributions

1. **Problem Solutions** - Submit your solutions in any programming language
2. **Documentation** - Improve explanations and tutorials
3. **Bug Reports** - Report issues with problem links or metadata
4. **Feature Requests** - Suggest improvements to the repository structure

### Submitting a Solution

#### 1. Fork the Repository
```bash
git clone https://github.com/SwatiNH/dsa-daily-solver.git
cd dsa-daily-solver
git checkout -b solution/category/problem-id
```

#### 2. Create Your Solution Folder
Follow this structure:
```
SOLUTIONS/{category}/{problem-id}/{language}/
├── solution.{ext}           # Your solution code
├── README.md                # Explanation of approach
└── complexity-analysis.md   # Time and space complexity
```

**Example:**
```
SOLUTIONS/sliding-window/sw-1/python/
├── solution.py
├── README.md
└── complexity-analysis.md
```

#### 3. Solution Template

**README.md:**
```markdown
# Solution for [Problem Name]

## Problem Link
[Link to LeetCode/Problem]

## Approach
[Explain your approach and why you chose it]

## Key Insights
- Insight 1
- Insight 2
- Insight 3

## Edge Cases Handled
- Edge case 1
- Edge case 2

## Alternative Approaches
[Mention any alternative solutions you considered]
```

**complexity-analysis.md:**
```markdown
# Complexity Analysis

## Time Complexity: O(n)
- [Explanation of why time complexity is O(n)]

## Space Complexity: O(1)
- [Explanation of why space complexity is O(1)]

## Trade-offs
[Discuss any trade-offs in this solution]
```

#### 4. Solution Code Standards

- **Comments**: Add comments explaining non-obvious logic
- **Variable Names**: Use clear, descriptive variable names
- **Code Style**: Follow language conventions
- **Test Cases**: Include example test cases in comments

**Python Example:**
```python
def solution(nums):
    """
    Solve the problem using sliding window technique.
    
    Args:
        nums: List of integers
        
    Returns:
        int: The result
        
    Time: O(n)
    Space: O(1)
    """
    # Initialize sliding window
    left = 0
    max_result = 0
    
    for right in range(len(nums)):
        # Expand window
        # ... logic ...
        
        # Contract window if needed
        while condition:
            left += 1
    
    return max_result
```

#### 5. Commit and Push
```bash
git add SOLUTIONS/
git commit -m "Add solution for category/problem-id in language

- Brief description of approach
- Time complexity: O(x)
- Space complexity: O(y)"

git push origin solution/category/problem-id
```

#### 6. Submit Pull Request
- Title: `Add solution for {category}/{problem-id} in {language}`
- Description: Mention approach, complexity, and any learnings
- Reference: Link the problem URL

### Naming Conventions

| Item | Format | Example |
|------|--------|---------|
| Branch | `solution/{category}/{problem-id}` | `solution/sliding-window/sw-1` |
| Folder | `SOLUTIONS/{category}/{problem-id}/{language}` | `SOLUTIONS/sliding-window/sw-1/python` |
| File | `solution.{ext}` | `solution.py` |

### Supported Languages

We welcome solutions in:
- Python
- Java
- C++
- JavaScript/TypeScript
- Go
- Rust
- C#
- PHP
- Any other language

## 🐛 Reporting Issues

Found a broken link or error? Open an issue with:
- Problem category and ID
- What's wrong
- Suggested fix (if applicable)

## 📚 Documentation Contributions

Help us improve by:
- Fixing typos
- Clarifying explanations
- Adding new guides
- Improving problem descriptions

Create a PR with your changes and we'll review!

## ✅ Review Process

1. **Automated Checks**: PR passes tests and formatting
2. **Code Review**: Team reviews solution quality and approach
3. **Approval**: PR is approved and merged
4. **Recognition**: Your name added to contributors list

## ❓ Questions or Suggestions?

- Open an issue for discussion
- Tag the issue with `question` or `enhancement`
- We'll respond promptly

## 🎓 Best Practices

### Before You Submit

- [ ] Solution compiles/runs without errors
- [ ] Code is well-commented and readable
- [ ] Complexity analysis is accurate
- [ ] README explains your approach clearly
- [ ] You've tested edge cases
- [ ] No sensitive information included

### After You Submit

- [ ] Respond to reviewer feedback promptly
- [ ] Make requested changes
- [ ] Retest after modifications
- [ ] Ask clarifying questions if needed

## 📝 Commit Message Guidelines

Format:
```
[Category/Problem-ID] Brief description of solution

- Approach used: [e.g., Sliding Window]
- Time Complexity: O(n)
- Space Complexity: O(1)
- Language: Python
- Tested on: LeetCode/HackerRank/etc
```

Example:
```
[sliding-window/sw-1] Add optimal sliding window solution

- Approach: Two-pointer sliding window technique
- Time Complexity: O(n)
- Space Complexity: O(1)
- Language: Python
- Tested on: LeetCode
```

## 🤝 Community Standards

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and improve
- Share knowledge generously
- No spam or self-promotion

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

**Thank you for contributing to DSA Daily Solver! Together we're building a better resource for engineers worldwide.** 🚀
