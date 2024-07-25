from random import choice, randint
import os


def get_response(user_input: str) -> str:
    lowered: str = user_input

    if lowered.split()[0] == "/bridge":
        string = "python3 ../bridge/predict.py " + "\""+ lowered.split()[1] + "\""
        os.system(string)
        f = open("message.txt", "r")
        message = f.read()
        return message