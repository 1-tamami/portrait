from flask import Flask, render_template, request
import datetime as dt
from send_email import SendEmail

server = Flask(__name__)

@server.route('/')
def top_page():
    current_year = dt.datetime.now().year
    return render_template(
        "index.html",
        copy_right_year = current_year
    )

@server.route('/contact', methods=["POST", "GET"])
def contact():
    current_year = dt.datetime.now().year
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        send_email = SendEmail(name, email, message)
        send_email.send_me_notification()
        return render_template("index.html", year=current_year)
    return render_template(
        "index.html",
        copy_right_year = current_year
    )


if __name__ == "__main__":
    server.run(debug=True, port=5050)
