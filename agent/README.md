# DSA Daily Solver - Agent Configuration

This directory contains the agentic workflow configuration and prompt templates for the DSA Daily Solver system.

## 📂 Directory Structure

```
├── prompts/                    # Natural language prompts for agent interaction
│   ├── problem-requests.md    # Prompts for getting problems
│   ├── hint-requests.md       # Prompts for getting hints
│   ├── solution-requests.md   # Prompts for viewing solutions
│   ├── analysis-requests.md   # Prompts for code analysis
│   └── general-queries.md     # General help and queries
│
├── skills/                     # Agent skill definitions and implementations
│   ├── skill-problem-fetcher.md    # Fetch problems by category or random
│   ├── skill-hint-provider.md      # Provide contextual hints
│   ├── skill-solution-guide.md     # Guide through solutions
│   ├── skill-code-analyzer.md      # Analyze user code and mistakes
│   └── skill-progress-tracker.md   # Track learning progress
│
├── agent.md                   # Agent architecture and workflow documentation
└── README.md                  # This file
```

## 🤖 Agent Workflow Overview

The agent operates through a multi-mode system:

### 1. **Problem Request Mode** 🎯
- User asks for a problem to solve
- Agent fetches from problem database
- Returns problem with metadata and suggestions

### 2. **Hint Mode** 💡
- User indicates they're stuck
- Agent provides progressive hints
- Guides without revealing solution

### 3. **Solution Mode** ✅
- User requests full solution
- Agent explains approach and complexity
- Provides pseudocode and resources

### 4. **Mistake Analysis Mode** 🔍
- User shares their code
- Agent analyzes and provides feedback
- Identifies thinking and coding issues
- Suggests improvements

### 5. **Progress Tracking Mode** 📊
- User requests statistics
- Agent displays achievement tracking
- Provides recommendations

## 🔄 Prompt Categories

### Problem Requests
Examples:
- "Give me a problem to solve"
- "Show me a sliding window problem"
- "I want to practice dynamic programming"
- "Random DSA problem please"

### Hint Requests
Examples:
- "I'm stuck, give me a hint"
- "Help with the approach"
- "What data structure should I use?"
- "I don't know where to start"

### Solution Requests
Examples:
- "Show me the solution"
- "How do I solve this optimally?"
- "Explain the best approach"
- "Show me sample code"

### Analysis Requests
Examples:
- "Analyze my code"
- "Review my solution"
- "What did I do wrong?"
- "What could be improved?"

### Progress Queries
Examples:
- "Show my statistics"
- "How many problems solved?"
- "What's my progress?"
- "Show my streak"

## 💻 How to Use

### Command Line Interface
```bash
python agent_cli.py
# Starts interactive agent session
```

### API Usage
```python
from dsa_agent_workflow import DSAAgentWorkflow

agent = DSAAgentWorkflow()
response = agent.process_user_prompt("Give me a problem to solve")
print(response.content)
```

### Integration with GitHub Copilot
The agent can be invoked through GitHub Copilot skills defined in `copilot-skills.json`

## 📋 Prompt Structure

Each prompt follows this format:

```markdown
# Prompt Name

## Intent
What this prompt is meant to achieve

## Keywords
- keyword1
- keyword2

## Expected Response
What the agent should return

## Example Interactions
- User: "..."
  Agent: "..."
```

## 🎓 Skill Definitions

Each skill has:

1. **Trigger Conditions** - When the skill should activate
2. **Input Parameters** - What data it needs
3. **Processing Logic** - How it works
4. **Output Format** - What it returns
5. **Error Handling** - What if something fails

## 🔗 Integration Points

### With Problem Database
- `dsa-templates.json` - Original 35 problems
- `additional-dsa-problems.json` - Additional 30 problems

### With Manager
- `dsa_manager.py` - Programmatic problem access
- `dsa_agent_workflow.py` - Agent implementation

### With Tracking
- `PROGRESS_TEMPLATE.md` - User progress tracking
- Session state management

## 🎯 Future Enhancements

1. Multi-language code analysis
2. Real-time complexity calculation
3. Video tutorial integration
4. Community solution discussion
5. Spaced repetition algorithm
6. ML-based mistake detection

## 📚 Resources

- [Agent Architecture](agent.md)
- [Prompt Templates](prompts/)
- [Skill Definitions](skills/)
- [DSA Manager](../dsa_manager.py)
- [Workflow Implementation](../dsa_agent_workflow.py)

## 🤝 Contributing

To add new prompts or skills:

1. Create file in appropriate folder
2. Follow the established format
3. Test with agent
4. Document the usage
5. Submit PR

## 📞 Support

For issues or questions:
- Check existing prompt examples
- Review skill documentation
- Test with the CLI tool
- Open an issue on GitHub

---

**Last Updated:** 2026-06-05
**Version:** 1.0.0
