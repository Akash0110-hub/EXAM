def eligible(classes_held, classes_attended):
    percentage = (classes_attended / classes_held) * 100

    if percentage >= 75:
        return "Eligible"
    else:
        return "Not Eligible"


if __name__ == "__main__":
    print(eligible(100, 80))
