# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The game was a webpage with five main features. The first feature I saw was the Developer Debug Info, which showed the secret number, attempts, score, difficulty, and history. The second feature was the guess input where I typed my answer, the third was the Submit Guess button, the fourth was the New Game button, and the fifth was the Show Hint checkbox.

One bug I noticed was that the hint logic was backwards. When my guess was too high, the app sometimes told me to go higher or showed the wrong outcome, so I suspected a problem in the check_guess logic. A second bug I noticed was that after the game ended, pressing New Game did not fully clear the old game over message or status. A third bug was that the app sometimes acted like I had already won or lost because old session state was still being used.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| guess of 70 | Too High | Too Low / wrong hint | none |
| guess of 100 | Too High | You already won, start a new game | none |
| guess of 54 | Too Low | Game over, start a new game and try again | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Codex as my AI coding teammate to inspect `app.py`, `logic_utils.py`, and the pytest file. A correct suggestion was to move `check_guess`, `parse_guess`, `get_range_for_difficulty`, and `update_score` into `logic_utils.py` so the game logic could be tested separately from the Streamlit UI. I verified this by checking that `app.py` imported the functions from `logic_utils.py` and by running pytest.

One misleading result was that the app first looked like it was not starting correctly, but the real issue was the sandbox blocking Streamlit's local server and file watcher. I verified this by reading the terminal error, then running Streamlit with an explicit localhost address and polling file watching. That showed me the problem was the run environment, not the game logic itself.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed only after the code behavior matched the expected behavior in the reproduction log. For the high/low bug, I added pytest checks where a guess of 60 against a secret of 50 returns "Too High" and "Go LOWER!", while a guess of 40 returns "Too Low" and "Go HIGHER!". This directly tested the bug I saw in the live app.

I also tested that decimal guesses are rejected instead of silently being converted into another number. AI helped design these tests by turning the bugs from my reflection into small examples with a known guess and secret. After that, I ran pytest to confirm the tests passed with the refactored logic.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I learned that Streamlit reruns the whole script from top to bottom whenever a user interacts with a widget, like clicking a button or changing an input. That means normal Python variables can get recreated unless the app stores important values in `st.session_state`. I would explain session state as the app's memory between reruns, because it keeps things like the secret number, attempts, score, status, and history from disappearing or changing at the wrong time. This project helped me understand why a game can look random or broken if state is initialized in the wrong place.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One strategy I want to reuse is writing down the exact bug reproduction before changing code. It made the fixes easier to check because I could compare the old wrong behavior with the expected behavior. I also want to keep asking AI for small, testable suggestions instead of accepting a big answer all at once.

Next time, I would ask the AI to separate code problems from environment problems earlier. In this project, one misleading moment was when Streamlit looked like it was failing because of the app, but the real problem was the sandbox and the old launcher command. This project changed the way I think about AI generated code because I saw that AI can be very useful, but I still have to verify its ideas with tests, terminal output, and the live app.
