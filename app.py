from flask import Flask, request
import LogAndReg

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return """
    <h2>Python Login & Register</h2>
    <a href="/register">Register</a><br><br>
    <a href="/login">Login</a>
    """

# Register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        email = request.form.get("email")
        password = request.form.get("password")

        if LogAndReg.emailAlreadyExists(email):
            return "<h3>Email already exists</h3><a href='/register'>Go back</a>"

        LogAndReg.createUser(name, surname, email, password)
        return "<h3>Registration successful</h3><a href='/login'>Login</a>"

    return """
    <h2>Register</h2>
    <link rel="stylesheet" href="/static/style.css">
    <form method="POST">
        Name: <input name="name"><br>
        Surname: <input name="surname"><br>
        Email: <input name="email"><br>
        Password: <input type="password" name="password"><br><br>
        <button type="submit">Register</button>
    </form>
    """

# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if LogAndReg.userExists(email, password):
            return "<h3>Login successful</h3>"
        else:
            return "<h3>Invalid email or password</h3><a href='/login'>Try again</a>"

    return """
    <h2>Login</h2>
    <form method="POST">
        Email: <input name="email"><br>
        Password: <input type="password" name="password"><br><br>
        <button type="submit">Login</button>
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)


