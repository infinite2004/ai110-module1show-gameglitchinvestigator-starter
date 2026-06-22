# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Blank or spaces-only input | "Identify three edge-case inputs that might still break this Streamlit number guessing game and generate pytest cases for the logic functions." | Test that `parse_guess("   ")` returns `False`, no guess value, and `"Enter a guess."` | Yes | A user can click Submit without typing a real number, so the parser should give a clear error instead of crashing or counting it as a valid guess. |
| Negative guess | Same prompt as above. | Test that `check_guess(-10, 50)` returns `"Too Low"` and `"Go HIGHER!"` | Yes | Negative numbers are outside the normal game range, but the comparison logic should still respond safely and predictably. |
| Extremely large guess | Same prompt as above. | Test that `check_guess(1_000_000_000, 50)` returns `"Too High"` and `"Go LOWER!"` | Yes | Very large integers should not break the comparison logic or produce a misleading hint. |
