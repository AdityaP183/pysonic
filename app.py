from config import app

@app.route("/", methods=["GET"])
def user_info():
    return {"message": "Welcome to PySonic Api!"}, 200


if __name__ == "__main__":
    app.run(port=8080)
