from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Login</h2>
    <form method="POST" action="/login">
        Username:<br>
        <input type="text" name="username"><br><br>
        Password:<br>
        <input type="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
    """

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    print("Username:", username)
    print("Password:", password)

    return "Login received."

app.run(host="0.0.0.0", port=5000)