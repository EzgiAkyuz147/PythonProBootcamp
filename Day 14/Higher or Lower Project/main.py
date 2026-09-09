import art,game_data, random

is_game_over = False
yet_true = 0
compare_a = ""
compare_b = ""
game = game_data.data

count = 0
for key in game:
    count += 1
x= count
def rand():
    return random.randint(1,x-1)

def compare(followers_a, followers_b,selection):
    if selection == "A":
        if followers_a > followers_b:
            return True
        else:
            return False
    else:
        if followers_a < followers_b:
            return True
        else:
            return False

while not is_game_over:
    print(art.logo)

    if yet_true == 0:
        compare_a = game[rand()]
        compare_b = game[rand()]
    else:
        compare_a = compare_b
        compare_b = game[rand()]
    print(f"Compare A: {compare_a["name"]}, a {compare_a["description"]}, from {compare_a["country"]}")
    print(art.vs)
    print(f"Compare B: {compare_b["name"]}, a {compare_b["description"]}, from {compare_b["country"]}")
    followers = input("Who has more followers? Type A or B: ")
    result = compare(compare_a["follower_count"], compare_b["follower_count"], followers)
    if result == True:
        yet_true += 1
        print(f"You are right! Current score: {yet_true}")
    else:
        print(art.logo)
        print(f"Sorry, you are wrong! Final score: {yet_true}")
        is_game_over = True