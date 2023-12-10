from flask import send_file

from utils import respOutCustome, exportFileCSV
def exportCsv(data):
    respApp = exportFileCSV(data)
    return respOutCustome(
        status="00",
        message="successfully",
        data= respApp
    )