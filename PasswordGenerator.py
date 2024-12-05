import pyotp
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from SecretKey import secret

# Create the TOTP object
totp = pyotp.TOTP(secret)

# E-posta gönderme fonksiyonu
def send_email(recipient_email, otp_code):
    sender_email = "oguzhanfatihk@gmail.com"
    sender_password = "uxgdqgepqmxabihb"

    subject = "Your TOTP Code"
    body = f"Your One-Time Password (TOTP) code is: {otp_code}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, recipient_email, text)
            print(f"OTP code sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

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
