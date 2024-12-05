from flask import Flask, render_template, request, redirect, url_for, flash, session
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
            session['authenticated'] = True  # Set session as authenticated
            flash("Verification successful!", "success")
            return redirect(url_for("dashboard"))  # Redirect to a new page on successful verification
        else:
            flash("Verification failed!", "danger")
        return redirect(url_for("index"))

    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    # This page is accessible only if the user is authenticated
    if not session.get('authenticated'):
        return redirect(url_for("index"))  # Redirect to index if not authenticated

    return render_template("dashboard.html")


@app.route("/logout")
def logout():
    # Logout user by clearing session
    session.pop('authenticated', None)
    flash("You have been logged out.", "info")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
