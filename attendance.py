def check_attendance(classes_held, classes_attended):
    percentage = (classes_attended / classes_held) * 100
    return "Eligible" if percentage >= 75 else "Not Eligible"


if __name__ == "__main__":
    # Optional default values for manual run
    print(check_attendance(100, 80))
