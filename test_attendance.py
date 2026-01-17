from attendance import eligible

def test_yes(): assert eligible(100,80)
def test_no(): assert not eligible(100,60)
def test_exact(): assert eligible(100,75)
