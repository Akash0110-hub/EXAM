from attendance import eligble

def test_eligible():
    assert eligble(100, 80) == "Eligible"

def test_not_eligible():
    assert eligble(100, 60) == "Not Eligible"

def test_exact_75():
    assert eligble(100, 75) == "Eligible"
