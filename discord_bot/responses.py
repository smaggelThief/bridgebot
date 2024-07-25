from predict import predict

def get_response(user_input: str, username) -> str:
    if user_input.split()[0] == "/bridge":

        # store formatted string and isolated confidence in data variable
        data = predict(user_input.split()[1])

        # create leaderboard array from stored file
        f = open("leaderboard.txt", "r")
        leaderboard = f.read().split("\n")
        f.close()

        # loop through leaderboard 
        counter_lol = 0
        for spot in leaderboard[::-1]:
            if data[1] == spot.split()[1]:
                # only the first user to score an image gets the spot
                return data[0]
            if data[1] < float(spot.split()[1]):
                # insert user's score into leaderboard and write new leaderboard to file
                leaderboard.insert((10 - counter_lol), str(username + " " + str(data[1]) + " " + user_input.split()[1]))
                f = open('leaderboard.txt', "w")
                f.write("\n".join(leaderboard[:9]))
                f.close()
                return data[0]
            else:
                counter_lol += 1

        # run this code if user sets a new record
        leaderboard.insert(0, str(username + " " + str(data[1]) + " " + user_input.split()[1]))
        f = open("leaderboard.txt", "w")
        f.write("\n".join(leaderboard[:9]))
        f.close()
        return str(data[0] + ". That's a new record!")
    if user_input.split()[0] == "/bot":
        return "BOT!"
    if user_input.split()[0] == "/top_bridge":
        f = open("leaderboard.txt", "r")
        leaderboard = f.read().split("\n")
        f.close()
        return str(leaderboard[0])
    if user_input.split()[0] == "/leaderboard":
        f = open("leaderboard.txt", "r")
        leaderboard = f.read().split("\n")
        f.close()
        counter_lol = 0
        for spot in leaderboard:
            leaderboard[counter_lol] = str(spot.split()[:2])
            counter_lol += 1
        text = ("\n").join(leaderboard)
        return str(text)
    if user_input.split()[0] == "/top":
        return "top"