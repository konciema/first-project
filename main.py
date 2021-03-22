from flask import Flask, render_template, request

app = Flask(__name__)

print(app)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        name = request.form.get("contact-name")
        email = request.form.get("contact-email")
        message = request.form.get("contact-message")

        return f"Hello {name} with email: {email} and message: {message} !"


if __name__ == '__main__':
    app.run()