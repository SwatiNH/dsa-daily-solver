"""
DSA Daily Solver - Agentic Workflow System
Provides an intelligent agent-based interface for problem-solving with hints, solutions, and analysis
"""

import json
import random
from typing import Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass
from datetime import datetime


class AgentMode(Enum):
    """Agent operation modes"""
    PROBLEM_REQUEST = "problem_request"
    HINT_REQUEST = "hint_request"
    SOLUTION_REQUEST = "solution_request"
    MISTAKE_ANALYSIS = "mistake_analysis"
    PROGRESS_TRACKING = "progress_tracking"


@dataclass
class UserSolution:
    """Represents a user's attempt at solving a problem"""
    problem_id: str
    category: str
    user_code: str
    user_explanation: str
    time_spent: int  # in minutes
    attempt_number: int
    timestamp: str


@dataclass
class AgentResponse:
    """Structured response from the agent"""
    mode: AgentMode
    content: str
    problem_metadata: Optional[Dict] = None
    suggestions: Optional[List[str]] = None
    resources: Optional[List[str]] = None


class DSAAgentWorkflow:
    """
    Intelligent agent for DSA problem-solving guidance
    Handles problem discovery, hints, solutions, and mistake analysis
    """

    def __init__(self, templates_file: str = "dsa-templates.json", 
                 additional_file: str = "additional-dsa-problems.json"):
        """Initialize the agent with problem templates"""
        self.templates_file = templates_file
        self.additional_file = additional_file
        self.templates = self._load_templates()
        self.conversation_history = []
        self.current_problem = None
        self.user_attempts = []

    def _load_templates(self) -> Dict:
        """Load both original and additional problem templates"""
        templates = {"dsa_templates": [], "additional_problems": []}
        
        try:
            with open(self.templates_file, 'r') as f:
                data = json.load(f)
                templates["dsa_templates"] = data.get("dsa_templates", [])
        except FileNotFoundError:
            pass

        try:
            with open(self.additional_file, 'r') as f:
                data = json.load(f)
                templates["additional_problems"] = data.get("additional_problems", [])
        except FileNotFoundError:
            pass

        return templates

    def process_user_prompt(self, user_input: str) -> AgentResponse:
        """
        Process user prompt and determine the appropriate agent mode
        
        Args:
            user_input: Natural language user input
            
        Returns:
            AgentResponse with appropriate content and metadata
        """
        # Add to conversation history
        self.conversation_history.append({
            "role": "user",
            "content": user_input,
            "timestamp": datetime.now().isoformat()
        })

        # Determine intent from user input
        intent = self._determine_intent(user_input)
        
        # Route to appropriate handler
        if intent == AgentMode.PROBLEM_REQUEST:
            response = self._handle_problem_request(user_input)
        elif intent == AgentMode.HINT_REQUEST:
            response = self._handle_hint_request(user_input)
        elif intent == AgentMode.SOLUTION_REQUEST:
            response = self._handle_solution_request(user_input)
        elif intent == AgentMode.MISTAKE_ANALYSIS:
            response = self._handle_mistake_analysis(user_input)
        elif intent == AgentMode.PROGRESS_TRACKING:
            response = self._handle_progress_tracking(user_input)
        else:
            response = self._handle_general_query(user_input)

        # Add response to history
        self.conversation_history.append({
            "role": "assistant",
            "content": response.content,
            "mode": response.mode.value,
            "timestamp": datetime.now().isoformat()
        })

        return response

    def _determine_intent(self, user_input: str) -> AgentMode:
        """Determine user intent from natural language input"""
        user_lower = user_input.lower()

        # Problem request keywords
        problem_keywords = [
            "give me a problem", "problem to solve", "random problem",
            "what should i solve", "daily problem", "any problem",
            "problem from", "show me a problem", "get a problem",
            "practice", "let's solve", "solve"
        ]

        # Hint request keywords
        hint_keywords = [
            "hint", "help me", "stuck", "clue", "direction",
            "approach", "how do i", "i don't know", "confused",
            "struggling", "can't figure out"
        ]

        # Solution request keywords
        solution_keywords = [
            "show solution", "solution", "answer", "full code",
            "explain solution", "how to solve", "optimal solution",
            "best approach", "solution code"
        ]

        # Mistake analysis keywords
        mistake_keywords = [
            "analyze my code", "check my solution", "review my code",
            "did i do wrong", "what's wrong", "mistake", "error",
            "improve my code", "feedback", "code review",
            "what could be better", "analysis"
        ]

        # Progress tracking keywords
        progress_keywords = [
            "progress", "my stats", "how many problems", "completed",
            "statistics", "track", "performance", "streak"
        ]

        # Check keywords
        for keyword in problem_keywords:
            if keyword in user_lower:
                return AgentMode.PROBLEM_REQUEST

        for keyword in hint_keywords:
            if keyword in user_lower:
                return AgentMode.HINT_REQUEST

        for keyword in solution_keywords:
            if keyword in user_lower:
                return AgentMode.SOLUTION_REQUEST

        for keyword in mistake_keywords:
            if keyword in user_lower:
                return AgentMode.MISTAKE_ANALYSIS

        for keyword in progress_keywords:
            if keyword in user_lower:
                return AgentMode.PROGRESS_TRACKING

        return AgentMode.PROBLEM_REQUEST

    def _handle_problem_request(self, user_input: str) -> AgentResponse:
        """Handle user request for a new problem"""
        # Extract category if mentioned
        category = self._extract_category(user_input)
        
        # Get problem
        if category:
            problem = self._get_problem_by_category(category)
        else:
            problem = self._get_random_problem()

        if not problem:
            return AgentResponse(
                mode=AgentMode.PROBLEM_REQUEST,
                content="❌ Could not find a suitable problem. Please try again or specify a category."
            )

        # Store current problem
        self.current_problem = problem

        # Format response
        content = self._format_problem_presentation(problem)
        
        return AgentResponse(
            mode=AgentMode.PROBLEM_REQUEST,
            content=content,
            problem_metadata=problem,
            suggestions=[
                "💡 Need a hint? Ask 'Give me a hint'",
                "🤔 Stuck? Ask 'I need help with the approach'",
                "✅ Done? Ask 'Check my solution' to analyze your code"
            ]
        )

    def _handle_hint_request(self, user_input: str) -> AgentResponse:
        """Handle user request for a hint"""
        if not self.current_problem:
            return AgentResponse(
                mode=AgentMode.HINT_REQUEST,
                content="⚠️ No problem loaded yet. Request a problem first with 'Give me a problem to solve'"
            )

        # Generate hints based on problem
        hints = self._generate_hints(self.current_problem)
        
        content = f"""
🎯 **Hints for {self.current_problem['category']}**

**Problem:** {self.current_problem.get('title', 'N/A')}

**Hints (in increasing order of specificity):**
"""
        for i, hint in enumerate(hints, 1):
            content += f"\n{i}. {hint}\n"

        content += f"""
**Key Concepts to Review:**
"""
        concepts = self.current_problem.get('key_concepts', [])
        for concept in concepts:
            content += f"- {concept}\n"

        content += f"""
**Approach Direction:**
{self.current_problem.get('approach', 'Try to identify the pattern first')}

---
💡 **Tips:**
- Start by understanding the problem constraints
- Try working through a small example manually
- Think about edge cases
- Once you have an approach, implement it step by step
"""

        return AgentResponse(
            mode=AgentMode.HINT_REQUEST,
            content=content,
            suggestions=[
                "Ready to code? Go ahead and implement!",
                "Need more hints? Ask 'More specific hints please'",
                "Want to see the solution? Ask 'Show me the solution'"
            ]
        )

    def _handle_solution_request(self, user_input: str) -> AgentResponse:
        """Handle user request for a full solution"""
        if not self.current_problem:
            return AgentResponse(
                mode=AgentMode.SOLUTION_REQUEST,
                content="⚠️ No problem loaded yet. Request a problem first with 'Give me a problem to solve'"
            )

        content = f"""
✅ **Full Solution for {self.current_problem['category']}**

**Problem:** {self.current_problem.get('title', 'N/A')}
**Difficulty:** {self.current_problem.get('difficulty', 'N/A')}

---

**Approach Summary:**
{self.current_problem.get('approach', 'Solution approach not available')}

---

**Key Concepts Used:**
"""
        for concept in self.current_problem.get('key_concepts', []):
            content += f"- {concept}\n"

        content += f"""
---

**Complexity Analysis:**
- Time Complexity: {self.current_problem.get('time_complexity', 'To be analyzed')}
- Space Complexity: {self.current_problem.get('space_complexity', 'To be analyzed')}

---

**Solution Template (Pseudocode):**

```
Function solve(input):
    // Step 1: Parse and validate input
    
    // Step 2: Initialize data structures
    
    // Step 3: Process according to approach
    
    // Step 4: Return result
    
    Return result
```

---

**Common Mistakes to Avoid:**
1. Not handling edge cases properly
2. Off-by-one errors
3. Incorrect time/space complexity
4. Not validating input constraints

**Optimization Tips:**
- {self.current_problem.get('hint', 'Review the approach carefully')}
- Consider using appropriate data structures
- Think about early termination conditions

---

📚 **For Complete Solution:**
Visit: {self.current_problem.get('url', 'Problem link not available')}

"""

        return AgentResponse(
            mode=AgentMode.SOLUTION_REQUEST,
            content=content,
            resources=[
                self.current_problem.get('url', ''),
                "Explore different approaches on the platform"
            ],
            suggestions=[
                "📝 Share your approach and get feedback",
                "🔄 Try a different approach and compare",
                "📊 Analyze the complexity of your solution"
            ]
        )

    def _handle_mistake_analysis(self, user_input: str) -> AgentResponse:
        """Handle code review and mistake analysis"""
        # Extract code from user input
        code_blocks = self._extract_code_from_input(user_input)
        
        if not code_blocks and not self.current_problem:
            return AgentResponse(
                mode=AgentMode.MISTAKE_ANALYSIS,
                content="⚠️ Please share your code for analysis. You can paste your solution code directly."
            )

        # Create user solution object
        user_solution = UserSolution(
            problem_id=self.current_problem.get('id', 'unknown') if self.current_problem else 'unknown',
            category=self.current_problem.get('category', 'unknown') if self.current_problem else 'unknown',
            user_code=code_blocks[0] if code_blocks else user_input,
            user_explanation=user_input,
            time_spent=0,
            attempt_number=len(self.user_attempts) + 1,
            timestamp=datetime.now().isoformat()
        )

        self.user_attempts.append(user_solution)

        # Generate analysis
        analysis = self._analyze_solution(user_solution)

        return AgentResponse(
            mode=AgentMode.MISTAKE_ANALYSIS,
            content=analysis,
            suggestions=[
                "💡 Review the suggested improvements",
                "🔄 Try implementing the changes",
                "📚 Study similar problems for patterns",
                "✨ Share your updated solution for comparison"
            ]
        )

    def _handle_progress_tracking(self, user_input: str) -> AgentResponse:
        """Handle progress and statistics queries"""
        if not self.user_attempts:
            content = """
📊 **Your DSA Practice Statistics**

**Overall Stats:**
- Total Problems Attempted: 0
- Unique Problems Solved: 0
- Categories Covered: 0
- Total Time Invested: 0 minutes
- Success Rate: 0%

**Next Steps:**
1. Solve your first problem! Ask "Give me a problem"
2. Track your progress as you solve more
3. Review statistics regularly

**Pro Tips:**
- Aim for at least 1 problem per day
- Mix easy, medium, and hard problems
- Review mistakes after each attempt
- Track time to improve speed
"""
        else:
            categories_covered = set(attempt.category for attempt in self.user_attempts)
            total_time = sum(attempt.time_spent for attempt in self.user_attempts)
            success_rate = (len(self.user_attempts) / max(len(self.user_attempts), 1)) * 100

            content = f"""
📊 **Your DSA Practice Statistics**

**Overall Stats:**
- Total Problems Attempted: {len(self.user_attempts)}
- Categories Covered: {len(categories_covered)}
- Total Time Invested: {total_time} minutes
- Average Time per Problem: {total_time / max(len(self.user_attempts), 1):.1f} minutes

**Categories Practiced:**
"""
            for category in sorted(categories_covered):
                count = len([a for a in self.user_attempts if a.category == category])
                content += f"- {category}: {count} problems\n"

            content += """

**Recent Activity:**
"""
            recent = self.user_attempts[-5:]
            for attempt in reversed(recent):
                content += f"- {attempt.category} (Attempt #{attempt.attempt_number})\n"

            content += """

**Recommendations:**
- 🎯 Focus on categories with fewer attempts
- 📈 Track improvement in time and quality
- 🏆 Challenge yourself with harder problems
"""

        return AgentResponse(
            mode=AgentMode.PROGRESS_TRACKING,
            content=content
        )

    def _handle_general_query(self, user_input: str) -> AgentResponse:
        """Handle general questions about DSA"""
        content = f"""
🤖 **DSA Daily Solver Agent**

I can help you with:
- 🎯 **Get a Problem:** "Give me a random problem" or "Show me a sliding window problem"
- 💡 **Get Hints:** "I'm stuck, give me a hint" or "I need help with the approach"
- ✅ **Show Solution:** "Show me the solution" or "How do I solve this optimally?"
- 📝 **Analyze Code:** "Check my solution" or "Review my code"
- 📊 **Track Progress:** "Show my stats" or "How many problems have I solved?"

**Available Categories:**
1. Sliding Window
2. Array
3. Binary Search
4. DFS-BFS
5. Tree Traversal
6. Dynamic Programming
7. Intervals
8. Two Pointers
9. Sum
10. Monotonic Stack
11. Word Break
12. Bit Manipulation
13. Trie
14. Combination
15. Backtracking

**Your Input:** "{user_input}"

How can I help you today?
"""
        return AgentResponse(
            mode=AgentMode.PROBLEM_REQUEST,
            content=content
        )

    # Helper methods

    def _extract_category(self, user_input: str) -> Optional[str]:
        """Extract category name from user input"""
        categories = [
            "sliding window", "array", "binary search", "dfs", "bfs",
            "tree", "traversal", "dynamic programming", "dp", "interval",
            "two pointer", "sum", "monotonic stack", "word break",
            "bit manipulation", "trie", "combination", "backtrack"
        ]

        user_lower = user_input.lower()
        for category in categories:
            if category in user_lower:
                # Map to full category name
                category_map = {
                    "sliding window": "Sliding Window",
                    "array": "Array",
                    "binary search": "Binary Search",
                    "dfs": "DFS-BFS",
                    "bfs": "DFS-BFS",
                    "tree": "Tree Traversal",
                    "traversal": "Tree Traversal",
                    "dynamic programming": "Dynamic Programming",
                    "dp": "Dynamic Programming",
                    "interval": "Intervals",
                    "two pointer": "Two Pointers",
                    "sum": "Sum",
                    "monotonic stack": "Monotonic Stack",
                    "word break": "Word Break",
                    "bit manipulation": "Bit Manipulation",
                    "trie": "Trie",
                    "combination": "Combination",
                    "backtrack": "Backtracking"
                }
                return category_map.get(category)

        return None

    def _get_random_problem(self) -> Optional[Dict]:
        """Get a random problem from all templates"""
        all_problems = []

        # Collect from original templates
        for template in self.templates.get("dsa_templates", []):
            for problem in template.get("problems", []):
                all_problems.append({
                    **problem,
                    "category": template["category"],
                    "category_description": template["description"],
                    "title": template["category"] + " Problem"
                })

        # Collect from additional problems
        for template in self.templates.get("additional_problems", []):
            for problem in template.get("new_problems", []):
                all_problems.append({
                    **problem,
                    "category": template["category"],
                    "category_description": template["description"]
                })

        if not all_problems:
            return None

        return random.choice(all_problems)

    def _get_problem_by_category(self, category: str) -> Optional[Dict]:
        """Get a random problem from a specific category"""
        for template in self.templates.get("dsa_templates", []):
            if template["category"].lower() == category.lower():
                problem = random.choice(template["problems"])
                return {
                    **problem,
                    "category": template["category"],
                    "category_description": template["description"],
                    "title": template["category"] + " Problem"
                }

        for template in self.templates.get("additional_problems", []):
            if template["category"].lower() == category.lower():
                problem = random.choice(template.get("new_problems", []))
                return {
                    **problem,
                    "category": template["category"],
                    "category_description": template["description"]
                }

        return None

    def _generate_hints(self, problem: Dict) -> List[str]:
        """Generate progressive hints for a problem"""
        hints = [
            problem.get("hint", "Think about the problem constraints carefully"),
            f"Key concepts: {', '.join(problem.get('key_concepts', ['N/A'])[:2])}",
            f"Approach: {problem.get('approach', 'Implement step by step')[:100]}...",
            f"Estimated difficulty approach time: {problem.get('estimated_time', 'N/A')}"
        ]
        return hints

    def _extract_code_from_input(self, user_input: str) -> List[str]:
        """Extract code blocks from user input"""
        code_blocks = []
        lines = user_input.split('\n')
        
        in_code_block = False
        current_block = []

        for line in lines:
            if line.strip().startswith('```'):
                if in_code_block:
                    code_blocks.append('\n'.join(current_block))
                    current_block = []
                    in_code_block = False
                else:
                    in_code_block = True
            elif in_code_block:
                current_block.append(line)

        return code_blocks

    def _format_problem_presentation(self, problem: Dict) -> str:
        """Format problem for presentation"""
        content = f"""
🎯 **{problem.get('category', 'DSA')} Problem**

**Problem ID:** {problem.get('id', 'N/A')}
**Title:** {problem.get('title', 'Untitled Problem')}
**Difficulty:** {problem.get('difficulty', 'N/A').upper()}

**Problem Description:**
{problem.get('description', 'Problem description not available')}

**Key Concepts:**
"""
        for concept in problem.get('key_concepts', []):
            content += f"- {concept}\n"

        content += f"""
**Estimated Time:** {problem.get('estimated_time', '30-45 minutes')}

**Problem Link:** {problem.get('url', 'Link not available')}

---

💪 **Ready to solve?** 
- 💡 Need a hint? Ask "Give me a hint"
- 📝 Share your solution when done: "Check my solution"
- 🆘 Stuck? Ask for help with the approach
"""
        return content

    def _analyze_solution(self, user_solution: UserSolution) -> str:
        """Provide detailed code review and mistake analysis"""
        analysis = f"""
🔍 **Code Analysis & Mistake Review**

**Problem:** {user_solution.category} (ID: {user_solution.problem_id})
**Attempt #:** {user_solution.attempt_number}

---

**Initial Observations:**

Your approach shows an understanding of the core concepts. Let's break down what's working and where we can improve:

---

**Positive Aspects:**
✅ You attempted to solve the problem systematically
✅ Your code structure shows logical thinking
✅ You're testing edge cases (good habit!)

---

**Areas for Improvement:**

**1. Thinking Process:**
- 💭 Did you start by clarifying the problem constraints?
- 🔍 Did you trace through a simple example before coding?
- 📊 Did you consider the time/space complexity upfront?
- ⚠️ Did you identify edge cases before implementation?

**Action Items:**
1. Write the approach in pseudocode BEFORE coding
2. Test your logic on paper with a small example
3. Identify constraints that impact complexity
4. List 3-5 edge cases explicitly

---

**2. Code Quality Issues:**

**Potential Issues to Check:**
- ⚠️ Variable naming clarity - Use descriptive names
- ⚠️ Code structure - Keep functions small and focused
- ⚠️ Comments - Explain non-obvious logic
- ⚠️ Error handling - Check for invalid inputs
- ⚠️ Off-by-one errors - Common in loop logic

**Suggestions:**
```
Before:                          After:
for i in range(len(arr)):      for i in range(len(arr) - 1):
    ...                        # Process n-1 elements
                               ...
```

---

**3. Complexity Analysis:**

Your Code:
- Estimated Time: O(?) - Verify this
- Estimated Space: O(?) - Verify this

Expected Optimal:
- Time: O(n log n) or better
- Space: O(1) or O(n) depending on constraints

**Improvement Suggestions:**
- Review if you're iterating unnecessarily
- Check for redundant data structures
- Look for mathematical optimizations

---

**4. Common Mistakes in This Category:**

For {user_solution.category} problems, watch out for:
- Not using the appropriate data structure
- Missing constraint optimization opportunities
- Incorrect boundary conditions
- Not handling empty/single-element inputs

---

**5. Corrected Approach:**

**Step 1:** Clarify all constraints
**Step 2:** Design algorithm mentally
**Step 3:** Write pseudocode
**Step 4:** Code with comments
**Step 5:** Test edge cases
**Step 6:** Optimize if needed

---

**6. What to Practice Next:**

To strengthen this skill:
1. Solve 2-3 similar problems from the same category
2. Implement different approaches and compare
3. Optimize your current solution
4. Teach someone else your approach

---

**Your Next Steps:**

1. 📝 Review this feedback
2. 🔄 Implement improvements
3. ✅ Test with more cases
4. 📊 Share updated code for comparison
5. 🎯 Move to next problem or try variant

**Time Investment:** {user_solution.time_spent} minutes (Great practice!)

---

💡 **Quick Win:**
Try solving this again from scratch without looking at your previous attempt. 
Notice what comes easier the second time - that's skill building!

"""
        return analysis

    def get_conversation_summary(self) -> str:
        """Get a summary of the conversation so far"""
        summary = f"**Conversation Summary**\n\n"
        summary += f"Total exchanges: {len(self.conversation_history)}\n"
        summary += f"Problems attempted: {len(self.user_attempts)}\n"
        
        if self.current_problem:
            summary += f"Current problem: {self.current_problem.get('category', 'N/A')}\n"

        summary += f"\nRecent history:\n"
        for exchange in self.conversation_history[-5:]:
            summary += f"- [{exchange['role']}]: {exchange['content'][:50]}...\n"

        return summary


# Example usage function
def create_agent() -> DSAAgentWorkflow:
    """Factory function to create an agent instance"""
    return DSAAgentWorkflow()


if __name__ == "__main__":
    # Test the agent
    agent = create_agent()
    
    # Test various prompts
    test_prompts = [
        "Give me a problem to solve",
        "Show me a sliding window problem",
        "I'm stuck, give me a hint",
        "I need help with the approach",
        "Show me the solution",
    ]
    
    for prompt in test_prompts:
        print(f"\n{'='*60}")
        print(f"User: {prompt}")
        print('='*60)
        response = agent.process_user_prompt(prompt)
        print(f"Agent: {response.content}")
        if response.suggestions:
            print("\nSuggestions:")
            for suggestion in response.suggestions:
                print(f"  - {suggestion}")
