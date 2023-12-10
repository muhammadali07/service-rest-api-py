from utils import respOutCustome

async def login (data:dict):
    return respOutCustome(status="00", message="Successfully logged in", data=data)


def login_2 (data):
    return respOutCustome(status="00", message="Successfully logged in", data=data)


