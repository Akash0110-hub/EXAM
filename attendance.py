def eligible(held, attended):
    return (attended / held) * 100 >= 75

if __name__ == "__main__":
    h = int(input())
    a = int(input())
    print("Eligible" if eligible(h,a) else "Not Eligible")

