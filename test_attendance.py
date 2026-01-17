from attendance import check_attendance

def test_eligible():
    assert check_attendance(100, 80) == "Eligible"

def test_not_eligible():
    assert check_attendance(100, 60) == "Not Eligible"

def test_exact_75():
    assert check_attendance(100, 75) == "Eligible"
