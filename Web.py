from flask import Flask, render_template, request, redirect, url_for, flash
import pyotp
from SecretKey import secret

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Set a secret key for Flask sessions

# Create the TOTP object
totp = pyotp.TOTP(secret)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the code entered by the user
        user_code = request.form.get("otp")

        # Verify the code
        if totp.verify(user_code):
            flash("Verification successful!", "success")
        else:
            flash("Verification failed!", "danger")
        return redirect(url_for("index"))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
