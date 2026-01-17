from attendance import eligible

def test_eligible():
    assert eligible(100, 80) == "Eligible"

def test_not_eligible():
    assert eligible(100, 60) == "Not Eligible"

def test_exact_75():
    assert eligible(100, 75) == "Eligible"
