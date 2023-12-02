with open("inputs/input-02.txt") as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))


def solve1(games):
    ids = 0
    for game in games:
        game_id = int(game.split(":")[0].split()[1])
        samples = game.split(":")[1].strip().split(";")
        valid = True
        for sample in samples:
            balls = sample.split(",")
            red_count, green_count, blue_count = 0, 0, 0
            for ball in balls:
                if "red" in ball:
                    red_count = int(ball.strip().split(" ")[0])
                if "green" in ball:
                    green_count = int(ball.strip().split(" ")[0])
                if "blue" in ball:
                    blue_count = int(ball.strip().split(" ")[0])
            if red_count > 12 or green_count > 13 or blue_count > 14:
                valid = False
        if valid:
            ids += game_id
    return ids


def solve2(games):
    power = 0
    for game in games:
        game_id = int(game.split(":")[0].split()[1])
        samples = game.split(":")[1].strip().split(";")
        min_red, min_green, min_blue = 0, 0, 0
        for sample in samples:
            balls = sample.split(",")
            for ball in balls:
                if "red" in ball:
                    min_red = max(int(ball.strip().split(" ")[0]), min_red)
                if "green" in ball:
                    min_green = max(int(ball.strip().split(" ")[0]), min_green)
                if "blue" in ball:
                    min_blue = max(int(ball.strip().split(" ")[0]), min_blue)
        power += min_red * min_green * min_blue
    return power


if __name__ == "__main__":
    print(solve1(lines))
    print(solve2(lines))
