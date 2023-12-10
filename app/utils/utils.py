import csv

def respOutCustome(status:str, message:str, data:None):
    data = {
        "data": data,
        "message": message,
        "status_code": status
    }
    return data

# export file
def exportFileCSV(data:dict):
    with open("data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)