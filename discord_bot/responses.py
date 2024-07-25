from predict import predict

def get_response(user_input: str) -> str:
    lowered: str = user_input

    if lowered.split()[0] == "/bridge":
        return predict(lowered.split()[1])
