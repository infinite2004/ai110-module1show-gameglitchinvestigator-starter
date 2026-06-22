from logic_utils import check_guess, parse_guess


def test_parse_guess_rejects_blank_input():
    # Blank input should ask the user to enter a guess instead of crashing.
    ok, guess, error = parse_guess("   ")
    assert ok is False
    assert guess is None
    assert error == "Enter a guess."


def test_negative_guess_is_treated_as_too_low():
    # A negative number is outside the game range, but comparison still works.
    outcome, message = check_guess(-10, 50)
    assert outcome == "Too Low"
    assert message == "Go HIGHER!"


def test_extremely_large_guess_is_treated_as_too_high():
    # Very large integers should not crash the comparison logic.
    outcome, message = check_guess(1_000_000_000, 50)
    assert outcome == "Too High"
    assert message == "Go LOWER!"
