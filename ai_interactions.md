# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Blank or spaces-only input | "Identify three edge-case inputs that might still break this Streamlit number guessing game and generate pytest cases for the logic functions." | Test that `parse_guess("   ")` returns `False`, no guess value, and `"Enter a guess."` | Yes | A user can click Submit without typing a real number, so the parser should give a clear error instead of crashing or counting it as a valid guess. |
| Negative guess | Same prompt as above. | Test that `check_guess(-10, 50)` returns `"Too Low"` and `"Go HIGHER!"` | Yes | Negative numbers are outside the normal game range, but the comparison logic should still respond safely and predictably. |
| Extremely large guess | Same prompt as above. | Test that `check_guess(1_000_000_000, 50)` returns `"Too High"` and `"Go LOWER!"` | Yes | Very large integers should not break the comparison logic or produce a misleading hint. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
