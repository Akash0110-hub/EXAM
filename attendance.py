def eligible(held,attended):
    percentage = (attended /held) * 100
    return "Eligible" if percentage >= 75 else "Not Eligible"


if __name__ == "__main__":
    # Optional default values for manual run
    print(eligble(100, 80))
