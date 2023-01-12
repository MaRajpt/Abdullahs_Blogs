





















a_followers = 10
b_followers = 20


def compare(a_followers, b_followers):
    if a_followers > b_followers:
        return 'A'

    elif b_followers > a_followers:
        return 'B'

score = 0
choice = input("Who has more followers? Type 'A' or 'B': ")
if compare(a_followers, b_followers) == choice:
    score += 1
else:
    print("yolo")
print(score)

# gg bos
