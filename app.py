
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("register.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        if not name or not email or not password:
            return "All fields are required.", 400

        # Demonstration only: do not store plain-text passwords.
        return render_template(
            "success.html",
            name=name
        )

    return render_template("register.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
