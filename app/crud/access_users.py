async def login (data:dict):
    return respOutCustome(status="00", message="Successfully logged in", data=data)


def login_2 (data):
    return respOutCustome(status="00", message="Successfully logged in", data=data)


def respOutCustome(status:str, message:str, data:None):
    data = {
        "data": data,
        "message": message,
        "status_code": status
    }
    return data