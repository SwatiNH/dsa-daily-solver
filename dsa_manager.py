"""
GitHub Copilot Skills for DSA Daily Solver
This module provides utilities to interact with DSA problem templates
"""

import json
import random
from typing import Dict, List, Optional
from pathlib import Path


class DSATemplateManager:
    """Manages DSA problem templates and provides problem suggestions"""
    
    def __init__(self, template_file: str = "dsa-templates.json"):
        """Initialize the manager with template data"""
        self.template_file = template_file
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict:
        """Load DSA templates from JSON file"""
        try:
            with open(self.template_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: {self.template_file} not found")
            return {"dsa_templates": []}
    
    def get_all_categories(self) -> List[str]:
        """Get list of all DSA categories"""
        return [template["category"] for template in self.templates["dsa_templates"]]
    
    def get_category_by_id(self, category_id: int) -> Optional[Dict]:
        """Get category details by ID"""
        for template in self.templates["dsa_templates"]:
            if template["id"] == category_id:
                return template
        return None
    
    def get_category_by_name(self, category_name: str) -> Optional[Dict]:
        """Get category details by name"""
        for template in self.templates["dsa_templates"]:
            if template["category"].lower() == category_name.lower():
                return template
        return None
    
    def get_random_problem(self) -> Dict:
        """
        Get a random DSA problem from all categories
        
        Returns:
            Dict containing: {
                'category': str,
                'problem_id': str,
                'problem_url': str,
                'difficulty': str,
                'category_description': str
            }
        """
        # Select random category
        category = random.choice(self.templates["dsa_templates"])
        
        # Select random problem from category
        problem = random.choice(category["problems"])
        
        return {
            "category": category["category"],
            "category_description": category["description"],
            "problem_id": problem["id"],
            "problem_url": problem["url"],
            "difficulty": problem["difficulty"],
            "category_difficulty": category["difficulty"]
        }
    
    def get_problems_by_category(self, category_name: str) -> Optional[List[Dict]]:
        """
        Get all problems from a specific category
        
        Args:
            category_name: Name of the category
            
        Returns:
            List of problems or None if category not found
        """
        category = self.get_category_by_name(category_name)
        if not category:
            return None
        
        return [{
            "problem_id": p["id"],
            "url": p["url"],
            "difficulty": p["difficulty"]
        } for p in category["problems"]]
    
    def get_problems_by_difficulty(self, difficulty: str) -> List[Dict]:
        """
        Get all problems of a specific difficulty level
        
        Args:
            difficulty: 'easy', 'medium', or 'hard'
            
        Returns:
            List of problems matching the difficulty
        """
        problems = []
        for template in self.templates["dsa_templates"]:
            for problem in template["problems"]:
                if problem["difficulty"].lower() == difficulty.lower():
                    problems.append({
                        "category": template["category"],
                        "problem_id": problem["id"],
                        "url": problem["url"],
                        "difficulty": problem["difficulty"]
                    })
        return problems
    
    def get_statistics(self) -> Dict:
        """Get statistics about the DSA templates"""
        total_categories = len(self.templates["dsa_templates"])
        total_problems = sum(
            len(template["problems"]) 
            for template in self.templates["dsa_templates"]
        )
        
        difficulty_count = {"easy": 0, "medium": 0, "hard": 0}
        for template in self.templates["dsa_templates"]:
            for problem in template["problems"]:
                diff = problem["difficulty"].lower()
                if diff in difficulty_count:
                    difficulty_count[diff] += 1
        
        return {
            "total_categories": total_categories,
            "total_problems": total_problems,
            "difficulty_breakdown": difficulty_count,
            "categories": self.get_all_categories()
        }
    
    def get_daily_challenge(self, seed: Optional[int] = None) -> Dict:
        """
        Get daily challenge (deterministic random based on date)
        
        Args:
            seed: Optional seed for reproducibility (default: today's date)
            
        Returns:
            Daily challenge problem
        """
        if seed is None:
            from datetime import date
            seed = int(date.today().strftime("%Y%m%d"))
        
        random.seed(seed)
        problem = self.get_random_problem()
        random.seed()  # Reset seed
        
        return problem
    
    def get_category_progression(self) -> List[str]:
        """
        Get recommended progression path for learning
        
        Returns:
            Ordered list of categories by recommended learning order
        """
        recommended_order = [
            "Array",
            "Sliding Window",
            "Two Pointers",
            "Binary Search",
            "Sum",
            "DFS-BFS",
            "Tree Traversal",
            "Intervals",
            "Word Break",
            "Monotonic Stack",
            "Dynamic Programming",
            "Combination",
            "Backtracking",
            "Bit Manipulation",
            "Trie"
        ]
        
        return [cat for cat in recommended_order if cat in self.get_all_categories()]


# Example usage functions for Copilot skills

def skill_get_random_problem():
    """Copilot Skill: Get a random DSA problem"""
    manager = DSATemplateManager()
    problem = manager.get_random_problem()
    
    return f"""
🎯 **Daily DSA Problem**

**Category:** {problem['category']}
**Description:** {problem['category_description']}
**Problem ID:** {problem['problem_id']}
**Difficulty:** {problem['difficulty']}

**Problem Link:** {problem['problem_url']}

---
💡 **Hint:** Focus on understanding the problem constraints and edge cases first.
⏱️ **Time Suggestion:** 30-45 minutes
"""


def skill_get_category_problems(category_name: str):
    """Copilot Skill: Get all problems from a category"""
    manager = DSATemplateManager()
    category = manager.get_category_by_name(category_name)
    
    if not category:
        return f"❌ Category '{category_name}' not found. Available categories: {', '.join(manager.get_all_categories())}"
    
    problems = manager.get_problems_by_category(category_name)
    
    output = f"""
📚 **{category_name} Problems**

{category['description']}

**Total Problems:** {len(problems)}

"""
    
    for i, problem in enumerate(problems, 1):
        output += f"{i}. [{problem['problem_id']}]({problem['url']}) - {problem['difficulty']}\n"
    
    return output


def skill_get_statistics():
    """Copilot Skill: Get statistics and overview"""
    manager = DSATemplateManager()
    stats = manager.get_statistics()
    
    return f"""
📊 **DSA Problem Repository Statistics**

**Total Categories:** {stats['total_categories']}
**Total Problems:** {stats['total_problems']}

**Difficulty Breakdown:**
- Easy: {stats['difficulty_breakdown']['easy']}
- Medium: {stats['difficulty_breakdown']['medium']}
- Hard: {stats['difficulty_breakdown']['hard']}

**Categories Available:**
{chr(10).join(f"- {cat}" for cat in stats['categories'])}
"""


def skill_get_daily_challenge():
    """Copilot Skill: Get today's daily challenge"""
    manager = DSATemplateManager()
    problem = manager.get_daily_challenge()
    
    return f"""
🌟 **Today's DSA Challenge**

**Category:** {problem['category']}
**Problem ID:** {problem['problem_id']}
**Difficulty:** {problem['difficulty']}

**Problem Link:** {problem['problem_url']}

This is your deterministic daily problem. Same time every day = same problem!
Try to solve it in 30-45 minutes.

Good luck! 💪
"""


if __name__ == "__main__":
    # Test the manager
    manager = DSATemplateManager()
    
    print("=== DSA Template Manager Test ===\n")
    
    print("1. Random Problem:")
    print(skill_get_random_problem())
    
    print("\n2. Sliding Window Problems:")
    print(skill_get_category_problems("Sliding Window"))
    
    print("\n3. Statistics:")
    print(skill_get_statistics())
    
    print("\n4. Daily Challenge:")
    print(skill_get_daily_challenge())
