import re
import pyotp
import smtplib
import time
from SecretKey import secret


totp = pyotp.TOTP(secret)


def send_email(recipient, otp):
    # E-posta adresi formatını kontrol et
    if not re.match(r"[^@]+@[^@]+\.[^@]+", recipient):
        raise ValueError(f"Invalid email address: {recipient}")

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("oguzhanfatihk@gmail.com", "uxgdqgepqmxabihb")
            message = f"Subject: Your OTP\n\nYour OTP is: {otp}"
            server.sendmail("oguzhanfatihk@gmail.com", recipient, message)
    except smtplib.SMTPAuthenticationError as e:
        print(f"Authentication failed: {e}")
        raise

# Ana kod bloğu
if __name__ == "__main__":
    while True:
        user_input = input("Do you want to generate a TOTP code? (yes/no): ").strip().lower()

        if user_input == "yes":
            otp_code = totp.now()
            delivery_method = input("Do you want the OTP code sent to your email or displayed in the console? (email/console): ").strip().lower()

            if delivery_method == "email":
                recipient_email = input("Please enter your email address: ").strip()
                send_email(recipient_email, otp_code)
            elif delivery_method == "console":
                print(f"Your OTP code is: {otp_code}")
            else:
                print("Invalid option selected.")

            print("You will be able to create a new password after 30 seconds")
            time.sleep(30)
            print("\nYou can now generate a new OTP code!")

        elif user_input == "no":
            print("No OTP code generated.")
