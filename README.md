# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] The game is a Streamlit number guessing game where the player chooses a difficulty, enters guesses, receives higher/lower hints, and tries to find the secret number before running out of attempts.
- [x] I found that the high/low hints were reversed, old won/lost state could carry into a new game, and invalid decimal guesses were not handled clearly.
- [x] I fixed the guess comparison logic, reset all important `st.session_state` fields when a new game starts, moved reusable logic into `logic_utils.py`, and added pytest coverage for the repaired behavior.

## 📸 Demo Walkthrough

The fixed game now behaves like this from start to finish:

1. User opens the Streamlit app and selects Normal difficulty, which sets the range to 1 through 100 with 8 attempts.
2. User enters a guess of 40 when the secret number is 50.
3. Game returns "Too Low" and shows the hint "Go HIGHER!", then subtracts 5 points.
4. User enters a guess of 60.
5. Game returns "Too High" and shows the hint "Go LOWER!", then subtracts 5 more points.
6. User enters a decimal guess such as 54.7.
7. Game rejects the input with "That is not a whole number." instead of silently changing the guess.
8. User enters the correct guess of 50.
9. Game returns "Correct!", marks the status as won, shows the final score, and stops accepting more guesses until New Game is pressed.
10. User presses New Game, and the app clears the old attempts, score, status, and guess history before starting again.

## 🧪 Test Results

```
$ pytest
============================= test session starts ==============================
platform darwin -- Python 3.11.7, pytest-7.4.0, pluggy-1.0.0
rootdir: /Users/abdulrahmanqureshi/Downloads/ai110-module1show-gameglitchinvestigator-starter-main
plugins: anyio-3.7.1
collected 4 items

tests/test_game_logic.py ....                                            [100%]

============================== 4 passed in 0.02s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
