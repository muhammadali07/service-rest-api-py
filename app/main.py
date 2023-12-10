from flask import Flask, request, jsonify, send_file
from flask_cors import cross_origin
from app import access_users, export_file

app = Flask(__name__)

@app.route("/")
@cross_origin()
def hello_world():
    return "<p>Hello, World Guys!</p>"


@app.route("/login", methods=["GET"]) # standart routing
async def login():
    data = request.get_json()
    username = data.get("name", "")
    password = data.get("password", "")
    result = await access_users.login(data)
    return jsonify(result)


@app.route("/login-2", methods=["GET"]) # standart routing
def login2():
    data = request.get_json()
    username = data.get("name", "")
    password = data.get("password", "")
    result = access_users.login_2(data)
    return jsonify(result)


@app.route("/path-variable/<name>", methods=["GET"]) #path variable
def path_varianel(name):
    strWord = "nama saya adalah {0}".format(name)
    return jsonify(strWord)


@app.route("/query-parameter", methods=["GET"])
def query_parameter():
    name = request.args.get("name")
    age = request.args.get("age")

    data = {
        "name": name,
        "age": age
    }

    return jsonify(data)

@app.route("/body-request", methods=["GET", "POST"])
def body_request():
    if not request.is_json:
        return jsonify({"error": "Konten harus berupa JSON"}), 400
    
    data = request.json

    return jsonify({"status_code": "00", "message": "sucessfully", "data":data}), 200

@app.route("/download-csv", methods=["POST"])
def exportCSV():
    data = request.json
    print(data)
    result = export_file.exportCsv(data)
    return send_file(result["data"])

if __name__== "__main__":
    app.run(debug=True)